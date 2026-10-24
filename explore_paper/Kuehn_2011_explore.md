# Kuehn (2011) — Khung toán học cho chuyển tiếp tới hạn: phân nhánh, hệ nhanh–chậm và động lực học ngẫu nhiên

**Bài báo:** Christian Kuehn, *A mathematical framework for critical transitions: Bifurcations, fast–slow systems and stochastic dynamics* — “Một khung toán học cho chuyển tiếp tới hạn: phân nhánh, hệ nhanh–chậm và động lực học ngẫu nhiên”. *Physica D* **240** (2011), 1020–1035. DOI ghi trong PDF: 10.1016/j.physd.2011.02.012.

**Nguồn và quy ước dẫn trang:** Chỉ sử dụng [PDF được chỉ định](<../paper/1 A mathematical framework for critical transitions: Bifurcations, fast–slow systems and stochastic dynamics.pdf>). Đã đọc toàn bộ 16 trang PDF, gồm phần thảo luận và danh mục tài liệu, đồng thời đối chiếu trực quan các trang gốc, công thức trọng tâm và Hình 1–14. Trang PDF 1–16 tương ứng trang tạp chí 1020–1035; không có bìa riêng. Mọi số trang bên dưới là **trang tạp chí**. Không sử dụng web và không đọc các tài liệu ngoài được bài báo trích dẫn.

Bài báo nối ba lớp lập luận: phân nhánh mô tả sự mất ổn định của hệ với tham số cố định; hệ nhanh–chậm đưa sự trôi của tham số vào động lực học; động lực học ngẫu nhiên giải thích dao động và sự thoát trước khi đạt ngưỡng tất định. Trên nền đó, tác giả khảo sát phương sai và tự tương quan như các **dấu hiệu cảnh báo sớm** (*early-warning signals*, EWS). Đóng góp chính là cách tổ chức và cụ thể hóa khung phương pháp luận này, kèm các ví dụ giải tích, hình học và mô phỏng dạng chuẩn. Bài chưa cung cấp một bộ dự báo sự kiện đã được đánh giá ngoài mẫu hoặc trên dữ liệu thực. [Tóm tắt, tr. 1020; Mục 1, tr. 1021; Mục 10, tr. 1033–1034]

Trong bản phân tích, **Tác giả khẳng định (Authors claim)** chỉ phát biểu của bài; **Bằng chứng hỗ trợ (Evidence supports)** chỉ mức kết luận thực sự được công thức hoặc mô phỏng hỗ trợ; **Diễn giải của người phân tích (Analyst interpretation)** chỉ suy luận và đề xuất bổ sung. Đã thực hiện Prompt 02: sửa trực tiếp các diễn giải cần giới hạn và bổ sung kiểm định phản biện ở cuối cùng tệp. Các bất nhất của PDF được ghi cạnh nội dung liên quan; công thức do người phân tích suy ra được đánh dấu rõ, không gán cho tác giả.

## 1. Từ động cơ ứng dụng đến câu hỏi phương pháp luận

Tác giả mở đầu bằng những chuyển đổi nhanh trong hệ sinh thái, khí hậu, thị trường tài chính và y học, trong đó có **cơn hen và động kinh.** Đặc trưng làm việc gồm sự thay đổi định tính đột ngột, diễn ra nhanh hơn động lực học thông thường, vượt một ngưỡng và đưa hệ ra xa trạng thái cũ. Tác giả đồng thời giả định một thành phần tất định chi phối cùng dao động ngẫu nhiên nhỏ. Đây là bối cảnh và giả định khởi đầu; PDF không phân tích dữ liệu của bốn lĩnh vực này để xác nhận cùng một cơ chế. [Mục 1, tr. 1020–1021]

Vấn đề tác giả nêu là các quan sát như **hồi phục chậm, phương sai tăng, bất đối xứng tăng và tự tương quan tăng** cần được đặt trong một mô hình động lực học chính xác. Phân tích bằng mô hình tự hồi quy đã được dùng trước đó, nhưng chưa tự giải thích loại phân nhánh, vai trò của hai thang thời gian, độ trễ sau mất ổn định hay sự thoát do nhiễu. Bài phát triển một cách đọc dựa trên phương trình để làm rõ những điều kiện này. Đó là động cơ lý thuyết, không phải một kết quả so sánh cho thấy phương pháp thống kê trước đó có độ chính xác thấp hơn. [Mục 1, tr. 1021]

Câu hỏi khoa học xuyên suốt là: **khi nào một hệ có tham số biến thiên chậm chuyển từ chuyển động chậm ổn định sang chuyển động nhanh, và những đại lượng quan sát trước chuyển tiếp phản ánh cơ chế đó trong điều kiện nào?** Câu hỏi được tách thành bốn phần: định nghĩa chuyển tiếp; phân loại phân nhánh; bổ sung độ trễ và nhiễu; đối chiếu đại lượng lý thuyết với ước lượng từ chuỗi hữu hạn. [Mục 2–4, tr. 1021–1027; Mục 7–9, tr. 1030–1034]

**Tác giả khẳng định:** các lý thuyết toán học tiêu chuẩn có thể tạo một nền tảng thống nhất cho nhiều dấu hiệu được quan sát trong ứng dụng. **Bằng chứng hỗ trợ:** bài thực hiện được việc đó cho một số dạng chuẩn cục bộ, đặc biệt ba mô hình một biến nhanh với nhiễu cộng. **Diễn giải của người phân tích:** giá trị thiết thực nhất là xác định điều kiện và sai lệch của một chỉ báo; chưa đủ căn cứ chuyển từ “chỉ báo có xu hướng thay đổi” sang “dự báo đúng một biến cố cụ thể”. [Mục 7–10, tr. 1030–1034]

## 2. Cách đặt bài toán, đầu vào và đầu ra

Đầu vào chính của bài là **phương trình đã biết và các tham số mô hình được chỉ định**, sau đó mới sinh chuỗi để khảo sát chỉ báo. Tác giả không bắt đầu từ một chuỗi thực chưa biết cơ chế rồi khám phá phương trình chi phối. Trong phần tất định, số biến nhanh có thể lớn hơn một; phần định lượng ngẫu nhiên chủ yếu xét một biến nhanh x và một biến chậm y. Hopf cần hai biến nhanh và được phân tích riêng về cấu trúc và độ trễ. [Mục 2, tr. 1021–1024; Mục 3, tr. 1025; Mục 7, Phương trình (39), tr. 1030]

| Thành phần                           | Cách bài báo thiết lập                                                                                                                                                           |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Đầu vào lý thuyết                 | Trường vectơ f và g đủ trơn; dạng phân nhánh; tỷ lệ thang thời gian ε; cường độ và dạng nhiễu; điều kiện đầu; miền và điều kiện biên                  |
| Dữ liệu mô phỏng                   | Một hoặc nhiều quỹ đạo của cùng hệ; biến nhanh x được lấy mẫu; y là tham số động đã biết trong mô hình                                                        |
| Thông tin biết trước quan trọng   | Trong các dạng chuẩn chính, ngưỡng phân nhánh tất định được đặt tại y = 0; nhánh hút, nhánh đẩy và biên thoát được tính từ phương trình              |
| Đầu ra giải tích                   | Phân loại chuyển tiếp; số mũ hồi phục; quy luật độ trễ và thoát; mật độ dừng; mômen và lân cận chứa quỹ đạo                                                 |
| Đầu ra số                           | Phương sai theo y, tỷ lệ quỹ đạo đã thoát, phương sai cửa sổ và tự tương quan; xu hướng của các đại lượng này                                              |
| Ước lượng tham số được gợi ý | Từ đoạn xa chuyển tiếp, khớp quá trình Ornstein–Uhlenbeck để ước lượng các hệ số hiệu dụng, rồi suy ra bậc độ lớn của ε và σ dưới giả định bổ sung |
| Đầu ra chưa được triển khai     | Quy tắc báo động với ngưỡng đã hiệu chỉnh, phân bố thời gian còn lại đến sự kiện hoặc bộ dự báo đã kiểm chứng ngoài mẫu                                 |

Nguồn bảng: Mục 2–4, tr. 1021–1027; Mục 7–9, tr. 1030–1034.

Không có nhãn để huấn luyện bộ phân loại. Tác giả biết trước loại mô hình và mốc phân nhánh để diễn giải các đường chỉ báo; đây không phải chứng minh rằng loại phân nhánh và mốc đó có thể đồng thời được suy ra chính xác từ dữ liệu quan sát. Các mốc đỏ ở Hình 1 được thêm để chỉ vị trí thay đổi rõ về mặt thị giác, không phải đầu ra của một bộ phát hiện tự động. [Mục 1, tr. 1021; Hình 1, tr. 1022]

Cần phân biệt bốn nhiệm vụ:

- **Mô tả động lực học:** phần được thực hiện rõ nhất, bằng hình học nhanh–chậm và phân tích ngẫu nhiên.
- **Phát hiện hồi cứu:** có minh họa chuỗi đã chuyển tiếp, nhưng chưa xây dựng tiêu chí phát hiện và đánh giá sai số vị trí.
- **Ước lượng tham số hoặc mốc tới hạn:** có gợi ý ước lượng hệ số ở vùng ổn định và tính độ trễ nếu đã biết thông tin mô hình; chưa có thí nghiệm suy luận đầy đủ từ chuỗi chưa biết tham số.
- **Dự báo trước sự kiện:** là mục tiêu định hướng. **Bài khảo sát những dấu hiệu có thể hữu ích, chưa báo cáo độ nhạy, tỷ lệ cảnh báo sai, thời gian báo trước hoặc độ chính xác thời điểm nhảy trên tập kiểm tra.**

Nguồn: Mục 3, tr. 1025; Mục 4, tr. 1027; Mục 8–10, tr. 1031–1034.

## 3. Công cụ được kế thừa và phần bài báo phát triển

Tác giả nói rõ việc đưa tham số biến thiên chậm vào hệ là thao tác tiêu chuẩn của lý thuyết nhiều thang thời gian. Định lý Fenichel, dạng chuẩn phân nhánh, phương trình Fokker–Planck và lý thuyết thoát do nhiễu đều được kế thừa. Vì vậy, không nên gán việc phát minh các công cụ này cho bài báo. Phạm vi đánh giá tính mới ở đây chỉ dựa trên cách tác giả định vị công trình và các lập luận trong PDF, không phải một tra cứu quyền ưu tiên độc lập. [Mục 1–4, tr. 1021–1027]

| Thành phần                                                | Nguồn gốc được PDF chỉ ra                                                      | Vai trò trong công trình                                                                                                        |
| ----------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------- |
| Phân nhánh và dạng chuẩn                               | Tài liệu [11], [12]; tiếp cận điểm chuyển của Thompson–Sieber ở [13], [14] | Phân loại các cơ chế mất ổn định; không phải công cụ mới                                                             |
| Đa tạp chậm và tính hyperbol theo hướng pháp tuyến | Định lý 2.1–2.2; tài liệu [21]–[27]                                           | Tách vùng động lực học ổn định thông thường với lân cận mất ổn định                                             |
| Quỹ đạo ứng viên ghép các đoạn nhanh và chậm     | Tài liệu [29], [30]                                                                | Công cụ hình học được dùng để xây dựng Định nghĩa 2.4                                                               |
| Định nghĩa chuyển tiếp và thước đo liên quan      | Định nghĩa 2.4, 2.9 và 3.1                                                       | Bài đề xuất cách đặc tả chuyển tiếp, số mũ hồi phục và khoảng cách sau nhảy trong khung này                     |
| Độ trễ phân nhánh động                               | Tài liệu [36]–[42]                                                                | Kết quả có trước được đưa vào bài toán dự báo vị trí nhảy; tác giả nhấn mạnh việc cần tính tới độ trễ |
| Hệ nhanh–chậm ngẫu nhiên và tập trung quỹ đạo     | Berglund–Gentz, đặc biệt [32], [52]                                              | Nền tảng cho Phương trình (16)–(21) và Định lý 4.1                                                                       |
| Phân nhánh của độ đo và mật độ                    | Arnold, Baxendale, Arnold–Boxler; [47], [59]–[66]                                  | Dùng lý thuyết sẵn có để gợi ý dấu hiệu từ thay đổi hình dạng mật độ                                            |
| Phương sai và tự tương quan                           | Các chỉ báo đã được nêu trong [1], [33], [74], [75]                         | Bài phân tích chúng trên dạng chuẩn, chỉ ra tác động của biên, cửa sổ và một quỹ đạo đơn lẻ                 |

