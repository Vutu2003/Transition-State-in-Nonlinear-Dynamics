**Recurrence Condensation During Critical Transitions in Complex Systems — Jella et al. (2025)**

Manaswini Jella, Induja Pavithran, Vishnu R. Unni, Norbert Marwan, Jürgen Kurths và R. I. Sujith. *Chaos* **35**, 083107 (2025). DOI: [10.1063/5.0267157](https://doi.org/10.1063/5.0267157).

*Bản tổng hợp chỉ dựa trên [PDF được cung cấp](</home/vutu0809/Desktop/PHASE2/paper/10 Recurrence condensation during critical transitions in complex systems.pdf>). Số trang dưới đây theo article, từ 083107-1 đến 083107-14, không tính hai trang bìa PDF. Các đánh giá về giới hạn bằng chứng và reproduction dựa trên những phân tích và thông tin mà paper báo cáo.*

Trong turbulent combustor, trạng thái nguy hiểm xuất hiện khi acoustic pressure chuyển từ low-amplitude chaotic fluctuations sang high-amplitude self-sustained periodic oscillations. Trạng thái dao động có tổ chức này được gọi là thermoacoustic instability và có thể đe dọa thiết bị. Khó khăn mà Jella et al. đặt ra là transition này đi qua intermittency: những đoạn dao động tương đối đều đặn xen kẽ với chaotic fluctuations, khiến việc xác định một critical point từ dữ liệu nhiễu trở nên không rõ ràng. Nghiên cứu vì thế tìm một dấu hiệu phản ánh sự tổ chức lại của dynamics, đồng thời có thể giúp định vị transition trong control-parameter space. [Sec. I, tr. 2–3]

Research question có hai lớp gắn với nhau: **cấu trúc recurrence thay đổi thế nào khi hệ chuyển từ chaos sang periodicity, và có thể dùng quy luật biến thiên của các recurrence measures để xác định critical parameter hay không?** Ý tưởng phát triển từ spectral condensation — năng lượng phân bố trên nhiều frequencies tập trung vào một dominant mode — và công trình trước về power-law scaling của recurrence quantification analysis (RQA) measures ở period-doubling transitions. Do đó, đóng góp cần tìm ở cách diễn giải và khai thác recurrence trong transition này; các công cụ phân tích và ý tưởng scaling của recurrence measures đã có tiền lệ được chính paper dẫn lại. [Sec. I, tr. 2–3; Sec. IV, tr. 12]

Tác giả gọi sự thay đổi đang quan sát là **recurrence condensation**. Ở combustion noise, recurrence plot (RP) chứa các diagonal lines ngắn, đứt đoạn, với spacing biến thiên; tại intermittency, các cấu trúc có trật tự xuất hiện theo từng patches; đến thermoacoustic instability, những diagonal lines dài và liên tục chiếm ưu thế. Hai đặc trưng bổ sung nhau: diagonal length phản ánh thời gian mà hai trajectory segments duy trì evolution tương tự, còn spacing giữa các lines phản ánh recurrence time scales. Condensation ở đây là sự tập trung từ nhiều recurrence time scales về một dominant time scale. [Fig. 2; Sec. III.A, tr. 7–8]

Để quan sát quá trình ấy, tác giả giữ fuel flow rate ở 28 SLPM và tăng air flow rate quasi-statically từ 410 đến 650 SLPM, theo bước 10 SLPM. Reynolds number tăng từ khoảng $2.13\times10^4$ đến $3.18\times10^4$; acoustic pressure được lấy mẫu ở 10 kHz trong 3 s. Phase space reconstruction dùng Cao’s algorithm để chọn embedding dimension và average mutual information để chọn time delay, với Euclidean norm khi xác định recurrence. Dữ liệu cho phép so sánh dynamics tại những control-parameter values khác nhau. [Secs. II.A, II.C; Sec. III.A]

Một lựa chọn methodology quyết định cách đọc kết quả là **tách threshold dùng để visualization khỏi threshold dùng để tính RQA**. Fig. 2 dùng $\varepsilon$ bằng 20% attractor size để thể hiện nhiều time scales; các đoạn được vẽ dài lần lượt 1 s, 1 s và 0.1 s. Với RQA, tác giả điều chỉnh $\varepsilon$ để giữ $RR=0.05$, nghĩa là recurrence points tương ứng với 5% pairwise distances nhỏ nhất. Measures được tính trên windows 1500 data points rồi lấy trung bình; $l_{\min}=v_{\min}=k_{\min}=2$. Vì RR đã được cố định, kết quả cần đọc qua cách recurrence points tổ chức thành line structures, không thể diễn giải condensation thành RR tăng. [Sec. II.C, tr. 4; Fig. 2; Sec. III.B, tr. 8]

Để làm rõ dominant time scale, tác giả dùng $\tau$-recurrence rate:

$$
\tau\text{-RR}=\frac{1}{N-\tau}\sum_{i=1}^{N-\tau}R_{i,i+\tau}.
$$

Trực giác của Eq. (4) là giữ cố định một lag $\tau$, rồi hỏi tỷ lệ các cặp trạng thái cách nhau đúng lag ấy recurrent. Như vậy, diagonal structures trở thành một đường biểu diễn những recurrence lags nổi bật. Tại periodic oscillations, Fig. 2(III-E) vẫn cho thấy một spike train, với peaks lặp đều; câu diễn giải trong bài rằng $\tau$-RR trở thành một “constant value” cần được đọc cùng hình này. Điều được thể hiện là một nhịp recurrence chi phối, không phải $\tau$-RR bằng nhau ở mọi lag. [Sec. II.D; Fig. 2; Sec. III.A]

Inter-spike spectrum (ISS) làm rõ hơn nhịp lặp đó. Appendix phân rã $\tau$-RR trên các Dirac combs có inter-spike periods khác nhau, dùng LASSO để chọn sparse loadings; regularization được chọn với Pearson correlation giữa signal và reconstruction là $\rho=0.9$. Có thể hiểu đây là việc tìm một số ít nhịp lặp đủ để biểu diễn spike train. ISS chuyển từ nhiều contributions sang một dominant peak ở Fig. 2(F), cung cấp bằng chứng trực tiếp cho recurrence condensation. ISS ở đây không phải histogram của recurrence times, cũng không phải Fourier spectrum thông thường. [Appendix, Eq. (A1), tr. 13]

Về dynamical interpretation, kết quả cho thấy recurrence ngày càng có tổ chức khi hệ hình thành periodic oscillations. Tác giả lưu ý dominant acoustic mode vốn đã hiện diện trước transition, nên sự thay đổi quan trọng là mức độ chi phối của một time scale. Tuy nhiên, việc combustion noise là high-dimensional deterministic chaos contaminated with colored noise được bài dựa vào các nghiên cứu trước. Paper hiện tại phân tích một acoustic-pressure observable; nó không trực tiếp xác lập lại toàn bộ spatiotemporal dynamics hoặc chứng minh mọi degrees of freedom đã quy về một mode. Liên hệ với spectral condensation là một analogy có ý nghĩa diễn giải, chưa phải một equivalence được chứng minh. [Secs. I, III.A]

RQA bổ sung cho ISS bằng cách mô tả những khía cạnh khác nhau của sự tổ chức ấy. Chẳng hạn, determinism (DET) và average diagonal line length (L) có cùng tử số nhưng trả lời hai câu hỏi khác nhau:

$$
DET=\frac{\sum_{l=l_{\min}}^N lP(l)}{\sum_{l=1}^N lP(l)},
\qquad
L=\frac{\sum_{l=l_{\min}}^N lP(l)}{\sum_{l=l_{\min}}^N P(l)}.
$$

Trong Eqs. (5)–(6), trọng số $l$ chuyển số lượng diagonal lines thành số recurrence points nằm trên chúng. $DET$ hỏi bao nhiêu recurrence points thuộc những diagonal segments đủ dài; $L$ hỏi một segment như vậy kéo dài trung bình bao lâu. Cả hai có xu hướng tăng trong thí nghiệm, phù hợp với sự duy trì evolution tương tự lâu hơn. Đây là evidence về sự đều đặn và predictability theo cách diễn giải RQA, không phải bằng chứng hệ chuyển từ stochastic sang deterministic: trạng thái ban đầu đã được tác giả xem là chaotic. [Sec. II.D; Sec. III.B; Fig. 3]

Phần gắn trực tiếp hơn với recurrence condensation nằm ở recurrence time $RT$ và recurrence time entropy $RTE$:

$$
RT=\frac{\sum_{k=k_{\min}}^N kP(k)}{\sum_{k=k_{\min}}^N P(k)},
\qquad
RTE=-\sum_{k=k_{\min}}^N p(k)\ln p(k).
$$

Ở Eqs. (10)–(11), $k$ là độ dài vertical white line, biểu diễn khoảng không recurrence giữa các recurrence points. $RT$ đo average gap; $RTE$ đo uncertainty của phân bố những gaps ấy. Cả hai giảm khi tiến đến thermoacoustic instability: các lần recurrence trung bình gần nhau hơn và recurrence times ít phân tán hơn. Chính thành phần thứ hai mới giúp phân biệt việc average return time giảm với việc nhiều time scales tập trung về một nhịp chi phối. [Sec. II.D; Sec. III.B; Fig. 3(g–h)]

Các measures còn lại làm rõ vì sao không thể gộp mọi thay đổi thành một “entropy giảm”. Diagonal line entropy $Entr=-\sum p(l)\ln p(l)$ có cùng Shannon form với RTE nhưng áp dụng cho diagonal lengths; nó **tăng ban đầu rồi mới giảm**, phản ánh sự biến thiên của loại cấu trúc này qua transition. Trong khi đó, laminarity $LAM$ và trapping time $TT$ đều giảm, tương ứng với vertical black lines ít chi phối hơn và ngắn hơn. Periodicity tăng vẫn phù hợp với local trapping giảm: duy trì chuyển động đều đặn quanh một orbit khác với lưu lại lâu trong một neighborhood. Vì vậy, DET, Entr, LAM, TT, RT và RTE cung cấp những góc nhìn bổ sung; mỗi measure không tự nó chứng minh toàn bộ hệ chỉ còn một time scale. [Eqs. (7)–(9); Fig. 3; Sec. III.B]

Từ mô tả dynamics, bài chuyển sang câu hỏi khó hơn: làm thế nào đặt một critical point vào quá trình biến đổi tương đối liên tục này? Tác giả nhận thấy absolute differences của measures có thể được fit theo power law. Công thức bài viết là:

$$
|a-a_c|=|Re-Re_c|^{\lambda},
\qquad a_c=a(Re_c).
$$

Ở đây, $a$ là một measure, còn $a_c$ là giá trị của chính measure tại candidate critical parameter. Trực giác là chuyển gốc của cả control parameter lẫn measure về một candidate point rồi khảo sát quan hệ trên log–log scale; $\lambda$ là slope của quan hệ ấy. Vì dùng absolute differences, công thức không trực tiếp cho biết measure gốc tăng hay giảm. Đây cũng là scaling của độ lệch so với một reference value, không phải phân bố power-law của recurrence times. [Sec. III.B, tr. 9–10]

Quy trình thực hiện là lần lượt coi mỗi sampled $Re$ như một candidate $Re_c$, lấy measures ở các parameter values trước đó trừ đi giá trị tại candidate, rồi fit power law. Tác giả chọn candidate cho fitting error nhỏ nhất, được mô tả đồng thời qua minimum uncertainty của $\lambda$. Trong thí nghiệm, $DET,Entr,LAM,TT,RT,RTE$ cho good fit tại $Re_c=2.96\times10^4$; bài cũng báo cáo minimum uncertainty của $p'_{\mathrm{rms}}$ tại điểm này. Như vậy, nét mới của thao tác này là dùng chất lượng scaling để xác định reference point, thay vì chỉ mô tả rằng một indicator thay đổi trước transition. [Figs. 3–4; Sec. III.B]

Ý nghĩa của kết quả phải giữ đúng phạm vi: **$Re_c=(2.96\pm0.069)\times10^4$ vẫn nằm trong intermittency**, như caption Fig. 3 nêu rõ. Nó không đồng nhất với trạng thái limit cycle oscillations (LCO) được minh họa tại $Re=3.09\times10^4$ ở Fig. 2. Đây trước hết là critical point được xác định bằng tiêu chí scaling của paper; thí nghiệm không cung cấp một bifurcation point độc lập để đối chiếu. Giá trị uncertainty đi kèm $Re_c$ cũng không được trình bày như một confidence interval suy ra từ thủ tục chọn critical point.

Chất lượng bằng chứng không đồng đều giữa measures. $L$ không nằm trong danh sách experimental measures có minimum uncertainty tại critical point chung; Fig. 4(c) báo cáo exponent $0.30\pm0.91$, với uncertainty lớn. $Entr$ lại có exponent âm, $-0.14\pm0.05$. Những kết quả này cần được đọc như empirical fits trên phạm vi dữ liệu đã phân tích. Paper không đưa ra analytic derivation cho exponents hay chứng minh một asymptotic scaling law đúng tùy ý gần critical point. [Fig. 4; Sec. III.B]

Để kiểm tra liệu critical point do fitting chọn có ý nghĩa bifurcation hay không, tác giả chuyển sang một noisy nonlinear oscillator:

$$
\ddot{\eta}+\alpha\dot{\eta}+\omega^2\eta
=\dot{\eta}\left(\beta+K\eta^2-\gamma\eta^4\right)+\xi,
\qquad
\langle\xi(t)\xi(t+\tau)\rangle=\Gamma\delta(\tau).
$$

Eq. (1) đặt linear damping cạnh nonlinear feedback và additive white noise, cho phép khảo sát oscillatory transition trong một model có Hopf point đã biết. Paper dùng $\omega=2\pi\times120$ rad/s, $\beta=50$ rad/s, $\Gamma=10$, và giảm $\alpha$ từ 80 xuống 45 rad/s. Các giá trị được báo cáo là $K=9,\gamma=0.7$ cho subcritical case và $K=-9,\gamma=-0.7$ cho supercritical case. Đây là model kiểm tra cách nhận diện critical point; tác giả nói rõ nó không nhằm tái tạo đầy đủ experimental combustor. [Sec. II.B; Sec. III.C]

Trong subcritical case, amplitude có abrupt jump, trong khi nhiều RQA measures biến đổi trước khi đạt LCO. Trong supercritical case, amplitude tăng dần. Với cả hai, nhiều measures chọn $\alpha_c=50$, trùng Hopf point được paper xác định; caption Fig. 6 nêu cụ thể $DET,L,LAM,TT,RT,RTE$ cho subcritical case. Đây là bằng chứng numerical quan trọng nhất cho ý nghĩa của tiêu chí fitting: nó khôi phục known bifurcation point trong các model được thử. Kết quả không chứng minh experimental combustor nhất thiết có cùng bifurcation mechanism. [Figs. 5–8; Sec. III.C]

Đồng thời, các exponents thay đổi giữa experiment và models. Một số giá trị báo cáo trong Figs. 4, 6 và 8 cho thấy rõ điều đó:

| Measure | Thermoacoustic experiment | Noisy subcritical Hopf | Noisy supercritical Hopf |
| ------- | ------------------------: | ---------------------: | -----------------------: |
| $DET$ |           $0.57\pm0.05$ |        $0.44\pm0.05$ |          $0.50\pm0.05$ |
| $TT$  |           $0.25\pm0.06$ |        $0.45\pm0.04$ |          $0.43\pm0.04$ |
| $RT$  |           $0.36\pm0.03$ |        $0.56\pm0.07$ |          $0.65\pm0.07$ |

Các dấu $\pm$ giữ theo uncertainty tác giả báo cáo; paper không xác định rõ chúng là loại confidence interval nào. Fig. 9 và phần discussion cũng thừa nhận exponents khác nhau. Vì thế, nhận xét của tác giả về tính universal của scaling laws nên được hiểu ở mức khả năng xuất hiện scaling trong nhiều transition pathways; paper chưa xác lập một universal exponent hay universality class. Tương tự, broader applicability sang những complex systems khác vẫn là triển vọng, vì dữ liệu kiểm tra ở đây gồm một thermoacoustic experiment và hai trường hợp của cùng oscillator model. [Secs. III.C, IV]

Đánh giá methodological contribution, bài kết nối được ba bước có ích: một dynamical interpretation mang tên recurrence condensation; một bộ measurements mô tả sự tổ chức lại của recurrence; và một cách chọn critical parameter qua power-law fit, có đối chiếu với known Hopf points. Tuy nhiên, bằng chứng cho bước cuối vẫn là empirical. Paper không báo cáo so sánh với alternative fitting functions, kiểm định thống kê riêng để phân biệt power law với các dạng quan hệ khác, hoặc một sensitivity analysis có hệ thống theo threshold, window length và noise intensity. Vì vậy, minimum fitting uncertainty là tiêu chí đã hoạt động trong các trường hợp được trình bày, chưa phải một điều kiện được chứng minh là đủ để nhận diện critical point nói chung. [Secs. III–IV]

Đặt trong classical early warning signals (EWS) literature, đóng góp của bài phù hợp với một **recurrence-based approach bổ sung cho việc characterization và critical-point identification**. Chính introduction đặt RQA trong dòng nghiên cứu EWS đã tồn tại. Bài không phân tích critical slowing down, không liên hệ RQA scaling với recovery rate, và không benchmark với variance hoặc lag-1 autocorrelation. Đặc biệt, $RT$ trong bài là recurrence time, nên kết quả $RT$ giảm không thể được dùng như một phép kiểm chứng hoặc bác bỏ critical slowing down. Trong phạm vi nguồn này, chưa có căn cứ để kết luận phương pháp vượt trội classical EWS. [Secs. I–III]

Bằng chứng early warning cụ thể là nhiều measures thay đổi trước fully developed periodic oscillations. Còn việc tìm critical point dựa trên quét candidate parameters, sử dụng cả measure tại candidate và so sánh chất lượng fits; paper không trình bày một prospective forecasting protocol với lead time, false-alarm rate hay out-of-sample validation. Vì vậy, cần phân biệt khả năng nhận ra precursor variation mà các hình thể hiện với khả năng dự báo trước một unknown critical point bằng dữ liệu đang đến. Khả năng thứ hai chưa được kiểm chứng trong nghiên cứu này.

Về reproduction, paper cung cấp một workflow khá rõ ở cấp ý tưởng: experimental sampling, control-parameter range, cách chọn embedding, hai threshold protocols, window size, minimal line lengths, các công thức RQA, oscillator equation và tham số, cùng cách dựng ISS. Những thông tin đó đủ làm nền cho một independent implementation. Tuy nhiên, PDF chưa báo cáo actual embedding dimensions và delays, window stride/overlap, numerical solver và time step của model, simulation duration, transient removal hay random seeds. Phần fitting cũng chưa định nghĩa đầy đủ cách tính uncertainty của $\lambda$ và regression specification. Đây là khoảng trống trong reporting, không phải kết quả của một lần reproduction thất bại.

Data availability chỉ ghi dữ liệu được cung cấp từ corresponding author upon reasonable request; paper không dẫn public code repository. Vì vậy, đánh giá hợp lý là có thể tái triển khai logic của phương pháp, còn exact numerical và figure reproduction cần dữ liệu gốc cùng implementation details từ tác giả. Giá trị được hỗ trợ rõ nhất của nghiên cứu nằm ở việc biến sự tập trung của recurrence time scales thành một mô tả có thể đo lường, rồi dùng empirical scaling để định vị transition; phạm vi predictive validity và generalization vẫn cần được kiểm tra thêm.
