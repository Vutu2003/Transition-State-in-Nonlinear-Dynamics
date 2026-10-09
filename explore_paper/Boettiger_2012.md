
# Boettiger & Hastings (2012) — Quantifying Limits to Detection of Early Warning for Critical Transitions

**Journal:** Journal of the Royal Society Interface, 9, 2527–2539  
**DOI:** 10.1098/rsif.2012.0125  
**Type:** Methodological / Statistical Evaluation  
**Core concepts:** EWS, model comparison, likelihood ratio, parametric bootstrap, ROC, false positives, false negatives.

---

## 1. Central Problem — Có EWS chưa chắc cảnh báo đáng tin

Các nghiên cứu trước (Scheffer, Dakos) cho thấy khi hệ tiến gần critical transition, những indicators như autocorrelation và variance có thể tăng:

$$
x(t)\rightarrow M(t)\rightarrow \tau
$$

Trong đó $M(t)$ là EWS trajectory và $\tau$ là Kendall's tau đo monotonic trend.

**Nhưng một increasing trend không đồng nghĩa với reliable detection:**

- **False positive (FP):** Hệ ổn định nhưng xuất hiện EWS.
- **False negative (FN):** Hệ tiến gần transition nhưng không xuất hiện EWS rõ ràng.

Ví dụ: Một stable system trong Figure 6 vẫn có rising autocorrelation với $\tau=0.7$.

**Research question:**

> Làm thế nào định lượng khả năng phân biệt một stable system với một approaching-transition system, đồng thời đo false-alarm và missed-detection rates?

---

## 2. Why Traditional EWS Can Fail — Năm hạn chế

### 2.1. Hidden dynamical assumptions

Classical EWS thường dựa trên cơ chế:

$$
\text{Approaching saddle-node}
\rightarrow \text{Critical slowing down}
\rightarrow \uparrow AR(1),\ \uparrow Variance
$$

Nhưng transition còn có thể xảy ra do large perturbations, noise-induced basin escape hoặc parameter changes quá nhanh.

**EWS signature không phải bằng chứng duy nhất của cơ chế transition.**

### 2.2. Arbitrary rolling windows

Lý thuyết thường dự đoán changes in ensemble statistics; thực tế thường chỉ có một trajectory, nên phải dùng sliding windows:

$$
x(t)\rightarrow M(t)
$$

Window length, overlap và preprocessing ảnh hưởng đến kết quả. Đồng thời, mỗi window cần đủ stationary để ước lượng metrics, trong khi toàn bộ hệ đang thay đổi.

### 2.3. Trend is not detection reliability

Kendall's $\tau$ định lượng xu hướng nhưng không trực tiếp cung cấp false-positive/false-negative rates.

### 2.4. Problematic null models

- Standard Kendall significance tests có thể vi phạm independence do temporal dependence và overlapping windows.
- Random shuffling phá hủy autocorrelation tự nhiên.
- Parametric surrogates tốt hơn ở một số khía cạnh nhưng phụ thuộc model assumptions.

### 2.5. Limited statistical power

Một indicator có thể tăng trước transition nhưng vẫn không phân biệt đáng tin giữa $H_0$ và $H_1$ khi dữ liệu hữu hạn.

**Takeaway:** Indicator correctness, statistical significance và detection performance là ba vấn đề khác nhau.

---

## 3. Proposed Solution — EWS as Model Comparison

Thay vì chỉ kiểm tra một metric có tăng hay không, tác giả xây dựng hai competing dynamical hypotheses:

| Hypothesis | Dynamics | Interpretation |
|---|---|---|
| $H_0$ | Constant stability | Stable system |
| $H_1$ | Declining stability | Approaching saddle-node bifurcation |

### 3.1. Dynamical foundation

Saddle-node normal form:

$$
\frac{dx}{dt}=r_t-x^2
$$

Với $r_t>0$, stable equilibrium là $x^*=\sqrt{r_t}$.

Local linear recovery rate có độ lớn:

