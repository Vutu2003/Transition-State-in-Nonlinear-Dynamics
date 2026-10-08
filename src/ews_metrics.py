"""Reusable EWS metrics for finite, regularly sampled real time series.

Invalid, short, or undefined inputs raise ValueError; inputs are never changed.
Rolling windows overlap by default. Kendall tau is descriptive, not a test of
significance for dependent windows. Frequencies use cycles per time unit.
"""

from collections.abc import Callable
from functools import lru_cache
from typing import Any, Literal

import numpy as np
from numpy.typing import ArrayLike, NDArray
from scipy import signal, stats

FloatArray = NDArray[np.float64]


@lru_cache(maxsize=128)
def _dfa_basis(scale: int, order: int) -> FloatArray:
    """Cache an orthonormal polynomial basis on a scaled local axis."""
    axis = np.linspace(-1.0, 1.0, scale)
    design = np.polynomial.polynomial.polyvander(axis, order)
    basis, _ = np.linalg.qr(design, mode="reduced")
    basis.setflags(write=False)
    return basis


def compute_dfa_core(
    x: ArrayLike,
    scales: ArrayLike,
    order: int = 1,
    *,
    min_segments: int = 1,
) -> tuple[NDArray[np.int64], FloatArray]:
    """Return scales and RMS fluctuations of a mean-centered profile.

    Fit a degree-order polynomial in forward, nonoverlapping boxes; discard
    each scale's incomplete tail. Sort/deduplicate integer scales and skip
    those below order+2 or with fewer than min_segments complete boxes.
    QR fits the same polynomial space as polyfit with a scaled local axis.
    Numerically unresolved residuals return zero; inputs are never changed.
    """
    values = _series(x, 3)
    order = _integer(order, "order", 0)
    min_segments = _integer(min_segments, "min_segments")
    requested = _series(scales)
    if (
        np.any(requested < 1)
        or np.any(requested != np.floor(requested))
        or np.any(requested >= np.iinfo(np.int64).max)
        or np.asarray(scales).dtype.kind == "b"
    ):
        raise ValueError("scales must be positive integers")
    selected = np.unique(requested)
    selected = selected[
        (selected >= order + 2) & (selected <= values.size // min_segments)
    ].astype(np.int64)
    if selected.size == 0:
        raise ValueError("no scales have enough complete polynomial boxes")
    profile = np.cumsum(values - values.mean())
    if not np.all(np.isfinite(profile)):
        raise ValueError("DFA profile exceeds numerical precision")
    fluctuations = np.empty(selected.size)
    floor = 64 * np.finfo(float).eps * np.max(np.abs(profile))
    for index, scale in enumerate(selected):
        n_boxes = values.size // scale
        boxes = profile[: n_boxes * scale].reshape(n_boxes, scale)
        basis = _dfa_basis(int(scale), order)
        coefficients = np.einsum("ij,jk->ik", boxes, basis)
        residual = boxes - np.einsum("ik,jk->ij", coefficients, basis)
        rms = float(np.linalg.norm(residual) / np.sqrt(residual.size))
        fluctuations[index] = 0.0 if rms <= floor else rms
    return selected, fluctuations


def dfa_fit(scales: ArrayLike, fluctuations: ArrayLike) -> dict[str, float]:
    """Fit log10 F = alpha*log10 scale + intercept by unweighted OLS.

    Require at least three distinct positive scales and positive finite F.
    R2 and stderr describe the regression, not a test of long-range memory.
    """
    sizes = _series(scales, 3)
    values = _series(fluctuations, 3)
    if sizes.shape != values.shape:
        raise ValueError("scales and fluctuations must have equal lengths")
    if np.any(sizes <= 0) or np.any(values <= 0):
        raise ValueError("DFA fitting requires positive scales and F")
    if np.unique(sizes).size != sizes.size:
        raise ValueError("DFA fitting requires distinct scales")
    if np.ptp(values) == 0:
        raise ValueError("DFA fit diagnostics require varying fluctuations")
    fitted = stats.linregress(np.log10(sizes), np.log10(values))
    return {
        "alpha": float(fitted.slope),
        "intercept": float(fitted.intercept),
        "R2": float(fitted.rvalue**2),
        "stderr": float(fitted.stderr),
    }


def dfa(
    x: ArrayLike,
    scales: ArrayLike,
    order: int = 1,
    *,
    min_segments: int = 1,
) -> dict[str, Any]:
    """Return the DFA curve and global fit without automatic classification."""
    sizes, fluctuations = compute_dfa_core(
        x, scales, order, min_segments=min_segments
    )
    fitted = dfa_fit(sizes, fluctuations)
    return {
        "scales": sizes,
        "fluctuations": fluctuations,
        "global_alpha": fitted["alpha"],
        "global_R2": fitted["R2"],
        "global_intercept": fitted["intercept"],
        "global_stderr": fitted["stderr"],
    }


def dfa_exponent(
    x: ArrayLike,
    scales: ArrayLike,
    order: int = 1,
    *,
    min_segments: int = 1,
) -> float:
    """Return the raw DFA alpha, suitable for rolling_metric."""
    result = dfa(x, scales, order, min_segments=min_segments)
    return float(result["global_alpha"])


def _series(x: ArrayLike, minimum: int = 1) -> FloatArray:
    """Validate a finite, real, one-dimensional series."""
    if np.iscomplexobj(x):
        raise ValueError("x must contain real values")
    try:
        values = np.asarray(x, dtype=float)
    except (TypeError, ValueError) as exc:
        raise ValueError("x must be a numerical sequence") from exc
    if values.ndim != 1 or values.size < minimum:
        raise ValueError(
            f"x must be one-dimensional with at least {minimum} values"
        )
    if not np.all(np.isfinite(values)):
        raise ValueError("x must contain only finite values")
    return values


def _integer(value: int, name: str, minimum: int = 1) -> int:
    """Validate an integer parameter."""
    if isinstance(value, (bool, np.bool_)) or not isinstance(
        value, (int, np.integer)
    ):
        raise ValueError(f"{name} must be an integer")
    if value < minimum:
        raise ValueError(f"{name} must be at least {minimum}")
    return int(value)


def _real_scalar(value: float, name: str) -> float:
    """Validate a finite, real numerical scalar."""
    if (
        not np.isscalar(value)
        or isinstance(value, (str, bytes, bool, np.bool_))
        or np.iscomplexobj(value)
    ):
        raise ValueError(f"{name} must be a finite real scalar")
    try:
        scalar = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must be a finite real scalar") from exc
    if not np.isfinite(scalar):
        raise ValueError(f"{name} must be a finite real scalar")
    return scalar


def _positive(value: float, name: str) -> float:
    """Validate a positive finite scalar."""
    scalar = _real_scalar(value, name)
    if scalar <= 0:
        raise ValueError(f"{name} must be positive and finite")
    return scalar


def lag1_autocorrelation(
    x: ArrayLike, *, method: Literal["acf", "pearson"] = "acf"
) -> float:
    """Return lag-1 ACF or Pearson correlation of adjacent pairs.

    ACF = sum(z[:-1] * z[1:]) / sum(z**2), z = x - mean(x).
    The default uses a common mean and biased covariance, as R acf does.
    Pearson separately centers and normalizes both paired slices (n >= 3).
    """
    values = _series(x, 2)
    centered = values - values.mean()
    if np.dot(centered, centered) == 0:
        raise ValueError("autocorrelation is undefined for constant x")
    if method == "acf":
        return float(
            np.dot(centered[:-1], centered[1:]) / centered.dot(centered)
        )
    if method == "pearson":
        _series(values, 3)
        left = values[:-1] - values[:-1].mean()
        right = values[1:] - values[1:].mean()
        denominator = np.linalg.norm(left) * np.linalg.norm(right)
        if denominator == 0:
            raise ValueError(
                "Pearson correlation requires varying paired slices"
            )
        return float(left.dot(right) / denominator)
    raise ValueError("method must be 'acf' or 'pearson'")


def fit_ar1(
    x: ArrayLike, *, intercept: bool = True, demean: bool = False
) -> tuple[float, float]:
    """Fit x[t+1] = a + phi*x[t] + error by conditional least squares.

    Return (phi, a). With intercept=False, fit through the origin. Setting
    demean=True centers the whole record first (R ar.ols convention); the
    returned intercept is converted back to the original scale.
    """
    values = _series(x, 3)
    offset = values.mean() if demean else 0.0
    left, right = values[:-1] - offset, values[1:] - offset
    if intercept:
        left_mean, right_mean = left.mean(), right.mean()
        predictor = left - left_mean
        response = right - right_mean
    else:
        left_mean = right_mean = 0.0
        predictor, response = left, right
    denominator = predictor.dot(predictor)
    if denominator == 0:
        raise ValueError("AR(1) slope is unidentified for this predictor")
    phi = float(predictor.dot(response) / denominator)
    constant = float(right_mean - phi * left_mean + offset * (1 - phi))
    return phi, constant


def ar1_coefficient(
    x: ArrayLike, *, intercept: bool = True, demean: bool = False
) -> float:
    """Return the OLS slope phi in x[t+1] = a + phi*x[t] + error."""
    return fit_ar1(x, intercept=intercept, demean=demean)[0]


def return_rate(
    x: ArrayLike,
    *,
    definition: Literal["inverse", "decay"] = "inverse",
    intercept: bool = True,
    demean: bool = False,
) -> float:
    """Return 1/phi ('inverse') or 1-phi ('decay'), as in Dakos 2012.

    These are discrete indicators, not continuous recovery rates. Negative
    and nonstationary phi are retained; inverse is undefined at phi=0.
    """
    phi = ar1_coefficient(x, intercept=intercept, demean=demean)
    if definition == "decay":
        return 1.0 - phi
    if definition == "inverse":
        if phi == 0:
            raise ValueError("inverse return rate is undefined at phi=0")
        return 1.0 / phi
    raise ValueError("definition must be 'inverse' or 'decay'")


def standard_deviation(x: ArrayLike, *, ddof: int = 1) -> float:
    """Return sqrt(sum((x-mean(x))**2)/(n-ddof)); default is sample SD."""
    ddof = _integer(ddof, "ddof", 0)
    values = _series(x, ddof + 1)
    return float(np.std(values, ddof=ddof))


def coefficient_of_variation(x: ArrayLike, *, ddof: int = 1) -> float:
    """Return SD/mean(x), retaining the mean's sign; zero mean is invalid."""
    values = _series(x)
    mean = float(values.mean())
    if mean == 0:
        raise ValueError("coefficient of variation requires a nonzero mean")
    return standard_deviation(values, ddof=ddof) / mean


def skewness(x: ArrayLike, *, bias: bool = True) -> float:
    """Return signed m3/m2**1.5; bias=False applies Fisher's correction.

    mk = mean((x-mean(x))**k). Require n >= 3 and nonzero variance.
    """
    values = _series(x, 3)
    if np.ptp(values) == 0:
        raise ValueError("skewness requires nonzero variance")
    result = float(stats.skew(values, bias=bias))
    if not np.isfinite(result):
        raise ValueError("skewness is unresolved at numerical precision")
    return result


def kurtosis(
    x: ArrayLike, *, fisher: bool = False, bias: bool = True
) -> float:
    """Return m4/m2**2 (Pearson); fisher=True subtracts 3.

    mk = mean((x-mean(x))**k). bias=False applies SciPy's k-statistic
    correction. Require n >= 4 and nonzero variance.
    """
    values = _series(x, 4)
    if np.ptp(values) == 0:
        raise ValueError("kurtosis requires nonzero variance")
    result = float(stats.kurtosis(values, fisher=fisher, bias=bias))
    if not np.isfinite(result):
        raise ValueError("kurtosis is unresolved at numerical precision")
    return result


def power_spectral_density(
    x: ArrayLike,
    *,
    fs: float = 1.0,
    method: Literal["periodogram", "welch"] = "periodogram",
    window: str = "boxcar",
    nperseg: int | None = None,
) -> tuple[FloatArray, FloatArray]:
    """Return (frequency, one-sided density) with mean removal.

    Density = |FFT(window*(x-mean(x)))|**2/(fs*sum(window**2)), with
    interior positive bins doubled. Units are x**2 per frequency unit.
    Welch averages segment spectra; this differs from R's AR spectrum.
    """
    values = _series(x, 2)
    fs = _positive(fs, "fs")
    if method == "periodogram":
        if nperseg is not None:
            raise ValueError("nperseg is only supported for Welch")
        return signal.periodogram(
            values, fs=fs, window=window, detrend="constant", scaling="density"
        )
    if method == "welch":
        segment = min(256, values.size) if nperseg is None else nperseg
        segment = _integer(segment, "nperseg", 2)
        if segment > values.size:
            raise ValueError("nperseg must not exceed series length")
        return signal.welch(
            values,
            fs=fs,
            window=window,
            nperseg=segment,
            detrend="constant",
            scaling="density",
        )
    raise ValueError("method must be 'periodogram' or 'welch'")


def spectral_ratio(
    x: ArrayLike,
    *,
    low_frequency: float = 0.05,
    high_frequency: float = 0.5,
    fs: float = 1.0,
    method: Literal["periodogram", "welch"] = "periodogram",
    window: str = "boxcar",
    nperseg: int | None = None,
) -> float:
    """Return S(low_frequency)/S(high_frequency), using linear interpolation.

    Frequencies must satisfy first positive bin <= low < high <= last bin.
    This is a point-density ratio, not integrated band power.
    """
    frequencies, density = power_spectral_density(
        x, fs=fs, method=method, window=window, nperseg=nperseg
    )
    low_frequency = _positive(low_frequency, "low_frequency")
    high_frequency = _positive(high_frequency, "high_frequency")
    if not (
        frequencies[1] <= low_frequency < high_frequency <= frequencies[-1]
    ):
        raise ValueError(
            "frequency pair is outside the resolved positive spectrum"
        )
    low = float(np.interp(low_frequency, frequencies, density))
    high = float(np.interp(high_frequency, frequencies, density))
    if high == 0:
        raise ValueError("high-frequency density must be nonzero")
    return low / high


def spectral_exponent(
    x: ArrayLike,
    *,
    frequency_range: tuple[float, float] | None = None,
    fs: float = 1.0,
    method: Literal["periodogram", "welch"] = "periodogram",
    window: str = "boxcar",
    nperseg: int | None = None,
) -> float:
    """Return beta in S(f) proportional to f**(-beta), via log-log OLS.

    Use positive frequencies and positive densities in the closed fit range.
    beta is minus the fitted slope; exclude DC and require at least 3 bins.
    """
    frequencies, density = power_spectral_density(
        x, fs=fs, method=method, window=window, nperseg=nperseg
    )
    lower, upper = (frequencies[1], frequencies[-1])
    if frequency_range is not None:
        bounds = _series(frequency_range, 2)
        if bounds.size != 2:
            raise ValueError("frequency_range must contain two bounds")
        lower, upper = bounds
        if not (0 < lower < upper <= fs / 2):
            raise ValueError("frequency_range must lie in (0, fs/2]")
    selected = (frequencies >= lower) & (frequencies <= upper) & (density > 0)
    if selected.sum() < 3:
        raise ValueError("spectral exponent requires at least 3 positive bins")
    slope = stats.linregress(
        np.log(frequencies[selected]), np.log(density[selected])
    ).slope
    return float(-slope)


def rolling_metric(
    x: ArrayLike,
    metric_fn: Callable[..., float],
    window_size: int,
    step: int = 1,
    *,
    alignment: Literal["endpoint", "center"] = "endpoint",
    **metric_kwargs: Any,
) -> tuple[FloatArray, FloatArray]:
    """Return (values, positions) for complete windows, without smoothing.

    Positions are zero-based endpoints or arithmetic centers (half-integers
    for even windows). Each callable receives a copy; its errors propagate.
    """
    values = _series(x)
    window_size = _integer(window_size, "window_size")
    step = _integer(step, "step")
    if window_size > values.size:
        raise ValueError("window_size must not exceed series length")
    if alignment not in {"endpoint", "center"}:
        raise ValueError("alignment must be 'endpoint' or 'center'")
    starts = np.arange(0, values.size - window_size + 1, step)
    estimates = np.asarray(
        [
            metric_fn(
                values[start : start + window_size].copy(), **metric_kwargs
            )
            for start in starts
        ],
        dtype=float,
    )
    if estimates.ndim != 1 or not np.all(np.isfinite(estimates)):
        raise ValueError(
            "metric_fn must return a finite scalar for each window"
        )
    offset = (
        window_size - 1 if alignment == "endpoint" else (window_size - 1) / 2
    )
    return estimates, np.asarray(starts + offset, dtype=float)


def kendall_tau(x: ArrayLike, positions: ArrayLike | None = None) -> float:
    """Return Kendall tau-b of values versus positions (default sample index).

    Ties are corrected. Constant values/positions make tau undefined.
    No independent-sample p-value is returned for overlapping windows.
    """
    values = _series(x, 2)
    times = (
        np.arange(values.size) if positions is None else _series(positions, 2)
    )
    if times.size != values.size:
        raise ValueError("positions and x must have equal lengths")
    tau = float(stats.kendalltau(times, values, variant="b").statistic)
    if not np.isfinite(tau):
        raise ValueError("Kendall tau is undefined for constant ranks")
    return tau


def gaussian_smooth(
    x: ArrayLike,
    bandwidth: float,
    *,
    convention: Literal["r_ksmooth", "sigma"] = "r_ksmooth",
) -> FloatArray:
    """Return sum(K(t-j)*x[j])/sum(K(t-j)) on a regular unit grid.

    K(d)=exp(-d**2/(2*sigma**2)), truncated at 4*sigma. r_ksmooth uses
    sigma=0.3706506*bandwidth; sigma uses bandwidth directly. Normalize
    available weights at boundaries; no reflection or zero padding bias.
    This two-sided smoother uses future observations.
    """
    values = _series(x)
    bandwidth = _positive(bandwidth, "bandwidth")
    if convention not in {"r_ksmooth", "sigma"}:
        raise ValueError("convention must be 'r_ksmooth' or 'sigma'")
    sigma = bandwidth * (0.3706506 if convention == "r_ksmooth" else 1.0)
    radius = min(int(np.floor(4 * sigma)), values.size - 1)
    offsets = np.arange(-radius, radius + 1, dtype=float)
    kernel = np.exp(-0.5 * (offsets / sigma) ** 2)
    numerator = signal.convolve(values, kernel, mode="same", method="direct")
    denominator = signal.convolve(
        np.ones(values.size), kernel, mode="same", method="direct"
    )
    return numerator / denominator


def gaussian_detrend(
    x: ArrayLike,
    bandwidth: float,
    *,
    convention: Literal["r_ksmooth", "sigma"] = "r_ksmooth",
) -> tuple[FloatArray, FloatArray]:
    """Return (x-trend, trend) using the specified Gaussian kernel."""
    values = _series(x)
    trend = gaussian_smooth(values, bandwidth, convention=convention)
    return values - trend, trend


def log_transform(x: ArrayLike, *, offset: float = 1.0) -> FloatArray:
    """Return log(x+offset); require finite offset and x+offset > 0."""
    values = _series(x)
    offset = _real_scalar(offset, "offset")
    if np.any(values + offset <= 0):
        raise ValueError("log transform requires x+offset > 0")
    return np.log(values + offset)


def standardize(x: ArrayLike, *, ddof: int = 1) -> FloatArray:
    """Return (x-mean(x))/SD(x); require nonzero SD."""
    values = _series(x)
    scale = standard_deviation(values, ddof=ddof)
    if scale == 0:
        raise ValueError("standardization requires nonzero variance")
    return (values - values.mean()) / scale
