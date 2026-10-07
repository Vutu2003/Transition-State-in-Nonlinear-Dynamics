# Kuehn (2011) — Key Notes

## 1. Critical transition và fast–slow dynamics

**Critical transition** có thể được hiểu bằng **fast–slow dynamics**: một biến hoặc tham số thay đổi chậm có thể đưa hệ tiến dần tới vùng mất ổn định, sau đó trajectory chuyển nhanh sang một trạng thái khác.

Dạng tổng quát của một **fast–slow system**:

$$
\dot{x}=f(x,y),
\qquad
\dot{y}=\epsilon g(x,y),
\qquad
0<\epsilon\ll1
$$

Trong đó:

- $x$: biến phản ứng nhanh;
- $y$: biến hoặc tham số thay đổi chậm;
- $\epsilon$: mức phân tách giữa hai time scales.

**Ý nghĩa:** hệ có thể thay đổi chậm trong một thời gian dài, sau đó xuất hiện một thay đổi nhanh khi cấu trúc ổn định không còn duy trì được trajectory.

$$
\text{slow parameter drift}
\rightarrow
\text{loss of stability}
\rightarrow
\text{fast transition}
$$

---

## 2. Bifurcation không đồng nghĩa với observed transition

**Bifurcation point** là nơi cấu trúc động lực học thay đổi, nhưng trajectory thực tế không nhất thiết chuyển đúng tại đó.

Có thể tồn tại **bifurcation delay**:

$$
\text{bifurcation point}
\neq
\text{observed transition time}
$$

Hệ có thể vượt qua điểm mất ổn định rồi mới chuyển trạng thái sau đó.

**Ý nghĩa:** thời điểm cơ chế động lực học thay đổi và thời điểm ta quan sát thấy transition có thể khác nhau.

---

## 3. Critical slowing down

Khi stability suy yếu, hệ hồi phục chậm hơn sau một **perturbation**.

Gần một trạng thái cân bằng, perturbation nhỏ $u$ có thể được mô tả gần đúng bởi:

$$
\dot{u}\approx \lambda u
$$

Nếu:

$$
\lambda<0
$$

thì perturbation suy giảm và hệ quay lại trạng thái cân bằng.

Khi tiến gần transition:

$$
\lambda\rightarrow0^{-}
$$

thì lực phục hồi yếu dần và recovery trở nên chậm hơn.

Do đó:

$$
\text{stability}\downarrow
\rightarrow
\text{recovery rate}\downarrow
\rightarrow
\text{recovery time}\uparrow
$$

Đây là **critical slowing down**.

Critical slowing down là cơ sở lý thuyết cho một số dấu hiệu trước transition.

---

## 4. Variance và autocorrelation

Khi recovery chậm hơn:

- **variance** có thể tăng;
- **autocorrelation** có thể tăng vì perturbation tồn tại lâu hơn.

Trong mô hình tuyến tính có additive noise, variance gần equilibrium có dạng trực giác:

$$
\operatorname{Var}(x)
\approx
\frac{\sigma^2}{2|\lambda|}
$$

Trong đó:

- $\sigma$: cường độ noise;
- $|\lambda|$: độ mạnh của lực phục hồi.

Khi:

$$
|\lambda|\downarrow
$$

thì với cùng mức noise:

$$
\operatorname{Var}(x)\uparrow
$$

Tương tự, autocorrelation ở độ trễ $\tau$ có dạng gần đúng:

$$
\rho(\tau)\approx e^{\lambda\tau}
$$

Khi:

$$
\lambda\rightarrow0^{-}
$$

thì:

$$
\rho(\tau)\uparrow
$$

**Trực giác:** perturbation mất nhiều thời gian hơn để biến mất, nên system vừa dao động rộng hơn vừa giữ “memory” lâu hơn.

Nhưng:

$$
\boxed{
\text{variance/autocorrelation increase}
\neq
\text{proof of critical transition}
}
$$

Chúng chỉ là **indicators có điều kiện**, phụ thuộc vào mechanism, noise và cách đo.

---

## 5. Noise có thể làm transition xảy ra sớm

Noise không chỉ là nhiễu đo.

Trong stochastic dynamical systems, noise có thể đẩy trajectory ra khỏi trạng thái hút **trước khi deterministic bifurcation point được đạt tới**.

$$
\text{noise}
+
\text{weakening stability}
\rightarrow
\text{early escape}
$$

Vì vậy:

$$
\text{observed transition time}
$$

phụ thuộc không chỉ vào stability mà còn vào:

$$
\text{noise level}
+
\text{time-scale separation}
$$

**Ý nghĩa:** một observed transition không nhất thiết xảy ra vì attractor vừa mất stability; noise có thể làm trajectory thoát sớm hơn.

---

## 6. Single time series và sliding window có thể làm méo indicator

Lý thuyết thường mô tả ensemble hoặc probability distribution, nhưng dữ liệu thực tế thường chỉ có **single sample path**.

Khi dùng **sliding window**:

$$
x(t)
\rightarrow
M(t)
$$

ta không quan sát trực tiếp theoretical quantity mà đang tạo ra một **finite-time estimate**.

Indicator có thể bị ảnh hưởng bởi:

- window length;
- background trend;
- estimator bias;
- temporal dependence;
- geometry của trajectory.

Do đó:

$$
\boxed{
\text{theoretical indicator}
\neq
\text{finite-window estimate}
}
$$

Ngoài ra:

$$
\boxed{
\text{ensemble trend}
\neq
\text{individual trajectory trend}
}
$$

Một indicator trung bình có thể tăng, nhưng một single trajectory vẫn có thể cho trend ngược lại.

**Ý nghĩa cho time-series analysis:** trajectory của metric quan sát được là kết quả kết hợp giữa underlying dynamics và properties của estimator/window.

---

# One-line takeaway

$$
\boxed{
\text{slow drift}
\rightarrow
\text{weaker stability}
\rightarrow
\text{slower recovery}
\rightarrow
\text{changed fluctuations}
\rightarrow
\text{transition}
}
$$

**Nhưng mọi mũi tên đều phụ thuộc vào mechanism, noise và measurement.**

---

# Công thức cần nhớ

Chỉ cần nhớ ý nghĩa của bốn quan hệ sau:

$$
\dot{x}=f(x,y),
\qquad
\dot{y}=\epsilon g(x,y),
\qquad
0<\epsilon\ll1
$$

→ biểu diễn **fast–slow dynamics**.

$$
\dot{u}\approx\lambda u,
\qquad
\lambda\rightarrow0^{-}
$$

→ stability suy yếu và recovery chậm lại.

$$
\operatorname{Var}(x)
\approx
\frac{\sigma^2}{2|\lambda|}
$$

→ recovery yếu hơn có thể làm variance tăng.

$$
\rho(\tau)\approx e^{\lambda\tau}
$$

→ recovery chậm hơn có thể làm autocorrelation tăng.

Không cần học derivation của các công thức này ở giai đoạn hiện tại; điều quan trọng là hiểu **phenomenon mà chúng biểu diễn**.