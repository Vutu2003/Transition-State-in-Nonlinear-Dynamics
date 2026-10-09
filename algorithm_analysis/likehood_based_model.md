
# Likelihood-Based Model Comparison — Core Methodology

**Nguồn:** Boettiger & Hastings (2012)  
**Keywords:** Likelihood, MLE, hypothesis testing, model comparison, likelihood ratio, bootstrap, ROC.

## 1. Central Idea — Từ quan sát sang kiểm tra giả thuyết

Một hiện tượng quan sát được có thể được giải thích bởi nhiều cơ chế khác nhau.

Thay vì chỉ đo một đặc trưng của dữ liệu, **likelihood-based model comparison** đặt câu hỏi:

> Dữ liệu quan sát được phù hợp với cơ chế nào hơn, trong số những cơ chế được mô hình hóa?

Giả sử có hai competing hypotheses:

- **H₀:** Dữ liệu được tạo bởi model M₀.
- **H₁:** Dữ liệu được tạo bởi model M₁.

Mỗi model mô tả một giả thuyết về quá trình sinh dữ liệu (data-generating process).

## 2. Likelihood — Đo mức độ phù hợp của dữ liệu

Với observed data $X$ và model $M_j$:

$$
L_j(\theta_j;X)=p(X\mid\theta_j,M_j)
$$

Trong đó:

- $X$: Observed data, được giữ cố định.
- $M_j$: Probabilistic model.
- $\theta_j$: Model parameters.
- $L_j$: Likelihood của parameters khi đã quan sát $X$.

**Lưu ý quan trọng:**

$$
P(X\mid H_j)\neq P(H_j\mid X)
$$

Likelihood không phải xác suất một giả thuyết đúng.

## 3. Maximum Likelihood Estimation (MLE)

Vì model parameters thường chưa biết, ta tìm bộ parameters khiến observed data có likelihood lớn nhất:

$$
\boxed{
\hat{\theta}_j
=
\arg\max_{\theta_j}
\log L_j(\theta_j;X)
}
$$

Thực hiện độc lập cho cả $M_0$ và $M_1$.

**Kết quả:** Hai fitted models, mỗi model được tối ưu để giải thích cùng một dataset.

## 4. Likelihood-Ratio Comparison

So sánh maximum likelihood của hai models bằng deviance:

$$
\boxed{
D=2\left[
\log L_1(\hat{\theta}_1;X)
-
\log L_0(\hat{\theta}_0;X)
\right]
}
$$

- $D$ lớn và dương: model $M_1$ fit dữ liệu tốt hơn $M_0$.
- $D$ gần 0: hai models có mức độ phù hợp tương tự.
- $D$ âm: $M_0$ fit tốt hơn, nếu hai models không nested.

**Nhưng:** Likelihood ratio không tự động cho biết statistical significance hoặc detection reliability. Model phức tạp hơn cũng có thể đạt likelihood cao hơn nhờ nhiều parameters.

## 5. Quantifying Uncertainty — Bootstrap + ROC

Trong Boettiger & Hastings, tác giả sử dụng **parametric bootstrap**:

1. Fit $M_0$ và $M_1$ trên observed data.
2. Generate nhiều synthetic datasets từ mỗi fitted model.
3. Refit cả hai models trên từng dataset.
4. Tính deviance $D$ cho từng realization.
5. Xây dựng hai distributions:

$$
p(D\mid M_0),\qquad p(D\mid M_1)
$$

Hai distributions overlap càng nhiều thì khả năng phân biệt hai hypotheses càng thấp.

Với threshold $c$, cảnh báo $H_1$ khi $D>c$:

$$
\mathrm{FPR}(c)=P(D>c\mid M_0)
$$

$$
\mathrm{TPR}(c)=P(D>c\mid M_1)
$$

Thay đổi $c$ tạo **ROC curve**, mô tả trade-off giữa false alarms và successful detections.

Đây là cách chuyển từ **model fit** sang **detection reliability**.

## 6. Generalization — Không giới hạn ở Critical Transitions

| Application | Model M₀ | Model M₁ |
|---|---|---|
| Time-series analysis | Stationary process | Time-varying process |
| Signal detection | Noise only | Signal + noise |
| Nonlinear dynamics | Linear stochastic dynamics | Nonlinear stochastic dynamics |
| Change-point detection | Constant parameters | Changing parameters |
| Physiological coupling | Constant coupling | Time-varying coupling |
| EWS detection | Stable recovery rate | Declining recovery rate |

**Likelihood-based comparison là framework thống kê tổng quát.** OU và saddle-node SDE chỉ là hai dynamical models cụ thể được Boettiger & Hastings lựa chọn.

## 7. Three Levels of Scientific Inference

Cần phân biệt:

1. **Model fit:** Model giải thích observed data tốt đến đâu?
2. **Model discrimination:** Có thể phân biệt các competing models đáng tin đến mức nào?
3. **Mechanism identification:** Model được lựa chọn có thực sự đại diện cho cơ chế sinh dữ liệu không?

Một model có likelihood cao hơn chưa chứng minh đó là true mechanism.

$$
\boxed{
\text{Better model fit}
\not\Rightarrow
\text{True mechanism}
}
$$

Kết luận phụ thuộc vào model assumptions, identifiability, data quality và những alternative hypotheses được đưa vào so sánh.

---

## Final Takeaway

Quy trình tổng quát:

$$
\boxed{
\begin{aligned}
&\text{Observed data}\\
&\downarrow\\
&\text{Competing probabilistic models}\\
&\downarrow\\
&\text{Maximum likelihood estimation}\\
&\downarrow\\
&\text{Likelihood-ratio comparison}\\
&\downarrow\\
&\text{Bootstrap / statistical evaluation}\\
&\downarrow\\
&\text{Detection reliability}
\end{aligned}
}
$$

**Bài học cốt lõi:**

> Likelihood-based model comparison giúp đánh giá dữ liệu ủng hộ giả thuyết nào hơn. Bootstrap và ROC giúp đánh giá khả năng phân biệt các giả thuyết đó. Tuy nhiên, phân biệt tốt các models không đồng nghĩa với chứng minh cơ chế thực sự.

**Model comparison ≠ Mechanism identification.**
