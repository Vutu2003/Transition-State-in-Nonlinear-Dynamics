"""Analytical and reference-library checks for EWS estimators."""

import numpy as np
import pytest
from numpy.testing import assert_allclose, assert_array_equal
from scipy import signal, stats
from statsmodels.tsa.ar_model import AutoReg
from statsmodels.tsa.stattools import acf

from src import ews_metrics as ews


@pytest.fixture
def sample():
    """Return a fixed asymmetric numerical sample."""
    return np.array([1.0, 2.0, 1.5, 4.0, 3.0, 7.0, 2.5, 3.5])


@pytest.mark.parametrize("ddof", [0, 1, 2])
def test_sd_and_cv(sample, ddof):
    expected = np.std(sample, ddof=ddof)
    assert ews.standard_deviation(sample, ddof=ddof) == pytest.approx(expected)
    assert ews.coefficient_of_variation(sample, ddof=ddof) == pytest.approx(
        expected / sample.mean()
    )
    assert ews.coefficient_of_variation(-sample, ddof=ddof) < 0


@pytest.mark.parametrize("bias", [True, False])
@pytest.mark.parametrize("fisher", [True, False])
def test_moment_conventions(sample, bias, fisher):
    assert ews.skewness(sample, bias=bias) == pytest.approx(
        stats.skew(sample, bias=bias)
    )
    assert ews.kurtosis(sample, fisher=fisher, bias=bias) == pytest.approx(
        stats.kurtosis(sample, fisher=fisher, bias=bias)
    )
    assert ews.skewness(-sample, bias=bias) == pytest.approx(
        -ews.skewness(sample, bias=bias)
    )


def test_acf_vs_pearson(sample):
    assert ews.lag1_autocorrelation(sample) == pytest.approx(
        acf(sample, nlags=1, adjusted=False, fft=False)[1]
    )
    assert ews.lag1_autocorrelation(sample, method="pearson") == pytest.approx(
        np.corrcoef(sample[:-1], sample[1:])[0, 1]
    )
    assert not np.isclose(
        ews.lag1_autocorrelation(sample),
        ews.lag1_autocorrelation(sample, method="pearson"),
    )


def test_ar1_reference_and_intercept(sample):
    fitted = AutoReg(sample, lags=1, trend="c").fit()
    phi, intercept = ews.fit_ar1(sample)
    assert_allclose([intercept, phi], fitted.params, rtol=1e-12, atol=1e-12)
    through_origin = AutoReg(sample, lags=1, trend="n").fit()
    assert ews.ar1_coefficient(sample, intercept=False) == pytest.approx(
        through_origin.params[0]
    )
    centered = sample - sample.mean()
    expected = centered[:-1].dot(centered[1:]) / centered[:-1].dot(
        centered[:-1]
    )
    phi, constant = ews.fit_ar1(sample, demean=True, intercept=False)
    assert phi == pytest.approx(expected)
    assert constant == pytest.approx(sample.mean() * (1 - phi))


def test_linear_trend_and_return_rates():
    x = np.arange(10.0)
    assert_allclose(ews.fit_ar1(x), [1.0, 1.0], atol=1e-14)
    assert ews.lag1_autocorrelation(x, method="pearson") == pytest.approx(1)
    assert ews.return_rate(x) == pytest.approx(1)
    assert ews.return_rate(x, definition="decay") == pytest.approx(0)
    exponential = 0.7 ** np.arange(15)
    assert ews.return_rate(exponential) == pytest.approx(1 / 0.7)
    assert ews.return_rate(exponential, definition="decay") == pytest.approx(
        0.3
    )
    assert ews.return_rate([1, 0, -1], definition="decay") == pytest.approx(0)
    with pytest.raises(ValueError):
        ews.return_rate([1, 0, -1, 0])


