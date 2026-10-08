# Dakos et al. (2012): báo cáo tái tạo core metric-based EWS

Ngày kiểm tra: 08/10/2026. Notebook: [dakos_2012.ipynb](../experiments/dakos_2012.ipynb).
Module: [ews_metrics.py](../src/ews_metrics.py). Kiểm thử: [test_ews_metrics.py](../tests/test_ews_metrics.py).

Cấu trúc project cố định: notebook nằm trong `experiments/`, báo cáo trong
`report/`, core module trong `src/`, tests trong `tests/` và dependencies
trong `requirements.txt`. Thí nghiệm không tạo thư mục kết quả hoặc xuất
CSV/JSON/PNG ra disk. Kết quả được giữ trong RAM và hiển thị trong notebook;
người dùng có thể lưu notebook cùng outputs bằng chức năng Save của IDE.
Notebook diễn giải đầy đủ từng bước theo mạch cơ chế → kiểm chứng estimator
→ mô phỏng → tiền xử lý → tín hiệu → DFA → sensitivity → stationary null
→ stochastic ensemble → đối chiếu và giới hạn. Báo cáo này là bản kèm theo;
không cần đọc nó để hiểu toàn bộ thí nghiệm trong notebook.

**Kết luận:** các estimator đã được kiểm chứng số học; mô phỏng tái tạo được
nhiều đặc điểm định tính. Chưa tái tạo hoàn toàn kết quả bài báo, đặc biệt SD
của CSD sau detrending và một phần sensitivity. Không khẳng định khớp định lượng.

## A. Nguồn và trích xuất phương pháp

