
# 8. Farazmand & Sapsis (2018) — Extreme Events: Mechanisms and Prediction

**Journal:** Applied Mechanics Reviews  
**DOI:** 10.1115/1.4042065  
**Type:** Theoretical / Methodological Review  
**Keywords:** Extreme events, chaotic dynamics, rare events, precursors, variational optimization, conditional probability, prediction.

---

## 1. Research Problem — Tại sao Extreme Events khó dự đoán?

Extreme events là những biến cố có giá trị bất thường, có thể xuất hiện đột ngột trong high-dimensional nonlinear dynamical systems.

Ví dụ: rogue waves, turbulent bursts, earthquakes.

**Những thách thức chính:**

- **High-dimensional chaos:** Sensitivity to initial conditions gây hạn chế về prediction horizon.
- **Partial observability:** Không thể đo toàn bộ system state.
- **Model uncertainty:** Governing equations có thể không được biết hoặc không đủ chính xác.
- **Data scarcity:** Extreme events hiếm, gây khó khăn cho learning và statistical validation.

**Research questions:**

1. Những dynamical mechanisms nào tạo ra extreme events?
2. Những observable precursors nào có thể báo trước extreme events?
3. Làm thế nào định lượng reliability của prediction?

### Four Pillars — Figure 1

| Component | Question |
|---|---|
| Mechanisms | Tại sao extreme events hình thành? |
| Real-time Prediction | Làm sao cảnh báo trước từng event? |
| Mitigation | Có thể ngăn chặn hoặc hạn chế event không? |
| Statistics | Event xuất hiện với tần suất và xác suất nào? |

**Paper tập trung vào Mechanisms và Real-time Prediction.**

Extreme Value Theory và Large Deviation Theory chủ yếu hỗ trợ nghiên cứu extreme-event statistics. Chúng không tự động cung cấp real-time prediction cho từng event.

---

## 2. Mathematical Foundation — Extreme Events trong State Space

### 2.1. Dynamical system và observable

Xét một hệ:

$$
\frac{\partial u}{\partial t}=\mathcal N(u)
$$

Với solution map:

$$
u(t)=S^t(u_0)
$$

Trong đó:

- $u(t)\in\mathcal U$: Full system state.
- $\mathcal N$: Governing dynamics.
- $S^t$: Evolution operator.
- $u_0$: Initial state.

Ta thường chỉ quan sát một đại lượng:

$$
x(t)=f(u(t))=f(S^t(u_0))
$$

Ở đây $f:\mathcal U\rightarrow\mathbb R$ là một **observable**.

**Insight:** Observed time series chỉ phản ánh một phần underlying dynamical state.

### 2.2. Extreme Event Set — Definition 1

Định nghĩa threshold $f_e$:

$$
\boxed{
E_f(f_e)=\{u\in\mathcal U:f(u)>f_e\}
}
$$

Extreme event xảy ra khi trajectory đi vào vùng $E_f$ trong state space.

**Figure 2:** Một burst trong time series tương ứng với trajectory đi qua extreme-event region.

Đối với unusually small values, có thể xét observable $-f$.

### 2.3. Extreme Event vs. Rare Transition

| Extreme Event | Rare Transition |
|---|---|
| Observable vượt threshold | Hệ chuyển giữa long-lived states |
| Có thể là transient excursion | Có thể tồn tại lâu ở state mới |
| Không nhất thiết đổi attractor | Có thể là noise-induced switching |
| Định nghĩa phụ thuộc observable và threshold | Định nghĩa dựa trên state/regime dynamics |

**Quan trọng:**

$$
\boxed{
\text{Extreme Event}\neq\text{Critical Transition}
}
$$

Một extreme burst có thể xuất hiện ngay trong cùng một chaotic attractor mà không cần bifurcation.

---

## 3. Routes to Extreme Events — Các cơ chế hình thành

**Central idea:** Những extreme events có hình dạng tương tự trên time series có thể phát sinh từ các dynamical mechanisms khác nhau.

### 3.1. Multiscale Systems — Slow–Fast Bursting

Trong slow–fast systems, dynamics diễn ra ở nhiều time scales.

Slow manifold có hai loại vùng:

- $M_a$: Attracting manifold — hút trajectories.
- $M_r$: Repelling manifold — đẩy trajectories ra xa.

**Bursting mechanism — Figures 4–7:**

$$
\boxed{
\text{Slow Motion}
\rightarrow
\text{Repelling Region}
\rightarrow
\text{Fast Excursion}
\rightarrow
\text{Burst}
\rightarrow
\text{Return}
}
$$