def test_noise_and_known_distributions():
    rng = np.random.default_rng(2012)
    white = rng.normal(size=100_000)
    assert abs(ews.lag1_autocorrelation(white)) < 0.012
    assert ews.standard_deviation(white) == pytest.approx(1, abs=0.015)
    assert abs(ews.skewness(white)) < 0.04
    assert ews.kurtosis(white) == pytest.approx(3, abs=0.08)
    asymmetric = rng.exponential(size=200_000)
    assert ews.skewness(asymmetric) == pytest.approx(2, abs=0.1)
    assert ews.kurtosis(asymmetric) == pytest.approx(9, abs=0.8)
    ar = signal.lfilter([1], [1, -0.8], white)[1000:]
    assert ews.ar1_coefficient(ar) == pytest.approx(0.8, abs=0.015)
    assert ews.lag1_autocorrelation(ar) == pytest.approx(0.8, abs=0.015)
    assert ews.standard_deviation(ar) == pytest.approx(
        np.sqrt(1 / (1 - 0.8**2)), abs=0.04
    )


@pytest.mark.parametrize("method", ["periodogram", "welch"])
@pytest.mark.parametrize("window", ["boxcar", "hann"])
def test_psd_reference(sample, method, window):
    kwargs = {"nperseg": 4} if method == "welch" else {}
    expected = getattr(signal, method)(
        sample,
        fs=4,
        window=window,
        detrend="constant",
        scaling="density",
        **kwargs,
    )
    actual = ews.power_spectral_density(
        sample, fs=4, method=method, window=window, **kwargs
    )
    assert_allclose(actual, expected, rtol=1e-13, atol=1e-13)


def test_sinusoid_psd_normalization():
    fs = 20
    x = 3 * np.sin(2 * np.pi * 2 * np.arange(1000) / fs)
    frequency, density = ews.power_spectral_density(x, fs=fs)
    assert frequency[np.argmax(density)] == pytest.approx(2)
    assert density.sum() * (frequency[1] - frequency[0]) == pytest.approx(4.5)


def test_spectral_ratio_and_power_law():
    size = 2048
    frequency = np.fft.rfftfreq(size)
    amplitude = np.zeros(frequency.size)
    amplitude[1:-1] = frequency[1:-1] ** -0.75
    x = np.fft.irfft(amplitude, n=size)
    fit_range = (frequency[2], frequency[-2])
    assert ews.spectral_exponent(
        x, frequency_range=fit_range
    ) == pytest.approx(1.5, abs=1e-10)
    low, high = frequency[10], frequency[100]
    assert ews.spectral_ratio(
        x, low_frequency=low, high_frequency=high
    ) == pytest.approx((low / high) ** -1.5, rel=1e-10)
    frequency, density = ews.power_spectral_density(x)
    assert ews.spectral_ratio(x, low_frequency=0.05, high_frequency=0.4) == (
        pytest.approx(
            np.interp(0.05, frequency, density)
            / np.interp(0.4, frequency, density)
        )
    )


def test_rolling_alignment_and_steps():
    x = np.arange(9.0)
    values, positions = ews.rolling_metric(x, np.mean, 4)
    assert_array_equal(values, np.arange(1.5, 7))
    assert_array_equal(positions, np.arange(3, 9))
    values, positions = ews.rolling_metric(
        x, np.mean, 4, step=4, alignment="center"
    )
    assert_array_equal(values, [1.5, 5.5])
    assert_array_equal(positions, [1.5, 5.5])
    values, _ = ews.rolling_metric(x, ews.standard_deviation, 4, ddof=0)
    assert_allclose(values, np.std(np.arange(4), ddof=0))


def test_rolling_does_not_mutate_input():
    x = np.arange(5.0)
    original = x.copy()

    def mutating_metric(window):
        """Change the private window and return a scalar."""
        window[:] = 0
        return 1.0

    ews.rolling_metric(x, mutating_metric, 3)
    assert_array_equal(x, original)


def test_kendall_ties_and_trends():
    assert ews.kendall_tau(np.arange(5)) == pytest.approx(1)
    assert ews.kendall_tau(-np.arange(5)) == pytest.approx(-1)
    values, positions = [1, 1, 3, 2, 4], [0, 0, 1, 2, 3]
    assert ews.kendall_tau(values, positions) == pytest.approx(
        stats.kendalltau(positions, values, variant="b").statistic
    )