Đã đọc PDF số 4 trong `paper/`, Table 1, Methods, Figures 1, 2, 3, 10, 11 và
Table 3. Nguồn trực tuyến là [bài báo PLOS](https://doi.org/10.1371/journal.pone.0041010),
[repository R của nhóm tác giả](https://github.com/earlywarningtoolbox/earlywarnings-R),
[R ksmooth documentation](https://stat.ethz.ch/R-manual/R-devel/library/stats/html/ksmooth.html)
và [mã kernel R](https://github.com/wch/r-source/blob/trunk/src/library/stats/src/ksmooth.c).

Các chi tiết trích xuất: Equation 8 dùng logistic growth, saturating harvest và
multiplicative white noise; r=1, K=10, h=1; c tăng từ 1 đến 2.6771;
CSD có 1.000 điểm, sigma=0.03; flickering có 10.000 điểm, sigma=0.15;
measurement SD=0.1 cho cả hai; red noise có T=20 và beta=0.07.
Figure 2 dùng 970 điểm CSD đầu với window 485, bandwidth 97; flickering dùng
toàn bộ chuỗi với window 5.000 và log(z+1) rồi standardize. Figure 10 kiểm tra
window khoảng 25–75% và bandwidth 5–200. Figure 11 dùng 1.000 ARMA surrogates.

Mã R truy cập ngày 08/10/2026 là mã hiện tại, chưa xác nhận là bản năm 2012.
`generic_ews.R` dùng `ar.ols(demean=TRUE, intercept=FALSE)`, sample SD,
`moments::kurtosis`, R `acf`, R `spec.ar` và endpoint alignment. Hàm này lấy
`abs(skewness)`, còn `sensitivity_ews.R` giữ dấu. Bản tái tạo giữ skewness có
dấu, phù hợp định nghĩa và các tau âm trong bài báo. Return rate được code R
tính bằng inverse dù phần mô tả function ghi `1-ar(1)`; API triển khai cả hai.

R `ksmooth` định nghĩa bandwidth theo quartiles, với Gaussian sigma xấp xỉ
0.3706506 lần bandwidth, cutoff 4 sigma và chuẩn hóa trọng số tại biên.
Module theo đúng quy ước này trên lưới lấy mẫu đều. Cũng có tùy chọn dùng sigma
trực tiếp. Biểu thức SD in trong PDF thiếu căn bậc hai; module tính SD đúng
về toán học và theo R `sd`, không tính variance rồi gọi là SD.

SHA-256 của ba file R đã đọc, để nhận diện phiên bản tham khảo:

```text
generic_ews.R     13d2834337c8ba01f50a9d63c6292b656cb01a8dc913327be05c1d003bdec374
sensitivity_ews.R c3318975313426bd35638a773d194bc0917215d17892aeee9ab6fcd5f681225f
surrogates_ews.R  dd4209f4eb8a7eeea3ce075ccc02d437830b7a8684c0e72907b68444e05d08e2
```

Metadata `foldbif` trong package ghi `TBA` cho format/source. Vì chưa xác minh
đây là chuỗi gốc của Figures 1–2, notebook dùng mô phỏng mới và không gán
nguồn gốc không có bằng chứng cho dữ liệu package.

## B. Metrics và kiểm chứng số học

Đặt z=x-mean(x), mk=mean(z**k), phi là fitted AR(1) coefficient.
Các functions chấp nhận real array-like một chiều, không thay đổi input và
raise `ValueError` với input không hợp lệ hoặc estimator không xác định.

| Function | Định nghĩa / convention | Kiểm chứng |
|---|---|---|
| `lag1_autocorrelation` | sum(z[:-1]*z[1:])/sum(z**2); tùy chọn Pearson paired slices | statsmodels ACF, NumPy Pearson, white noise, AR(1) |
| `fit_ar1`, `ar1_coefficient` | OLS x[t+1]=a+phi*x[t]; hỗ trợ intercept hoặc toàn chuỗi demean | statsmodels AutoReg, trend tuyến tính, exponential decay |
| `return_rate` | `1/phi` hoặc `1-phi`; không gọi là continuous recovery rate | Phi biết trước, phi âm, phi=0, phi=1 |
| `power_spectral_density` | One-sided periodogram/Welch; density units x²/frequency; bỏ mean | scipy.signal, sinusoid peak, integrated power |
| `spectral_ratio` | S(f_low)/S(f_high), linear interpolation; mặc định 0.05/0.5 | Synthetic power law, kiểm tra tần số ngoài dải |
| `spectral_exponent` | beta=-slope(log S versus log f), S~f^(-beta) | Power law beta=1.5 khớp trong 1e-10 |
| `standard_deviation` | sqrt(sum(z²)/(n-ddof)), mặc định ddof=1 | NumPy ddof=0/1/2, constant, Gaussian, AR variance |
| `coefficient_of_variation` | SD/mean, giữ dấu mean; mean=0 không xác định | NumPy, positive/negative mean, constant |
| `skewness` | Signed m3/m2^1.5; bias correction tùy chọn | SciPy, Gaussian, exponential distribution, sign reversal |
| `kurtosis` | Pearson m4/m2²; Fisher subtracts 3 tùy chọn | SciPy cả hai bias/Fisher conventions, Gaussian/exponential |
| `compute_dfa_core` | Mean-centered integrated profile, polynomial detrending theo forward nonoverlapping boxes, RMS, bỏ đuôi mỗi scale | User polyfit broadcasting và independent per-box least squares orders 0–3; nghiệm giải tích linear input |
| `dfa_fit`, `dfa`, `dfa_exponent` | OLS log10 F versus log10 s; raw alpha, intercept, R², slope stderr; ít nhất 3 scales phân biệt | Exact power law, SciPy regression, white/Brownian noise, affine/trend invariance, rolling adapter, invalid fits |
| `rolling_metric` | Complete windows, step=1; zero-based endpoint hoặc center | Window values, overlapping/nonoverlapping, even centers, input isolation |
| `kendall_tau` | Tau-b, có correction ties; không trả independent-sample p-value | SciPy, ties, monotonic trends, constant ranks |
| `gaussian_smooth`, `gaussian_detrend` | Normalized truncated Gaussian; R bandwidth hoặc sigma | Direct kernel-weight reference, boundary, constant, linear interior |
| `log_transform`, `standardize` | log(x+offset); (x-mean)/SD | NumPy, positivity và zero-variance checks |

**183 tests passed**, chạy bằng `.venv/bin/python -m pytest tests -q`.
Ruff kiểm tra E/F/I với line length 79 đạt cho source, tests và notebook.
Gaussian được đối chiếu công thức kernel tương ứng R, chưa chạy so sánh trực
tiếp bằng R runtime. Test reference-library dùng tolerance 1e-12 hoặc gần đó;
test phân phối có tolerance phù hợp sampling uncertainty và seed cố định.

Edge cases bao gồm empty/short/non-1D, NaN/Inf/complex, constant,
unresolved moments do precision, log không có domain hợp lệ, zero mean,
window/step không hợp lệ, spectral range sai và scalar parameters không hợp lệ.
PSD của constant trả zero; SD của constant trả zero; moments chuẩn hóa không
xác định thì báo lỗi. Tối thiểu: ACF/PSD 2 điểm, fitted AR và skewness 3 điểm,
kurtosis 4 điểm; SD cần n>ddof; spectral exponent cần ít nhất 3 positive bins.

## C. Mô phỏng và giả định

Tích phân Itô Euler–Maruyama, dt=0.1, sampling interval=1, 10 substeps mỗi
observation. Grazing giữ cố định trong mỗi observation interval. Observation
đầu tiên được ghi sau interval đầu. Khởi tạo tại equilibrium cao ở c=1, q=0.
Process, red-noise và measurement RNG là ba streams tách từ SeedSequence.
Seeds chính: 2012 cho CSD, 2013 cho flickering. Measurement error được thêm
sau integration, không clipping observations.

Biomass được project lên [0, infinity) nếu Euler step âm. **Không có lần
projection nào** ở hai realization chính. Boundary behavior chưa được xác
định từ paper; không coi lựa chọn này là hành vi GRIND đã xác minh.

Flickering dùng `q[t+1]=0.95*q[t]+0.07*eta[t]`, với eta~N(0,1), cập nhật mỗi
observation; thêm inflow `q*x` vào drift trong tất cả substeps. Công thức in
trong paper là `i[t+1]=(0.95*i[t]+0.07*eta[t])*x[t]`. Nếu i là inflow được giữ
qua các bước, hệ số nhớ ở equilibrium đầu x≈8.889 là ≈8.44, vượt 1.
Diễn giải q là biến nhớ không thứ nguyên giúp nhiễu đỏ stationary trước khi
scale theo biomass. Đây là **khác biệt rõ với recurrence in nguyên văn**,
không phải xác nhận một lỗi trong paper hoặc replication chính xác của GRIND.

| Chẩn đoán | CSD | Flickering |
|---|---:|---:|
| Số observations | 1.000 | 10.000 |
| Lần đầu biomass <2 | 978 | 204 |
| Số crossings threshold biomass=2 | 1 | 69 |
| Biomass cuối | 0.4175 | 0.5049 |
| Boundary projections | 0 | 0 |

Threshold 2 chỉ là chẩn đoán thực nghiệm, không phải phép xác định basin
boundary. Đồ thị flickering cho thấy các đoạn dài ở biomass cao/thấp xen kẽ;
thời điểm bắt đầu excursions khác paper. Fold deterministic tìm được tại
c=2.604365, x=4.781284, khớp c≈2.604 được báo cáo.

Kiểm tra deterministic integration: max error so với dt=0.025 là 0.040792
khi dt=0.1 và 0.013551 khi dt=0.05. Giảm dt cải thiện kết quả. Đây không phải
kiểm tra strong convergence của SDE; cấu hình GRIND và stochastic path gốc
chưa có đủ thông tin để so sánh.

## C.1. DFA: validation core người dùng và Figure 3

**Kết luận validation:** phần tính fluctuation function trong script người dùng
đúng về profile, forward segmentation, polynomial fit và RMS. Broadcasting
`np.polyval(coeffs, t[:, None]).T` đúng với coefficients của `polyfit`.
Trên sample length 997, scales 10/15/23/50/100, orders 0–3, core tích hợp
khớp script polyfit với max absolute F error <=8.89e-16. Các tests cũng đối
chiếu từng box bằng `np.linalg.lstsq` độc lập. Module dùng QR trên local
axis [-1,1] để fit cùng polynomial space, cải thiện conditioning.

Với input x[i]=i và DFA1, nghiệm giải tích là
`F(s)=sqrt((s²-1)*(s²-4)/720)`; max error 4.85e-12 trên scales
10/20/50/100/200. DFA2 loại được linear trend của input, trả F=0 trong
numerical tolerance. Mean-centered profile constant cũng trả F=0; alpha
trong các trường hợp này không xác định và báo `ValueError`.

Thí nghiệm reference có 65.536 samples mỗi tín hiệu, RNG=42, scales 16–1.024:
white noise alpha=0.511478, R²=0.999430; independent random walk
alpha=1.46707, R²=0.999604. Tests dùng sampling tolerance 0.08 so với
0.5 và 1.5. Đây là validation estimator, không phải calibration sinh thái.

Các sửa đổi so với script gửi:

- Sửa typo import; từ chối fractional/zero/negative/nonfinite scales,
  invalid order và invalid arrays. Không silently truncate scales bằng int.
- Sort/deduplicate scales; skip scale thiếu độ dài cho order+2 hoặc thiếu
  min_segments. Mặc định min_segments=1 giữ convention ban đầu; experiment=2.
- `dfa_fit` đòi ít nhất ba positive distinct scales, F positive/finite,
  matching shapes và varying fluctuations; không âm thầm bỏ NaN hoặc F=0
  rồi thay fit range. Fit suy biến báo lỗi thay vì trả NaN/Inf diagnostics.
- Không tích hợp automatic interpretation: nhánh `<0.5`, `<1.0`, `<1.5`
  trước `isclose` gây nhãn sai ở 0.49/0.99/1.49, và slope hữu hạn chưa chứng
  minh long-range memory hoặc loại nonstationarity.
- Không tích hợp crossover heuristic: chia sẻ một điểm không ép continuity
  hai fits; cộng R² và thresholds chưa là model-selection/significance test.
  Crossover không thuộc workflow Figure 3. Plotting ở notebook.

**Quy trình Figure 3:** giữ observed records/seeds hiện tại; CSD=970 điểm,
window=485; flickering=10.000 điểm, window=5.000. Detrend linear toàn raw
record trước rolling, theo Step 2 và Figure 3; không dùng Gaussian hay log
input của Figure 2. Sau đó tích phân mean-centered profile và DFA1 trong
từng box; rolling step=1, endpoint alignment. Paper không nêu exact scale
grid và segmentation kernel. Bản này chọn 20 integer log-spaced scales:

```text
10,11,12,14,16,18,20,23,26,29,33,37,42,48,54,61,69,78,88,100
```

Sensitivity window fractions tự chọn 25/35/45/50/55/65/75%, dùng
`np.rint(fraction*N)` (ties-to-even). CSD widths=242,340,436,485,534,630,728;
flickering=2500,3500,4500,5000,5500,6500,7500. Mỗi width chạy tất cả rolling
windows; số estimates CSD 729/631/535/486/437/341/243 và flickering
7501/6501/5501/5001/4501/3501/2501. Lưới này không được nhận là exact grid
Figure 3E,F. Không thay Gaussian bandwidth cho DFA.

| Chẩn đoán DFA1 raw alpha | CSD | Flickering |
|---|---:|---:|
| Primary window | 485 | 5.000 |
| Kendall tau-b | 0.496551 | 0.855583 |
| Alpha đầu → cuối | 0.736454 → 0.859669 | 1.25732 → 1.51203 |
| Alpha min..max | 0.675909..0.865801 | 1.24777..1.52177 |
| Log-log R² đầu → cuối | 0.962295 → 0.972854 | 0.998325 → 0.996526 |
| Window sensitivity tau min..max | 0.183213..0.514559 | 0.680285..0.871787 |
| Widths có tau dương | 7/7 | 7/7 |
| Tau khi detrend riêng mỗi rolling window | 0.557660 | 0.855316 |
| Max alpha difference whole-record / within-window | 0.0312212 | 0.000442947 |

**Đánh giá:** cả hai khớp hướng rising memory; flickering có trend mạnh,
alpha dao động quanh 1.5 cuối chuỗi. CSD tăng vừa phải và vẫn xa 1.5;
window sensitivity dương nhưng có tau thấp, chưa khớp strong-positive
pattern được mô tả. Changing regimes có thể ảnh hưởng DFA của flickering;
không gán duy nhất cho critical slowing down. Detrend comparison không đổi
dấu trend ở realization này. Whole-record detrending có future information;
đây là offline reproduction, không phải causal online detector.

**Giới hạn calibration:** [hướng dẫn của nhóm tác giả](https://www.early-warning-signals.org/?page_id=113) phân biệt exponent alpha
với indicator đã rescale. [Livina & Lenton (2007)](https://doi.org/10.1029/2006GL028672) xây dựng empirical AR(1) calibration
sang DFA propagator, không phải phép chia alpha/1.5. Notebook báo raw alpha
và đường tham chiếu random-walk 1.5; chưa tái tạo calibrated indicator hoặc
đối chiếu giá trị tới ngưỡng 1 của paper. Kernel DFA Fortran/C-MATLAB gốc
được paper nêu là cung cấp theo liên hệ tác giả, chưa có trong repository.
Short-range slope và R² cao không tự chứng minh long-range power law hay
bifurcation. Không báo independent-window p-values hoặc dùng Figure 11
significance của ACF/SD/skewness cho DFA.

## D. Paper comparison

Pass dưới đây chỉ có nghĩa là đặc điểm định tính nêu trong hàng được khớp.
Partial/Fail không phủ nhận numerical validation của core module.

| Item | Original paper | Reproduced result | Assessment |
|---|---|---|---|
| Figure 1 CSD | Collapse khoảng observation 970 | Biomass <2 ở 978; nhánh cao chuyển xuống nhánh thấp | Pass định tính |
| Figure 1 flickering | Repeated state excursions, rõ hơn sau khoảng 2.000 | Nhiều excursions và chuyển xuống biomass thấp; first crossing ở 204; red recurrence khác | Partial |
| Figure 2 AR1/ACF CSD | Raw/residual đều tăng | Tau 0.888728 / 0.842892; residual ACF 0.396→0.588 | Pass hướng; Partial định lượng |
| Figure 2 SD CSD | Raw và detrended SD tăng | Raw tau 0.822867; residual tau -0.415366, giảm nhiều rồi tăng cuối | Partial tổng thể; Fail cho residual trend |
| Figure 2 skewness CSD | Raw/residual giảm nhưng irregular | Tau -0.399856 / -0.190785 | Pass hướng; Partial magnitude |
| Figure 2 flickering ACF | Gần saturation, tăng yếu | Raw 0.915→0.983; processed 0.959→0.988 | Pass saturation; Partial trend strength |
| Figure 2 flickering SD | Tăng rồi giảm, peak khoảng 8.000 | Raw peak 8.109; processed peak 8.630, đều giảm cuối | Pass định tính |
| Figure 2 flickering skewness | Tăng | Raw/processed tau 0.936141 / 0.987923 | Pass hướng |
| Kendall tau | Published CSD values | Cùng dấu, sai lệch tới 0.284215 | Partial; không khớp exact |
| Figure 3 DFA | Rising memory cả hai; strong positive window sensitivity; CSD indicator gần 1, flickering quanh 1 | Raw-alpha tau 0.496551 / 0.855583; sensitivity dương 7/7 mỗi scenario; alpha CSD 0.736→0.860, flickering 1.257→1.512 | Pass hướng; Partial strength; calibrated magnitude chưa tái tạo |
| Figure 10 | ACF robust; SD thường tăng trừ bandwidth nhỏ; skewness yếu | ACF dương 96.4% cấu hình; SD âm 100%; skewness âm 99.0% nhưng đa phần yếu | Partial; Fail cho SD pattern |
| Figure 11 | ACF significant; skewness không significant | Primary-config p≈0.0030 và 0.3806; SD p≈0.7173 | Partial; full grid deferred |

Published tau được trích từ Results, Step 3; không tự suy ra số SD/flickering
khi chưa xác nhận một giá trị từ nội dung nguồn.

| CSD metric | Published tau | Computed tau | Computed - published |
|---|---:|---:|---:|
| ACF raw | 0.911 | 0.888728 | -0.022272 |
| ACF residual | 0.944 | 0.842892 | -0.101108 |
| Skewness raw | -0.436 | -0.399856 | 0.036144 |
| Skewness residual | -0.475 | -0.190785 | 0.284215 |

AR1 trong Figure 2 có thể bị đọc là fitted AR coefficient. Figure chính ở
notebook ghi rõ ACF(1), figure bổ sung ghi OLS AR(1). CSD demeaned OLS tau
0.844114 gần nhưng không bằng ACF tau 0.842892. Hai return-rate indicators
có tau -0.844114. Supplementary PSD/ratio/exponent dùng SciPy estimators,
chỉ là extended verification, không đánh giá như reproduction của R `spec.ar`.

## E. Sensitivity và significance

Sensitivity dùng 51 window sizes: 243,253,...,723 và thêm 485,728;
12 bandwidths: 5,25,...,185 và thêm 97,200. Tổng 612 cấu hình, mỗi cấu hình
tính ba indicators. Chênh lệch làm tròn biên 25%/75% được công bố rõ.
Vectorized formulas trong experiment layer đã khớp `rolling_metric` ở raw
và residual CSD với tolerance rtol=1e-11, atol=1e-12.

| Vùng bandwidth | ACF tau range / tỉ lệ dương | SD tau range / tỉ lệ dương | Skewness tau range / tỉ lệ âm |
|---|---|---|---|
| <=25 | -0.268..0.844 / 78.4% | -0.947..-0.482 / 0% | -0.731..-0.184 / 100% |
| 45..105 | 0.535..0.894 / 100% | -0.628..-0.301 / 0% | -0.433..0.111 / 97.6% |
| >=125 | 0.584..0.897 / 100% | -0.456..-0.271 / 0% | -0.701..-0.156 / 100% |

ACF direction ổn định hơn tại bandwidth >=45. Skewness chỉ có |tau|>0.5
trong 16.5% cấu hình, nên cùng dấu không đồng nghĩa với trend mạnh. SD không
tái tạo pattern paper ở realization này. Không chọn cấu hình để maximize tau.

Surrogate experiment fit 20 ARMA candidates: p=1..4, q=0..4, zero mean, chọn
AIC trong stationary/invertible converged fits. Cả 20 fit hội tụ; ARMA(4,4)
được chọn, AIC=-222.238457. Min AR root modulus=1.007835; min MA root
modulus=1.000000045, rất gần invertibility boundary. Significance phụ thuộc
null fit và cần thận trọng khi diễn giải sensitivity với estimation khác.
Không chứng minh Gaussian stationary ARMA mô tả đầy đủ residual distribution.

Sinh 1.000 surrogates, seed=2014, burn-in=5.000, length=970, window=485.
Không detrend lại surrogate; giữ residual-series null như workflow đã chọn.
Upper tail cho ACF/SD, lower tail cho signed skewness của downward transition.
Monte Carlo p dùng correction `(1+extreme)/(1000+1)`.

| Metric | Observed tau | Directional p | Monte Carlo SE |
|---|---:|---:|---:|
| ACF(1) | 0.842892 | 0.002997 | 0.001729 |
| SD | -0.415366 | 0.717283 | 0.014240 |
| Skewness | -0.190785 | 0.380619 | 0.015354 |

Đây là conditional evidence cho null model và cấu hình đã chọn, không phải
false-alarm rate của EWS detector. Full Figure 11 sensitivity/significance grid
**deferred**; không tuyên bố tái tạo significance trên toàn parameter space.

## F. Discrepancies và stochastic variability

Ensemble CSD bổ sung gồm seeds 2100–2119, giữ cùng cutoff 970, window 485,
bandwidth 97. Tỉ lệ expected direction: ACF 20/20, SD 16/20, skewness 13/20.
Median tau lần lượt 0.871393, 0.691248, -0.340036. SD tau range
-0.646515..0.842722 cho thấy primary negative SD trend không đủ để kết luận
estimator sai. Seed 2119 có biomass <2 ở observation 963, trước cutoff;
ensemble không phải 20 record bảo đảm hoàn toàn pre-transition.

Các nguồn sai lệch cần phân biệt:

- **Stochastic variation:** seed và realization gốc không có; ensemble cho
  thấy SD/skewness directions có thể đổi. Không đổi primary realization.
- **Thông tin còn thiếu:** x0, solver/timestep GRIND, cách cập nhật red noise,
  exact observation timing và boundary chưa xác định đầy đủ.
- **Numerical integration:** Euler–Maruyama khác solver gốc; mới kiểm tra
  convergence deterministic, chưa kiểm tra convergence stochastic có coupling.
- **Estimator conventions:** common-mean ACF khác Pearson/OLS; moments giữ
  dấu và Pearson kurtosis; Welch/periodogram khác autoregressive PSD của R.
- **Preprocessing:** R bandwidth được resolve; smoother hai phía có future
  leakage, nhất là cuối chuỗi. Giữ cutoff 970 dù collapse realization ở 978.
- **Model interpretation:** q*x red inflow là diễn giải khác recurrence in
  nguyên văn và có thể thay đổi excursion frequency/magnitude.
- **Potential implementation errors:** kiểm thử analytical/library và kernel
  reference chưa phát hiện lỗi công thức core; vẫn chưa loại trừ khác biệt với
  simulation implementation gốc. Không quy mọi discrepancy cho randomness.

SD residual có thể giảm phần lớn chuỗi rồi tăng ở cuối trong khi ACF tăng.
Multiplicative noise sigma*x giảm cùng biomass, có thể cạnh tranh với hiệu
ứng giảm return rate. Đây là một cơ chế khả dĩ, không phải kết luận nguyên
nhân đã xác minh của chênh lệch paper.

## G. Reusability và chạy lại

Toàn bộ core implementation nằm trong một module, chỉ cần NumPy/SciPy.
Simulation, plots và surrogate fitting nằm trong notebook riêng.
Các bước experiment không ghi file kết quả; bảng và figures hiển thị inline.
DFA được bổ sung theo yêu cầu mới: `compute_dfa_core`, `dfa_fit`, `dfa` và scalar adapter `dfa_exponent`. Các algorithms khác ngoài scope chưa triển khai. Numerical core không tự phân loại alpha hoặc tìm crossover.

```python
from src.ews_metrics import (
    gaussian_detrend,
    kendall_tau,
    lag1_autocorrelation,
    rolling_metric,
)

residual, trend = gaussian_detrend(time_series, bandwidth=50)
values, positions = rolling_metric(
    residual,
    lag1_autocorrelation,
    window_size=200,
    alignment="endpoint",
)
tau = kendall_tau(values, positions)
```

`positions` là zero-based index; notebook cộng 1 khi vẽ observation numbers.
Không xem overlapping windows là independent observations. Endpoint alignment
chỉ áp dụng cho metric; Gaussian smoother toàn chuỗi vẫn không causal.

Từ root repository, cài [requirements.txt](../requirements.txt)
vào môi trường Python 3.12, chọn kernel `.venv/bin/python`, rồi Run All notebook.
Notebook đã chạy 19 code cells, không có error outputs, chứa 10 đồ thị inline.
Scientific assertions kiểm tra equilibrium roots, fold, seed reproducibility,
integration refinement và vectorized/reference trajectories đã đạt. Một bước
reference validation hiển thị sai số của ACF/Pearson/OLS/SD/CV/moments và kiểm
tra return-rate/sinusoid normalization trước khi mô phỏng. Mỗi phần phân tích
có mục đích, cách đọc output, điều rút ra và lý do chuyển sang bước tiếp theo.

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python -m pytest tests -q
.venv/bin/ruff check src/ews_metrics.py tests/test_ews_metrics.py \
    experiments/dakos_2012.ipynb --select E,F,I --line-length 79
```

Kết quả được đọc trực tiếp trong notebook: simulation diagnostics, preprocessing
figure, rolling trajectories và tau tables, indicators mở rộng, PSD đầu/cuối,
DFA reference/Figure 3/F(s) plots và window sensitivity tables,
sensitivity heatmaps/regions, toàn bộ ARMA AIC candidates/warnings, surrogate
tau distributions/significance, từng ensemble seed và paper-comparison table.

Các biến trong RAM phục vụ việc inspect sau Run All: `csd`, `flickering`,
`records`, `trajectories`, `sensitivity`, `sensitivity_rows`, `arma_candidates`,
`surrogate_taus`, `ensemble_rows`, `comparison_rows`, `dfa_trajectories`,
`dfa_rows`, `dfa_sensitivity_rows` và `summary`. Bản tổng hợp
`summary` là dictionary trong RAM, không phải file JSON. Không có export helper
hoặc export toggle. Lưu notebook với inline outputs giữ câu chuyện và kết quả
ngay trong một tài liệu, không cần generated result files.

Đã chạy notebook từ working directory `experiments/` và so sánh project files
trước/sau: không tạo hay thay đổi file nào khác ngoài notebook được lưu với
outputs, và không tạo thư mục `results/`. Core regression suite vẫn đạt
**183 tests**, Ruff E/F/I với line length 79 đạt.

## H. Final assessment

1. **Numerical correctness:** các functions đã qua 183 automated tests và
   reference comparisons theo conventions được công bố.
2. **Qualitative reproduction:** khớp CSD collapse/rising ACF, flickering
   regimes, SD hump, increasing skewness và DFA trend direction; CSD residual SD, DFA strength/critical behavior chưa khớp đầy đủ.
3. **Quantitative reproduction:** chưa đạt exact curves/tau/p-values; đã ghi
   computed values, differences và model/preprocessing assumptions.
4. **Unresolved limitations:** thiếu simulation configuration gốc, red-noise
   ambiguity, near-boundary ARMA fit, stochastic convergence chưa kiểm tra,
   full Figure 11 grid deferred. Không báo cáo complete paper reproduction.
