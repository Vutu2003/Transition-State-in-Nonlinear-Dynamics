# Jella và cộng sự (2025) — Ngưng tụ tái diễn trong chuyển tiếp tới hạn của hệ phức tạp

**Tên bài báo:** *Recurrence condensation during critical transitions in complex systems* — “Ngưng tụ tái diễn trong các chuyển tiếp tới hạn của hệ phức tạp”.

**Tác giả:** Manaswini Jella, Induja Pavithran, Vishnu R. Unni, Norbert Marwan, Jürgen Kurths và R. I. Sujith. **Công bố:** *Chaos* **35**, 083107 (2025). **DOI:** [10.1063/5.0267157](https://doi.org/10.1063/5.0267157).

**Phạm vi nguồn:** Chỉ sử dụng [PDF được chỉ định](<../paper/10 Recurrence condensation during critical transitions in complex systems.pdf>), đã đọc toàn bộ 16 trang PDF và đối chiếu trực quan Hình 1–9. Không sử dụng web hoặc đọc tài liệu ngoài. Số trang bên dưới theo trang bài báo 083107-1 đến 083107-14, tương ứng trang PDF 3–16. Hai trang đầu là bìa; bìa lưu trữ ghi tập 36, nhưng trang nhà xuất bản và nội dung bài ghi **35**, nên thông tin công bố ở đây theo nội dung bài báo.

Bài báo đặt hai câu hỏi liên tiếp: khi hệ chuyển từ hỗn loạn sang tuần hoàn, cấu trúc tái diễn của quỹ đạo thay đổi như thế nào; và có thể dùng sự thay đổi đó để định vị một điểm tới hạn hay không? Tác giả gọi sự tập trung từ nhiều thang thời gian tái diễn về một thang chi phối là **ngưng tụ tái diễn** (*recurrence condensation*). Sau đó, tác giả dùng chất lượng khớp quy luật lũy thừa để chọn tham số tới hạn. Bằng chứng chính cho bước chọn tham số là sự trùng khớp với điểm phân nhánh Hopf đã biết trong hai trường hợp mô phỏng; chưa phải kiểm chứng khả năng dự báo trước một sự kiện chưa xảy ra. [Tóm tắt, tr. 1; Mục III–IV, tr. 7–12]

## 1. Bài toán, động cơ nghiên cứu và câu hỏi khoa học

Trong hệ nhiệt âm, tương tác giữa trường âm và tốc độ giải phóng nhiệt không ổn định có thể tạo dao động áp suất tự duy trì với biên độ lớn, đe dọa tính toàn vẹn của thiết bị. Buồng đốt trong bài trải qua quá trình chuyển từ dao động biên độ thấp sang dao động tuần hoàn biên độ cao. Giữa hai trạng thái là **trạng thái gián đoạn** (*intermittency*): các đoạn dao động tương đối đều đặn xen kẽ với dao động hỗn loạn. Quá trình chuyển dần như vậy khiến việc chọn một mốc tới hạn từ biên độ trở nên không rõ ràng. [Mục I, tr. 2–3; Mục III.A, tr. 7–8; Hình 2]

**Tác giả khẳng định (Authors claim):** Các phương pháp thống kê gặp khó khăn khi chuỗi ngắn, có nhiễu và chuyển tiếp diễn ra từ từ; phân tích tái diễn có thể nắm bắt những thay đổi tinh tế của động lực học. Đây là động cơ được tác giả nêu, không phải kết luận từ một thí nghiệm so sánh hiệu năng với phương sai, tự tương quan trễ 1 hoặc các thuật toán định vị điểm tới hạn khác. [Phần giới thiệu nghiên cứu, tr. 1–2; Mục I, tr. 2–3]

**Bằng chứng hỗ trợ (Evidence supports):** Các biểu diễn và đại lượng tái diễn biến đổi có cấu trúc khi tham số được thay đổi; mô hình Hopf cho phép đối chiếu điểm được chọn với mốc đã biết. Bài không báo cáo phép so sánh có hệ thống để chứng minh phương pháp vượt các **dấu hiệu cảnh báo sớm** (*early warning signals*, EWS) truyền thống, hoặc chịu nhiễu và thiếu dữ liệu tốt hơn các phương án khác. [Mục III.A–C, tr. 7–12; Hình 2–8]

**Diễn giải của người phân tích (Analyst interpretation):** Câu hỏi trọng tâm gồm mô tả sự tổ chức lại của động lực học và ước lượng vị trí tới hạn trong không gian tham số điều khiển. Giá trị phương pháp luận nằm ở cách nối hai phần này, thay vì chỉ nhận thấy một chỉ số tăng hoặc giảm. Tính đặc hiệu của tiêu chí chọn điểm đối với hiện tượng tới hạn vẫn cần kiểm tra thêm. [Mục III.B, tr. 9–10; Mục IV, tr. 12]

## 2. Đầu vào, thông tin biết trước và đầu ra

Đầu vào của toàn bộ quy trình thực nghiệm là **nhiều chuỗi áp suất một chiều, mỗi chuỗi gắn với một số Reynolds đã biết**. Một chuỗi tại một điều kiện đủ để dựng biểu diễn tái diễn, nhưng bước ước lượng điểm tới hạn cần so sánh nhiều điều kiện và cần giá trị của đại lượng tại chính điểm ứng viên. Vì vậy, “chỉ cần một đại lượng quan sát” không có nghĩa “chỉ cần một chuỗi duy nhất và không cần biết tham số điều khiển”. [Mục II.A, II.C, tr. 3–4; Mục III.B, tr. 8–10]

| Thành phần                        | Thí nghiệm buồng đốt                                                                                                                            | Kiểm chứng bằng mô hình                                                                                |
| ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| Dữ liệu đầu vào                | Dao động áp suất p′(t) tại nhiều giá trị Re                                                                                                 | Chuỗi biến dao động η(t) tại nhiều hệ số cản α                                                   |
| Thông tin biết trước            | Lưu lượng khí/nhiên liệu, thông tin để tính Re, tần số lấy mẫu và thứ tự thay đổi điều kiện                                    | Phương trình (1), các tham số mô hình, hệ số cản được điều khiển và điểm Hopf đã biết |
| Điều không cần biết đầy đủ | Phương trình chi phối toàn bộ buồng đốt                                                                                                     | Không phải bài toán khám phá phương trình: phương trình đã được chỉ định                |
| Đầu ra mô tả                    | Cấu trúc tái diễn, các thang thời gian chi phối và đại lượng định lượng theo Re                                                      | Các đại lượng định lượng theo α và quan hệ lũy thừa                                           |
| Đầu ra ước lượng              | Tham số tới hạn được chọn bằng tiêu chí khớp                                                                                              | Tham số tới hạn ước lượng để đối chiếu với mốc Hopf                                           |
| Nhãn đối chiếu                  | Không có nhãn sự kiện để huấn luyện bộ phân loại hoặc một mốc phân nhánh thực nghiệm độc lập dùng để tính độ chính xác | Điểm phân nhánh đã biết dùng để kiểm chứng, không phải nhãn huấn luyện                     |

Nguồn bảng: Mục II.A–D, tr. 3–6; Mục III.B–C, tr. 8–12.

Tác giả chia dữ liệu thành cửa sổ, tính các đại lượng rồi **lấy trung bình qua các cửa sổ**. Đầu ra dùng cho phép khớp là quan hệ giữa đại lượng và tham số. Việc có cửa sổ trượt ở bên trong không đồng nghĩa đã xây dựng một bộ phát hiện sự kiện trực tuyến. [Mục III.B, tr. 8]

Cần phân biệt ba mức sử dụng:

- **Mô tả hồi cứu:** giải thích sự thay đổi động lực học trên những điều kiện đã thu thập.
- **Định vị điểm tới hạn:** quét các điểm ứng viên, dùng giá trị tại ứng viên làm mốc và chọn quan hệ lũy thừa phù hợp nhất.
- **Dự báo trước sự kiện:** chỉ dùng dữ liệu có sẵn tại thời điểm dự báo để dự đoán một chuyển tiếp tương lai chưa biết. Bài chưa thiết kế quy trình này, chưa báo cáo thời gian báo trước, tỷ lệ cảnh báo sai hoặc đánh giá trên dữ liệu ngoài mẫu.

Phân biệt trên dựa vào quy trình ở Mục III.B–C, tr. 9–12 và Hình 3–8. Một số chỉ số đổi trước khi dao động tuần hoàn phát triển hoàn toàn là dấu hiệu tiền chuyển tiếp; điều đó chưa tự chứng minh khả năng dự báo trước một điểm tới hạn chưa biết.

Giá trị tham chiếu có thể được tính khi đã đo tới điểm ứng viên; dùng nó để định vị hồi cứu không tự tạo lỗi sử dụng dữ liệu tương lai. Tuy nhiên, dự báo từ một thời điểm sớm hơn không được dùng giá trị tại ứng viên chưa quan sát. Hơn nữa, việc so sánh cực tiểu trên cả dãy ứng viên, có các điểm vượt mốc được chọn như Hình 4, 6, 8, chưa cung cấp một quy tắc dừng trực tuyến đã được kiểm chứng. [Mục III.B–C, tr. 9–12]

## 3. Nguồn gốc phương pháp và phạm vi tính mới

Tác giả kế thừa phép nhúng trễ, biểu diễn tái diễn, các đại lượng định lượng, phân tích phổ liên xung và ý tưởng lũy thừa trong nghiên cứu trước. Tính mới cần tìm ở cách diễn giải và kết hợp chúng trong bài toán hiện tại. Đối chiếu dưới đây chỉ dựa vào những tài liệu được chính bài dẫn, không thay thế một tổng quan tài liệu có hệ thống. [Mục I, tr. 2–3; Mục IV, tr. 12]

| Thành phần                                                                                                           | Nguồn gốc mà bài báo nêu                                                                       | Vai trò trong công trình này                                                                                                                         |
| ---------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Đồ thị tái diễn** (*recurrence plot*, RP), phép nhúng trễ và chuẩn Euclid                          | Eckmann và cộng sự, tài liệu 47; Cao, tài liệu 48; Fraser–Swinney, tài liệu 49             | Công cụ được kế thừa, không phải biểu diễn mới do bài phát minh                                                                            |
| **Phân tích định lượng tái diễn** (*recurrence quantification analysis*, RQA) và cách chọn ngưỡng | Phương trình (2)–(11); tài liệu 35, 50–56                                                     | Dùng để đo sự tổ chức của các điểm tái diễn                                                                                                 |
| **Phổ liên xung** (*inter-spike spectrum*, ISS), biểu diễn các chu kỳ lặp của dãy đỉnh              | Kraemer và cộng sự (2022), tài liệu 52; Phụ lục                                               | Công cụ được kế thừa để làm rõ thang thời gian chi phối                                                                                     |
| **Ngưng tụ phổ** (*spectral condensation*), năng lượng tập trung vào một dạng dao động chi phối   | Pavithran và cộng sự (2020), tài liệu 32                                                        | Cơ sở liên tưởng cho cách diễn giải; chưa chứng minh hai hiện tượng tương đương                                                        |
| Quy luật lũy thừa của các đại lượng tái diễn                                                                | Afsar và cộng sự (2015), tài liệu 44, trong bối cảnh nhân đôi chu kỳ và biên hỗn loạn | Ý tưởng đã có tiền lệ, không thể coi mọi phép khớp RQA theo lũy thừa là mới                                                             |
| Ngưng tụ tái diễn và chọn mốc tới hạn qua chất lượng khớp                                                 | Mục III.A–C và IV                                                                                 | Phần được phát triển trong bài: nối cách diễn giải động lực học với thủ tục chọn tham số, có minh họa thực nghiệm và mô phỏng |

Nguồn: Mục I, tr. 2–3; Mục II.C–D, tr. 4–6; Mục IV, tr. 12; Phụ lục, tr. 13; danh mục tài liệu, tr. 13–14.

Ngay trong phần tổng quan, tác giả đã dẫn ứng dụng RP/RQA cho mất ổn định nhiệt âm trước đó, gồm tài liệu 41–42. Vì vậy, không đủ cơ sở gọi đây là lần đầu dùng phân tích tái diễn cho buồng đốt. Phần mở rộng cần đánh giá là cách diễn giải ngưng tụ tái diễn và thủ tục chọn mốc theo chất lượng khớp, trong bối cảnh chuyển từ hỗn loạn sang tuần hoàn. [Mục I, tr. 2–3]

## 4. Tái dựng quy trình phương pháp

### 4.1. Tái tạo không gian pha và xây dựng đồ thị tái diễn

Từ chuỗi một chiều, tác giả tạo các vectơ trạng thái bằng phép nhúng trễ. Dưới đây dùng τ_d cho độ trễ nhúng để phân biệt với độ trễ khi đo tái diễn; đây là đổi ký hiệu để giải thích, không phải thay đổi thuật toán:

$$
\mathbf X_i=
\left[x_i,x_{i+\tau_d},\ldots,x_{i+(m-1)\tau_d}\right].
$$

Chiều nhúng m được chọn bằng thuật toán Cao; độ trễ bằng phương pháp thông tin tương hỗ trung bình. Hai trạng thái được coi là tái diễn nếu khoảng cách Euclid nhỏ hơn ngưỡng ε:

$$
R_{ij}=
\Theta\!\left(\varepsilon-\|\mathbf X_i-\mathbf X_j\|_2\right).
$$

Θ là hàm bước Heaviside; R là ma trận nhị phân. N trong các công thức tái diễn cần được hiểu nhất quán với số vectơ trạng thái dùng trong tính toán, có xét phần dữ liệu mất do phép nhúng. [Mục II.C, tr. 4; Phương trình (2)]

Hai cách chọn ngưỡng phục vụ hai mục đích khác nhau:

1. **Để minh họa ở Hình 2:** ngưỡng bằng 20% kích thước tập hút; độ dài đoạn tín hiệu lần lượt là 1 s, 1 s và 0.1 s.
2. **Để tính RQA:** điều chỉnh ngưỡng sao cho **tỷ lệ tái diễn** (*recurrence rate*, RR) giữ ở 0.05. Theo mô tả của bài, các điểm tái diễn ứng với 5% khoảng cách cặp nhỏ nhất.

Nguồn: Mục II.C, tr. 4; chú thích Hình 2, tr. 5; Mục III.A, tr. 8. Vì RR được cố định, thay đổi cần quan tâm là cách các điểm tổ chức thành đường và khoảng trống, không phải RR tăng.

Bài chưa cho đầy đủ giá trị chiều nhúng và độ trễ thực tế, cách chọn chung hay riêng theo trạng thái, cách tính kích thước tập hút và toàn bộ bước chuẩn hóa dữ liệu. Quy ước xử lý đường chéo chính và **khoảng loại trừ lân cận thời gian** (*Theiler window*) trong việc đếm đường cũng chưa được xác định đầy đủ. Không nên tự xem quy ước mặc định của một thư viện là chi tiết tác giả đã báo cáo. [Mục II.C–D, tr. 4–6; Phương trình (3)]

### 4.2. Đo cấu trúc đường chéo và khoảng trống tái diễn

Gọi P(l) là số đường chéo có độ dài l. Đại lượng **mức xác định** (*determinism*, DET) đo tỷ phần điểm nằm trên các đường chéo đủ dài; **độ dài đường chéo trung bình** (*average diagonal line length*, L) đo độ dài trung bình của các đường đó:

$$
DET=
\frac{\sum_{l=l_{\min}}^{N}lP(l)}
{\sum_{l=1}^{N}lP(l)},
\qquad
L=
\frac{\sum_{l=l_{\min}}^{N}lP(l)}
{\sum_{l=l_{\min}}^{N}P(l)}.
$$

Hai đại lượng tăng phù hợp với việc các đoạn quỹ đạo duy trì diễn biến tương tự lâu hơn. Tên gọi DET không chứng minh hệ đã chuyển từ ngẫu nhiên sang xác định; tác giả vốn xem trạng thái đầu là hỗn loạn xác định có nhiễu. Đây cũng không phải phép đo độ chính xác dự báo ngoài mẫu. [Mục II.D.1, tr. 4–6; Phương trình (5)–(6); Mục III.A–B, tr. 7–9]

Với P(k) là số khoảng trống trắng theo phương thẳng đứng có độ dài k, bài dùng **thời gian tái diễn** (*recurrence time*, RT) và **entropy thời gian tái diễn** (*recurrence time entropy*, RTE):

$$
RT=
\frac{\sum_{k=k_{\min}}^{N}kP(k)}
{\sum_{k=k_{\min}}^{N}P(k)},
\qquad
RTE=-\sum_{k=k_{\min}}^{N}p(k)\ln p(k).
$$

RT đo khoảng không tái diễn trung bình; RTE đo độ bất định của độ dài các khoảng đó. Bài viết xác suất theo số đoạn trắng N_k:

$$
p(k)=\frac{P(k)}{N_k}.
$$

Khi tái triển khai, cần xác nhận cách chuẩn hóa trước hay sau khi loại các đoạn ngắn. RT ở đây là thời gian tái diễn, không phải thời gian hồi phục sau nhiễu loạn. [Mục II.D.2, tr. 6–7; Phương trình (10)–(11)]

| Đại lượng                                                                                                               | Cấu trúc được đo             | Xu hướng thực nghiệm        | Giới hạn diễn giải                                                                          |
| --------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- | ------------------------------- | ----------------------------------------------------------------------------------------------- |
| DET và L                                                                                                                   | Các đường chéo                | Tăng                           | Không tự chứng minh cơ chế nhân quả hoặc khả năng dự báo                            |
| **Entropy độ dài đường chéo** (*diagonal line entropy*, Entr)                                                | Phân bố độ dài đường chéo | Tăng ban đầu, sau đó giảm | Không thể gộp thành kết luận mọi loại entropy đều giảm                               |
| **Tỷ phần đường thẳng đứng** (*laminarity*, LAM) và **thời gian lưu giữ** (*trapping time*, TT) | Các đường đen thẳng đứng   | Giảm                           | Giảm lưu giữ cục bộ không đồng nghĩa giảm tính tuần hoàn                           |
| RT và RTE                                                                                                                  | Các khoảng trắng thẳng đứng  | Giảm                           | Khoảng trung bình ngắn hơn chưa đủ chứng minh toàn hệ chỉ còn một thang thời gian |

Nguồn: Mục II.D, tr. 4–7; Phương trình (7)–(11); Hình 3(I-b–h), tr. 6; Mục III.B, tr. 8–9.

Tác giả tính các đại lượng trên cửa sổ 1500 điểm rồi lấy trung bình; cả ba độ dài tối thiểu đều bằng 2:

$$
l_{\min}=v_{\min}=k_{\min}=2.
$$

Với lấy mẫu thực nghiệm 10 kHz, 1500 mẫu tương ứng 0.15 s trước khi xét ảnh hưởng phép nhúng; đây là quy đổi đơn vị của người phân tích. Bài không cho bước dịch hoặc mức chồng lấn cửa sổ, nên chưa thể suy ra số cửa sổ độc lập hay cỡ mẫu hiệu dụng. [Mục II.A, tr. 3; Mục III.B, tr. 8]

### 4.3. Từ tỷ lệ tái diễn theo độ trễ đến phổ liên xung

**Tỷ lệ tái diễn theo độ trễ** (*τ-recurrence rate*, τ-RR) là trung bình các phần tử trên một đường chéo lệch của ma trận tái diễn. Viết h cho độ trễ này để không nhầm với độ trễ nhúng:

$$
\tau\text{-}RR(h)=
\frac{1}{N-h}\sum_{i=1}^{N-h}R_{i,i+h}.
$$

Đỉnh xuất hiện tại những độ trễ mà hai trạng thái thường tái diễn. Trong Hình 2(III-E), trạng thái tuần hoàn vẫn tạo một dãy đỉnh lặp đều, không phải đường hằng trên mọi độ trễ. Vì vậy, lời mô tả của tác giả về một giá trị hằng cần được đọc cùng hình: dữ liệu trực quan ủng hộ một nhịp tái diễn chi phối. [Mục II.D, tr. 4; Phương trình (4); Hình 2(E), tr. 5; Mục III.A, tr. 8]

ISS biểu diễn dãy đỉnh bằng những **dãy xung Dirac cách đều** (*Dirac combs*) có chu kỳ khác nhau. Đây không phải phổ Fourier thông thường hoặc biểu đồ tần suất của thời gian tái diễn. Phụ lục viết bài toán tái dựng:

$$
\chi^T\boldsymbol\beta=\mathbf s.
$$

χ là tập hàm cơ sở, β là các hệ số và s là tín hiệu τ-RR. Tác giả dùng **hồi quy thưa LASSO**, tức phương pháp khuyến khích chỉ một số ít hệ số khác không, và chọn mức điều chuẩn sao cho hệ số tương quan Pearson giữa tín hiệu gốc và tín hiệu tái dựng là:

$$
\rho=0.9.
$$

Nguồn: Phụ lục, tr. 13; Phương trình (A1); Hình 2(F), tr. 5. Bài chưa mô tả đủ việc tạo/chuẩn hóa tập hàm cơ sở, tìm mức điều chuẩn và chuyển hệ số thành công suất tương đối để chốt một cách triển khai duy nhất.

Mức tương quan này là tiêu chí chọn độ phù hợp của phép tái dựng, không phải mức ý nghĩa thống kê hoặc xác suất chứng minh một chu kỳ là duy nhất. Bài không báo cáo kiểm định giả thuyết cho sự xuất hiện của từng đỉnh ISS. [Phụ lục, tr. 13]

**Điểm cần làm rõ khi tái lập:** Phụ lục gọi hệ là thiếu phương trình so với số ẩn, nhưng lại ghi:

$$
\chi\in\mathbb R^{M\times N},
\qquad
M=\frac N2+1.
$$

Nếu hiểu trực tiếp các kích thước này với N > 2, ma trận chuyển vị có nhiều hàng hơn cột. Do đó, mô tả “thiếu phương trình” không tự khớp với phép đếm kích thước. Phép đếm này chưa xác định hạng thực tế của ma trận hoặc cách triển khai trong mã nguồn. Đây là nhận xét của người phân tích, không phải lý do để âm thầm sửa phép chuyển vị hoặc kết luận đã tái lập đúng ISS. [Phụ lục, tr. 13]

### 4.4. Ước lượng điểm tới hạn bằng chất lượng khớp lũy thừa

Quan hệ tác giả viết trong phần văn bản, không đánh số phương trình, là:

$$
|a-a_c|=|Re-Re_c|^\lambda,
\qquad
a_c=a(Re_c).
$$

a là một đại lượng tái diễn; a_c là giá trị của chính đại lượng đó tại điểm ứng viên; λ là số mũ. Đây là quan hệ giữa độ lệch của đại lượng và độ lệch của tham số, không phải phân bố có đuôi lũy thừa của thời gian tái diễn. Việc lấy trị tuyệt đối cũng không cho biết đại lượng gốc tăng hay giảm. [Mục III.B, tr. 9–10; Hình 3(II)]

Quy trình được tái dựng ở mức ý tưởng:

1. Lấy một giá trị tham số đã đo làm điểm tới hạn ứng viên, lấy đại lượng tại đó làm giá trị tham chiếu.
2. Với các điều kiện trước ứng viên theo hướng thay đổi tham số, tính độ lệch tuyệt đối so với giá trị tham chiếu.
3. Khớp quan hệ lũy thừa, khảo sát trên hệ trục logarit hai chiều và thu số mũ cùng độ bất định của phép khớp.
4. Lặp lại trên các ứng viên; chọn điểm cho quan hệ phù hợp nhất, được bài diễn đạt qua sai số khớp nhỏ nhất và độ bất định số mũ nhỏ nhất.
5. Áp dụng tương tự cho mô hình Hopf. Vì hệ số cản giảm, các điều kiện trước ứng viên có α lớn hơn ứng viên, không phải luôn nhỏ hơn.

Nguồn: Mục III.B–C, tr. 9–12; Hình 4, 6, 8.

**Giới hạn thông tin được báo cáo:** Chưa rõ phép khớp thực tế là hồi quy trên logarit hay bình phương tối thiểu phi tuyến; hệ số chặn/hệ số tỷ lệ được cố định hay được ước lượng; trọng số, hàm mất mát, số điểm tối thiểu, cách xử lý độ lệch bằng không và định nghĩa độ bất định của số mũ. Bản phân tích giữ đúng công thức tác giả viết, không tự bổ sung hàm mục tiêu rồi coi đó là cách tác giả đã làm. Điểm ứng viên tạo độ lệch bằng không nên không thể đưa trực tiếp vào phép lấy logarit; cách xử lý các độ lệch bằng không tại những điểm khác cũng cần xác nhận. [Mục III.B, tr. 9–10]

**Công thức in trong bài chưa đủ làm công thức khớp số:** DET là một tỷ lệ trong đoạn từ 0 đến 1; Hình 3 có độ lệch DET nhỏ hơn 1, khoảng cách Re lớn hơn 1, còn Hình 4(b) ghi số mũ dương 0.57. Vì thế, đẳng thức trên với hệ số tỷ lệ bằng 1 không thể đồng thời mô tả các giá trị thô ấy. Cần làm rõ hệ số tỷ lệ hoặc phép chuẩn hóa đã dùng. Một dạng khớp tổng quát có thể xem xét là:

$$
|a-a_c|\approx C|Re-Re_c|^\lambda,
\qquad C>0.
$$

Đây là dạng do người phân tích bổ sung để chỉ ra thông tin còn thiếu, không phải khẳng định tác giả đã ước lượng C. Thiếu chi tiết này chưa bác bỏ các đường khớp trong hình, nhưng cản trở tái lập chính xác số mũ và độ bất định. [Phương trình (5); Hình 3(II-b), tr. 6; Hình 4(b), tr. 7; Mục III.B, tr. 10]

**Dùng chung tham chiếu tạo phụ thuộc thống kê:** Để minh họa, giả sử sai số ước lượng ở các điều kiện khác nhau độc lập với nhau; ký hiệu giá trị trung bình thật là μ, sai số là e và độ lệch có dấu là d. Với hai điểm khác nhau và cùng khác điểm tham chiếu:

$$
a_i=\mu_i+e_i,\qquad a_c=\mu_c+e_c,
\qquad d_i=a_i-a_c,
$$

$$
\operatorname{Cov}(d_i,d_j)=\operatorname{Var}(e_c),
\qquad i\ne j,\quad i,j\ne c.
$$

Đây là suy luận đại số của người phân tích từ cách trừ chung một giá trị tham chiếu, không phải kết quả thống kê bài báo đã đo. Sau trị tuyệt đối và logarit, công thức hiệp phương sai trên không còn áp dụng nguyên dạng, nhưng cũng không có cơ sở tự coi các điểm khớp là độc lập. Nếu các cửa sổ hoặc điều kiện còn phụ thuộc nhau, cần mô hình sai số đầy đủ hơn. PDF chưa cho cách truyền sai số tham chiếu vào phép khớp, nên chưa đánh giá được mức hiệu chỉnh của thanh sai số; không thể từ đó kết luận tác giả chắc chắn dùng hồi quy sai. [Cơ sở quy trình: Mục III.B, tr. 9–10; Hình 4, 6, 8]

**Tác giả khẳng định:** Điểm có độ bất định phép khớp nhỏ nhất là điểm tới hạn. **Bằng chứng hỗ trợ:** Tiêu chí chọn một mốc chung cho nhiều đại lượng trong thí nghiệm và khôi phục mốc Hopf đã biết ở các mô hình. **Diễn giải của người phân tích:** Chưa có định lý bảo đảm tiêu chí này đủ hoặc duy nhất. Sai số phần dư nhỏ nhất và độ bất định hệ số góc nhỏ nhất cũng không mặc nhiên là cùng một hàm mục tiêu, vì độ bất định còn phụ thuộc số điểm và cách bố trí dữ liệu. [Mục III.B–C, tr. 9–12; Hình 4, 6, 8]

### 4.5. Các giả định quyết định phạm vi áp dụng

Quy trình cần dữ liệu đủ đại diện cho từng điều kiện tham số; đại lượng quan sát phải phản ánh sự thay đổi động lực học; phép nhúng và ngưỡng phải cho phép so sánh cấu trúc; quan hệ lũy thừa phải có ý nghĩa đối với việc chọn mốc. Tác giả mô tả các trạng thái hỗn loạn là trạng thái tiệm cận có tính dừng thống kê tại tham số cố định, không phải đáp ứng quá độ; bài chưa trình bày một bộ kiểm tra tính dừng độc lập. Quan trọng nhất, không cần biết đầy đủ phương trình buồng đốt khác với không cần biết tham số điều khiển. [Mục II.A–C, tr. 3–4; Mục III.A–B, tr. 7–10]

## 5. Thiết kế thực nghiệm và mô phỏng

### 5.1. Thí nghiệm buồng đốt với tham số được điều khiển

Hình 1 mô tả buồng đốt rối dùng vật cản để ổn định ngọn lửa, với cảm biến áp suất trên buồng cháy. Lưu lượng nhiên liệu được giữ ở 28 SLPM, tức lít tiêu chuẩn mỗi phút; lưu lượng khí tăng gần tĩnh từ 410 đến 650 SLPM, theo bước 10 SLPM. Cảm biến có độ phân giải 0.15 Pa, lấy mẫu ở 10 kHz trong 3 s, qua bộ chuyển đổi tương tự–số 16 bit. Re được tính từ lưu lượng, hình học và độ nhớt, không được suy ra từ tín hiệu tái diễn. [Mục II.A, tr. 3; Hình 1]

Khoảng tham số được tác giả báo cáo:

$$
Re_{\mathrm{start}}=(2.13\pm0.066)\times10^4,
\qquad
Re_{\mathrm{end}}=(3.18\pm0.072)\times10^4.
$$

Bài nêu độ bất định của bộ điều khiển lưu lượng là ±0.8% giá trị đọc và ±0.2% toàn thang. Không được biến các thông số đo lường này thành khoảng tin cậy của thủ tục chọn điểm tới hạn nếu chưa có phân tích lan truyền sai số và ảnh hưởng của việc lựa chọn ứng viên. [Mục II.A, tr. 3; Hình 3–4]

### 5.2. Hai trường hợp phân nhánh Hopf trong cùng một họ mô hình

Tác giả dùng mô hình dao động tự kích có nhiễu trắng cộng:

$$
\ddot\eta+\alpha\dot\eta+\omega^2\eta
=\dot\eta\left(\beta+K\eta^2-\gamma\eta^4\right)+\xi,
\qquad
\langle\xi(t)\xi(t+\tau)\rangle=\Gamma\delta(\tau).
$$

Đây là Phương trình (1); ξ là nhiễu, Γ là cường độ nhiễu và α là hệ số cản được thay đổi. [Mục II.B, tr. 3–4]

| Tham số hoặc trường hợp                            | Giá trị bài báo nêu     |
| ------------------------------------------------------- | ---------------------------- |
| Tần số góc ω                                        | 2π × 120 rad/s             |
| Hệ số β                                              | 50 rad/s                     |
| Cường độ nhiễu Γ                                  | 10                           |
| Hệ số cản α                                         | Giảm từ 80 xuống 45 rad/s |
| **Hopf dưới tới hạn** (*subcritical Hopf*)  | K = 9; γ = 0.7              |
| **Hopf trên tới hạn** (*supercritical Hopf*) | K = −9; γ = −0.7          |

Nguồn: Mục II.B, tr. 3–4; Phương trình (1). Giữ nguyên các dấu tham số theo PDF; bản phân tích chưa thực hiện mô phỏng để xác nhận hoặc sửa chúng.

Mốc Hopf được bài báo dùng là α bằng 50. Có thể kiểm tra mốc mất ổn định tuyến tính cục bộ này trực tiếp từ Phương trình (1): bỏ nhiễu và các số hạng phi tuyến, thu được:

$$
\ddot\eta+(\alpha-\beta)\dot\eta+\omega^2\eta=0.
$$

Hệ số cản tuyến tính đổi dấu tại:

$$
\alpha_c=\beta=50.
$$

Đây là suy luận toán học của người phân tích từ phương trình, không phải kết quả tái lập số đã thực hiện. **Mốc 50 là điểm Hopf của hệ xác định khi bỏ nhiễu.** Việc mô phỏng có nhiễu chọn được mốc này chưa chứng minh nó là điểm phân nhánh ngẫu nhiên theo một định nghĩa cụ thể. Mốc ổn định cục bộ cũng không tự xác định mọi ngưỡng nhảy biên độ hữu hạn hoặc chuyển trạng thái do nhiễu trong trường hợp dưới tới hạn. [Phương trình (1); Mục II.B, tr. 3–4; Mục III.C, tr. 10–11]

Tác giả nói rõ mô hình được dùng để kiểm tra ý nghĩa của điểm được chọn, không nhằm tái tạo đầy đủ buồng đốt. Hai trường hợp không tương đương hai hệ thực nghiệm độc lập hoặc kiểm chứng trên mọi cơ chế phân nhánh. [Mục III.C, tr. 10–12; Hình 5–8]

### 5.3. Cách đánh giá và những chi tiết chưa được báo cáo

| Hạng mục                | Bài báo cho biết                                                                                                                                            | Giới hạn cần giữ rõ                                                                                                                                |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Huấn luyện/kiểm tra    | Không có quy trình học có giám sát                                                                                                                      | Không có đánh giá dự báo trước sự kiện trên tập kiểm tra tách riêng                                                                     |
| Mốc đối chiếu         | So điểm được chọn với điểm Hopf đã biết                                                                                                            | Thí nghiệm buồng đốt chưa có mốc phân nhánh độc lập để tính sai số ước lượng                                                       |
| So sánh                  | So sánh cấu trúc, xu hướng và số mũ giữa thí nghiệm và hai trường hợp mô hình                                                                 | Các giá trị căn trung bình bình phương, viết tắt RMS, là chỉ số biên độ để đối chiếu; chưa phải so sánh thuật toán đầy đủ |
| Phương án đối chứng | Không báo cáo phép so sánh có hệ thống, thí nghiệm loại bỏ từng thành phần hoặc bộ tín hiệu thay thế/đối chứng không có chuyển tiếp | Chưa có bằng chứng về ưu thế tương đối hoặc tính đặc hiệu với hiện tượng tới hạn                                                  |
| Độ bất định          | Thanh sai số của số mũ và độ bất định của Re                                                                                                        | Chưa rõ loại thanh sai số, mức bao phủ và phân bố sai số của điểm được chọn qua nhiều lần chạy                                      |
| Độ nhạy                | Một cấu hình RR, cửa sổ và độ dài tối thiểu được nêu; mô hình có Γ bằng 10                                                                 | Chưa có khảo sát có hệ thống theo ngưỡng, chiều nhúng, độ trễ, cửa sổ hoặc cường độ nhiễu                                         |
| Mô phỏng                | Có phương trình, tham số và khoảng thay đổi hệ số cản                                                                                              | Thiếu bộ giải, bước thời gian, thời lượng, cách bỏ quá độ, hạt giống ngẫu nhiên và số lần mô phỏng                               |
| Dữ liệu/mã nguồn      | Dữ liệu được cung cấp qua yêu cầu hợp lý tới tác giả liên hệ                                                                                    | PDF không dẫn kho mã nguồn hoặc đường tải dữ liệu công khai; chưa xác minh tài nguyên bên ngoài PDF                                   |

Nguồn: Mục II–III, tr. 3–12; Hình 3–9; phần khả dụng dữ liệu, tr. 12. Những điểm “chưa báo cáo” là đánh giá mức độ mô tả trong PDF, không phải kết quả kiểm tra mã nguồn hoặc một lần tái lập thất bại.

RMS áp suất cũng được báo cáo có độ bất định số mũ nhỏ nhất tại cùng mốc thực nghiệm. Vì vậy, kết quả hiện tại chưa tách được lợi ích tăng thêm của các đặc trưng tái diễn so với chỉ số biên độ, hoặc chứng minh ISS là thành phần cần thiết của thủ tục chọn điểm. Cần phép so sánh và loại bỏ thành phần có cùng dữ liệu, tiêu chí và ngân sách tham số để trả lời. [Mục III.B, tr. 10; Hình 4(a); Phụ lục]

## 6. Kết quả và mức độ bằng chứng

### 6.1. Quan sát ngưng tụ tái diễn

Hình 2 đặt cạnh nhau ba trạng thái:

$$
\begin{aligned}
\text{Hỗn loạn:}\quad &Re=2.13\times10^4,\\
\text{Gián đoạn:}\quad &Re=2.88\times10^4,\\
\text{Dao động chu trình giới hạn:}\quad &Re=3.09\times10^4.
\end{aligned}
$$

**Dao động chu trình giới hạn** (*limit cycle oscillations*, LCO) là trạng thái tuần hoàn tự duy trì trong bài. Các hàng A–C thể hiện tín hiệu và quỹ đạo pha; D là RP; E–F là τ-RR và ISS. Đường chéo chuyển từ ngắn, đứt đoạn sang những mảng có tổ chức, rồi dài và liên tục. ISS chuyển từ nhiều đóng góp sang một đỉnh chi phối. Đây là chuỗi bằng chứng trực tiếp cho khái niệm ngưng tụ tái diễn mà tác giả đề xuất. [Hình 2, tr. 5; Mục III.A, tr. 7–8]

**Bằng chứng hỗ trợ:** Trong biểu diễn và các điều kiện được chọn, một nhịp tái diễn trở nên chi phối khi tính tuần hoàn phát triển. **Diễn giải của người phân tích:** Hình không chứng minh tất cả bậc tự do của hệ không gian–thời gian đã thu về một dạng dao động, hoặc ngưng tụ tái diễn gây ra mất ổn định. Độ dài cửa sổ và thang trục giữa các trạng thái khác nhau; không thể dựa riêng vào độ đậm của hình để kết luận RR tăng. Việc trạng thái đầu là hỗn loạn xác định nhiều chiều có nhiễu dựa vào các nghiên cứu trước mà bài dẫn, chưa được xác lập lại đầy đủ bằng một phép kiểm tra hỗn loạn độc lập ở đây. [Mục III.A, tr. 7–8; chú thích Hình 2; tài liệu 57–60]

### 6.2. Điểm tới hạn thực nghiệm vẫn thuộc trạng thái gián đoạn

Hình 3(I) cho thấy DET và L tăng; RT, RTE, LAM, TT giảm; Entr tăng rồi giảm. Cột II thể hiện độ lệch trên hệ trục logarit hai chiều với mốc đã chọn. Mục III.B nêu khớp tốt cho DET, Entr, LAM, TT, RT, RTE tại mốc chung. Hình 4 thể hiện số mũ và thanh sai số theo các điểm ứng viên. Danh sách đạt độ bất định nhỏ nhất trong phần văn bản còn có RMS áp suất, nhưng không có L. [Hình 3, tr. 6; Hình 4, tr. 7; Mục III.B, tr. 8–10]

Mốc được chú thích trong Hình 3 là:

$$
Re_c=(2.96\pm0.069)\times10^4.
$$

**Tại mốc này, hệ vẫn gián đoạn**, không phải đã có dao động tuần hoàn phát triển hoàn toàn. Nó khác trạng thái LCO ở Hình 2. Thí nghiệm chưa cung cấp một điểm phân nhánh độc lập để tính sai số ước lượng; dấu ± cũng chưa được giải thích thành khoảng tin cậy của thủ tục lựa chọn mốc. [Chú thích Hình 3, tr. 6; chú thích Hình 4, tr. 7; Hình 2, tr. 5]

Bằng chứng giữa các đại lượng không đồng đều. Phần số liệu kèm Hình 4(c–d) ghi:

$$
\lambda_L=0.30\pm0.91,
\qquad
\lambda_{Entr}=-0.14\pm0.05.
$$

Độ bất định của số mũ gắn với L rất lớn; số mũ của Entr âm. Vì thế không thể kết luận mọi đại lượng đều xác định điểm tới hạn chính xác như nhau hoặc mọi số mũ đều dương. Các quan hệ này được khớp trên dữ liệu hữu hạn, chưa phải suy dẫn giải tích của số mũ hay chứng minh quy luật đúng khi tiến tùy ý sát điểm tới hạn. [Hình 4(c–d), tr. 7; Mục III.B, tr. 9–10]

**Bất nhất cần xác minh:** Hình 9 vẽ thanh sai số của L thực nghiệm ngắn hơn nhiều so với mức ±0.91 được ghi tại Hình 4(c). Bản phân tích giữ nguyên con số in ở Hình 4(c), không tự sửa thành một giá trị khác hoặc dùng hình tổng hợp để thay thế. Chưa có dữ liệu và mã khớp để xác định hình nào phản ánh đúng độ bất định. [Đối chiếu trực quan Hình 4(c), tr. 7 và Hình 9, tr. 12]

### 6.3. Mô hình khôi phục điểm Hopf đã biết

Trong trường hợp Hopf dưới tới hạn, Hình 5 có thay đổi biên độ đột ngột và biến đổi tiền chuyển tiếp của các đại lượng tái diễn. Hình 6 chọn mốc 50; chú thích nêu cụ thể DET, L, LAM, TT, RT, RTE. Trong trường hợp trên tới hạn, Hình 7 có biên độ tăng dần; Hình 8 và Mục III.C.2 báo nhiều đại lượng chọn mốc 50, trong khi dao động tuần hoàn quan sát ở α bằng 49. Kết quả chung là:

$$
\widehat{\alpha}_c=50=\alpha_{\mathrm{Hopf}}.
$$

Dấu mũ ở đây chỉ ước lượng do bản phân tích dùng để phân biệt với mốc Hopf của hệ không nhiễu, như đã giải thích ở Mục 5.2. Sự trùng khớp là bằng chứng số quan trọng cho thủ tục lựa chọn trong các trường hợp được trình bày, không phải độ chính xác thống kê qua nhiều lần chạy độc lập. [Hình 5–8, tr. 8–11; Mục III.C, tr. 10–12]

Một số số mũ đọc trực tiếp từ phần số liệu kèm Hình 4, 6, 8:

| Đại lượng | Thí nghiệm nhiệt âm | Hopf dưới tới hạn có nhiễu | Hopf trên tới hạn có nhiễu |
| ------------- | ----------------------: | -------------------------------: | ------------------------------: |
| DET           |            0.57 ± 0.05 |                     0.44 ± 0.05 |                    0.50 ± 0.05 |
| L             |            0.30 ± 0.91 |                     0.09 ± 0.01 |                    0.14 ± 0.02 |
| TT            |            0.25 ± 0.06 |                     0.45 ± 0.04 |                    0.43 ± 0.04 |
| RT            |            0.36 ± 0.03 |                     0.56 ± 0.07 |                    0.65 ± 0.07 |

Giá trị và dấu ± giữ theo tác giả, không suy ra từ việc số hóa biểu đồ cột Hình 9. PDF chưa xác định đủ để gọi các khoảng này là khoảng tin cậy ở một mức bao phủ cụ thể. [Hình 4, 6, 8]

**Tác giả khẳng định:** Quy luật có tính phổ quát và phương pháp có triển vọng áp dụng rộng. **Bằng chứng hỗ trợ:** Quan hệ lũy thừa và sự trùng khớp điểm tới hạn xuất hiện trong một thí nghiệm và hai trường hợp của cùng họ mô hình; số mũ khác nhau giữa các hệ, điều Hình 9 cũng nêu rõ. Chưa có bằng chứng về một số mũ phổ quát, một lớp phổ quát hoặc độ đúng trên mọi cơ chế chuyển tiếp. [Hình 9; Mục III.C, tr. 11; Mục IV, tr. 12]

### 6.4. Mỗi hình kiểm tra điều gì và không chứng minh điều gì?

| Hình           | Nội dung và bằng chứng chính                                                             | Giới hạn                                                                                                               |
| --------------- | --------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Hình 1, tr. 3  | Sơ đồ thí nghiệm và vị trí đo áp suất                                              | Không phải đánh giá hiệu năng hoặc tiêu chí tới hạn độc lập                                               |
| Hình 2, tr. 5  | Tín hiệu, RP, τ-RR, ISS qua hỗn loạn → gián đoạn → LCO                              | Không chứng minh quan hệ nhân quả, RR tăng hoặc dự báo trước sự kiện                                        |
| Hình 3, tr. 6  | Xu hướng RQA và quan hệ lũy thừa tại mốc được chọn                                | Biến đổi trước LCO không tương đương dự báo trước điểm tới hạn chưa biết                            |
| Hình 4, tr. 7  | Số mũ và thanh sai số theo ứng viên Re                                                  | Không phải phân bố độ bất định của mốc được chọn; không phải mọi đại lượng đều đồng thuận rõ |
| Hình 5, tr. 8  | Xu hướng và quan hệ lũy thừa của mô hình dưới tới hạn                            | Không có đánh giá độ chính xác theo nhiều hạt giống ngẫu nhiên hoặc mức nhiễu                           |
| Hình 6, tr. 9  | Độ bất định phép khớp nhỏ nhất tại điểm Hopf trong trường hợp dưới tới hạn | Chưa kiểm tra tính đặc hiệu với hiện tượng tới hạn trên các trường hợp đối chứng                     |
| Hình 7, tr. 10 | Chuyển tiếp dần và quan hệ lũy thừa của mô hình trên tới hạn                     | Không phải dữ liệu của một hệ thực nghiệm độc lập khác                                                      |
| Hình 8, tr. 11 | Điểm được chọn khớp mốc Hopf trong trường hợp trên tới hạn                      | Chưa đánh giá thời gian báo trước hoặc tỷ lệ cảnh báo sai                                                   |
| Hình 9, tr. 12 | So sánh số mũ giữa các hệ và trường hợp                                             | Chưa xác lập số mũ hay lớp phổ quát; biểu đồ cột không thay thế kiểm định thống kê                    |

## 7. Đóng góp thực sự và các tình huống có thể làm phương pháp thất bại

Đóng góp có bằng chứng gồm ba phần gắn nhau: khái niệm ngưng tụ tái diễn; đo hiện tượng bằng những công cụ tái diễn đã có; và chọn tham số tham chiếu thông qua chất lượng quan hệ lũy thừa, có đối chiếu mốc Hopf đã biết. Điều đáng học là cách nối một biểu diễn động lực học với bài toán ước lượng tham số. Tuy nhiên, thủ tục lựa chọn vẫn cần kiểm tra độc lập trước khi trở thành một phương pháp định vị điểm tới hạn có phạm vi rộng. [Mục III–IV, tr. 7–12]

**Các rủi ro dưới đây là suy luận cần kiểm tra, không phải kết quả bài báo đã đo:**

- **Xu hướng trơn cũng có thể tạo quan hệ gần lũy thừa trên một khoảng hữu hạn.** Đường gần thẳng trên trục logarit chưa đủ xác lập phân nhánh. Cần đối chứng không có điểm tới hạn và so sánh dạng hàm khác; bài chưa báo cáo các bước này. [Đối chiếu tiêu chí ở Mục III.B, tr. 9–10]
- **Các ứng viên có thể dùng lượng dữ liệu và khoảng khớp khác nhau.** Khi dùng mọi điều kiện trước ứng viên, độ bất định của hệ số góc có thể phụ thuộc thiết kế hồi quy chứ không chỉ động lực học. Cần kiểm tra tính công bằng của phép so sánh giữa ứng viên. [Quy trình ở Mục III.B–C, tr. 9–11]
- **Biểu diễn và sự bão hòa của đại lượng có thể ảnh hưởng kết quả.** Ngưỡng, phép nhúng, độ dài cửa sổ và DET gần bão hòa có thể làm đổi hình dạng quan hệ với tham số. Một cấu hình cố định chưa đủ chứng minh độ vững. [Mục II.C–D, tr. 4–6; Hình 3; Mục III.B, tr. 8]
- **Ý nghĩa điểm tới hạn phụ thuộc đại lượng đích.** Mốc mất ổn định tuyến tính, ngưỡng nhảy biên độ và ngưỡng chuyển trạng thái do nhiễu không mặc nhiên trùng nhau. Trong thí nghiệm, mốc được chọn còn nằm trong gián đoạn. [Phương trình (1); chú thích Hình 3; Mục III.C, tr. 10–11]
- **Thiếu tham số điều khiển hoặc cửa sổ trộn nhiều trạng thái.** Nếu không quan sát được tham số, tín hiệu quá độ chi phối, hoặc chuyển tiếp không hướng đến tuần hoàn, quy trình hiện tại có thể không còn phù hợp; các trường hợp này chưa được kiểm chứng trong PDF. [Phạm vi và giả định ở Mục II–III]

**Minh họa giới hạn nhận dạng, do người phân tích xây dựng:** Xét một đại lượng chỉ biến thiên tuyến tính theo tham số q, với v khác không:

$$
a(q)=u+vq
\quad\Longrightarrow\quad
|a(q)-a(q_c)|=|v|\,|q-q_c|.
$$

Mọi điểm tham chiếu đều cho quy luật lũy thừa chính xác với số mũ bằng 1, dù quan hệ này không có điểm tới hạn ưu tiên. Ví dụ đại số này chỉ cho thấy khớp lũy thừa đơn thuần chưa bảo đảm nhận dạng duy nhất hoặc tính đặc hiệu với phân nhánh; không phải dữ liệu RQA của bài, một mô phỏng mới hay bằng chứng rằng kết quả tại mốc 50 là sai. Muốn nâng tiêu chí thành một bộ ước lượng rộng hơn, cần giả định bổ sung và kiểm tra trên đối chứng không có chuyển tiếp. [Tiêu chí được đánh giá: Mục III.B, tr. 9–10]

Bài không phân tích **chậm dần tới hạn** (*critical slowing down*), không liên hệ số mũ RQA với tốc độ hồi phục sau nhiễu loạn. RT giảm là kết quả về khoảng tái diễn, không phải phép kiểm chứng hoặc bác bỏ thời gian hồi phục tăng. Tương tự, sự đi kèm theo tham số giữa tổ chức tái diễn và mất ổn định không tự xác lập chiều nhân quả. [Phương trình (10)–(11), Mục II.D.2, tr. 6–7; Mục III–IV]

## 8. Hướng mở rộng sang tín hiệu y sinh: giả thuyết chưa được kiểm chứng

Bài dẫn một ứng dụng trước về biến thiên nhịp tim ở tài liệu 7, nhưng nghiên cứu hiện tại **không có EEG, ECG, PPG, dữ liệu bệnh nhân hoặc đánh giá sự kiện lâm sàng**. Tương ứng, EEG là điện não đồ, ECG là điện tâm đồ và PPG là tín hiệu quang thể tích. Do không đọc các tài liệu ngoài PDF, chưa thể từ danh mục tham khảo này kết luận một khoảng trống nghiên cứu y sinh đã được xác lập. [Mục I, tr. 2; tài liệu 7–8, tr. 13; thiết kế ở Mục II]

**Giả thuyết của người phân tích:** Biểu diễn tái diễn theo thời gian có thể hữu ích để mô tả biến đổi trạng thái sinh lý khi chưa biết đầy đủ phương trình chi phối. Tuy nhiên, có hai mức chuyển giao khác nhau: nghiên cứu RP/RQA như một biểu diễn; và chuyển nguyên thủ tục chọn điểm tới hạn theo lũy thừa. Mức thứ hai hiện cần tham số điều khiển đã biết và dữ liệu tại điểm ứng viên, nên chưa áp dụng trực tiếp cho một chuỗi sinh lý không có phép quét tham số tương ứng.

Một thiết kế mở rộng có thể bắt đầu bằng việc định nghĩa rõ sự kiện hoặc thay đổi trạng thái cần phát hiện, có nhãn đối chiếu độc lập, tính đặc trưng mà không dùng dữ liệu tương lai, rồi đánh giá trên các đoạn thời gian tách riêng. Bài toán phát hiện cần đo độ trễ phát hiện và cảnh báo sai; chỉ gọi là dự báo trước sự kiện khi quy trình thực sự dự báo trước, khi đó mới có ý nghĩa đánh giá thời gian báo trước. Đây là đề xuất nghiên cứu, không phải đánh giá Jella và cộng sự đã thực hiện.

Không mặc định biến cố sinh lý là phân nhánh, chuyển tiếp tới hạn hoặc chuyển từ hỗn loạn sang tuần hoàn. Nhiễu tạo tác, đáp ứng quá độ, chuyển đổi trạng thái và thay đổi kéo dài có thể là các bài toán khác nhau. Câu hỏi mở trước mắt là **mô tả và phát hiện thay đổi khi thiếu tham số điều khiển**, rồi kiểm tra liệu cách đặt bài toán theo cơ chế tới hạn có phù hợp hay không.

## 9. Hồ sơ phương pháp (Methodological Fingerprint)

| Trường                                        | Đặc trưng của bài báo                                                                                                                                                                                          |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bài toán (Problem)                            | Mô tả chuyển từ hỗn loạn sang tuần hoàn qua gián đoạn và định vị tham số tới hạn trong hệ có nhiễu. [Mục I, III.A]                                                                             |
| Đầu vào (Input)                              | Nhiều chuỗi một chiều gắn với Re hoặc α đã biết; không chỉ một chuỗi chưa gắn nhãn có tham số điều khiển hoàn toàn không biết. [Mục II.A–C, III.B]                                      |
| Thông tin biết trước (Known information)    | Tham số và thứ tự thay đổi, cách lấy mẫu; mô hình còn có phương trình và mốc Hopf. Thí nghiệm không cần đầy đủ phương trình chi phối. [Mục II]                                        |
| Đầu ra (Output)                               | RP, τ-RR, ISS, xu hướng RQA; số mũ và điểm tham chiếu tới hạn được chọn. [Mục II.C–D, III]                                                                                                          |
| Phương án đối chiếu (Existing baseline)   | Có RMS biên độ trong các hình, chưa có so sánh có hệ thống với phương sai, tự tương quan hoặc thuật toán định vị khác. [Hình 3–8]                                                         |
| Thành phần mới (New component)               | Khái niệm ngưng tụ tái diễn và cách dùng chất lượng khớp để chọn tham số; các công cụ đo và ý tưởng lũy thừa có tiền lệ. [Mục I, III–IV]                                             |
| Giả định (Assumptions)                       | Dữ liệu đại diện cho từng điều kiện, phép tái tạo và ngưỡng so sánh được, đại lượng quan sát phản ánh động lực học, tiêu chí lũy thừa có ý nghĩa. [Mục II.C, III.A–B]         |
| Kiểm chứng (Validation)                       | Một thí nghiệm buồng đốt và hai trường hợp Hopf có nhiễu trong cùng họ mô hình; đối chiếu mốc Hopf của hệ xác định khi bỏ nhiễu. [Phương trình (1); Mục II.A–B, III.C]               |
| Kết quả chính (Main finding)                 | Mốc thực nghiệm gần 2.96 × 10⁴ vẫn gián đoạn; hai mô hình chọn hệ số cản 50, khớp mốc Hopf. [Hình 3–4, 6, 8]                                                                                     |
| Câu hỏi còn mở (Unresolved questions)       | Hệ số tỷ lệ/hàm mục tiêu, sai số dùng chung tham chiếu, bất nhất thanh sai số, tính đặc hiệu trên đối chứng, độ vững và khả năng dự báo trước sự kiện. [Mục III.B–IV; Hình 4, 9] |
| Khả năng tái lập (Reproduction feasibility) | Có thể tái triển khai ý tưởng; tái tạo chính xác cần dữ liệu và chi tiết về phép nhúng, cửa sổ, hồi quy, mô phỏng, ISS. [Phương pháp, Phụ lục, phần khả dụng dữ liệu]              |

## 10. Quyết định tái lập và tài liệu đọc tiếp

### 10.1. Quyết định: ứng viên tái lập có điều kiện (Reproduction candidate)

Bài đáng được chọn làm ứng viên tái lập vì quy trình đủ cụ thể để đặt các phép kiểm tra có tính quyết định và có mốc Hopf đã biết để đối chiếu. Chưa nên coi đây là phương pháp nền tảng đã được xác nhận cho dự báo y sinh: yêu cầu về phép quét tham số và thiếu đánh giá dự báo trước sự kiện là khác biệt trực tiếp. Ưu tiên ban đầu nên là kiểm tra tính đặc hiệu và độ ổn định của tiêu chí khớp, rồi mới tái tạo toàn bộ hình. Đây là quyết định của người phân tích, chưa phải thông báo tái lập thành công.

### 10.2. Nên kiểm tra phần nào trước?

1. **Chốt quy ước đo lường.** Dùng tín hiệu tuần hoàn và tín hiệu có nhiễu đơn giản để kiểm tra đếm đường, khoảng trắng, chuẩn hóa, xử lý đường chéo và hai cách chọn ngưỡng. Xác định phép nhúng và xử lý cửa sổ trước khi so số mũ. Đây là kiểm tra đề xuất cho một triển khai tương lai, chưa được thực hiện trong bản phân tích. [Cơ sở: Mục II.C–D; Mục III.B]
2. **Kiểm tra tiêu chí chọn điểm với cả trường hợp có và không có chuyển tiếp.** Viết rõ mô hình hồi quy, hệ số tỷ lệ, hàm mục tiêu và công thức độ bất định; tính đến sai số dùng chung tham chiếu; so ảnh hưởng của lượng dữ liệu, khoảng khớp, độ lệch bằng không và dạng hàm thay thế. Khi lấy mẫu lại để đánh giá độ bất định, phải tính lại cả giá trị tham chiếu và bước chọn ứng viên. Không xem cực tiểu độ bất định tự nó là phép kiểm chứng. Đây là đề xuất kiểm tra, không phải quy trình tác giả đã báo cáo. [Cơ sở: Mục III.B, tr. 9–10]
3. **Tái tạo mô hình dao động trong điều kiện kiểm soát.** Xác nhận phương trình, dấu tham số, cách rời rạc hóa nhiễu, miền ổn định và mốc Hopf cục bộ; sau đó ghi rõ bộ giải, bước thời gian, thời lượng, bỏ quá độ và hạt giống ngẫu nhiên. Phải tách các lựa chọn bổ sung khỏi thông tin bài báo cung cấp. [Mục II.B, tr. 3–4]
4. **Đánh giá nhiều lần mô phỏng và khảo sát độ nhạy.** Đo độ chệch, độ phân tán của điểm được chọn so với mốc 50; so mức đồng thuận giữa đại lượng; thay nhiễu, ngưỡng, phép nhúng và cửa sổ. Các thống kê này là đề xuất đánh giá, không phải kết quả PDF đã báo. [Cơ sở kiểm chứng: Mục III.C; Hình 6, 8]
5. **Chuyển sang dữ liệu thực nghiệm có nguồn gốc rõ.** Cần dữ liệu gốc và chi tiết triển khai để tái tạo chính xác. ISS cần kiểm tra riêng tập hàm cơ sở và điều chuẩn; bài chưa chứng minh phải có ISS mới chọn được điểm bằng các đại lượng RQA. [Mục III.B; Phụ lục; phần khả dụng dữ liệu]

Với dấu γ âm ở trường hợp trên tới hạn, giữ nguyên thông số trong PDF không tự bảo đảm mọi quỹ đạo mô phỏng đều bị chặn với mọi điều kiện đầu và lần sinh nhiễu. Cần kiểm tra ổn định, khả năng thoát khỏi miền dao động và cách bỏ quá độ. Đây là câu hỏi của người phân tích, không phải kết luận rằng bài chắc chắn in sai dấu hoặc mô hình đã bị bác bỏ. Tương tự, cách ghi kích thước trong Phụ lục cần làm rõ trước khi khẳng định đã tái lập đúng ISS. [Mục II.B, tr. 3–4; Phụ lục, tr. 13]

### 10.3. Thông tin còn thiếu để tái lập chính xác

Cần tối thiểu dữ liệu áp suất gốc và ánh xạ tới Re; tiền xử lý; chiều nhúng/độ trễ thực tế và cách chọn theo trạng thái; bước dịch cửa sổ; quy ước đếm đường; mô hình hồi quy và định nghĩa độ bất định; chi tiết bộ giải, nhiễu, thời lượng và lặp mô phỏng; cách tạo/chuẩn hóa các hàm cơ sở của ISS và tìm mức điều chuẩn. Một triển khai độc lập có thể tự chọn các chi tiết này, nhưng phải ghi rõ đâu là lựa chọn mới, đâu là phương pháp đã được báo cáo. Không nên gọi khác biệt số liệu là tái lập thất bại trước khi chốt chúng. [Mục II–III; Phụ lục]

Phần khả dụng dữ liệu chỉ nói dữ liệu được cung cấp qua yêu cầu hợp lý tới tác giả liên hệ. PDF không dẫn kho mã nguồn hoặc dữ liệu công khai. Vì không dùng web, bản phân tích không xác nhận tài nguyên có thể tồn tại ở nơi khác. [Phần khả dụng dữ liệu, tr. 12]

### 10.4. Tài liệu đọc tiếp từ danh mục của bài

- **Marwan và cộng sự (2007), *Recurrence plots for the analysis of complex systems*** — “Đồ thị tái diễn để phân tích các hệ phức tạp”, *Physics Reports* 438, 237–329. Dùng để đối chiếu nền tảng và quy ước RP/RQA; tài liệu 35, 50, 55.
- **Afsar và cộng sự (2015), *Scaling behaviour for recurrence-based measures at the edge of chaos*** — “Ứng xử theo quy luật tỷ lệ của các đại lượng tái diễn tại biên hỗn loạn”, *EPL* 112, 10005. Liên quan trực tiếp nguồn gốc và tính mới của phép khớp; tài liệu 44.
- **Kraemer và cộng sự (2022), *Spike spectra for recurrences*** — “Phổ xung cho hiện tượng tái diễn”, *Entropy* 24, 1689. Cần đối chiếu để chốt cách tính ISS; tài liệu 52.
- **Kraemer và cộng sự (2018), *Recurrence threshold selection for obtaining robust recurrence characteristics in different embedding dimensions*** — “Chọn ngưỡng để có đặc trưng tái diễn ổn định ở các chiều nhúng khác nhau”, *Chaos* 28, 085720. Liên quan ngưỡng và phép nhúng; tài liệu 51.
- **Noiray (2017), *Linear growth rate estimation from dynamics and statistics of acoustic signal envelope in turbulent combustors*** — “Ước lượng tốc độ tăng trưởng tuyến tính từ động lực học và thống kê đường bao tín hiệu âm trong buồng đốt rối”, *Journal of Engineering for Gas Turbines and Power* 139, 041503. Nguồn mô hình ở Mục II.B; tài liệu 46.
- **Nair và Sujith (2014), *Multifractality in combustion noise: Predicting an impending combustion instability*** — “Tính đa phân hình của nhiễu cháy: dự báo mất ổn định cháy sắp xảy ra”, *Journal of Fluid Mechanics* 747, 635–655. Nguồn mà bài chỉ tới cho mô tả thí nghiệm và động lực học; tài liệu 40.

Các mục trên chỉ được nhận diện từ danh mục tài liệu ở tr. 13–14. Chưa đọc nội dung các tài liệu này; không sử dụng chúng như nguồn bằng chứng độc lập cho bản phân tích.

## Critical Audit

### Điểm mạnh đã kiểm chứng (Verified strengths)

- **Có chuỗi bằng chứng từ biểu diễn đến định lượng.** Đồ thị tái diễn, tỷ lệ theo độ trễ, ISS và RQA cùng mô tả sự tổ chức lại từ nhiều thang tái diễn sang một nhịp chi phối. Đây là bằng chứng mô tả từ thí nghiệm, chưa phải chứng minh cơ chế nhân quả. [Hình 2–3; Mục III.A–B, tr. 7–10]
- **Có mốc mô hình để đối chiếu.** Hai trường hợp Hopf có nhiễu chọn hệ số cản 50, trùng mốc mất ổn định tuyến tính của hệ khi bỏ nhiễu. Điều này mạnh hơn việc chỉ quan sát xu hướng, nhưng phạm vi kiểm chứng vẫn là hai trường hợp thuộc cùng họ mô hình. [Phương trình (1); Hình 6, 8; Mục III.C, tr. 10–12]
- **Nguồn gốc công cụ được dẫn rõ.** Bài dẫn nền tảng RP/RQA, ISS và tiền lệ lũy thừa của Afsar và cộng sự; nhờ đó có thể phân biệt phần kế thừa với cách kết hợp hiện tại. [Mục I–II; tài liệu 44, 47–56; Phụ lục]

### Hiệu chỉnh và giới hạn diễn giải (Corrections / qualifications)

- **Bài toán là mô tả và định vị tham số trên dữ liệu đã đo.** Cần nhiều điều kiện có tham số điều khiển đã biết và giá trị tại ứng viên; chưa có quy tắc dự báo trực tuyến, thời gian báo trước hoặc tỷ lệ cảnh báo sai. Dùng tham chiếu đã đo không tự là lỗi sử dụng dữ liệu tương lai trong phân tích hồi cứu. [Mục III.B–C; Hình 4, 6, 8]
- **Làm rõ công thức khớp và ISS.** Đẳng thức lũy thừa in trong bài thiếu mô tả hệ số tỷ lệ/chuẩn hóa để khớp các giá trị thô; kích thước ma trận ISS chưa khớp mô tả hệ thiếu phương trình. Tương quan Pearson 0.9 chỉ là tiêu chí tái dựng. Các điểm này đã được giải thích tại Mục 4.3–4.4, không tự sửa phương pháp tác giả. [Phương trình (5), (A1); Hình 3–4; Mục III.B, tr. 10; Phụ lục]
- **Hiệu chỉnh mức chắc chắn của kết quả.** Mốc thực nghiệm vẫn thuộc gián đoạn, chưa có mốc phân nhánh độc lập; không phải mọi đại lượng đều cho bằng chứng như nhau. Giữ nguyên số mũ L là 0.30 ± 0.91 theo Hình 4(c), đồng thời đánh dấu thanh sai số không tương ứng ở Hình 9. [Chú thích Hình 3; Hình 4(c), 9]
- **Giới hạn khẳng định rộng.** Mốc Hopf không nhiễu khác với một ngưỡng chuyển trạng thái ngẫu nhiên đã được xác định; sự hiện diện của nhiễu chưa chứng minh độ vững khi thay mức nhiễu. Các kết quả chưa xác lập tính phổ quát, ưu thế so với phương án đối chứng hoặc hiệu lực dự báo y sinh. [Mục II.B, III.C–IV; Hình 5–9; Mục 8 của bản phân tích]

### Hạn chế phương pháp luận (Methodological limitations)

- **Chưa bảo đảm nhận dạng duy nhất.** Ví dụ tuyến tính tại Mục 7 cho quan hệ lũy thừa ở mọi điểm tham chiếu. Bài chưa báo cáo định lý hoặc đối chứng không có chuyển tiếp để xác lập tính đặc hiệu của tiêu chí. Đây là giới hạn suy luận, không phải một lần tái lập thất bại. [Tiêu chí tại Mục III.B, tr. 9–10]
- **Chưa đánh giá được độ hiệu chỉnh của sai số.** Phép trừ chung tham chiếu tạo phụ thuộc giữa các độ lệch; thay ứng viên còn có thể đổi số điểm và khoảng khớp. PDF chưa mô tả xử lý hiệp phương sai, sai số tham chiếu, việc chọn cực tiểu qua nhiều ứng viên hoặc mức bao phủ của thanh sai số. [Mục III.B–C; Hình 4, 6, 8; suy luận tại Mục 4.4 của bản phân tích]
- **Thiếu bằng chứng về lợi ích tăng thêm và khái quát.** RMS cũng chọn cùng mốc thực nghiệm; chưa có so sánh thuật toán công bằng, loại bỏ thành phần, khảo sát độ nhạy có hệ thống hoặc phân bố sai số qua nhiều lần mô phỏng độc lập. Không thể suy từ “chưa báo cáo” thành “đã thất bại”. [Hình 4(a), 6, 8; Mục III.B–IV]
- **Tái lập chính xác còn phụ thuộc thông tin bổ sung.** Thiếu dữ liệu tải công khai, mã nguồn được dẫn trong PDF, giá trị nhúng thực tế, bước dịch cửa sổ, mô hình hồi quy/độ bất định và chi tiết mô phỏng/ISS. Dữ liệu được cung cấp qua yêu cầu hợp lý; tái triển khai ý tưởng khả thi hơn tái tạo đúng mọi số liệu ngay từ PDF. [Mục II–III; Phụ lục; phần khả dụng dữ liệu, tr. 12]

### Câu hỏi còn mở (Open questions)

- **Tiêu chí nào thực sự được tối ưu?** Cần công bố hệ số tỷ lệ/chuẩn hóa, hàm mất mát, trọng số, định nghĩa thanh sai số và cách xử lý điểm bằng không; giải thích quan hệ giữa cực tiểu phần dư và cực tiểu độ bất định số mũ. [Mục III.B, tr. 10; Hình 4, 6, 8]
- **Điểm được chọn ổn định đến đâu?** Cần kiểm tra các ứng viên trên khoảng khớp tương đương, truyền sai số tham chiếu, đánh giá toàn bộ bước chọn điểm qua nhiều lần chạy và xác minh độ bất định L giữa Hình 4(c)–9. [Mục III.B–C; đề xuất kiểm tra tại Mục 10.2]
- **Các chi tiết mô hình và ISS cần được xác nhận ra sao?** Cần dữ liệu/mã để chốt kích thước, hạng và chuẩn hóa hàm cơ sở ISS; đồng thời kiểm tra miền quỹ đạo bị chặn của mô hình với các dấu tham số đã in. Không đủ căn cứ tự kết luận lỗi in hoặc thay dấu. [Phương trình (1), Mục II.B; Phụ lục; Mục 10.2 của bản phân tích]
- **Có thể chuyển sang y sinh với đầu vào nào?** Đây là giả thuyết: cần xác định tham số thay thế hoặc chuyển sang bài toán phát hiện trạng thái, có mốc đối chiếu độc lập và kiểm tra theo thời gian không dùng dữ liệu tương lai. PDF không có ECG/EEG/PPG hoặc kiểm chứng lâm sàng. [Phạm vi dữ liệu tại Mục II.A–B; phân tích giả thuyết tại Mục 8]

**Kết luận về tính mới (Novelty verdict):** Phù hợp nhất với **mở rộng phương pháp (Methodological extension)** và **đóng góp khái niệm (Conceptual contribution)**: kết hợp các công cụ đã có với cách diễn giải ngưng tụ tái diễn và thủ tục chọn tham số theo chất lượng khớp. Một thí nghiệm cùng hai trường hợp Hopf hỗ trợ cách kết hợp này; các tiền lệ do bài dẫn chưa cho phép kết luận đây là phương pháp hoàn toàn mới hoặc ứng dụng đầu tiên của phân tích tái diễn cho buồng đốt. [Mục I, III–IV; tài liệu 41–44, 52]