$$
\lambda_{\mathrm{recovery}}=2\sqrt{r_t}
$$

Khi $r_t\rightarrow0^+$:

$$
\lambda_{\mathrm{recovery}}\rightarrow0
\quad\Rightarrow\quad
\text{Critical slowing down}
$$

### 3.2. Two stochastic models

**$H_0$ — Constant-stability Ornstein–Uhlenbeck model**

$$
dX_t=r(u-X_t)\,dt+\sigma\,dB_t
$$

Trong đó $r>0$ là constant recovery rate, $u$ là equilibrium mean và $\sigma$ là noise amplitude.

**$H_1$ — Approaching saddle-node**

Bifurcation parameter giảm theo thời gian:

$$
r_t=r_0-mt,\qquad m>0
$$

Tác giả sử dụng stochastic dynamics gần stable equilibrium:

$$
dX_t=
\sqrt{r_t}\bigl(f(r_t)-X_t\bigr)\,dt
+\sigma\sqrt{f(r_t)}\,dB_t
$$

Trong đó $f(r_t)=u+\sqrt{r_t}$; các hệ số và conventions cần giữ đúng theo Equation (3.2) khi triển khai.

**Interpretation:** $H_0$ giả định recovery rate không đổi; $H_1$ giả định recovery rate suy giảm khi tiến gần bifurcation.

> Cặp models này chỉ nhắm đến một trường hợp B-tipping cụ thể. Nó không phải detector tổng quát cho N-tipping hoặc R-tipping.

---

## 4. Statistical Workflow — From Time Series to Detection Reliability

### Step 1 — Fit both models using maximum likelihood

Với observations $X=\{x_1,\ldots,x_n\}$:

$$
\log L(M)=
\sum_{i=2}^{n}
\log P(x_i\mid x_{i-1},\Delta t_i,M)
$$

Ước lượng parameters tối ưu riêng cho $H_0$ và $H_1$.

- OU model: conditional moments có nghiệm giải tích.
- Time-varying model: moment equations được giải số để tính likelihood.

### Step 2 — Compare models using deviance

$$
\boxed{d=2(\log\widehat L_1-\log\widehat L_0)}
$$

$d$ lớn: dữ liệu ủng hộ $H_1$ mạnh hơn so với $H_0$.

Nhưng **deviance đơn lẻ chưa cho biết detection error rates**.

### Step 3 — Parametric simulation / bootstrap

1. Fit $H_0$ và $H_1$ trên observed time series.
2. Generate 500 realizations từ mỗi fitted model.
3. Refit **cả hai models** trên từng realization.
4. Compute deviance $d$ cho mọi realization.
5. Thu được hai distributions:

$$
P(d\mid H_0),\qquad P(d\mid H_1)
$$

Nếu hai distributions overlap nhiều, detection khó; nếu tách biệt, discrimination tốt hơn.

### Step 4 — Evaluate ROC and error trade-off

Với decision threshold $c$, cảnh báo khi $d>c$:

$$
\mathrm{FPR}(c)=P(d>c\mid H_0)
$$

$$
\mathrm{TPR}(c)=P(d>c\mid H_1)
$$

Trong đó:

- **FPR:** False alarm rate.
- **TPR / Sensitivity:** Tỷ lệ phát hiện đúng approaching-transition cases.
- **FNR = 1 − TPR:** Missed-detection rate.

Thay đổi threshold $c$ tạo thành **ROC curve** (TPR vs. FPR).

**Tại sao không chỉ dùng AIC hoặc p-value?**

AIC so sánh model fit và complexity nhưng không trực tiếp định lượng FP/FN. Một significance threshold cũng chỉ chọn một điểm trên trade-off, thay vì cho thấy toàn bộ detection performance.

---

## 5. Results — What the Figures Demonstrate

### Section 4: Model-based detection

Ba datasets:

| Dataset | Observations | Nature |
|---|---:|---|
| Simulated population | 40 | Nonlinear stochastic birth–death |
| Daphnia chemostat | 16 | Ecological experiment |
| Glaciation | 121 | Antarctic ice-core record |