Tác giả sử dụng singular Hopf normal form:

$$
\begin{aligned}
\varepsilon\dot x &= y-x^2-x^3\\
\dot y &= z-x\\
\dot z &= -\nu-ax-by-cz
\end{aligned}
$$

Với $\varepsilon\ll1$, $x$ là fast variable và $y,z$ là slow variables.

Critical manifold:

$$
M_0=\{(x,y,z):y=x^2+x^3\}
$$

Hệ có thể tạo:

- **Periodic bursts:** Stable periodic orbit.
- **Chaotic bursts:** Irregular excursions.

Ví dụ: Coupled FitzHugh–Nagumo oscillators tạo chaotic bursts từ nonlinear coupling.

**Insight:** Burst có thể được sinh ra nội sinh từ slow–fast geometry, không nhất thiết do stochastic shocks.

### 3.2. Homoclinic and Heteroclinic Bursting

Các extreme excursions có thể liên quan đến stable và unstable manifolds quanh saddle-type structures.

**Homoclinic orbit:** Trajectory rời một equilibrium rồi quay lại chính equilibrium đó theo nghĩa tiệm cận.

**Heteroclinic orbit:** Trajectory kết nối hai equilibria khác nhau theo nghĩa tiệm cận.

Ví dụ Shilnikov saddle-focus:

$$
\text{Spiral toward equilibrium}
\rightarrow
\text{Unstable ejection}
\rightarrow
\text{Burst}
$$

Các unstable periodic orbits gần homoclinic connection có thể tạo chaotic bursting.

**Insight:** Extreme events có thể xuất hiện do phase-space geometry của deterministic dynamics.

### 3.3. Noise-Induced Transitions

Trong multistable systems, stochastic perturbations có thể đẩy trajectory vượt qua potential barrier và chuyển sang stable state khác.

Overdamped Langevin dynamics:

$$
dU_t=-\nabla V(U_t)\,dt
+\sqrt{2}\,\sigma(U_t)\,dW_t
$$

Trong đó:

- $V$: Potential landscape.
- $-\nabla V$: Deterministic drift.
- $\sigma\,dW_t$: Stochastic forcing.

Đây là một cơ chế có liên hệ với **noise-induced tipping (N-tipping)**.

#### Transition Path Theory (TPT)

TPT nghiên cứu những reactive trajectories chuyển từ state A sang state B.

**Forward committor:**

$$
q^+(u)=P(\text{Reach B before A}\mid U_0=u)
$$

**Reactive density:**

$$
\rho_{AB}(u)=q^+(u)q^-(u)\rho(u)
$$

Trong đó:

- $q^+$: Forward committor.
- $q^-$: Backward committor.
- $\rho$: Invariant state density.

Reactive probability current giúp xác định những transition pathways có xác suất cao.

**Limitation:** Việc giải các Kolmogorov/Fokker–Planck equations trở nên rất tốn kém trong high-dimensional systems.

### Summary — Section 3

| Mechanism | Origin |
|---|---|
| Slow–fast bursting | Fast excursions gần repelling slow manifold |
| Homoclinic / heteroclinic | Unstable manifold geometry |
| Noise-induced transitions | Stochastic escape giữa stable states |

**Core insight:**

$$
\boxed{
\text{Similar Observed Events}
\not\Rightarrow
\text{Same Underlying Mechanism}
}
$$

Không thể suy luận chắc chắn underlying mechanism chỉ từ hình dạng của một observed spike.

---

## 4. Variational Method — Physics-Based Precursor Discovery

### 4.1. Research Motivation

Các phương pháp geometric analysis ở Section 3 khó áp dụng trực tiếp cho high-dimensional chaotic systems.

**New question:**

> Thay vì tìm toàn bộ attractor geometry, liệu có thể tìm một số initial states có khả năng phát triển thành extreme events?

### 4.2. Extreme Event Domain of Attraction — Definition 2

Tác giả định nghĩa:

$$
\boxed{
A_f(\tau,f_e)=
\left\{
u_0\notin E_f:
\exists t\in(0,\tau],
S^t(u_0)\in E_f
\right\}
}
$$

Đây là tập hợp các non-extreme initial states sẽ đi vào extreme-event region trong vòng $\tau$.

Việc xác định toàn bộ tập này thường không khả thi.

### 4.3. Constrained Variational Optimization

Tác giả đề xuất tìm representative precursor state bằng:

$$
\boxed{
\hat u_0=
\arg\max_{u_0\in\mathcal A}
\left[
f(S^\tau(u_0))-f(u_0)
\right]
}
$$