@pytest.mark.parametrize("convention", ["r_ksmooth", "sigma"])
def test_gaussian_kernel_and_boundaries(sample, convention):
    bandwidth = 3
    sigma = bandwidth * (0.3706506 if convention == "r_ksmooth" else 1)
    distance = np.arange(sample.size)[:, None] - np.arange(sample.size)
    kernel = np.exp(-0.5 * (distance / sigma) ** 2)
    kernel[np.abs(distance) > 4 * sigma] = 0
    expected = kernel @ sample / kernel.sum(axis=1)
    residual, trend = ews.gaussian_detrend(
        sample, bandwidth, convention=convention
    )
    assert_allclose(trend, expected, rtol=1e-13, atol=1e-13)
    assert_allclose(residual + trend, sample, atol=1e-13)
    assert_allclose(ews.gaussian_smooth(np.ones(20), bandwidth), 1, atol=1e-13)


def test_gaussian_linear_interior_and_transformations(sample):
    x = np.arange(100.0)
    assert_allclose(ews.gaussian_smooth(x, 3)[10:-10], x[10:-10], atol=1e-12)
    assert_allclose(ews.log_transform(sample), np.log1p(sample))
    assert_allclose(ews.log_transform(sample, offset=0), np.log(sample))
    standardized = ews.standardize(sample)
    assert standardized.mean() == pytest.approx(0, abs=1e-14)
    assert standardized.std(ddof=1) == pytest.approx(1)


SCALAR_METRICS = [
    ews.lag1_autocorrelation,
    ews.ar1_coefficient,
    ews.return_rate,
    ews.standard_deviation,
    ews.coefficient_of_variation,
    ews.skewness,
    ews.kurtosis,
    ews.spectral_ratio,
    ews.spectral_exponent,
    ews.kendall_tau,
    ews.standardize,
]


@pytest.mark.parametrize("metric", SCALAR_METRICS)
@pytest.mark.parametrize("bad", [[], [1], [[1, 2]], [1, np.nan], [1, np.inf]])
def test_invalid_series(metric, bad):
    with pytest.raises(ValueError):
        metric(bad)


@pytest.mark.parametrize(
    "metric",
    [
        ews.lag1_autocorrelation,
        ews.ar1_coefficient,
        ews.return_rate,
        ews.skewness,
        ews.kurtosis,
        ews.spectral_ratio,
        ews.spectral_exponent,
        ews.kendall_tau,
        ews.standardize,
    ],
)
def test_degenerate_metrics(metric):
    with pytest.raises(ValueError):
        metric(np.ones(20))


def test_constant_defined_metrics():
    assert ews.standard_deviation(np.ones(4)) == 0
    assert ews.coefficient_of_variation(np.ones(4)) == 0
    _, density = ews.power_spectral_density(np.ones(20))
    assert_array_equal(density, np.zeros(11))