Nguồn bảng: Mục 1–5, tr. 1021–1029; Mục 7–10, tr. 1030–1034; danh mục tài liệu, tr. 1034–1035. Những tài liệu này **chưa được đọc độc lập** trong bước hiện tại.

**Diễn giải của người phân tích:** đóng góp phương pháp luận có sức nặng là sự kết nối: từ một định nghĩa hình học đến các đại lượng có thể đo, đồng thời chỉ ra rằng cách lấy mẫu và điều kiện biên có thể thay đổi kết luận. Đây là một bài tổng quan có phát triển và minh họa, không phải một thuật toán duy nhất với một hàm mục tiêu tối ưu hóa. [Mục 2–10]

Đối chiếu cụ thể với các công trình trước mà PDF nêu: Thompson–Sieber [13], [14] đã đặt vấn đề phân tích điểm chuyển bằng phân nhánh; Berglund–Gentz [16], [17], [32] đã phát triển tiếp cận nhanh–chậm ngẫu nhiên; Arnold–Boxler [64] cung cấp ví dụ phân nhánh ngẫu nhiên được sử dụng lại. Phần riêng của bài hiện tại nằm ở cách định nghĩa chuyển tiếp qua quỹ đạo ứng viên, các thước đo kèm theo, và cách nối những kết quả đó với việc đo EWS trên dạng chuẩn. Gợi ý dùng phân nhánh P là một **diễn giải khái niệm cho cảnh báo**, chưa thành một bộ ước lượng, hàm mục tiêu, đặc trưng hoàn toàn mới hoặc quy trình kiểm chứng dự báo mới. Không đủ bằng chứng trong PDF để xác nhận quyền ưu tiên “đầu tiên” trên toàn bộ tài liệu. [Mục 1, tr. 1021; Định nghĩa 2.4, 2.9, 3.1, tr. 1023–1025; Mục 5, tr. 1028–1029]

## 4. Quy trình lý thuyết: xác định cơ chế trước khi chọn chỉ báo

### 4.1. Đưa sự trôi tham số vào hệ nhanh–chậm

Hai cách viết trên thang thời gian nhanh và chậm là:

$$
\begin{aligned}
\frac{dx}{dt}&=f(x,y), & \frac{dy}{dt}&=\varepsilon g(x,y),\\
\varepsilon\frac{dx}{d\tau}&=f(x,y), & \frac{dy}{d\tau}&=g(x,y),\qquad \tau=\varepsilon t,\quad 0<\varepsilon\ll1.
\end{aligned}
$$

Ở đây x là biến nhanh, y là biến chậm; ε đặc trưng sự tách thang thời gian. Các phương trình trên tương ứng Phương trình (3)–(4), Mục 2, tr. 1021. Trong nhiều ví dụ, g bằng 1 để y tăng đều; điều này là lựa chọn mô hình, không phải thuộc tính bắt buộc của hệ thực.

Cho ε tiến về 0 trên thang nhanh sẽ đóng băng y; cho ε tiến về 0 trên thang chậm tạo một ràng buộc đại số. Tập cân bằng của hệ nhanh được xác định bởi:

$$
C=\{(x,y):f(x,y)=0\},\qquad
0=f(x,y),\qquad \frac{dy}{d\tau}=g(x,y).
$$

C là tập tới hạn, hoặc đa tạp tới hạn khi có cấu trúc đa tạp; hai phương trình sau là hệ rút gọn trên đó. Nguồn: Phương trình (5) và phần định nghĩa ngay sau, Mục 2, tr. 1022.

**Tính hyperbol theo hướng pháp tuyến** (*normal hyperbolicity*) yêu cầu các trị riêng của đạo hàm theo x có phần thực khác 0; nhánh hút có tất cả phần thực âm. Định lý Fenichel bảo đảm một đa tạp chậm bất biến địa phương nằm cách một mảnh đóng và bị chặn có tính chất đó một khoảng bậc ε, khi ε đủ nhỏ. Điều này biện minh cho việc xem hệ ổn định bám theo nhánh chậm trước chuyển tiếp; định lý không áp dụng trực tiếp tại điểm mất tính hyperbol. [Định lý 2.1–2.2, tr. 1022]

### 4.2. Định nghĩa chuyển tiếp bằng hình học quỹ đạo

Trong giới hạn kỳ dị, một **quỹ đạo ứng viên** (*candidate*) là đường có hướng ghép hữu hạn các đoạn quỹ đạo của hệ nhanh hoặc hệ chậm. Định nghĩa 2.4 gọi một điểm mất tính hyperbol trên C là chuyển tiếp tới hạn nếu tồn tại quỹ đạo ứng viên đi tới điểm đó trên một nhánh hút có tính hyperbol và đổi loại chuyển động tại điểm ấy. Cách đọc của tác giả là đổi từ chuyển động chậm ổn định sang chuyển động nhanh. Định nghĩa có tính **tồn tại**, không đòi mọi quỹ đạo qua lân cận đều thực hiện một cú nhảy lớn giống nhau. [Mục 2, Định nghĩa 2.4, tr. 1023]

Điểm này đặc biệt quan trọng đối với **phân nhánh trao đổi ổn định** (*transcritical bifurcation*): bài xếp nó vào chuyển tiếp tới hạn vì có một hướng thoát thích hợp, dù không phải mọi đoạn nhanh đều thoát xa. Định nghĩa 3.1 bổ sung khoảng cách nhỏ nhất và lớn nhất từ điểm chuyển tiếp đến tập giới hạn sau chuyển động nhanh. Với dạng chuẩn trao đổi ổn định, tác giả ghi khoảng cách nhỏ nhất bằng 0, lớn nhất vô hạn; do đó định nghĩa không đồng nghĩa mọi chuyển tiếp đều kết thúc ở một trạng thái hữu hạn cách xa như nhau. [Mệnh đề 2.8, tr. 1024; Định nghĩa 3.1, tr. 1025]

Để giải thích vai trò của các dạng chuẩn, có thể gom các trường vectơ chính như sau:

$$
\begin{aligned}
\text{fold:}\quad &x'=-y-x^{2},\\
\text{transcritical:}\quad &x'=yx-x^{2},\\
\text{pitchfork:}\quad &x'=yx+a x^{3},\\
\text{Hopf:}\quad &r'=yr+\ell_{1}r^{3},\qquad \theta'=1.
\end{aligned}
$$

Các nhãn trong công thức lần lượt chỉ **phân nhánh nếp gấp** (*fold bifurcation*, còn gọi nút–yên), phân nhánh trao đổi ổn định, **phân nhánh chạc ba** (*pitchfork bifurcation*) và phân nhánh Hopf. Dấu phẩy trên chỉ đạo hàm theo thời gian nhanh; r và θ là bán kính và góc của dạng chuẩn Hopf. Bản phân tích dùng a cho hệ số bậc ba của chạc ba, thay ký hiệu α tại Mục 2 để tránh trùng với số mũ hồi phục bên dưới. Đây chỉ là đổi tên biến. Nguồn: Phương trình (7)–(8), Mệnh đề 2.5–2.8, tr. 1022–1024.

| Loại phân nhánh        | Kết luận theo định nghĩa của bài                    | Điều kiện cần giữ khi diễn giải                                                    |
| ------------------------- | ---------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Nếp gấp                 | Là chuyển tiếp tới hạn                                | Xét hướng tham số đi tới chỗ nhánh hút biến mất                                |
| Hopf dưới tới hạn     | Là chuyển tiếp tới hạn                                | Hệ số Lyapunov thứ nhất dương theo quy ước dạng chuẩn của bài                 |
| Hopf trên tới hạn      | Không là chuyển tiếp tới hạn theo định nghĩa này | Sự xuất hiện dao động nhỏ liên tục không tạo đoạn thoát nhanh như yêu cầu |
| Chạc ba dưới tới hạn | Là chuyển tiếp tới hạn                                | Hệ số a dương trong công thức trên                                                 |
| Chạc ba trên tới hạn  | Không là chuyển tiếp tới hạn theo định nghĩa này | Kết luận phụ thuộc định nghĩa và hướng đi trong không gian tham số           |
| Trao đổi ổn định     | Là chuyển tiếp tới hạn theo tính tồn tại           | Không được suy ra mọi quỹ đạo đều nhảy xa                                      |

Nguồn: Mệnh đề 2.5–2.8, Hình 3, tr. 1023–1024. Chạc ba và trao đổi ổn định cần thêm cấu trúc thích hợp; bài không xem chúng là hai phân nhánh tổng quát không điều kiện của mọi họ hệ một tham số.

Các dạng chuẩn là mô hình **cục bộ**. Quỹ đạo đi tới vô hạn trong một dạng chuẩn không chứng minh hệ vật lý có một trạng thái vô hạn; nó cho biết quỹ đạo rời miền mà mô hình cục bộ mô tả. Cấu trúc toàn cục mới xác định trạng thái đích hữu hạn, nếu có. Đây là diễn giải của người phân tích dựa trên cách dùng dạng chuẩn và khoảng cách nhảy ở Mục 2–3, tr. 1023–1025.

### 4.3. Chậm dần tới hạn có mức định lượng khác nhau

Tuyến tính hóa quanh cân bằng hút cho tốc độ suy giảm nhiễu loạn; trị riêng trội tiến gần trục ảo làm hồi phục chậm đi. Với các dạng chuẩn đang xét và y âm, kết quả có thể viết rõ bằng trị riêng hoặc phần thực trội:

$$
\begin{aligned}
\lambda_{\mathrm{fold}}(y)&=-2\sqrt{-y},\\
\operatorname{Re}\lambda_{\mathrm{Hopf}}(y)&=y,\\
\lambda_{\mathrm{pitchfork}}(y)&=y,\qquad
\lambda_{\mathrm{transcritical}}(y)=y.
\end{aligned}
$$

λ mô tả suy giảm nhiễu loạn trên thang nhanh. Các biểu thức được diễn giải từ Phương trình (9) và Mệnh đề 2.10, tr. 1024–1025; dùng phần thực cho Hopf để phân biệt tốc độ suy giảm với tần số dao động.

Bài gọi α là **số mũ hồi phục** (*recovery exponent*). Viết theo độ lớn khoảng cách đến ngưỡng để tránh lũy thừa phân số của y âm, ta có:

$$
|\operatorname{Re}\lambda(y)|=O(|y|^{\alpha}),\qquad
\alpha=\begin{cases}
1/2,&\text{fold},\\
1,&\text{Hopf, pitchfork, transcritical}.
\end{cases}
$$

Đây là cách trình bày lại bằng độ lớn của bản phân tích, không phải số mũ mới; nguồn là Định nghĩa 2.9 và Mệnh đề 2.10, tr. 1024–1025. **Giới hạn toán học:** ký hiệu O chỉ một chặn trên tiệm cận và tự nó không xác định duy nhất số mũ; các giá trị α ở đây phải được hiểu là số mũ của hạng trội trong những biểu thức λ tường minh phía trên. Khác biệt này gợi ý khả năng phân biệt một số cơ chế nếu biết tham số và đo được quy luật hồi phục. Bài chưa kiểm chứng bộ phân loại cơ chế từ chuỗi hữu hạn chưa biết y; chạc ba và trao đổi ổn định còn có cùng tuyến tính hóa trên nhánh x bằng 0.