**Figures 2–4:** Observed time series → model simulations → overlapping deviance distributions.

**Figure 5:** ROC của likelihood-based method. Performance thay đổi mạnh giữa datasets; glaciation cho discrimination tốt nhất trong fitted-model simulations.

### Section 5: Comparison against metric-based EWS

Tác giả tính rolling-window variance và autocorrelation (window size = 50% data length), rồi sử dụng Kendall's $\tau$ để đo trend.

**Figure 6:** Một stable simulation vẫn có autocorrelation trend $\tau=0.7$. Như vậy, positive EWS trend không đảm bảo hệ đang tiến gần transition.

**Figure 7:** Distributions của Kendall's $\tau$ dưới $H_0$ và $H_1$ overlap đáng kể.

**Figure 8:** ROC so sánh variance, autocorrelation và likelihood-based detector. Likelihood thường có discrimination tốt hơn trong các ví dụ được xét.

Tại **FPR = 5%**, True Positive Rates (Table 1):

| Dataset | Variance-based | Likelihood-based |
|---|---:|---:|
| Simulation | 25% | 61% |
| Daphnia | 5% | 34% |
| Glaciation | 5.4% | 100% |

Các giá trị phản ánh **conditional performance trên simulations từ fitted models**, không phải accuracy đã được xác nhận bằng prospective real-world testing.

---

## 6. Discussion — Contributions and Limitations

### Main contributions

1. Chuyển EWS research từ *detecting expected patterns* sang *quantifying detection errors*.
2. Đưa ra framework model-based likelihood + simulation + ROC.
3. Cho thấy summary-statistic trends có thể thiếu statistical power ngay cả trong điều kiện thuận lợi cho CSD.
4. Chứng minh performance phụ thuộc cả indicator, sampling effort và signal strength.

### Main limitations

- **Mechanism-specific:** Hướng tới slow saddle-node B-tipping; không bao quát N-tipping, R-tipping hay các transitions không có CSD.
- **Model dependence:** FP/FN rates được ước lượng dưới fitted models; model misspecification có thể làm các ước lượng này sai lệch.
- **Data limitations:** Short, noisy observations có thể khiến hai hypotheses khó phân biệt.
- **No universal superiority:** Kết quả không chứng minh likelihood luôn tốt hơn mọi metric-based hoặc nonlinear detector.
- **Detection ≠ event-time prediction:** Phân biệt stable vs. approaching-transition dynamics không tự động dự đoán chính xác thời điểm tipping.

---

## 7. Connection to Previous Papers

| Paper | Scientific role |
|---|---|
| Kuehn (2011) | Mathematical mechanisms of critical transitions |
| Ashwin et al. (2012) | B-, N-, R-tipping taxonomy |
| Scheffer et al. (2009) | Observable EWS signatures |
| Dakos et al. (2012) | Estimating EWS, trend, robustness, significance |
| **Boettiger & Hastings (2012)** | **Quantifying discrimination, false alarms and missed detections** |

### The conceptual progression

$$
\underbrace{x(t)\rightarrow M(t)}_{\text{Estimate indicator}}
\rightarrow
\underbrace{\tau}_{\text{Measure trend}}
\rightarrow
\underbrace{(\mathrm{TPR},\mathrm{FPR})}_{\text{Evaluate detector}}
$$

**Caution:** High Kendall's $\tau$ or a statistically significant EWS trend does not necessarily imply reliable transition detection.

### Final takeaway

> **Boettiger & Hastings (2012) chuyển câu hỏi từ "Indicator có thay đổi trước transition không?" sang "Indicator có phân biệt được hệ ổn định với hệ đang tiến gần transition, với mức độ sai số nào?"**

Đây là nghiên cứu về **reliability of detection**, không phải một universal transition detector.

**Research implication:** Một EWS method chỉ thực sự có ý nghĩa cảnh báo khi cả dynamical assumptions và detection error rates đều được làm rõ.