**Interpretation:**

Trong các initial states có thể xuất hiện trong natural dynamics, trạng thái nào khiến observable tăng mạnh nhất trong khoảng $\tau$?

Có hai constraints:

**1. Physical constraint**

Trajectory phải tuân theo governing equations:

$$
\dot u=\mathcal N(u)
$$

**2. Statistical / Attractor constraint**

Initial state phải nằm trong một approximation của attractor:

$$
\mathcal A=
\{u_0:c_i\le C_i(u_0)\le\bar c_i\}
$$

Constraint thứ hai ngăn optimization lựa chọn những trạng thái phi thực tế, hầu như không xảy ra trong natural dynamics.

**Figure 10:** Những initial states đủ gần optimal precursor cũng có thể tạo extreme events.

**Important distinction:**

- Optimal precursor: Trạng thái tạo mức tăng observable lớn.
- Most probable precursor: Trạng thái xuất hiện với xác suất cao trước events.

Hai khái niệm không nhất thiết trùng nhau.

### 4.4. Application I — Turbulent Kolmogorov Flow

**Problem:** Nguyên nhân nào tạo extreme energy dissipation bursts?

Tác giả sử dụng variational optimization và phân tích Fourier modes.

**Finding:**

- Ba Fourier modes tạo một interacting triad.
- Năng lượng được chuyển từ mode $(1,0)$ sang mode $(0,k_f)$.
- Sự chuyển năng lượng này làm tăng energy input và energy dissipation.

**Figures 11–13:** Extreme bursts được giải thích bằng nonlinear energy transfers giữa các modes.

**Insight:** Precursor discovery có thể giúp xác định những interactions gây ra extreme events.

### 4.5. Application II — Oceanic Rogue Waves

**Problem:** Những localized wave groups nào có thể phát triển thành rogue waves?

Sử dụng nonlinear Schrödinger dynamics và reduced-order approaches.

Mỗi wave group được mô tả bằng:

- Amplitude $A$.
- Length scale $L$.

**Figure 16:** Xác định vùng $(A,L)$ có thể phát triển thành rogue waves và kết hợp với joint probability distribution để tìm dangerous wave groups.

**Insight:** Physically meaningful low-dimensional features có thể chứa predictive information về high-dimensional dynamics.

**Note:** Đây chủ yếu là ứng dụng các reduced-order methods đã được phát triển trong những nghiên cứu trước, không phải reproduction trực tiếp toàn bộ optimization ở Section 4.1.

### Limitations — Section 4

- Cần governing equations đủ chính xác.
- Optimization có thể có nhiều local optima.
- Kết quả phụ thuộc constraints, observable và time horizon.
- Một precursor state không tự động trở thành reliable real-time predictor.

---

## 5. Prediction of Extreme Events — Từ Precursors đến Reliable Indicators

### 5.1. Target Observable vs. Predictive Indicator

Tác giả phân biệt:

- $f(u)$: Target observable có extreme events.
- $g(u)$: Predictive indicator đo ở hiện tại.

Định nghĩa **future maximum**:

$$
\boxed{
f_m(u;t_1,t_2)=
\max_{t_1\le s\le t_2} f(S^s(u))
}
$$

Trong đó:

- $t_1$: Prediction horizon.
- $[t_1,t_2]$: Future prediction window.
- $f_e$: Extreme-event threshold.

Future event xảy ra nếu:

$$
f_m(u;t_1,t_2)>f_e
$$

**Prediction objective:**

$$
\boxed{
g(u_t)
\rightarrow
P(\text{Future Extreme Event})
}
$$

Indicator không nhất thiết có monotonic rising trend. Điều cần thiết là nó mang thông tin về một future event cụ thể.

### 5.2. Conditional Statistics — Definition 3

Tác giả dùng joint PDF của $(f_m,g)$ và conditional PDF để định nghĩa:

$$
\boxed{
P_{\mathrm{ee}}(g_0)=
P(f_m>f_e\mid g=g_0)
}
$$

Đây là xác suất xảy ra extreme event trong future window khi biết giá trị indicator hiện tại.

Một reliable predictor cần phân biệt được future extreme và non-extreme states.

**Figure 18 — Prediction outcomes:**

| Prediction | Actual Event | Outcome |
|---|---|---|
| No alarm | No event | Correct rejection |
| Alarm | Event | Correct prediction |
| No alarm | Event | False negative |
| Alarm | No event | False positive |

Một indicator liên tục cảnh báo sẽ phát hiện nhiều events nhưng gây nhiều false positives.