@pytest.mark.parametrize(
    "call",
    [
        lambda: ews.standard_deviation([1, 2], ddof=2),
        lambda: ews.standard_deviation([1, 2], ddof=-1),
        lambda: ews.standard_deviation([1, 2], ddof=0.5),
        lambda: ews.coefficient_of_variation([-1, 1]),
        lambda: ews.log_transform([-1, 2]),
        lambda: ews.log_transform([0, 1], offset=0),
        lambda: ews.gaussian_smooth([1, 2], 0),
        lambda: ews.gaussian_smooth([1, 2], np.inf),
        lambda: ews.gaussian_smooth([1, 2], 1, convention="bad"),
        lambda: ews.lag1_autocorrelation([1, 2], method="pearson"),
        lambda: ews.lag1_autocorrelation([1, 2, 3], method="bad"),
        lambda: ews.return_rate([1, 2, 3], definition="bad"),
        lambda: ews.kendall_tau([1, 2], [1, 2, 3]),
        lambda: ews.power_spectral_density([]),
        lambda: ews.power_spectral_density([1]),
        lambda: ews.power_spectral_density([1, np.nan]),
        lambda: ews.power_spectral_density([1, 2], fs=0),
        lambda: ews.power_spectral_density([1, 2], method="bad"),
        lambda: ews.power_spectral_density([1, 2], nperseg=2),
        lambda: ews.power_spectral_density([1, 2], method="welch", nperseg=3),
        lambda: ews.spectral_ratio(np.arange(20), low_frequency=0),
        lambda: ews.spectral_ratio(np.arange(20), high_frequency=0.7),
        lambda: ews.spectral_ratio(
            np.arange(20), low_frequency=0.3, high_frequency=0.2
        ),
        lambda: ews.spectral_exponent(np.arange(20), frequency_range=(0, 0.5)),
        lambda: ews.spectral_exponent(
            np.arange(20), frequency_range=(0.1, 0.8)
        ),
        lambda: ews.spectral_exponent(
            np.arange(20), frequency_range=(0.1, 0.11)
        ),
        lambda: ews.rolling_metric([1, 2], np.mean, 3),
        lambda: ews.rolling_metric([1, 2], np.mean, 0),
        lambda: ews.rolling_metric([1, 2], np.mean, 1, step=0),
        lambda: ews.rolling_metric([1, 2], np.mean, 1.5),
        lambda: ews.rolling_metric([1, 2], np.mean, 1, alignment="bad"),
        lambda: ews.rolling_metric([1, 2], lambda x: np.nan, 1),
    ],
)
def test_invalid_parameters(call):
    with pytest.raises(ValueError):
        call()


def test_core_functions_preserve_input(sample):
    original = sample.copy()
    for metric in SCALAR_METRICS:
        if metric in {ews.spectral_ratio, ews.spectral_exponent}:
            continue
        metric(sample)
    ews.gaussian_detrend(sample, 2)
    ews.log_transform(sample)
    ews.power_spectral_density(sample)
    assert_array_equal(sample, original)


@pytest.mark.parametrize("bad", ["bad", 1j, None, True, np.nan, np.inf])
def test_real_scalar_parameters(bad):
    with pytest.raises(ValueError):
        ews.gaussian_smooth([1, 2, 3], bad)
    with pytest.raises(ValueError):
        ews.power_spectral_density([1, 2, 3], fs=bad)
    with pytest.raises(ValueError):
        ews.log_transform([1, 2, 3], offset=bad)
    with pytest.raises(ValueError):
        ews.spectral_ratio(np.arange(30), low_frequency=bad)


@pytest.mark.parametrize(
    "bounds", [0.1, (0.1,), (0.1, 0.2, 0.3), (0.1, np.nan), (0.2, 0.1)]
)
def test_invalid_spectral_range_shape(bounds):
    with pytest.raises(ValueError):
        ews.spectral_exponent(np.arange(30), frequency_range=bounds)


@pytest.mark.parametrize("metric", [ews.skewness, ews.kurtosis])
def test_unresolved_moments(metric):
    values = np.array([1e15, 1e15, 1e15, 1e15 + 0.125])
    with pytest.warns(RuntimeWarning), pytest.raises(ValueError):
        metric(values)


def test_oscillatory_ar_and_zero_decay():
    alternating = (-0.5) ** np.arange(15)
    assert ews.ar1_coefficient(alternating) == pytest.approx(-0.5)
    assert ews.return_rate(alternating) == pytest.approx(-2)
    assert ews.return_rate(alternating, definition="decay") == pytest.approx(
        1.5
    )
    assert ews.return_rate([1, 0, -1, 0], definition="decay") == pytest.approx(
        1
    )


