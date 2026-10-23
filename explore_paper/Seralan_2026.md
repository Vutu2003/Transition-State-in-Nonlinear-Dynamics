**Complexity measures: Characterization of transition to extreme events in dynamical systems — Seralan et al. (2026)**

Vinoth Seralan, S. Leo Kingston, Suresh Kumarasamy, Ajit Mahata, Karthikeyan Rajagopal và Tomasz Kapitaniak. *Chaos* **36**, 083153 (2026), published online 28 August 2026. DOI: [10.1063/5.0304782](https://doi.org/10.1063/5.0304782).

*Nguồn duy nhất: [PDF được cung cấp](</home/vutu0809/Desktop/PHASE2/paper/12 Complexity measures-- Characterization of transition to extreme events in dynamical systems.pdf>). Dẫn chiếu theo số trang article, không tính trang bìa PDF. Năm trong tên file theo publication year 2026, không theo submission year 2025. Đánh giá reproduction là đánh giá thông tin được báo cáo, chưa phải chạy lại simulations.*

Một khó khăn trong nhận diện extreme events là rare bursts và frequent large-amplitude chaos có thể đạt maximum amplitudes gần như nhau. Chỉ nhìn độ lớn cực đại, thậm chí một giá trị trung bình mô tả dynamics, chưa đủ để phân biệt chúng. Seralan et al. bắt đầu từ đặc điểm thời gian của extremes: hệ thường ở trong một vùng nominal behavior, nhưng thỉnh thoảng xuất hiện excursions lớn và ngắn. Research question là **liệu sự khác biệt giữa các finite-time segments có thể tách extreme-event regimes khỏi các dạng non-extreme dynamics và xác định transition trong parameter space hay không?** [Sec. I]

Paper phát triển từ những nghiên cứu dùng mean recurrence time (MRT), đồng thời dẫn Das et al. về complexity kết hợp entropy với disequilibrium. Core idea ở đây là chuyển sự chú ý từ magnitude của một measure sang **variance của measure ấy giữa các windows**. Hai đại lượng được sử dụng là variance of mean recurrence time, $V_{\mathrm{MRT}}$, và variance of normalized Shannon entropy, $V_{\mathrm{ENT}}$. Khi rare bursts chỉ làm thay đổi dynamics trong một số windows, các windows có thể khác nhau rõ rệt; khi large events lặp thường xuyên, variation giữa windows có thể giảm. Đây là finite-time fluctuation interpretation mà bài dùng để giải thích kết quả, được kiểm tra bằng simulations trên nhiều models. [Secs. I–II]

Methodology bắt đầu bằng việc chia time series thành $k$ non-overlapping segments có duration cố định $T$. Trong mỗi segment $j$, tác giả trích local maxima thành peak sequence $E^{(j)}$, rồi tính riêng MRT và entropy. Sau đó mới tính variance trên $k$ giá trị của mỗi measure. Cần giữ đúng thứ tự này: đây không phải variance của amplitudes toàn signal, cũng không phải variance của mọi individual recurrence times trong một RP. [Sec. II, tr. 2–3]

MRT được tính từ white vertical line lengths trong recurrence plot của peak sequence:

$$
\mathrm{MRT}(E^{(j)})
=\frac{\sum_{l=1}^{N}l\,p_j(l)}{\sum_{l=1}^{N}p_j(l)}.
$$

Đây là Eq. (1), viết thêm subscript $j$ để làm rõ mỗi window có distribution riêng. White gaps ghi nhận những khoảng chưa recurrence; lấy average của chúng cho biết mức điển hình của khoảng recurrence trong segment. Paper dùng Euclidean distance và recurrence threshold bằng 30% standard deviation của signal. Vì RP được dựng trên sequence of peaks, không nên tự đồng nhất line length với physical time tính bằng giây; bài không đưa một phép chuyển đổi qua timestamps giữa các peaks. [Sec. II.A]

Entropy dùng cùng peak sequence nhưng hỏi một câu khác: amplitudes phân bố thế nào? Với $m$ equal-width bins trong khoảng $[\min E^{(j)},\max E^{(j)}]$, normalized Shannon entropy là:

$$
\mathrm{ENT}(E^{(j)})
=-\frac{1}{\log_2m}\sum_{i=1}^{m}p_i^{(j)}\log_2p_i^{(j)}.
$$

Eqs. (2)–(3) lượng hóa amplitude probabilities trong từng window. ENT này không phải recurrence time entropy (RTE): nó không dùng distribution của white vertical gaps. Sự khác nhau ấy quan trọng vì hai branches của methodology quan sát hai mặt khác nhau của dynamics — recurrence structure và amplitude distribution — trước khi áp dụng cùng một phép tổng hợp. [Sec. II.B]

Phép tổng hợp chính là sample variance:

$$
V_{\mathrm{MRT}}
=\frac{1}{k-1}\sum_{j=1}^{k}
\left[\mathrm{MRT}(E^{(j)})-\overline{\mathrm{MRT}}\right]^2,
$$

và $V_{\mathrm{ENT}}$ được tính tương tự bằng cách thay MRT bằng ENT. Trực giác của Eq. (4) là đo **sự không đồng đều giữa các local descriptions của cùng một record**. Một hệ có MRT lớn nhưng gần như không đổi giữa windows vẫn có variance nhỏ; một hệ chỉ thỉnh thoảng có windows khác biệt mạnh có thể có variance lớn. Chính sự tách biệt giữa level và fluctuation này là đóng góp trung tâm của paper. [Sec. II.C]

Brusselator được dùng đầu tiên để thiết lập baseline. Với $\mu=0.2$, $\alpha=1.114$, forcing frequency $\omega=0.69$ và forcing amplitude $I$ tăng dần, model đi qua period-doubling tới bounded chaos. MRT có thể khác nhau giữa periodic attractors và nhỏ hơn trong bounded chaos; ENT tăng khi xuất hiện chaotic motion. Tuy vậy, variances gần zero ở periodic dynamics và chỉ nhỏ trong bounded chaos. Kết quả này cho thấy một measure có level cao không tự động chỉ ra extremes, và bounded chaos vẫn có thể có fluctuations giữa windows tương đối nhỏ. [Eq. (5); Fig. 1; Sec. III.A]

Khi tăng $I$ xa hơn, interior-crisis-induced intermittency tạo rare excursions từ bounded chaotic region. Tác giả mô tả cơ chế là chaotic attractor va chạm unstable periodic orbits, trajectory có những bursts rồi quay lại vùng bounded motion. Các regimes được báo cáo gồm extreme events ở khoảng $I\in(0.0520,0.0545)$ và frequent large-amplitude dynamics ở $I\in(0.0546,0.056)$. Qualifier threshold $Q_{\mathrm{th}}=\langle x_{\max}\rangle+6\sigma$ được dùng để đối chiếu phân loại này. [Fig. 2; Sec. III.B]

Ở đây xuất hiện phép thử quan trọng nhất cho core idea: MRT của extreme regime và frequent large-amplitude regime có thể gần nhau, còn ENT riêng lẻ không phát hiện đầy đủ extreme region. Ngược lại, $V_{\mathrm{MRT}}$ và $V_{\mathrm{ENT}}$ cao trong extreme regime, thấp ở cả bounded chaos lẫn frequent large-amplitude chaos. Những phase diagrams ở Fig. 3 tiếp tục cho thấy vùng variance cao tương ứng với vùng extreme events trong một parameter space rộng hơn. Đây là evidence về sự phù hợp giữa indicators và regions được xác định từ dynamics cùng threshold, chưa phải một classification test trên independent data. [Figs. 2–3]

CO$_2$ laser kiểm tra cùng ý tưởng trong một dynamical setting khác. Theo mô tả của tác giả, rare pulses xuất hiện do grazing–sliding bifurcation gần discontinuous boundary $x=0$, thay vì interior crisis của Brusselator. Khi modulation parameter $\epsilon$ thay đổi trong khoảng $(1.625,1.685)$, model đi từ bounded chaos qua rare extremes tới frequent large-intensity events. MRT và ENT có những xu hướng riêng: chẳng hạn ENT gần một trong chaotic regime rồi giảm trong extreme regime, nên entropy cao nhất không phải tiêu chí nhận diện extremes. Tuy nhiên, cả hai variances vẫn cao trong extreme region và thấp ở non-extreme regions; Fig. 5 kiểm tra thêm trên parameter plane $(\epsilon,r)$. Đây là interpretation và numerical evidence mà paper báo cáo, không phải một derivation của grazing–sliding mechanism từ variance. [Eq. (6); Figs. 4–5; Sec. III.C]

Hai examples sau chuyển từ chaotic baseline sang periodic hoặc quasiperiodic baseline. Trong SQUID trimer gồm ba magnetically coupled devices, rare bursts xuất hiện từ quasiperiodic motion khi damping parameter giảm đến $\gamma=0.0234$. Bài gọi route này là quasiperiodic intermittency và dùng $Q_{\mathrm{th}}=\langle\phi_{1\max}\rangle+4\sigma$. Variances thấp trong quasiperiodic regime, tăng trong intermittent extreme regime, rồi giảm khi large-amplitude chaos trở nên thường xuyên. Trong coupled Hindmarsh–Rose neurons, PM intermittency xuất hiện tại coupling $k=0.0532$, với observable $x_{\parallel}=x_1+x_2$; hai variances cũng tăng trong rare bursting regime. [Eqs. (7)–(8); Figs. 6–7; Sec. IV]

HR model đặc biệt cho thấy không thể thay thế variance bằng một quy tắc tăng hoặc giảm chung của MRT. MRT có magnitude cao ở các periodic attractors, giảm khi chuyển sang extreme bursting rồi saturation ở frequent large-amplitude chaos. Trong khi đó, $V_{\mathrm{MRT}}$ vẫn thấp–cao–thấp qua ba regimes tương ứng. Kết quả cần giữ là mức độ fluctuating giữa windows, không phải phát biểu “extremes luôn làm MRT tăng” cho mọi system. [Fig. 7(b); Sec. IV.B]

Phạm vi kiểm tra có thể nhìn qua bốn dynamical settings:

| Model | Route được paper mô tả | Evidence chính cho variance measures |
| --- | --- | --- |
| Brusselator | Interior-crisis-induced intermittency | Tách rare extremes khỏi bounded và frequent large-amplitude chaos; có parameter-plane comparison |
| CO$_2$ laser | Grazing–sliding bifurcation | Cùng xu hướng variance dù mechanism khác Brusselator; có parameter-plane comparison |
| SQUID trimer | Quasiperiodic intermittency | Variance tăng ở rare bursts rồi giảm khi large events thường xuyên |
| Coupled Hindmarsh–Rose | Pomeau–Manneville intermittency | Variance phân biệt rare bursting dù MRT giảm từ periodic regime |

Appendix bổ sung time series và PDFs để đối chiếu sự tồn tại của rare large events. Tác giả mô tả heavy-tail distributions trong Brusselator, laser và SQUID; với HR, họ dùng thuật ngữ dragon-kings-like distribution vì có hump trong tail. Những mô tả đó không đi kèm power-law exponent estimation hay statistical comparison giữa các tail models. **Heavy tail, một đường cong trên log scale và power-law scaling là những kết luận khác nhau; paper này không xác lập critical exponents hoặc một power-law relation cho các variance measures.** [Figs. 8–9; Appendix]

Tương tự, recurrence condensation không phải khái niệm được triển khai trong nghiên cứu này. Phần RQA được khai thác tập trung vào MRT và variance của MRT, không phải sự tập trung recurrence times về một dominant period, cũng không phải bộ DET, LAM, TT hoặc diagonal entropy. Dynamical interpretation của bài là intermittent variation giữa finite-time segments. Các kết quả numerical ủng hộ interpretation này trong các systems được thử, nhưng paper không chứng minh variance cao chỉ có thể do extreme events hoặc cho một universal cutoff phân biệt mọi loại nonstationarity.

Methodological contribution nằm ở một bước chuyển đơn giản nhưng có ích: thay vì dùng một average descriptor để đại diện toàn dynamics, xét fluctuations của descriptor trên các segments. Sự đồng thuận giữa $V_{\mathrm{MRT}}$ và $V_{\mathrm{ENT}}$, cùng numerical examples thuộc bốn models, hỗ trợ tính áp dụng vượt ra ngoài một system. Tuy nhiên, kết luận của tác giả rằng indicator là “model-independent” cần được giới hạn theo evidence: bài cho thấy consistency trong các examples, không chứng minh model independence cho mọi nonlinear process. Nó cũng không báo cáo sensitivity analysis có hệ thống theo window duration, recurrence threshold, bin count, record length hay measurement noise. [Secs. II–V]

Paper có tuyên bố cải thiện hạn chế của công trình Das et al. trong việc phân biệt extreme events với large-amplitude chaos. Phần kết quả trực tiếp so sánh MRT/ENT với variances tương ứng và đối chiếu bifurcation diagrams. Bài không trình bày một benchmark tính đồng thời $C=SD$ và hai variance measures trên cùng datasets với classification metrics. Vì vậy, đóng góp được hỗ trợ rõ là tính hữu ích của finite-time variance trong các examples, chưa đủ để xếp hạng tổng quát phương pháp này cao hơn entropy–disequilibrium complexity. [Sec. I; Sec. III.B]

Trong classical EWS literature, đây là một approach về regime characterization và transition identification có khả năng phục vụ forecasting trong tương lai. Mặc dù có chữ “variance”, $V_{\mathrm{MRT}}$ và $V_{\mathrm{ENT}}$ là variance của derived measures, không phải variance trực tiếp của state variable. Paper không liên hệ chúng với critical slowing down, recovery rate hoặc lag-1 autocorrelation, cũng không kiểm tra warning lead time, false alarms hay out-of-sample event prediction. High variance được quan sát trong records đã có extreme bursts; việc định vị transition bằng parameter sweep chưa chứng minh khả năng cảnh báo trước event đầu tiên hoặc dự báo thời điểm burst kế tiếp. [Secs. I, V]

Về reproduction, paper công bố model equations, nhiều parameter values, công thức MRT/ENT/variance, non-overlapping segmentation và threshold rule $\varepsilon=0.3\sigma$. Nhưng hai lựa chọn rất quan trọng cho finite-time statistics — numerical window duration $T$ và số windows $k$ — không được báo cáo cụ thể; số entropy bins $m$ cũng chỉ xuất hiện dưới dạng ký hiệu. Bài chưa làm rõ đầy đủ standard deviation cho recurrence threshold được lấy theo từng segment hay toàn record, cùng các chi tiết xử lý RP boundaries và windows có ít peaks. Vì vậy, workflow có thể lập trình lại, còn exact numerical reproduction không thể chỉ dựa vào công thức variance.

Ngoài ra, numerical solver, time step, simulation length, transient removal và initial conditions chưa được mô tả đầy đủ. Một số model details được chuyển sang references thay vì cung cấp trọn vẹn trong paper. Data availability ghi dữ liệu hỗ trợ nằm trong article; điều này không đồng nghĩa article đi kèm raw time-series files hoặc executable code, và PDF không dẫn public code repository. Đánh giá hợp lý là bài cung cấp một methodological recipe và evidence bằng figures, nhưng cần thêm implementation details để tái tạo chính xác kết quả. Đóng góp có sức thuyết phục nhất là finite-time fluctuations giúp phân biệt rare excursions với frequent large events trong các models khảo sát; predictive validity và generalization vẫn là các bước chưa được kiểm chứng.