Một indicator không bao giờ cảnh báo sẽ tránh false positives nhưng bỏ sót tất cả events.

**Do đó, cần đánh giá cả hai loại prediction errors.**

### 5.3. Application — Kolmogorov Flow

Từ mechanism ở Section 4, tác giả đề xuất:

$$
g(u)=-|a(1,0)|
$$

Khi Fourier mode $(1,0)$ mất năng lượng, indicator tăng, báo trước sự gia tăng extreme energy dissipation.

**Figure 19:** Conditional event probability tăng mạnh khi indicator đạt vùng nguy hiểm, cho phép short-term prediction.

### 5.4. Application — Rogue Waves

Indicator được xây dựng bằng cách nhận diện các wave groups nằm trong dangerous amplitude–length-scale region.

**Figure 20:** Indicator có predictive information nhưng vẫn tồn tại false negatives.

**Insight:**

$$
\boxed{
\text{Mechanism-Informed Indicator}
\not\Rightarrow
\text{Perfect Prediction}
}
$$

Prediction horizon phụ thuộc vào dynamics và thường bị giới hạn bởi chaotic predictability.

### 5.5. Data-Driven Indicator Discovery

Đây là một open research direction quan trọng.

**Research question:**

> Nếu governing equations không được biết, liệu có thể tự động tìm một reliable predictive indicator từ observed data?

Tác giả xây dựng một **failure-rate objective**:

$$
\begin{aligned}
\mathcal L(g;g_e,t_1,t_2)
={}&P(f_m>f_e\mid g<g_e)\\
&+P(f_m<f_e\mid g>g_e)
\end{aligned}
$$

Trong đó:

- $g$: Candidate indicator.
- $g_e$: Alarm threshold.
- $t_1,t_2$: Prediction window.

**Optimization objective:**

$$
\boxed{
\min_{g,g_e,t_1,t_2}
\mathcal L(g;g_e,t_1,t_2)
}
$$

Nghĩa là đồng thời tối ưu:

1. **What to observe?** — Indicator $g$.
2. **When to alarm?** — Threshold $g_e$.
3. **How far ahead?** — Prediction window.

**Important:** $\mathcal L$ là tổng hai xác suất lỗi có điều kiện, không phải overall misclassification probability.

### Research Status

Paper **chưa giải quyết optimization problem này**.

Các khó khăn còn mở:

- Không gian candidate indicators rất lớn.
- Objective nonlinear và nonsmooth.
- Limited prediction horizon trong chaotic dynamics.
- Observability constraints: Indicator phải thực sự đo được.
- Thiếu dữ liệu về rare events.

**Contribution:** Đề xuất mathematical formulation cho việc discovery of data-driven reliable indicators, chưa phải một validated learning algorithm.

---

## 6. Synthesis — Storytelling của toàn bộ nghiên cứu

Logic của paper:

**Step 1 — Research Problem**

Extreme events xuất hiện hiếm và bất ngờ trong nonlinear chaotic systems.

**Step 2 — Dynamical Interpretation**

Một extreme event tương ứng với trajectory đi vào một vùng extreme-event set trong state space.

**Step 3 — Mechanism Understanding**

Các extreme events có thể được tạo ra bởi:

- Slow–fast instabilities.
- Homoclinic / heteroclinic dynamics.
- Noise-induced transitions.
- Nonlinear energy transfers.

**Step 4 — Precursor Discovery**

Dùng governing equations và statistical constraints để tìm initial states có khả năng tạo extreme events.

**Step 5 — Predictor Design**

Chuyển hiểu biết về precursors thành measurable indicators $g(u)$.

**Step 6 — Reliability Assessment**

Định lượng:

$$
P(\text{Future Event}\mid\text{Current Indicator})
$$

và đánh giá false positives, false negatives, prediction horizon.

**Step 7 — Open Direction**

Tìm indicator trực tiếp từ observed data thông qua optimization of predictive failure rate.

### Complete Research Logic

$$
\boxed{
\begin{gathered}
\text{Extreme Event Definition}\\
\downarrow\\
\text{Mechanism Understanding}\\
\downarrow\\
\text{Precursor-State Discovery}\\
\downarrow\\
\text{Measurable Predictor Design}\\
\downarrow\\
\text{Probabilistic Reliability Assessment}
\end{gathered}
}
$$

**Cần lưu ý:** Đây là research logic được tổng hợp từ paper, không phải một pipeline thống nhất đã được kiểm chứng trên mọi hệ.

---