### 4.4. Mốc phân nhánh và thời điểm nhảy không trùng nhau

Ở ε dương, quỹ đạo có thể tiếp tục bám gần nhánh đã mất ổn định trước khi rời đi. Với nếp gấp, Định lý 3.2 mô tả độ dịch trong y có bậc:

$$
\Delta y=O(\varepsilon^{2/3}).
$$

Δy là ký hiệu của bản phân tích cho độ dịch so với ngưỡng nếp gấp; nguồn là Định lý 3.2 và đoạn giải thích ngay sau, tr. 1025, cùng Hình 2(b), tr. 1023. **Lưu ý nguồn:** hệ viết ngay trước định lý ở tr. 1025 in dấu âm trong phương trình của y, trái với chiều tiến tới nếp gấp ở Ví dụ 2.3. Vì vậy, kết quả bậc độ trễ được ghi nhận theo phát biểu của bài, nhưng chiều tham số phải được làm rõ trước khi triển khai số; không sao chép nguyên hệ đó rồi mặc định nó tạo Hình 2.

Với Hopf, bài dùng ánh xạ giữa thời điểm đi vào và đi ra khỏi lân cận nhánh chậm:

$$
\Psi(\tau)=\int_{0}^{\tau}\lambda_{1}(s)\,ds,\qquad
\operatorname{Re}\Psi(\tau)=\operatorname{Re}\Psi(\Pi(\tau)).
$$

λ₁ là một trị riêng phức của tuyến tính hóa hệ nhanh; Π liên hệ thời điểm vào và ra. Nguồn: Phương trình (11), Định lý 3.3, tr. 1025. Ý nghĩa là sự suy giảm tích lũy trước mất ổn định phải được bù bởi tăng trưởng sau đó. Bài lưu ý có thêm giả thiết kỹ thuật và không trình bày đầy đủ chúng ở đây. Tính được vị trí nhảy từ ε, điều kiện đi vào và loại phân nhánh đã biết là dự báo có điều kiện theo mô hình; chưa phải một bài kiểm tra suy luận các đại lượng ấy từ dữ liệu chưa biết.

## 5. Đưa nhiễu vào khung: từ lân cận ổn định đến thoát sớm

### 5.1. Ba góc nhìn ngẫu nhiên bổ sung nhau

Bài đặt cạnh nhau: **quỹ đạo mẫu** (*sample path*) cho một hiện thực nhiễu; mật độ xác suất chuyển tiếp tiến hóa theo phương trình Fokker–Planck; và **hệ động lực ngẫu nhiên** (*random dynamical system*, RDS) để khảo sát độ đo bất biến và tập hút ngẫu nhiên. Đây là ba cách nghiên cứu một hệ ngẫu nhiên, không phải ba bộ dữ liệu hay ba thuật toán dự báo cạnh tranh. [Mục 4, Phương trình (12)–(15), tr. 1026]

Mô hình nhanh–chậm ngẫu nhiên trên thang chậm được viết:

$$
\begin{aligned}
dx_{\tau}&=\frac{1}{\varepsilon}f(x_{\tau},y_{\tau})\,d\tau
+\frac{\sigma_{f}}{\sqrt{\varepsilon}}\,dW_{\tau},\\
dy_{\tau}&=g(x_{\tau},y_{\tau})\,d\tau+\sigma_{g}\,dW_{\tau}.
\end{aligned}
$$

W là chuyển động Brown; các hệ số σ thể hiện cường độ nhiễu. Hệ số căn ε phát sinh từ đổi thang thời gian của Brown, không phải một tham số hiệu chỉnh tùy ý. Nguồn: Phương trình (16), tr. 1026. Bài sử dụng phương trình vi phân ngẫu nhiên theo Itô hoặc Stratonovich tùy mô hình và nhấn mạnh đây là một quyết định mô hình hóa có ý nghĩa, đặc biệt với nhiễu nhân.

Để phân tích đoạn còn ổn định, đặt độ lệch khỏi đa tạp chậm và phương sai chuẩn hóa như sau:

$$
\xi_{\tau}=x_{\tau}-h_{\varepsilon}(y_{\tau}),\qquad
X=\sigma_{f}^{-2}\operatorname{Var}(\xi_{\tau}^{0}),\qquad
\varepsilon\dot X=2A_{\varepsilon}(y)X+1.
$$

h là đồ thị đa tạp chậm; ξ⁰ là xấp xỉ tuyến tính của độ lệch; A là hệ số tuyến tính hóa có điều chỉnh do chuyển động chậm. Phương trình phương sai được dùng ở đây trong giản lược bỏ nhiễu biến chậm. **Đối chiếu toán học:** PDF in (20) ngay sau (19), nhưng khi giữ σg khác 0 và cùng nguồn Brown như (16), hệ số khuếch tán ở (19) cho:

$$
\varepsilon\dot X=2A_{\varepsilon}(y)X+
\left(1-\sqrt{\varepsilon}\frac{\sigma_{g}}{\sigma_{f}}
h_{\varepsilon}'(y)\right)^{2},\qquad \sigma_{f}>0.
$$

Đây là công thức người phân tích suy ra cho hệ **đã tuyến tính hóa và thay y bằng đường tất định trong (19)**, không phải nghiệm chính xác của hệ phi tuyến (16). Hạng cộng bằng 1 khi σg bằng 0; bỏ hiệu chỉnh ở bậc dẫn đầu cần kiểm soát thêm đạo hàm h. Sự giản lược không tự đồng đều sát điểm mất tính hyperbol, nơi đạo hàm nhánh có thể tăng mạnh. Nguồn đối chiếu: Phương trình (16)–(20), tr. 1026; lập luận đặt σg bằng 0 ở tr. 1027.

Ở vùng hút có tính hyperbol, nghiệm gần dừng của phương trình này và lân cận được xây dựng trong bài là:

$$
H_{\varepsilon}(y)=-\frac{1}{2A_{\varepsilon}(y)}+O(\varepsilon),\qquad
N(r;C_{\varepsilon})=
\left\{(x,y):\frac{(x-h_{\varepsilon}(y))^{2}}{H_{\varepsilon}(y)}<r^{2}\right\}.
$$

H xác định hình học của lân cận và r chọn độ rộng; nguồn: Phương trình (20)–(21), tr. 1026. Định lý 4.1 tóm tắt khả năng quỹ đạo ở lại lân cận với xác suất cao trên một thời gian phụ thuộc mạnh vào tỷ lệ giữa r và nhiễu; bài dẫn chứng minh chi tiết sang [32]. Khi độ lớn của tốc độ hút giảm, xấp xỉ tuyến tính dự đoán độ phân tán tăng. Không được kéo kết luận này xuyên qua điểm mất tính hyperbol hoặc bỏ qua điều kiện nhiễu nhỏ. [Định lý 4.1, tr. 1026; các nhận xét, tr. 1027]

### 5.2. Mô hình tham chiếu khi còn xa chuyển tiếp

Tác giả dùng **quá trình Ornstein–Uhlenbeck** (OU) với hệ số hồi phục dương và không đổi:

$$
dx_{\tau}=-\frac{\alpha}{\varepsilon}x_{\tau}\,d\tau
+\frac{\sigma}{\sqrt{\varepsilon}}\,dW_{\tau},\qquad
\lim_{\tau\to\infty}\operatorname{Var}(x_{\tau})=\frac{\sigma^{2}}{2\alpha}.
$$

α ở tiểu mục này là hệ số hồi phục của Phương trình (22), không phải số mũ hồi phục ở Mục 4.3 của bản phân tích. Phương sai dừng là Phương trình (24), tr. 1027. Đây là mô hình đối chiếu ổn định để hiểu thế nào là “phương sai không có xu hướng” trong giả định đã chọn; không phải kết luận mọi đoạn xa chuyển tiếp trong hệ thực đều có phương sai hằng.

**Lưu ý nguồn:** ngay sau Phương trình (23), PDF viết phương sai quá độ có một hạng phụ thuộc x₀ mặc dù điều kiện đầu được giả định tất định. Kiểm tra trực tiếp từ tích phân ngẫu nhiên trong (23) cho:

$$
\operatorname{Var}(x_{\tau})=
\frac{\sigma^{2}}{2\alpha}\left(1-e^{-2\alpha\tau/\varepsilon}\right),\qquad
\rho_{\mathrm{stat}}(h)=e^{-\alpha|h|/\varepsilon}.
$$

Công thức đầu ứng với điều kiện đầu tất định; công thức sau là tự tương quan của OU ở trạng thái dừng với độ trễ thời gian h. Đây là kết quả suy ra của người phân tích từ (22)–(23), không phải bản chép công thức quá độ trong PDF. Nó xác nhận phương sai dừng (24), đồng thời cho thấy phát biểu tự tương quan biến mất khi thời gian lớn cần được giới hạn: tương quan giảm khi **độ trễ** tăng, còn tại độ trễ cố định, quá trình dừng vẫn có tương quan khác 0. Biểu thức được PDF ký hiệu như mômen tích ở tr. 1027 cũng cần phân biệt với hiệp phương sai khi trung bình khác 0.

Gợi ý suy luận tham số của tác giả là khử xu hướng ở một đoạn ổn định đủ dài, khớp hệ OU hiệu dụng, rồi sử dụng:

$$
\widetilde\alpha=\frac{\alpha}{\varepsilon},\qquad
\widetilde\sigma=\frac{\sigma}{\sqrt{\varepsilon}}.
$$

Đây là các hệ số hiệu dụng trong Phương trình (25), tr. 1027. Nếu chỉ quan sát biến nhanh của mô hình OU hiệu dụng và chưa có hiệu chuẩn độc lập của α hoặc ε, ta chưa nhận dạng duy nhất từng tham số. Thật vậy, phép đổi sau giữ nguyên cả hai hệ số hiệu dụng:

$$
(\alpha,\sigma,\varepsilon)\longmapsto
(c\alpha,\sqrt{c}\,\sigma,c\varepsilon),\qquad c>0.
$$

Đây là kiểm tra **khả năng nhận dạng tham số** (*identifiability*) của người phân tích, với c được chọn sao cho ε mới vẫn thuộc miền giả định. Giả định α có bậc một chỉ hỗ trợ diễn giải bậc độ lớn như tác giả nêu, không cung cấp giá trị hiệu chuẩn. Quan sát thêm y với tốc độ đã biết có thể cung cấp thông tin khác; bài không đánh giá một quy trình suy luận kết hợp như vậy. Tác giả nêu ước lượng hợp lý cực đại như một lựa chọn nhưng không báo cáo kết quả khớp và sai số ước lượng. [Phương trình (25), tr. 1027]

Ví dụ 4.2 còn cho một điều kiện quan trọng: không có nhiễu Brown trực tiếp trong phương trình của y **không đồng nghĩa y tất định** nếu g phụ thuộc biến nhanh ngẫu nhiên. Với phép đổi X bằng x trừ y của ví dụ, đạo hàm đúng theo (26) là:

$$
\begin{aligned}
dX_{t}&=\left[-X_{t}-\varepsilon g(X_{t}+Y_{t},Y_{t})\right]dt+\sigma\,dW_{t},\\
\operatorname{Var}(X_{t})&=\operatorname{Var}(x_{t})+
\operatorname{Var}(y_{t})-2\operatorname{Cov}(x_{t},y_{t}).
\end{aligned}
$$

X và Y là tọa độ của Ví dụ 4.2. PDF in hạng đầu của phương trình biến đổi như −x; phép thế vào (26) cho −X như trên. Đẳng thức hai phương sai chỉ được bảo đảm khi y thực sự tất định, hoặc có một điều kiện đặc biệt làm các hạng bổ sung triệt tiêu; nó không theo sau riêng từ việc bỏ nhiễu trực tiếp ở phương trình chậm. Phần mô phỏng chính với g bằng 1 tránh được vấn đề này, nhưng không thể mở rộng lập luận đó cho mọi g. [Ví dụ 4.2, tr. 1027; Phương trình (39), tr. 1030]

### 5.3. Phân nhánh của mật độ và giới hạn của ví dụ nhiễu nhân

**Phân nhánh động lực ngẫu nhiên** (*dynamical bifurcation*, D-bifurcation) được định nghĩa qua các họ độ đo bất biến. **Phân nhánh hình thái mật độ** (*phenomenological bifurcation*, P-bifurcation) chỉ thay đổi định tính của họ mật độ dừng. Hai khái niệm không đồng nhất và không nhất thiết cùng xuất hiện. [Mục 5, tr. 1028–1029]

Ví dụ Arnold–Boxler được bài kế thừa là phân nhánh trao đổi ổn định với nhiễu nhân theo Stratonovich:

$$
dx_{t}=(yx_{t}-x_{t}^{2})\,dt+\sigma x_{t}\circ dW_{t}.
$$

Nguồn: Phương trình (28), tr. 1028. Trong phân tích chính của Mục 5, y là **tham số cố định của một họ hệ**; bài nói có thể cho y biến thiên chậm nhưng không thực hiện phân tích động đầy đủ đó. Kết quả được dẫn lại là điểm D tại 0 và các điểm P tại hai giá trị:

$$
y_{D}=0,\qquad y_{P\pm}=\pm\frac{\sigma^{2}}{2}.
$$

Nguồn: Định lý 5.1, Phương trình (31)–(32), Hình 6, tr. 1028. **Cần phân biệt nhánh độ đo:** điểm P dương được suy trực tiếp từ mật độ (32); bài suy điểm P âm bằng lập luận đối xứng hoặc phương trình Kolmogorov lùi, không triển khai một phép phát hiện trên quỹ đạo tiến đang bám nhánh hút. Thứ tự hình học “P âm trước D khi tăng y” chưa đủ để biến nó thành một dấu hiệu quan sát được. Với chính (28), nếu khởi tạo x bằng 0 thì cả trôi và khuếch tán đều bằng 0, nên quỹ đạo tiếp tục bằng 0, kể cả khi y được cho biến thiên chậm. Vì vậy cần nêu rõ đang quan sát họ độ đo nào và điều kiện kích thích nào; bài chưa kiểm chứng phát hiện P từ một chuỗi không dừng hữu hạn. [Phương trình (28)–(32), tr. 1028; các nhận định về dự báo ở tr. 1029]

Một điểm cần giữ riêng là độ tin cậy của kết luận phương sai trong ví dụ này. Phương trình (32) cho mật độ trên nửa trục dương:

$$
p_{s}^{y}(x)=\frac{1}{N_{y}}x^{2y/\sigma^{2}-1}
\exp\!\left(-\frac{2x}{\sigma^{2}}\right),\qquad x>0,\quad y>0.
$$

N là hằng số chuẩn hóa. Công thức đã được đối chiếu trực tiếp tr. 1028: số mũ hàm mũ là tuyến tính theo x. **Tác giả khẳng định:** Phương trình (33) và Hình 7 cho phương sai không đơn điệu, có cực trị. **Diễn giải và kiểm tra đại số của người phân tích:** nếu chuẩn hóa đúng mật độ (32), đặt hai ký hiệu phụ k và β thì:

$$
\begin{aligned}
k&=\frac{2y}{\sigma^{2}},\qquad \beta=\frac{2}{\sigma^{2}},\qquad
N_{y}=\frac{\Gamma(k)}{\beta^{k}},\\
\mathbb{E}[x]&=\frac{k}{\beta}=y,\qquad
\operatorname{Var}(x)=\frac{k}{\beta^{2}}=\frac{y\sigma^{2}}{2}.
\end{aligned}
$$

k và β chỉ là ký hiệu của bản phân tích để nhận diện tích phân gamma của chính (32); đây không phải công thức tác giả đã báo cáo. Đối chiếu đại số còn cho thấy trung bình được in ngay trước (33), và phương sai (33), viết lại được như sau:

$$
m_{\mathrm{print}}=N_{y}y,\qquad
v_{\mathrm{print}}=\frac{y\sigma^{2}}{2}+y^{2}(1-N_{y})^{2}.
$$

Hai ký hiệu mang chỉ số “print” chỉ các biểu thức **được in**, không phải mômen hợp lệ mà bản phân tích chấp nhận. Đẳng thức được kiểm tra bằng biến đổi đại số của đúng công thức ở tr. 1029, sử dụng N ở trên. Phần phụ thuộc hằng số chuẩn hóa giải thích cụ thể vì sao (33) khác phương sai của mật độ chuẩn hóa (32). Kết quả đơn điệu suy từ (32) **không nhất quán với (33) và Hình 7**; chưa thể lấy Hình 7 làm bằng chứng chắc chắn cho phương sai không đơn điệu của mô hình (28) như đang viết. Tuy nhiên, phương sai đúng trên nhánh mật độ dương vẫn giảm khi y giảm về 0 với σ cố định, nên ví dụ vẫn cho thấy phương sai không nhất thiết tăng theo một hướng tiếp cận điểm D. Điều đó khác với khẳng định có cực đại/cực tiểu trong cùng nhánh khi giữ σ cố định. Bất nhất mômen không tự bác bỏ vị trí phân nhánh P từ hình dạng mật độ, cũng không phủ định các ví dụ nhiễu cộng ở Mục 7–9.

### 5.4. Nhiễu có thể đưa hệ thoát trước ngưỡng tất định

Mục 6 dùng dạng nếp gấp với quy ước dấu khác Mục 2:

$$
dx_{t}=(y-x_{t}^{2})\,dt+\sigma\,dW_{t},\qquad y>0.
$$

Ở đây nhánh hút ở căn dương và nhánh đẩy ở căn âm của y; nguồn: Phương trình (35), tr. 1029. Tác giả xét thế năng bậc ba để giải thích rào thoát và thời gian thoát có sự phụ thuộc dạng hàm mũ vào nghịch đảo bình phương cường độ nhiễu. **Lưu ý nguồn:** dòng định nghĩa H ở tr. 1029 viết hiệu thế năng theo thứ tự “điểm hút trừ điểm đẩy” nhưng gán giá trị dương. Kiểm tra của người phân tích với đúng thế năng được in cho chiều cao rào dương:

$$
U(x)=-yx+\frac{x^{3}}{3},\qquad
\Delta U=U(-\sqrt{y})-U(\sqrt{y})=\frac{4}{3}y^{3/2}>0.
$$

ΔU là ký hiệu làm rõ của bản phân tích; hiệu theo thứ tự ngược như PDF viết bằng số âm. Nếu dùng quy luật thời gian thoát dạng hàm mũ ở Mục 6 thì phải dùng chiều cao rào dương nhất quán. Không được xem đây là một kiểm chứng số của xác suất thoát hoặc tự suy ra hằng số tiền nhân mà PDF chưa cung cấp.

Định lý 6.1 nêu hai miền tương quan giữa nhiễu và ε, với ranh giới đặc trưng:

$$
\sigma\ll\sqrt{\varepsilon}\quad\text{hoặc}\quad
\sigma\gg\sqrt{\varepsilon}.
$$

Theo phát biểu của bài, miền đầu làm thoát trước ngưỡng hiếm, miền sau làm nó rất dễ xảy ra. Nguồn: Phương trình (36), Định lý 6.1, tr. 1029. Đây là so sánh tiệm cận, không phải ngưỡng xác suất số học áp dụng cho mọi ε hữu hạn. **Bất nhất cần lưu ý:** Định lý 6.1 in g bằng 1 trong hệ (34), trong khi với trường vectơ ở (34) và y dương, hướng ấy tăng khoảng cách tới điểm nếp gấp tại 0. Phải xác định lại hướng trôi khi dùng kết quả cho bài toán tiến tới ngưỡng; bản phân tích không coi dấu được in là đã nhất quán.

Với trao đổi ổn định và chạc ba, tác giả chỉ nêu các kết quả trước đó **gợi ý** miền trung gian có thang:

$$
\sigma\approx\varepsilon^{3/4}.
$$

Nguồn: Phương trình (37), tr. 1030. Bài thừa nhận trường hợp này ít được nghiên cứu hơn, nên không nâng phát biểu này thành một định lý đầy đủ đã được chứng minh trong PDF.

Ví dụ van der Pol ngẫu nhiên ở Phương trình (38) và Hình 8 bổ sung vai trò phản hồi của biến chậm: một quỹ đạo có dao động lớn do nhiễu trong khi mô hình tất định tương ứng hội tụ về cân bằng ổn định. Điều này cho thấy cơ chế thoát và chiều biến thiên tham số phải được xem cùng nhau, thay vì coi mọi sự kiện đều do đi qua mốc phân nhánh của một họ hệ đóng băng. [Mục 6, tr. 1030]

## 6. Từ mô hình đến đại lượng đo: phương sai và tự tương quan

### 6.1. Mật độ dừng trong giới hạn đóng băng tham số

Mục 7 quay về ba dạng chuẩn một chiều và nhiễu cộng. Trên thang nhanh, hệ có dạng:

$$
dx_{t}=f(x_{t},y_{t})\,dt+\sigma\,dW_{t},\qquad
dy_{t}=\varepsilon\,dt.
$$

Nguồn: Phương trình (39), tr. 1030. Trước ngưỡng, y âm; khi ε bằng 0, y được đóng băng và mật độ theo x tuân theo:

$$
\frac{\partial p^{y}}{\partial t}
=-\frac{\partial}{\partial x}(fp^{y})
+\frac{\sigma^{2}}{2}\frac{\partial^{2}p^{y}}{\partial x^{2}},\qquad
J=fp^{y}-\frac{\sigma^{2}}{2}\frac{\partial p^{y}}{\partial x}.
$$

J là dòng xác suất; nguồn: Phương trình (40) và dòng định nghĩa J, tr. 1030. Ở trạng thái dừng với **biên phản xạ**, dòng bằng 0 và cho nghiệm thế năng:

$$
p_{s}^{y}(x)=\frac{1}{Z(y)}
\exp\!\left(\frac{2}{\sigma^{2}}\int_{a}^{x}f(w,y)\,dw\right),\qquad
Z(y)=\int_{a}^{b}\exp\!\left(\frac{2}{\sigma^{2}}\int_{a}^{u}f(w,y)\,dw\right)du.
$$

a và b là hai đầu miền; w và u là biến tích phân. Nguồn: Phương trình (41)–(42) và nghiệm ngay sau, tr. 1030. Bản phân tích dùng Z và viết đầy đủ tích phân của **hàm chưa chuẩn hóa** để tránh nhầm với dòng định nghĩa hằng số chuẩn hóa trong PDF, vốn in dưới dạng tích phân của chính mật độ đã chuẩn hóa. Đây là làm rõ ký hiệu, không thay thế mô hình biên của tác giả.

Các miền và mật độ cụ thể là phần quyết định của phương pháp:

$$
\begin{aligned}
f_{1}(x,y)&=-y-x^{2}, & (a,b)&=(-\sqrt{-y},\infty),\\
f_{2}(x,y)&=yx-x^{2}, & (a,b)&=(y,\infty),\\
f_{3}(x,y)&=yx+x^{3}, & (a,b)&=(-\sqrt{-y},\sqrt{-y}).
\end{aligned}
$$

Các chỉ số 1, 2, 3 lần lượt tương ứng nếp gấp, trao đổi ổn định và chạc ba dưới tới hạn; nguồn: Phương trình (43), tr. 1030. Các đầu biên hữu hạn nằm ở cân bằng đẩy của hệ nhanh. Tác giả thay biên ngẫu nhiên của bài toán thoát bằng biên tất định này, rồi áp phản xạ để tạo mật độ dừng tính được. Vì vậy, phép tính này mô tả một bài toán **đã ngăn thoát qua biên**, không phải phân bố của mọi quỹ đạo không ràng buộc.

$$
\begin{aligned}
p_{s,1}^{y}(x)&=\frac{1}{Z_{1}}\exp\!\left[\frac{2}{\sigma^{2}}
\left(-yx-\frac{x^{3}}{3}+\frac{2}{3}(-y)^{3/2}\right)\right],\\
p_{s,2}^{y}(x)&=\frac{1}{Z_{2}}\exp\!\left[\frac{2}{\sigma^{2}}
\left(\frac{yx^{2}}{2}-\frac{x^{3}}{3}-\frac{y^{3}}{6}\right)\right],\\
p_{s,3}^{y}(x)&=\frac{1}{Z_{3}}\exp\!\left[\frac{2}{\sigma^{2}}
\left(\frac{yx^{2}}{2}+\frac{x^{4}}{4}+\frac{y^{2}}{4}\right)\right].
\end{aligned}
$$

Đây là Phương trình (44), tr. 1030, với Z thay tên hằng số chuẩn hóa; mỗi mật độ chỉ dùng trên miền tương ứng ở (43). Mômen được tính từ tích phân của các mật độ này. Hình 9 dùng σ = 0,1. Chạc ba giữ đối xứng qua x bằng 0, còn nếp gấp và trao đổi ổn định có thể trở nên bất đối xứng; tác giả không tìm thấy phân nhánh P của ba họ mật độ này khi y âm. Như vậy, bất đối xứng và phân nhánh P không phải dấu hiệu bắt buộc cho mọi cơ chế đang xét. [Mục 7, tr. 1030–1031]

**Diễn giải của người phân tích:** tuyến tính hóa và bỏ ảnh hưởng biên trong miền còn tập trung gần cân bằng cho các quy luật phương sai dẫn đầu:

$$
\begin{aligned}
\operatorname{Var}_{\mathrm{fold}}(x)&\approx\frac{\sigma^{2}}{4\sqrt{-y}},\\
\operatorname{Var}_{\mathrm{transcritical}}(x)
&\approx\operatorname{Var}_{\mathrm{pitchfork}}(x)
\approx-\frac{\sigma^{2}}{2y},\qquad y<0.
\end{aligned}
$$

Các quan hệ này được suy ra bằng cách ghép tốc độ hồi phục của Mệnh đề 2.10 với phương sai OU ở (24); không phải một phép khớp số do bài báo cáo. Chúng giải thích trực giác tăng phương sai nhưng không được ngoại suy sát 0, nơi phi tuyến, biên, thoát và chuyển động chậm cùng quan trọng. Hình 9 thực tế cho cực đại rồi giảm, thay vì tăng vô hạn. [Mục 4, tr. 1027; Mục 7, tr. 1031]

### 6.2. Mô phỏng động và phương sai trên tập quỹ đạo còn lại

Mục 8 giữ ε dương, sinh 1.000 quỹ đạo với σ = 0,1 và ε = 0,02. Ở một thời điểm cố định, tác giả tính phương sai giữa các quỹ đạo còn chưa thoát. Một quỹ đạo bị loại khỏi mọi lần tính sau khi vượt biên ở (43); tỷ lệ đã thoát được vẽ riêng. Vì vậy, đại lượng trong Hình 10 là phương sai của tập còn sống theo quy tắc loại quỹ đạo, không phải phương sai vô điều kiện của toàn bộ quần thể. [Mục 8, tr. 1031; chú thích Hình 10, tr. 1032]

Hai phép tính được đối chiếu khác nhau ở **cả ε và điều kiện biên**: mật độ dừng có ε bằng 0 và biên phản xạ; mô phỏng có ε bằng 0,02 và loại quỹ đạo khi thoát. Khác biệt sát ngưỡng vì thế không cho phép quy nguyên nhân riêng cho ε. Tác giả trực tiếp thảo luận sự khác nhau giữa hai mô hình biên. [Mục 8, tr. 1031]

**Giới hạn bổ sung:** mật độ phản xạ không tự đồng nhất với phân bố điều kiện còn sống của quá trình bị hấp thụ, kể cả khi tham số được đóng băng. Gần ngưỡng, loại quỹ đạo có thể làm tập còn lại mang đặc trưng khác ban đầu; 1.000 là số quỹ đạo khởi tạo, không phải kích thước mẫu còn lại cố định ở mọi y. Đây là hệ quả của quy tắc được nêu trong chú thích Hình 10, tr. 1032; PDF không báo cáo độ bất định theo số quỹ đạo còn sống.

### 6.3. Phương sai cửa sổ trên một chuỗi

Để tiến gần tình huống chỉ có một chuỗi, bài lấy cửa sổ lùi có độ dài s và N* điểm quan sát:

$$
\begin{aligned}
\mu(t^{*})&=\frac{1}{N^{*}}\sum_{t_{j}\in[t^{*}-s,t^{*}]}x_{t_{j}},\\
V(t^{*})&=\frac{1}{N^{*}}\sum_{t_{j}\in[t^{*}-s,t^{*}]}
\left(x_{t_{j}}-\mu(t^{*})\right)^{2}.
\end{aligned}
$$

μ là trung bình trong cửa sổ, V là phương sai cửa sổ; mẫu số đúng theo bài là N*, không phải N* trừ 1. Nguồn: Phương trình (45), tr. 1031. s xấp xỉ 14,3051 trên thang nhanh, tương ứng khoảng y dài 0,2861 khi ε bằng 0,02. Đây là lựa chọn minh họa được báo cáo, chưa có nghiên cứu tối ưu hoặc độ nhạy theo s. Hình 11 vẫn dùng 1.000 quỹ đạo để tạo đường kết quả; nó không phải một kiểm chứng hiệu năng dự báo trên một chuỗi riêng lẻ. [Mục 8, tr. 1031–1032; chú thích Hình 11]

Các điểm trong một chuỗi có tự tương quan, và các cửa sổ trượt có thể dùng lại nhiều điểm. Do đó không được coi số điểm hoặc số cửa sổ là số lần lặp độc lập khi lượng hóa độ bất định. Bản thân lựa chọn mẫu số N* cũng không chứng minh V là một ước lượng không chệch của phương sai nhiễu trong chuỗi phụ thuộc và không dừng. Đây là giới hạn thống kê của phép đo trong (45), không phải kết quả một kiểm định mà bài đã thực hiện. [Mục 8–9, tr. 1031–1033]

Ở nếp gấp, trung bình tất định thay đổi theo nhánh hút cong. Một cửa sổ dài gần ngưỡng chứa đoạn biến thiên tất định mạnh hơn, nên phương sai quanh một trung bình hằng có thể tăng ngay cả khi chưa xét nhiễu. Hình 12 giải thích cơ chế này; ở trao đổi ổn định và chạc ba trước ngưỡng, nhánh hút x bằng 0 không tạo cùng xu hướng hình học. **Diễn giải của người phân tích:** phương sai cửa sổ trộn dao động ngẫu nhiên với sự di chuyển của trung bình; mức tăng không nhận diện duy nhất suy yếu ổn định. [Mục 8, Hình 12, tr. 1032–1033]

### 6.4. Tự tương quan và sự khác nhau giữa trung bình nhiều quỹ đạo với một chuỗi

Mục 9 viết ước lượng tự tương quan trễ k dưới dạng:

$$
R(k)=\frac{1}{(n-k)v^{2}}
\sum_{l=1}^{n-k}(x_{l}-\mu)(x_{l+k}-\mu).
$$

n là số điểm của đoạn, μ là trung bình và v là ký hiệu gốc. Nguồn: công thức không đánh số, Mục 9, tr. 1032. **Lưu ý nguồn:** ngay dưới công thức, bài gọi v là “phương sai” nhưng mẫu số lại dùng bình phương v. Chuẩn hóa thông thường tương ứng với công thức này khi v là độ lệch chuẩn; nếu v thực sự là phương sai thì phải dùng một lũy thừa v. Đây là bất nhất cần làm rõ trước khi tính lại, không được âm thầm đổi công thức rồi tuyên bố tái lập đúng bản in.

Hình 13 dùng trung bình từ 10.000 quỹ đạo, σ = 0,1, ε = 0,02 và độ trễ ghi là k = 0,002; đoạn tính dài 8k. Khác phần phương sai, quy tắc dừng là x vượt xuống −1 đối với nếp gấp/trao đổi ổn định, hoặc trị tuyệt đối của x vượt 1 đối với chạc ba. Công thức ước lượng dùng k như một chỉ số trễ nguyên, còn mô tả thí nghiệm ghi k như một độ trễ thời gian; PDF chưa cung cấp rõ phép đổi qua bước lấy mẫu. [Mục 9, tr. 1032; Hình 13, tr. 1033]

Tác giả thấy xu hướng tăng: gần tuyến tính cho trao đổi ổn định/chạc ba và có dạng gần bậc hai cho nếp gấp trong miền được vẽ. Các đường nét đứt là xấp xỉ đường xu hướng, không phải định luật phổ quát được chứng minh hoặc khoảng tin cậy. Hình 14 chỉ lấy hai quỹ đạo trao đổi ổn định và cho hai đường xu hướng ngược dấu: một tăng, một giảm. Điều đó là phản ví dụ trực tiếp cho suy luận rằng xu hướng tăng trung bình bảo đảm một chuỗi quan sát cũng tăng. [Mục 9, tr. 1033; Hình 14, tr. 1034]

## 7. Thiết kế mô phỏng, đối chứng và mức đầy đủ của thông tin

Không có dữ liệu thực, nhóm can thiệp lâm sàng, chia huấn luyện/kiểm tra hoặc tập kiểm tra độc lập trong công trình này. “Kiểm chứng” chủ yếu là đối chiếu hình học, công thức và mô phỏng của các mô hình đã biết. [Mục 2–9]

| Khối kiểm chứng                 | Thông tin tác giả báo cáo                                                                            | Vai trò và giới hạn                                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| Hình học nếp gấp, Hình 2      | ε = 0 ở hình giới hạn; ε = 0,02 và điều kiện đầu (1,2; −0,6) ở hình động                 | Minh họa ghép đoạn và độ trễ; chưa kiểm tra quy luật số mũ trên một dải ε                        |
| Độ trễ Hopf, Hình 4            | Hệ số Lyapunov thứ nhất 1; ε = 0,01; điều kiện đầu (0,3; 0,3; −0,5)                            | Minh họa bám nhánh đẩy sau y = 0; chưa lượng hóa sai số dự đoán thời điểm ra                      |
| Vùng ổn định OU, Hình 5       | ε = 0,02; σ = 0,1; α = 1                                                                               | Mô hình tham chiếu không mất ổn định; một minh họa tập trung quỹ đạo                                |
| Phân nhánh mật độ, Hình 6–7 | Hình 6 dùng σ bằng căn 0,8; các điểm P ở ±0,4; Hình 7 dẫn (33)                                | Minh họa phân nhánh P/D; kết luận phương sai ở Hình 7 có bất nhất với (32)                           |
| van der Pol ngẫu nhiên, Hình 8  | ε = 0,05; a = 1,05; σ = 0,1; đầu (2; 2/3); chạy tới τ = 2.400; phương pháp Euler–Maruyama      | Cho ví dụ nhiễu tạo dao động lớn; một quỹ đạo, chưa có phân bố xác suất sự kiện                |
| Mật độ dừng, Hình 9           | Ba dạng chuẩn, ε = 0; σ = 0,1; miền (43), mật độ (44), biên phản xạ                            | Tính phương sai với bài toán biên đã chỉ định                                                         |
| Tập quỹ đạo, Hình 10          | 1.000 quỹ đạo; σ = 0,1; ε = 0,02; loại theo (43)                                                    | Đối chiếu phương sai và tỷ lệ thoát với phép tính dừng                                               |
| Cửa sổ, Hình 11–12             | Cùng σ và ε; s xấp xỉ 14,3051; khoảng y xấp xỉ 0,2861; Hình 11 có 1.000 quỹ đạo             | Chỉ ra ảnh hưởng của cửa sổ và xu hướng tất định; không tối ưu s                                  |
| Tự tương quan, Hình 13–14     | 10.000 quỹ đạo ở Hình 13, hai quỹ đạo ở Hình 14; k = 0,002; đoạn dài 8k; σ = 0,1; ε = 0,02 | Phân biệt xu hướng trung bình với sai lệch trên từng quỹ đạo; cách chuyển k sang chỉ số chưa rõ |

Nguồn: chú thích Hình 2, tr. 1023; Hình 4–5, tr. 1025–1027; Hình 6–8, tr. 1028–1030; Mục 7–9 và Hình 9–14, tr. 1030–1034. Các dấu chấm phẩy trong điều kiện đầu tách tọa độ; dấu phẩy trong số là dấu thập phân.

Các **phương án đối chiếu** gồm hệ tất định với ngẫu nhiên; vùng OU còn ổn định với vùng gần mất ổn định; ba dạng chuẩn; mật độ dừng phản xạ với mô phỏng loại quỹ đạo; và trung bình nhiều quỹ đạo với quan sát từng quỹ đạo. Bài không so sánh hiệu năng với một danh sách thuật toán cảnh báo khác, không báo cáo thí nghiệm loại bỏ từng thành phần trong một bộ dự báo, không dùng tín hiệu thay thế để định lượng tính đặc hiệu. Mô hình OU và cân bằng tất định van der Pol cung cấp đối chiếu cơ chế có giới hạn, không tạo thành một đánh giá cảnh báo sai trên tập không có sự kiện. [Mục 4, 6–9]

Những chi tiết **PDF không cung cấp đủ để tái lập chính xác từng đường** gồm: mã nguồn hoặc kho mã; hạt giống ngẫu nhiên; bước tích phân và bước lưu mẫu đầy đủ; điều kiện đầu cho toàn bộ các quần thể ở Mục 8–9; tiêu chí số cụ thể để giải tích phân và cắt miền vô hạn; xử lý cửa sổ khi quỹ đạo bị loại; sai số Monte Carlo và kiểm tra hội tụ theo bước thời gian. Điều này nói về thông tin trong PDF, không khẳng định các tài nguyên đó không tồn tại ở nơi khác. [Mục 6–9, tr. 1030–1034; danh mục tài liệu, tr. 1034–1035]

Bài không báo cáo khoảng tin cậy cho xu hướng, độ bao phủ, kiểm định giả thuyết, thước đo phân biệt sự kiện/không sự kiện hoặc khảo sát độ nhạy có hệ thống theo ε, σ, s và độ trễ. Một số lựa chọn và thang tiệm cận được thảo luận về lý thuyết; việc đó không thay cho khảo sát hữu hạn về độ bền của chỉ báo. [Mục 8–10, tr. 1031–1034]

## 8. Các hình kiểm tra điều gì và chưa chứng minh điều gì?

| Hình, trang         | Khẳng định được khảo sát và điều thể hiện                                                                       | Giới hạn của bằng chứng                                                                                     |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| 1, tr. 1022          | Hai chuỗi mô phỏng nếp gấp/trao đổi ổn định có thay đổi nhanh giống một số chuỗi ứng dụng về hình thức | Không có dữ liệu thực; mốc đỏ không phải kết quả phát hiện tự động                              |
| 2–3, tr. 1023–1024 | Hình học chuyển từ bám nhánh chậm sang thoát nhanh; phân biệt các cấu trúc phân nhánh                         | Không xác nhận loại phân nhánh của một hệ thực chưa biết; không lượng hóa hiệu năng EWS        |
| 4, tr. 1025          | Quỹ đạo Hopf dưới tới hạn có thể nhảy sau mốc mất ổn định tĩnh                                               | Một cấu hình; chưa kiểm chứng dự báo thời điểm nhảy từ tham số ước lượng                       |
| 5, tr. 1027          | Quỹ đạo OU ở vùng ổn định và lân cận phụ thuộc phương sai                                                     | Một minh họa không chứng minh xác suất bao phủ thực nghiệm hoặc giới hạn báo động                 |
| 6, tr. 1028          | Điểm P thay đổi hình dạng mật độ khác vị trí điểm D                                                            | Không chứng minh có thể phát hiện sớm điểm P từ một chuỗi hữu hạn                                  |
| 7, tr. 1029          | Tác giả trình bày phương sai không đơn điệu của ví dụ nhiễu nhân                                             | Chưa dùng làm bằng chứng chắc chắn vì mật độ (32) chuẩn hóa cho mômen khác (33)                   |
| 8, tr. 1030          | Nhiễu có thể tạo chuyển động lớn lặp lại quanh hệ tất định vốn có cân bằng ổn định                      | Một quỹ đạo không cho tần suất, xác suất thoát hoặc tỷ lệ dự báo đúng                           |
| 9, tr. 1031          | Phương sai của ba mật độ phản xạ tăng rồi đạt cực đại và giảm; khác nhau giữa cơ chế                    | Cực đại phụ thuộc mô hình biên; không phải mốc phân nhánh mới được xác nhận                   |
| 10, tr. 1032         | So sánh mật độ dừng và tập quỹ đạo động; tỷ lệ thoát tăng ở trao đổi ổn định/chạc ba                  | Hai phía đổi cả ε và biên; phương sai quỹ đạo còn lại chịu ảnh hưởng loại mẫu                |
| 11, tr. 1032         | Thống kê cửa sổ cho xu hướng khác đại lượng tại y cố định                                                     | Kết quả còn tổng hợp từ 1.000 quỹ đạo, chưa đánh giá độ tin cậy từng chuỗi                     |
| 12, tr. 1033         | Hình học nhánh nếp gấp làm phương sai cửa sổ tăng do trung bình biến thiên                                     | Các đoạn đỏ minh họa phương sai đã phóng đại 20 lần, không phải khoảng tin cậy                 |
| 13, tr. 1033         | Tự tương quan trung bình tăng; trao đổi ổn định/chạc ba gần trùng nhau                                          | Đường xấp xỉ tuyến tính/bậc hai là mô tả trong miền mô phỏng; chưa phải định luật phân loại |
| 14, tr. 1034         | Hai chuỗi cùng cơ chế có thể có xu hướng tự tương quan trái dấu                                                | Chứng minh khả năng sai trên từng chuỗi, chưa ước lượng được tỷ lệ sai trong quần thể          |

Hình 9–14 tạo mạch bằng chứng quan trọng nhất cho thực hành phân tích chuỗi. Trước hết, lý thuyết cục bộ dự đoán tăng độ phân tán. Tiếp đó, điều kiện biên và sự thoát thay đổi mômen sát ngưỡng. Cuối cùng, cách tính trong một cửa sổ hữu hạn và biến động giữa quỹ đạo tạo thêm sai lệch. Vì vậy, “chỉ báo tăng” phải đi kèm định nghĩa chỉ báo, quần thể được giữ lại, miền tham số và cách quan sát. Đây là tổng hợp của người phân tích từ Mục 7–9, không phải kết quả của một phép đánh giá dự báo bổ sung.

## 9. Đóng góp thực sự, giới hạn và khả năng chuyển sang tín hiệu y sinh

Đóng góp rõ nhất là biến một tập quan sát rời rạc thành một chuỗi câu hỏi có cấu trúc: hệ bám nhánh ổn định nào; nhánh mất ổn định theo cơ chế gì; tham số trôi ra sao; nhiễu có làm thoát trước ngưỡng hay không; và đại lượng từ dữ liệu có cùng nghĩa với đại lượng lý thuyết hay không. Các số mũ hồi phục và phân biệt độ trễ với ngưỡng tĩnh làm rõ hơn vì sao các chuyển tiếp khác nhau có thể cho xu hướng khác nhau. [Mục 2–4, tr. 1021–1027]

Mặt mạnh tiếp theo là việc không dừng ở công thức phương sai: tác giả trực tiếp cho thấy ảnh hưởng của phản xạ/thoát, cửa sổ và quỹ đạo đơn lẻ. Hình 14 đặc biệt có giá trị vì ngăn việc suy ra hiệu năng cá thể từ trung bình quần thể. Ngược lại, kết luận phương sai của riêng ví dụ nhiễu nhân tại Mục 5 cần tạm giữ do bất nhất nội tại đã nêu; không nên dùng nó làm cơ sở duy nhất để thiết kế chỉ báo mới. [Mục 5, tr. 1028–1029; Mục 7–9, tr. 1030–1034]

Những tình huống mà chỉ báo có thể thất bại hoặc bị diễn giải quá mức gồm:

- Nhiễu đủ lớn gây thoát khi hệ còn cách ngưỡng tất định; xu hướng cảnh báo gắn với ngưỡng đó có thể chưa xuất hiện rõ. [Mục 6, tr. 1029–1030]
- Điều kiện biên, loại quỹ đạo đã thoát hoặc số quỹ đạo còn lại làm phương sai sát ngưỡng khác đại lượng lý thuyết mong đợi. [Mục 7–8, tr. 1030–1032]
- Xu hướng trung bình do hình học bị tính chung vào phương sai, như nếp gấp trong cửa sổ dài. [Mục 8, Hình 12, tr. 1032–1033]
- Một chuỗi ngắn cho ước lượng tự tương quan quá dao động để xác định đúng dấu xu hướng. [Mục 9, Hình 14, tr. 1033–1034]
- Biến đổi tọa độ hoặc biến chậm ngẫu nhiên thay đổi phương sai của đại lượng quan sát. [Ví dụ 4.2, tr. 1027]
- Dùng kết quả một chiều cho Hopf có nhiễu hai thành phần, hệ không gian hoặc cơ chế toàn cục vượt phạm vi đã phân tích. Tác giả nêu trực tiếp các hướng chưa xử lý này. [Mục 10(a)–(f), tr. 1033–1034]

**Khả năng chuyển sang y sinh — giả thuyết của người phân tích, chưa được bài kiểm chứng:** có thể dùng khung này để đặt giả thuyết cơ chế cho biến đổi trước cơn bệnh, nhưng phải xác định biến quan sát liên hệ với trạng thái động lực học nào và đại lượng nào thực sự biến thiên chậm. Điện não đồ (*electroencephalography*, EEG) là một ví dụ về phép đo nhiều kênh có thể được khảo sát sau này; bài hiện tại không có dữ liệu EEG, không nhận dạng phân nhánh từ EEG và không báo cáo dự báo động kinh. Tác giả chỉ dùng hen và động kinh làm động cơ ở phần mở đầu. [Mục 1, tr. 1020; phạm vi mô hình, Mục 7–10]

Một thiết kế bổ sung hợp lý sẽ kiểm tra liệu phương sai tăng còn tồn tại sau khi xử lý xu hướng trung bình và biến thiên của nhiễu; so sánh các đoạn có và không có sự kiện; tách người bệnh giữa giai đoạn phát triển và đánh giá; đo thời gian báo trước cùng tỷ lệ cảnh báo sai. Đây là kế hoạch của người phân tích, chưa được thực hiện ở bước hiện tại, và chưa phải một “khoảng trống y sinh” đã được xác lập bằng tổng quan tài liệu. Không mặc định cơn bệnh nào cũng có chậm dần tới hạn, phân nhánh hoặc tách thang thời gian như các dạng chuẩn.

## 10. Hồ sơ phương pháp

| Trường                                                  | Nội dung                                                                                                                                                                                                                                                                                                     |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Bài toán (Problem)**                            | Đặc tả chuyển tiếp từ bám nhánh chậm ổn định sang chuyển động nhanh, và giải thích điều kiện xuất hiện hoặc thất bại của các dấu hiệu trước chuyển tiếp.                                                                                                                    |
| **Đầu vào (Input)**                              | Phương trình tất định/ngẫu nhiên đã biết, tham số và điều kiện biên; chuỗi mô phỏng một biến nhanh, một hoặc nhiều quỹ đạo. Hopf dùng hai biến nhanh ở phần cấu trúc/độ trễ.                                                                                             |
| **Thông tin biết trước (Known information)**    | Loại dạng chuẩn, mốc phân nhánh, nhánh hút/đẩy, ε, σ và y trong mô phỏng; các biên loại quỹ đạo. Không phải bài toán hoàn toàn không biết cơ chế.                                                                                                                              |
| **Đầu ra (Output)**                               | Định nghĩa/phân loại chuyển tiếp, số mũ hồi phục, độ trễ và quy luật thoát, mật độ dừng và mômen; đường phương sai/tự tương quan, tỷ lệ thoát.                                                                                                                              |
| **Phương án đối chiếu (Existing baseline)**   | OU xa chuyển tiếp; hệ tất định; các loại phân nhánh; mật độ phản xạ so với mô phỏng loại quỹ đạo; thống kê tập quỹ đạo so với cửa sổ. Không có bảng so sánh thuật toán dự báo.                                                                                         |
| **Thành phần mới (New component)**               | Cụ thể hóa khung nhanh–chậm cho khái niệm chuyển tiếp và các thước đo liên quan; nối lý thuyết chuẩn với EWS; phân tích giải tích, số và hình học các sai lệch của chỉ báo. Tính mới không được xác minh bằng tra cứu ngoài PDF.                                   |
| **Giả định (Assumptions)**                       | Tách thang thời gian; trường vectơ đủ trơn; bám nhánh hút trước chuyển tiếp; dạng chuẩn cục bộ; phần lớn phép tính dùng nhiễu cộng nhỏ và biến chậm tất định; mật độ dừng phụ thuộc điều kiện biên đã chọn.                                                     |
| **Kiểm chứng (Validation)**                       | Chứng minh/phát biểu định lý và dẫn kết quả trước; mật độ Fokker–Planck; mô phỏng 1.000 hoặc 10.000 quỹ đạo ở các cấu hình chính; ví dụ từng quỹ đạo. Không có dữ liệu thực hoặc kiểm tra dự báo ngoài mẫu.                                                       |
| **Kết quả chính (Main finding)**                 | Một số dạng chuẩn có hồi phục chậm và chỉ báo trung bình tăng trong miền thích hợp; độ trễ, nhiễu, biên và cửa sổ làm thay đổi diễn giải. Xu hướng trung bình không bảo đảm cảnh báo đúng cho một chuỗi.                                                            |
| **Câu hỏi còn mở (Unresolved questions)**       | Nhận dạng riêng tham số từ hệ số hiệu dụng; quan sát được nhánh mật độ nào để dùng dấu hiệu P; độ tin cậy từng chuỗi; cửa sổ/độ trễ; biến đổi tọa độ; Hopf ngẫu nhiên đầy đủ, cơ chế toàn cục/không gian; xử lý bất nhất công thức trước tái lập. |
| **Khả năng tái lập (Reproduction feasibility)** | Khá thuận lợi cho tính lại mật độ (43)–(44) và mô phỏng định tính Hình 9–14; tái lập chính xác đường gốc bị giới hạn bởi thiếu mã, bước thời gian/lấy mẫu và chi tiết xử lý. Mục 5 cần giải quyết bất nhất (32)–(33) trước.                                  |

Nguồn cho hồ sơ: Mục 1–10, tr. 1020–1034; chi tiết thông số tại Hình 2, 4–14. Các đánh giá tính khả thi và câu hỏi triển khai là nhận định của người phân tích.

## 11. Đọc tiếp và quyết định tái lập

**Quyết định chính: phương pháp nền tảng (Core methodology).** Bài thích hợp làm cơ sở để chọn cơ chế, xác định giả định và hiểu giới hạn của chỉ báo. Chưa nên xem nó như một thuật toán dự báo có thể mang sang dữ liệu thực rồi đánh giá trực tiếp theo một quy trình đã hoàn chỉnh. Các phép tính nhiễu cộng ở Mục 7–9 là những khối nhỏ có thể tái lập sau, nhưng đó là một kế hoạch có điều kiện, không phải khẳng định đã chạy lại thành công.

Thứ tự kiểm tra đầu tiên được đề xuất như sau:

1. **Làm rõ các công thức nguồn trước khi sinh dữ liệu:** kiểm tra dấu của chuyển động y trong Mục 3 và 6; điều kiện bỏ nhiễu chậm trong (20); công thức OU, khả năng nhận dạng và phép đổi tọa độ; chuẩn hóa, nhánh độ đo và mômen của (32) so với (33); dấu rào thế năng; cách định nghĩa v và độ trễ k ở Mục 9. Kiểm định ở đây đã giải quyết được một số đẳng thức đại số, nhưng chưa xác minh một bản triển khai của tác giả hoặc những giả thiết đầy đủ được dẫn sang tài liệu ngoài. [Tr. 1025–1029, 1032]
2. **Tính lại Hình 9 từ (43)–(44):** ưu tiên tích phân mật độ và mômen tại σ = 0,1; kiểm tra chuẩn hóa, miền và ảnh hưởng biên. Đây là khối có đầu vào được đặc tả rõ nhất. [Mục 7, tr. 1030–1031]
3. **Mô phỏng Hình 10:** ghi riêng số quỹ đạo còn lại và tỷ lệ thoát; cố định quy tắc loại; kiểm tra hội tụ theo bước tích phân. Đối chiếu với mật độ phản xạ phải thừa nhận hai bài toán biên khác nhau. [Mục 8, tr. 1031–1032]
4. **Tính cửa sổ và tự tương quan:** dùng cùng cách chuẩn hóa đã công bố rõ; khảo sát ảnh hưởng cửa sổ, độ trễ và khử xu hướng; báo cáo phân bố kết quả giữa quỹ đạo thay vì chỉ trung bình. Đây là bổ sung của người phân tích, chưa được thực hiện. [Mục 8–9, tr. 1031–1034]

Không cần dữ liệu thực để tái lập các mô hình ở đây vì phương trình sinh dữ liệu đã có trong PDF. Cần tự công bố đầy đủ thuật toán số, hạt giống, bước thời gian, điều kiện đầu, quy tắc thoát, cắt miền và cách tổng hợp. Những quyết định tự bổ sung phải được đánh dấu để phân biệt **tái lập định tính** với khôi phục chính xác đường gốc. PDF không nêu một kho mã hoặc gói dữ liệu công khai để tải trực tiếp. [Mục 6–9, tr. 1030–1034]

Các tài liệu sau **chỉ được gợi ý từ danh mục của PDF, chưa được đọc trong bước này**:

| Ưu tiên | Tài liệu được bài dẫn, kèm nghĩa tiếng Việt                                                                                                                                                                                                                                                    | Lý do đọc tiếp                                                                                                                                                                                                            |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1         | [32] N. Berglund, B. Gentz (2006), *Noise-Induced Phenomena in Slow-Fast Dynamical Systems* — “Các hiện tượng do nhiễu trong hệ động lực chậm–nhanh”                                                                                                                                      | Kiểm tra giả thiết đầy đủ của tập trung quỹ đạo, thoát và các thang nhiễu; bản hiện tại chỉ tóm tắt các kết quả.                                                                                     |
| 2         | [35] C. Kuehn (2011), *A mathematical framework for critical transitions: normal forms, variance and applications* — “Khung toán học cho chuyển tiếp tới hạn: dạng chuẩn, phương sai và ứng dụng”; định danh ghi trong PDF: arXiv:1101.2908                                           | Tác giả chỉ sang tài liệu này cho dạng chuẩn, quy luật phương sai và các phân nhánh cần tới hai điều kiện suy biến độc lập. Không mặc định tài liệu đó giải quyết các bất nhất ở đây. |
| 3         | [37] M. Krupa, P. Szmolyan (2001), *Extending geometric singular perturbation theory to nonhyperbolic points — fold and canard points in two dimensions* — “Mở rộng lý thuyết nhiễu loạn kỳ dị hình học tới điểm không hyperbol: điểm nếp gấp và điểm canard trong hai chiều” | Kiểm tra phát biểu và hướng tham số cho độ trễ nếp gấp; canard chỉ quỹ đạo đặc biệt có thể bám cả nhánh hút và nhánh đẩy.                                                                        |
| 4         | [64] L. Arnold, P. Boxler (1992), *Stochastic bifurcation: instructive examples in dimension one* — “Phân nhánh ngẫu nhiên: các ví dụ minh họa một chiều”                                                                                                                                  | Kiểm tra miền ngẫu nhiên, mật độ và mômen của ví dụ nhiễu nhân trước khi dùng Hình 7.                                                                                                                       |
| 5         | [70] D. J. Highham, tên ghi theo danh mục PDF (2001), *An algorithmic introduction to numerical simulation of stochastic differential equations* — “Nhập môn thuật toán mô phỏng số phương trình vi phân ngẫu nhiên”                                                                  | Xác định cách triển khai và kiểm tra hội tụ phương pháp số. Tên trong danh mục cần đối chiếu khi tìm tài liệu; chưa xác minh bên ngoài.                                                             |
| 6         | [1] M. Scheffer và cộng sự (2009), *Early-warning signals for critical transitions* — “Dấu hiệu cảnh báo sớm cho chuyển tiếp tới hạn”                                                                                                                                                    | Đọc phần tổng quan ứng dụng mà bài hiện tại tự đặt vai trò bổ sung về toán học.                                                                                                                             |

Nguồn bảng: danh mục tài liệu, tr. 1034–1035; vai trò các tài liệu được nêu ở Mục 1–10. Năm và tình trạng tài liệu ở đây theo PDF năm 2011, không phải xác minh tình trạng xuất bản hiện tại.

## 12. Ghi nhận kiểm tra bản phân tích

Đã kiểm tra cách diễn đạt tiếng Việt, định nghĩa thuật ngữ và phân biệt kết quả tác giả với suy luận của người phân tích. Các công thức trọng tâm đã được đối chiếu với trang PDF gốc; những chỗ bản in không nhất quán được ghi rõ thay vì âm thầm sửa. Đã đọc lại tệp lưu trên đĩa và kiểm tra cú pháp khối toán: dấu dollar kép đứng riêng dòng, có cặp, nội dung không rỗng; ngoặc nhọn và môi trường căn chỉnh cân bằng; không có ký tự điều khiển lỗi hoặc công thức trong ô bảng/khối mã. Chưa có bước xác nhận hiển thị toàn bộ bằng một trình xem Markdown hỗ trợ toán, nên kiểm tra cú pháp không được gọi là đã biên dịch hoặc kiểm tra hiển thị thành công.

Chưa chạy tái lập các mô phỏng của bài. Trong Prompt 02, đã dùng đại số ký hiệu để xác nhận mômen của (32), dạng viết lại của (33), tính bất biến của các hệ số OU khi đổi tham số, dấu hiệu thế năng và đạo hàm các nguyên hàm trong (44). Các đẳng thức được kiểm tra bằng cách rút gọn hiệu về 0; đây là kiểm tra nội bộ công thức, không phải tái lập Hình 7 hoặc Hình 9–14, và cũng không phải kiểm chứng một mô hình trên dữ liệu thực. Chỉ cập nhật tệp phân tích này; không sửa PDF, bản thảo thảo luận nghiên cứu hoặc các tài liệu khác.

## Critical Audit

Phần này kiểm định bản chất phương pháp và độ mạnh của bằng chứng trong chính PDF. Các kết quả suy ra bổ sung đã được ghi rõ trong phần Explore phía trên; không dùng tài liệu ngoài và không coi danh mục tham khảo là các nguồn đã đọc độc lập.

### Verified strengths — Những điểm mạnh đã đối chiếu

- **Đặc tả cơ chế có cấu trúc:** Định nghĩa 2.4 nối nhánh hút của hệ nhanh với một quỹ đạo ứng viên chuyển sang chuyển động nhanh; Mệnh đề 2.5–2.8 phân biệt nếp gấp, Hopf và chạc ba dưới/trên tới hạn, cùng trao đổi ổn định. Mệnh đề 2.10 cho số mũ hồi phục khác nhau từ các dạng chuẩn, có thể đối chiếu bằng tuyến tính hóa. Đây là kết quả về mô hình, không phải nhận dạng cơ chế từ một chuỗi chưa biết phương trình. [Mục 2, tr. 1022–1025]
- **Có kiểm tra bằng nhiều cách và không che giấu phản ví dụ thực hành:** phương trình phương sai và mô hình OU mô tả vùng còn hút; mật độ Fokker–Planck và mô phỏng cho phép so sánh các mô hình biên; Hình 12 chỉ ra phần biến thiên tất định lẫn vào phương sai; Hình 14 cho ví dụ xu hướng tự tương quan sai dấu trên một quỹ đạo. Đạo hàm các nguyên hàm ở (44) đúng bằng trường vectơ tương ứng ở (43), theo kiểm tra đại số của người phân tích. [Mục 4, tr. 1026–1027; Mục 7–9, tr. 1030–1034]
- **Có nền tảng để mở rộng với phạm vi đã nêu:** bài phân biệt ngưỡng tĩnh, độ trễ và thoát do nhiễu; phần thảo luận thừa nhận chưa giải quyết Hopf ngẫu nhiên đầy đủ, cấu trúc không gian, phân nhánh toàn cục và ảnh hưởng nhiễu lên độ trễ. Những điểm mạnh này không phụ thuộc việc chấp nhận công thức phương sai sai khác ở Mục 5. [Mục 3, tr. 1025; Mục 6, tr. 1029–1030; Mục 10, tr. 1033–1034]

### Corrections / qualifications — Các sửa chữa và giới hạn diễn giải

- **Mômen của ví dụ nhiễu nhân:** mật độ (32) chuẩn hóa có trung bình y và phương sai bằng y nhân σ bình phương chia 2 trên nhánh y dương. Trung bình được in bằng N nhân y; (33) có thêm hạng không âm phụ thuộc N như đã viết rõ tại Mục 5.3 của bản phân tích. Do đó nhận định về cực trị phương sai ở Hình 7 chưa được chính mô hình và mật độ đã in hỗ trợ. Đã giữ riêng kết luận này với khả năng phương sai giảm khi đi từ phía y dương về 0; hai nhận định không tương đương. [Phương trình (28)–(33), tr. 1028–1029; Hình 7]
- **Điều kiện của công thức và phép xấp xỉ:** đã thay việc để mở công thức OU quá độ bằng kết quả suy ra trực tiếp từ (23), phân biệt mômen tích, hiệp phương sai và tự tương quan dừng. Đã chỉ rõ (20) cần bỏ hoặc kiểm soát nhiễu biến chậm; y không tất định chỉ vì phương trình của nó không có nhiễu trực tiếp. Đồng thời ghi dấu không nhất quán ở hệ nếp gấp trước Định lý 3.2, hướng g trong Định lý 6.1 và hiệu thế năng ở Mục 6. Đây là những bất nhất xác định được trong bản in; chưa thể suy ra tác giả đã dùng cùng các biểu thức ấy trong mã mô phỏng. [Tr. 1025–1027, 1029]
- **Khả năng nhận dạng và quan sát:** một chuỗi OU chỉ xác định các hệ số hiệu dụng khi không có thông tin hiệu chuẩn bổ sung; phép đổi tham số tại Mục 5.2 của bản phân tích chứng minh sự không duy nhất. Tương tự, điểm P đứng trước điểm D trên sơ đồ không bảo đảm xuất hiện trong mật độ của nhánh hút đang được quan sát; nghiệm x bằng 0 của (28) là trường hợp cụ thể không tự phát sinh dao động. Đã giới hạn phát biểu dự báo dựa vào P và các gợi ý suy luận tham số. [Phương trình (25), (28)–(32), tr. 1027–1029]
- **Diễn giải chỉ báo:** phương sai Hình 10 phụ thuộc tập còn sống, Hình 11 vẫn tổng hợp 1.000 quỹ đạo, còn Hình 13 lấy trung bình 10.000 quỹ đạo. Chúng chưa chứng minh dự báo cá thể hoặc phân loại cơ chế; các đường gần tuyến tính/bậc hai chỉ mô tả miền mô phỏng. Đã giữ nguyên công thức tự tương quan theo bản in nhưng chỉ rõ bất nhất giữa v và bình phương v, cùng thiếu phép đổi k từ thời gian sang chỉ số. [Mục 8–9, Hình 10–14, tr. 1031–1034]

### Methodological limitations — Những giới hạn phương pháp luận

- **Bản chất nhiệm vụ và độ mạnh của bằng chứng:** bằng chứng chắc nhất thuộc về mô tả động lực học và phân tích mô hình có phương trình, dạng phân nhánh và tham số đã biết. Có chứng minh cho các mệnh đề trong bài, định lý được dẫn từ công trình trước và mô phỏng dạng chuẩn; không có thí nghiệm kiểm soát trên hệ thực hoặc dữ liệu ứng dụng. Các giả thiết đầy đủ của Định lý 3.3, 4.1 và 6.1 không được trình bày hoặc chứng minh trọn vẹn ở đây. Bài chưa có quy tắc báo động, hiệu chuẩn xác suất, thời gian báo trước, so sánh hiệu năng hoặc đánh giá ngoài mẫu. Đây là **chưa được báo cáo**, không phải một thí nghiệm dự báo đã thất bại. [Mục 2–9, đặc biệt tr. 1025–1026, 1029, 1031–1034]
- **Tính đặc hiệu và phụ thuộc thống kê:** một chỉ báo tăng không xác định duy nhất suy yếu ổn định; hình học trung bình, biến thiên của nhiễu, tọa độ quan sát và loại quỹ đạo đều có thể tác động. Hình 9–10 đổi đồng thời ε và biên, nên không tách riêng được hai nguyên nhân. Các điểm liên tiếp và cửa sổ chồng lấn không độc lập; số quỹ đạo khởi tạo lớn không thay cho sai số ước lượng trên một chuỗi hoặc độ bất định sau loại mẫu. Thiếu tín hiệu thay thế, đối chứng không có sự kiện và đánh giá độ nhạy có hệ thống để định lượng tính đặc hiệu và cảnh báo sai. [Ví dụ 4.2, tr. 1027; Mục 7–9, tr. 1030–1034]
- **Tái lập:** các phương trình và phần lớn thông số chính đủ để xây dựng bản triển khai độc lập có ghi rõ lựa chọn. Tuy nhiên, mã, hạt giống, bước tích phân/lấy mẫu, đầy đủ điều kiện đầu, xử lý cửa sổ khi thoát, chi tiết tổng hợp Hình 11 và chuyển đổi độ trễ chưa được PDF đặc tả đủ. Ưu tiên tái lập mật độ (43)–(44), sau đó mô phỏng có báo số quỹ đạo còn lại; chưa thể cam kết khôi phục chính xác đường gốc hoặc đánh giá độ bền từ một cấu hình duy nhất. Không cần chia huấn luyện/kiểm tra cho kiểm tra công thức; chỉ cần thiết kế đánh giá độc lập khi phát triển thêm bộ dự báo. [Mục 7–9, tr. 1030–1034]
- **Chuyển sang y sinh — giả thuyết:** với điện tâm đồ (*electrocardiography*, ECG), điện não đồ (EEG) hoặc tín hiệu quang thể tích (*photoplethysmography*, PPG), cần chỉ rõ phép đo liên hệ với trạng thái nào, biến chậm nào được quan sát hoặc suy luận, và sự kiện đích được gán nhãn thế nào. Không thể mặc định biên độ tín hiệu thô là dao động quanh cân bằng một chiều; cần kiểm tra tính dừng cục bộ, tách thang thời gian, nhiễu đo, xu hướng và phép biến đổi đặc trưng. Đánh giá trên người bệnh độc lập cùng thời gian báo trước và cảnh báo sai là yêu cầu cho một nghiên cứu tiếp theo, chưa phải tính hợp lệ lâm sàng hoặc khoảng trống tài liệu đã được xác lập. PDF chỉ nêu y học làm động cơ và không có kiểm chứng ECG/EEG/PPG. [Mục 1, tr. 1020; Ví dụ 4.2, tr. 1027; Mục 10, tr. 1033–1034]

### Open questions — Những câu hỏi còn mở

1. **Quan sát và nhận dạng:** với một chuỗi không biết y hoặc dạng chuẩn, thông tin phụ trợ nào đủ tách tốc độ trôi, lực hồi phục và nhiễu? Làm thế nào nhận diện nhánh độ đo phù hợp trước khi dùng dấu hiệu P? Đây là câu hỏi suy ra từ (25), (28)–(32), chưa được công trình trả lời bằng một quy trình ước lượng. [Tr. 1027–1029]
2. **Tái lập có kiểm soát:** sau khi quy định nhất quán các công thức nguồn, kết quả thay đổi thế nào khi giữ cùng điều kiện biên để quét ε, σ, cửa sổ và độ trễ, đồng thời báo sai số theo quỹ đạo còn sống? Đối chiếu mật độ phản xạ với phân bố điều kiện còn sống cần thực hiện riêng. Đây là kế hoạch của người phân tích, chưa chạy. [Phương trình (43)–(45), Hình 9–14, tr. 1030–1034]
3. **Từ chỉ báo tới dự báo:** một quy tắc chỉ dùng quan sát quá khứ có đạt thời gian báo trước hữu ích với mức cảnh báo sai xác định không, và có phân biệt được cơ chế ngoài các ví dụ dùng để phát triển nó không? Hình 14 đặt ra vấn đề độ tin cậy cá thể nhưng chưa trả lời bằng tỷ lệ sai; việc mở sang tín hiệu y sinh cần một thiết kế đánh giá riêng. [Mục 9–10, tr. 1033–1034]

**Novelty verdict — Kết luận về tính mới:** Xếp bài vào **Conceptual contribution — đóng góp khái niệm**, kèm **Methodological extension — mở rộng phương pháp luận**, vì bài phát triển cách đặc tả chuyển tiếp và liên kết lý thuyết nhanh–chậm/ngẫu nhiên đã có với phân tích EWS và sai lệch phép đo. Chưa đủ bằng chứng để xếp thành một **New method — phương pháp mới** độc lập dưới dạng bộ ước lượng hoặc thuật toán dự báo đã được kiểm chứng: ví dụ Arnold–Boxler được kế thừa, công thức phương sai Mục 5 có bất nhất, còn đánh giá trên dữ liệu thực, ngoài mẫu và quyền ưu tiên toàn lĩnh vực chưa được cung cấp. [Mục 1–5, tr. 1021–1029; Mục 7–10, tr. 1030–1034]