def dfa_loop_reference(x, scales, order):
    """Fit each profile box separately with least squares."""
    profile = np.cumsum(x - np.mean(x))
    result = []
    for scale in scales:
        design = np.vander(np.arange(scale, dtype=float), order + 1)
        squared_errors = []
        for start in range(0, len(x) - scale + 1, scale):
            box = profile[start : start + scale]
            coefficients = np.linalg.lstsq(design, box, rcond=None)[0]
            squared_errors.extend((box - design @ coefficients) ** 2)
        result.append(np.sqrt(np.mean(squared_errors)))
    return np.asarray(result)


@pytest.mark.parametrize("order", [0, 1, 2, 3])
def test_dfa_forward_boxes_against_independent_fits(order):
    x = np.random.default_rng(19).normal(size=997)
    original = x.copy()
    scales = np.array([10, 15, 23, 50, 100])
    sizes, actual = ews.compute_dfa_core(x, scales, order)
    assert_array_equal(sizes, scales)
    assert_allclose(
        actual, dfa_loop_reference(x, scales, order), rtol=1e-11, atol=1e-11
    )
    assert_array_equal(x, original)


def test_dfa_user_polyfit_broadcasting_reference():
    x = np.random.default_rng(20).normal(size=503)
    profile = np.cumsum(x - x.mean())
    scales = [10, 17, 33, 100]
    expected = []
    for scale in scales:
        boxes = profile[: len(x) // scale * scale].reshape(-1, scale)
        axis = np.arange(scale)
        coefficients = np.polyfit(axis, boxes.T, 1)
        residual = boxes - np.polyval(coefficients, axis[:, None]).T
        expected.append(np.sqrt(np.mean(residual**2)))
    _, actual = ews.compute_dfa_core(x, scales)
    assert_allclose(actual, expected, rtol=1e-12, atol=1e-12)


def test_dfa_analytic_linear_input_and_polynomial_removal():
    x = np.arange(1000, dtype=float)
    scales = np.array([10, 20, 50, 100, 200])
    expected = np.sqrt((scales**2 - 1) * (scales**2 - 4) / 720)
    _, actual = ews.compute_dfa_core(x, scales, order=1)
    assert_allclose(actual, expected, rtol=1e-11, atol=1e-10)
    _, removed = ews.compute_dfa_core(x, scales, order=2)
    assert_array_equal(removed, np.zeros(len(scales)))
    with pytest.raises(ValueError):
        ews.dfa(x, scales, order=2)


def test_dfa_known_power_law_fit_and_diagnostics():
    scales = np.array([10, 20, 30, 50, 100])
    fit = ews.dfa_fit(scales, 3 * scales**1.25)
    assert fit["alpha"] == pytest.approx(1.25, abs=1e-12)
    assert fit["intercept"] == pytest.approx(np.log10(3), abs=1e-12)
    assert fit["R2"] == pytest.approx(1, abs=1e-12)
    assert fit["stderr"] < 1e-7
    noisy_f = np.array([1, 2, 2.5, 4.9, 7])
    reference = stats.linregress(np.log10(scales), np.log10(noisy_f))
    fit = ews.dfa_fit(scales, noisy_f)
    assert_allclose(
        [fit["alpha"], fit["intercept"], fit["R2"], fit["stderr"]],
        [
            reference.slope,
            reference.intercept,
            reference.rvalue**2,
            reference.stderr,
        ],
        atol=1e-12,
    )


@pytest.mark.parametrize("integrated, expected", [(False, 0.5), (True, 1.5)])
def test_dfa_white_and_brownian_references(integrated, expected):
    x = np.random.default_rng(42).normal(size=65_536)
    if integrated:
        x = np.cumsum(x)
    scales = np.unique(np.geomspace(16, 1024, 25).astype(int))
    fitted = ews.dfa(x, scales)
    assert fitted["global_alpha"] == pytest.approx(expected, abs=0.08)
    assert fitted["global_R2"] > 0.995


def test_dfa_offset_amplitude_and_linear_trend_invariance():
    x = np.random.default_rng(21).normal(size=1000)
    scales = [10, 20, 50, 100]
    _, base = ews.compute_dfa_core(x, scales)
    _, scaled = ews.compute_dfa_core(-3 * x + 7, scales)
    assert_allclose(scaled, 3 * base, rtol=1e-12, atol=1e-12)
    _, quadratic = ews.compute_dfa_core(x, scales, order=2)
    _, with_trend = ews.compute_dfa_core(
        x + 0.3 * np.arange(x.size), scales, order=2
    )
    assert_allclose(with_trend, quadratic, rtol=1e-10, atol=1e-10)


def test_dfa_scale_selection_and_segment_requirement():
    x = np.random.default_rng(22).normal(size=50)
    sizes, _ = ews.compute_dfa_core(x, [100, 50, 25, 25, 1, 10])
    assert_array_equal(sizes, [10, 25, 50])
    sizes, _ = ews.compute_dfa_core(
        x, [100, 50, 25, 25, 1, 10], min_segments=2
    )
    assert_array_equal(sizes, [10, 25])
    with pytest.raises(ValueError):
        ews.compute_dfa_core(x, [1, 2, 100])


@pytest.mark.parametrize(
    "x", [[], [1, 2], [[1, 2, 3]], [1, np.nan, 3], [1, np.inf, 3], [1, 2j, 3]]
)
def test_dfa_invalid_series(x):
    with pytest.raises(ValueError):
        ews.compute_dfa_core(x, [3, 4, 5])


@pytest.mark.parametrize(
    "scales",
    [
        [],
        [0, 10],
        [-1, 10],
        [10.5, 20],
        [np.nan, 10],
        [np.inf, 10],
        [1j, 10],
        [[10, 20]],
        [True, False],
        [1e30],
    ],
)
def test_dfa_invalid_scales(scales):
    with pytest.raises(ValueError):
        ews.compute_dfa_core(np.arange(100), scales)


@pytest.mark.parametrize("order", [-1, 1.5, True, np.nan])
def test_dfa_invalid_polynomial_order(order):
    with pytest.raises(ValueError):
        ews.compute_dfa_core(np.arange(100), [10, 20, 30], order)


@pytest.mark.parametrize("minimum", [0, -1, 1.5, True])
def test_dfa_invalid_segment_count(minimum):
    with pytest.raises(ValueError):
        ews.compute_dfa_core(
            np.arange(100), [10, 20, 30], min_segments=minimum
        )


@pytest.mark.parametrize(
    "scales, fluctuations",
    [
        ([10], [1]),
        ([10, 20], [1, 2]),
        ([10, 20, 30], [1, 2]),
        ([10, 10, 20], [1, 2, 3]),
        ([0, 10, 20], [1, 2, 3]),
        ([-1, 10, 20], [1, 2, 3]),
        ([10, 20, 30], [1, 0, 3]),
        ([10, 20, 30], [1, -1, 3]),
        ([10, 20, 30], [1, np.nan, 3]),
        ([10, np.inf, 30], [1, 2, 3]),
        ([10, 20, 30], [1, np.inf, 3]),
        ([10, 20, 30], [1, 1, 1]),
    ],
)
def test_dfa_invalid_fits(scales, fluctuations):
    with pytest.raises(ValueError):
        ews.dfa_fit(scales, fluctuations)


def test_dfa_constant_fluctuations_and_rolling_adapter():
    sizes, fluctuations = ews.compute_dfa_core(np.ones(100), [10, 20, 30])
    assert_array_equal(fluctuations, np.zeros(3))
    with pytest.raises(ValueError):
        ews.dfa_fit(sizes, fluctuations)
    x = np.random.default_rng(23).normal(size=100)
    values, positions = ews.rolling_metric(
        x, ews.dfa_exponent, 50, step=10, scales=[5, 10, 20]
    )
    expected = [
        ews.dfa(x[start : start + 50], [5, 10, 20])["global_alpha"]
        for start in range(0, 51, 10)
    ]
    assert_allclose(values, expected, atol=1e-12)
    assert_array_equal(positions, np.arange(49, 100, 10))