## 7. Scientific Contribution & Limitations

### Main Contributions

1. Tổng hợp các dynamical mechanisms sinh extreme events.
2. Phân biệt extreme bursts với rare transitions.
3. Trình bày variational optimization để tìm precursor states.
4. Minh họa mechanism discovery trong turbulent flows và rogue waves.
5. Định nghĩa conditional probability của future extreme events.
6. Đề xuất optimization formulation cho data-driven indicator discovery.

### Main Limitations

- Các cơ chế được nghiên cứu không đại diện cho mọi extreme events.
- Mechanism discovery thường phụ thuộc governing equations.
- High-dimensional state-space analysis rất tốn kém.
- Chaos giới hạn prediction horizon.
- Reliable indicators không tồn tại hoặc không quan sát được trong mọi hệ.
- Data-driven indicator optimization mới được đề xuất, chưa có general solution.
- Framework chủ yếu xét autonomous dynamical systems.

**Không có universal extreme-event prediction algorithm trong paper này.**

---

## 8. Position in the Literature & Phase 2A

### So sánh với các nghiên cứu trước

| Paper | Central Question |
|---|---|
| Kuehn (2011) | Critical transitions xuất hiện thế nào trong fast–slow dynamics? |
| Ashwin et al. (2012) | Những cơ chế tipping khác nhau là gì? |
| Scheffer et al. (2009) | Những generic EWS signatures nào có thể xuất hiện? |
| Dakos et al. (2012) | Làm thế nào tính và đánh giá EWS trends? |
| Boettiger & Hastings (2012) | Làm thế nào đánh giá detection reliability? |
| Scheffer et al. (2012) | Structure và dynamics bổ sung nhau thế nào? |
| **Farazmand & Sapsis (2018)** | **Làm thế nào tìm mechanisms, precursors và dự đoán từng extreme event?** |

### Hai hướng phân tích cần phân biệt

**Classical EWS:**

$$
x(t)\rightarrow M(t)
\rightarrow\text{Trend Detection}
$$

**Event-Specific Prediction:**

$$
x(t)\rightarrow g(t)
\rightarrow
P(\text{Event in Future Window}\mid g(t))
$$

Hai cách tiếp cận không loại trừ nhau.

Classical EWS thường quan tâm đến changes in stability; event-specific prediction quan tâm đến khả năng một observable vượt ngưỡng trong một khoảng thời gian xác định.

### Relevance to Phase 2A

**Conceptual contribution:**

Không nên tự động đồng nhất:

- Extreme burst.
- Rare transition.
- Regime switching.
- Critical transition.
- Bifurcation-induced tipping.

**Methodological contribution:**

Có thể nghiên cứu transition dynamics theo hướng:

$$
\text{Past/Present Signal Features}
\rightarrow
\text{Future Event Risk}
$$

Nhưng nếu áp dụng trên physiological time series, cần có:

- Operational event definition.
- Reliable event labels.
- Measurable precursors.
- Explicit prediction horizon.
- Out-of-sample validation.
- Evaluation of false positives and false negatives.

Đây là hướng suy rộng cho Phase 2A, không phải một phương pháp đã được paper chứng minh trên EEG, ECG hoặc PPG.

---

## 9. Final Takeaway

> **Farazmand & Sapsis (2018) chuyển trọng tâm từ việc nhận diện những dấu hiệu thống kê bất thường sang việc hiểu các dynamical mechanisms tạo ra extreme events, tìm precursor states và định lượng khả năng dự đoán các events trong tương lai.**

Ba distinctions quan trọng nhất:

1. **Extreme event không đồng nghĩa critical transition.**
2. **Precursor discovery không đồng nghĩa reliable prediction.**
3. **Predictive correlation không đồng nghĩa identification of underlying mechanism.**

$$
\boxed{
\text{Mechanisms}
\rightarrow
\text{Precursors}
\rightarrow
\text{Indicators}
\rightarrow
\text{Probabilistic Prediction}
}
$$

**Research classification:** Mechanism-oriented and prediction-oriented methodological review.

**Reproduction decision:** Không cần reproduction toàn paper. Nên lưu lại và có thể triển khai riêng conditional event prediction framework ở Section 5 khi đã có operational event definitions và dữ liệu phù hợp.

**Most valuable concepts to retain:**

- Extreme-event set $E_f$.
- Finite-time precursor set $A_f$.
- Variational precursor optimization.
- Future maximum $f_m$.
- Conditional event probability $P_{\mathrm{ee}}$.
- Indicator failure-rate optimization $\mathcal L$.
