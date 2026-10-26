# Seralan và cộng sự (2026) — Phương sai của các đại lượng theo cửa sổ để đặc trưng chuyển tiếp tới biến cố cực đoan

**Tên bài báo:** *Complexity measures: Characterization of transition to extreme events in dynamical systems* — “Các thước đo độ phức tạp: Đặc trưng chuyển tiếp tới biến cố cực đoan trong hệ động lực”.

**Tác giả:** Vinoth Seralan, S. Leo Kingston, Suresh Kumarasamy, Ajit Mahata, Karthikeyan Rajagopal và Tomasz Kapitaniak. **Công bố:** *Chaos* **36**, 083153 (2026), công bố trực tuyến ngày 28/8/2026. **DOI:** [10.1063/5.0304782](https://doi.org/10.1063/5.0304782).

**Phạm vi nguồn:** Chỉ sử dụng [PDF được chỉ định](<../paper/12 Complexity measures-- Characterization of transition to extreme events in dynamical systems.pdf>), đã đọc toàn bộ 13 trang, gồm bìa, nội dung, phụ lục và danh mục tài liệu; đối chiếu trực quan Hình 1–9 và các công thức chính. Không sử dụng web hoặc truy cập các tài liệu được dẫn. Các nguồn đọc tiếp ở cuối chỉ được nhận diện từ danh mục của chính PDF này.

**Quy ước trang:** “Tr. 1–12” bên dưới chỉ trang bài báo 083153-1 đến 083153-12, tương ứng trang PDF 2–13; trang PDF 1 là bìa. Năm công bố lấy theo trang đầu bài, không theo tên tệp hay ngày tải.

Câu hỏi trung tâm không chỉ là một chuỗi có entropy cao hay thời gian tái diễn dài hay không, mà là **các đại lượng này biến đổi giữa những đoạn liên tiếp như thế nào**. Tác giả chia chuỗi thành những đoạn không chồng lấn, tính thời gian tái diễn trung bình và entropy Shannon trong từng đoạn, rồi lấy phương sai giữa các đoạn. Trong các mô hình khảo sát, phương sai lớn xuất hiện ở miền có những đợt bùng phát lớn hiếm gặp, trong khi hỗn loạn bị giới hạn hoặc dao động lớn thường xuyên có phương sai nhỏ hơn. Bằng chứng là mô phỏng và đối chiếu hồi cứu theo tham số; chưa phải kiểm chứng dự báo trước thời điểm xuất hiện biến cố. [Mục I–II, tr. 2–3; Hình 2–7; Mục V, tr. 9–10]

## 1. Bài toán và động cơ: độ lớn trung bình có thể bỏ qua sự xen kẽ giữa các chế độ

Biến cố cực đoan được bài mô tả là những chuyến đi xa, tồn tại ngắn của quỹ đạo vốn dành phần lớn thời gian trong một miền dao động thông thường. Khi các chuyến đi xa trở nên thường xuyên, hệ có thể vẫn dao động với biên độ lớn nhưng tác giả gọi đó là chế độ không cực đoan. Vấn đề vì thế là phân biệt **biến cố lớn hiếm gặp**, **hỗn loạn bị giới hạn** và **dao động lớn thường xuyên**, chứ không đơn thuần phát hiện biên độ vượt một giá trị cố định. [Mục I, tr. 1–2; Mục III.B, tr. 4]

Bối cảnh được nêu gồm thiên tai, khí hậu, tài chính và các hệ kỹ thuật. Tuy nhiên, kiểm chứng trực tiếp của bài gồm bốn mô hình: Brusselator, laser CO₂, ba thiết bị giao thoa lượng tử siêu dẫn ghép từ và hai nơron Hindmarsh–Rose ghép qua khớp thần kinh. Không có chuỗi đo thực tế hay dữ liệu lâm sàng trong thiết kế được báo cáo. [Mục I, tr. 1–2; Mục III–IV, tr. 3–9]

**Tác giả khẳng định (Authors claim):** Các chỉ số độ phức tạp kinh điển chưa mô tả đủ những đợt lớn hiếm gặp. Thời gian tái diễn trung bình có thể gần nhau ở miền cực đoan và miền dao động lớn thường xuyên; entropy đơn lẻ cũng bỏ sót một phần miền cực đoan. Cần một đại lượng phản ánh sự dao động hữu hạn theo thời gian của chính các chỉ số đó. [Mục I, tr. 2; Mục III.B–C, tr. 4–7]

**Bằng chứng hỗ trợ (Evidence supports):** Hình 2 trực tiếp đặt các đường chỉ số gốc cạnh phương sai của chúng: thời gian tái diễn trung bình vẫn khá cao ở miền dao động lớn thường xuyên, trong khi phương sai giảm; entropy gốc không tạo một mức riêng duy nhất cho toàn bộ miền cực đoan. Các hình sau mở rộng đối chiếu này sang những hệ khác. Đây là so sánh nội tại với hai đại lượng thành phần, chưa phải đánh giá hiệu năng trên một tập phương pháp đối chiếu rộng. [Hình 2, tr. 5; Hình 4, 6–7, tr. 6, 8–9]

**Diễn giải của người phân tích (Analyst interpretation):** Ý tưởng khoa học hợp lý là đo mức không đồng nhất giữa các đoạn: một đoạn chỉ có dao động nền có thể cho chỉ số khác một đoạn chứa bùng phát. Phương sai có thể làm nổi bật sự xen kẽ đó. Tuy nhiên, “không đồng nhất giữa các đoạn” rộng hơn “biến cố cực đoan”; cần giữ sự phân biệt này khi diễn giải tính đặc hiệu của phương pháp. [Cơ sở: quy trình Mục II, tr. 2–3 và Phương trình (4)]

## 2. Đặt bài toán: một chuỗi để tính chỉ số, nhiều chuỗi để khảo sát chuyển tiếp

Đầu vào của một phép tính là **một chuỗi thời gian một chiều tại điều kiện tham số cố định**. Chuỗi được chia thành k đoạn, mỗi đoạn lấy dãy cực đại địa phương. Hai loại thống kê được tính riêng cho từng đoạn rồi tổng hợp bằng phương sai. Để dựng các đường và giản đồ miền trạng thái trong bài, cần **nhiều chuỗi**, mỗi chuỗi gắn với một giá trị hoặc cặp giá trị tham số đã biết. Không phải lấy phương sai giữa những giá trị tham số khác nhau. [Mục II, tr. 2–3; Hình 1–7]

| Thành phần | Nội dung và vai trò |
| --- | --- |
| Tín hiệu quan sát | x trong hình Brusselator; y trong laser CO₂; từ thông của thiết bị thứ nhất trong hệ siêu dẫn; tổng hai biến x của hệ nơron |
| Biểu diễn trung gian | Dãy biên độ cực đại của từng đoạn không chồng lấn |
| Lựa chọn phân tích | Độ dài đoạn T, số đoạn k, ngưỡng tái diễn, số khoảng chia biên độ m và quy tắc tìm cực đại |
| Thông tin biết trước khi kiểm chứng | Phương trình mô hình, tham số đang quét, biểu đồ phân nhánh và ngưỡng đánh dấu biến cố cực đoan |
| Đầu ra tại một điều kiện | Hai phương sai giữa các đoạn: phương sai thời gian tái diễn trung bình và phương sai entropy chuẩn hóa |
| Đầu ra của khảo sát tham số | Đường hoặc giản đồ hai phương sai; đối chiếu với miền có cực đại vượt ngưỡng |

Nguồn: Mục II–IV, tr. 2–9; Hình 1–9. Biến x của các hình Brusselator chưa được đồng nhất tường minh với hai biến u của Phương trình (5); đó là một chi tiết cần chốt khi tái lập, không phải một biến quan sát mới được tự suy ra ở đây.

Phương trình mô hình và tham số điều khiển không đi trực tiếp vào công thức phương sai. Chúng cần cho việc sinh dữ liệu và kiểm chứng mối liên hệ giữa chỉ số với các chế độ. Bài không đưa một bộ phân loại đã huấn luyện, không có nhãn lâm sàng và không có bước học tham số từ một tập huấn luyện. [Mục II–IV]

Phạm vi đầu ra cần phân biệt:

1. **Mô tả thống kê:** đo sự thay đổi của hai đại lượng giữa các đoạn; đây là phép tính được xác định trong bài.
2. **Nhận diện hồi cứu:** sau khi đã thu thập chuỗi, kiểm tra chỉ số cao có nằm cùng miền có biến cố cực đoan hay không; được minh họa qua đường quét và giản đồ tham số.
3. **Định vị điểm chuyển tiếp:** tác giả chỉ ra những bước đổi gần mốc khởi phát, nhưng chưa đưa quy tắc chọn mốc tự động, sai số định vị hay độ phân giải bảo đảm.
4. **Dự báo trước biến cố:** chưa có thiết kế chỉ dùng quá khứ để dự báo một thời điểm hoặc biên độ tương lai, cũng chưa có thời gian báo trước và tỷ lệ cảnh báo sai.

Nguồn: Mục I–II, tr. 2–3; Mục III–V, tr. 4–10. Lời dẫn về ích lợi cho dự báo là động cơ và hàm ý nghiên cứu, không phải kết quả dự báo đã được kiểm chứng.

## 3. Nguồn gốc phương pháp: mở rộng một ý tưởng đã có

| Thành phần | Tiền lệ được chính PDF nêu | Phần được thực hiện trong bài |
| --- | --- | --- |
| **Đồ thị tái diễn** (*recurrence plot*, RP) và **phân tích định lượng tái diễn** (*recurrence quantification analysis*, RQA) | Tài liệu 21 và 33–35 | Dùng ma trận tái diễn trên dãy cực đại; lấy độ dài các vệt trắng thẳng đứng để tính thời gian tái diễn |
| **Thời gian tái diễn trung bình** (*mean recurrence time*, MRT) | Tài liệu 35; Phương trình (1) | Đại lượng tính trong từng đoạn, không phải một chỉ số mới được phát minh |
| Entropy Shannon chuẩn hóa, ký hiệu ENT | Shannon, tài liệu 36; Phương trình (2)–(3) | Thống kê phân bố biên độ cực đại của từng đoạn |
| Phương sai MRT | Công trình về mạng điều hòa gen có trễ, tài liệu 27 | Đã được dùng cho các chuyển tiếp gián đoạn trước đó; bài hiện tại tự nêu tiền lệ này ở phần mở đầu |
| Phương sai ENT và kiểm chứng trên bốn mô hình | Mục I–V | Nhánh bổ sung được triển khai cùng phương sai MRT; mở rộng khảo sát sang chuyển tiếp từ hỗn loạn và phân biệt dao động lớn thường xuyên |
| Tích entropy và độ lệch khỏi phân bố đều | Das và cộng sự, tài liệu 28 | Được thảo luận làm đối chiếu trong tổng quan; bài không tính lại chỉ số này trên cùng các chuỗi để đánh giá trực tiếp |

Nguồn: Mục I–II, tr. 2–3; Mục III.B, tr. 5; danh mục tài liệu 21, 27–28, 33–36, tr. 12. Tài liệu trong danh mục chưa được xem như đã đọc độc lập.

Do đó, đóng góp phù hợp nhất là **mở rộng phương pháp và phạm vi kiểm chứng**, nhấn mạnh dao động giữa các đoạn của các thống kê kế thừa. Chưa đủ cơ sở gọi toàn bộ phép lấy phương sai MRT là mới. Tuyên bố ở tr. 5 rằng phương pháp khắc phục hạn chế của tài liệu 28 cần được đọc cùng việc **không có phép so sánh lại trên cùng dữ liệu** với chỉ số của Das và cộng sự. [Mục I, tr. 2; Mục III.B, tr. 5; Mục V, tr. 9–10]

## 4. Quy trình phương pháp và ý nghĩa các công thức

### 4.1. Chia chuỗi thành các đoạn rồi trích cực đại

$$
x^{(j)}=\{x_{(j-1)T+1},\ldots,x_{jT}\},\qquad
E^{(j)}=\{e_i^{(j)}\}_{i=1}^{n_j},\qquad
j=1,\ldots,k.
$$

Đây là cách phân đoạn và ký hiệu dãy cực đại ở đầu Mục II, tr. 2. Tác giả gọi T là thời lượng cố định, nhưng chỉ số mẫu trong công thức sử dụng T như số mẫu mỗi đoạn; không có thông tin lấy mẫu để chuyển hai cách biểu diễn thành một giá trị số cụ thể. k là số đoạn không chồng lấn; n có chỉ số j là số cực đại trong đoạn j, có thể khác nhau giữa các đoạn.

PDF không báo cáo các giá trị T, k hoặc độ dài toàn bộ chuỗi đã dùng để tạo từng điểm trên các đường phương sai. Cũng chưa nêu xử lý mẫu thừa ở cuối chuỗi, đoạn có quá ít cực đại, đỉnh bằng nhau hay đỉnh nằm sát ranh giới đoạn. Đây là các lựa chọn triển khai còn thiếu, không được tự điền bằng cấu hình của bài báo khác. [Mục II, tr. 2–3]

Chia theo thời lượng của tín hiệu gốc khác với chia thành những đoạn có cùng số cực đại. Nếu tốc độ phát đỉnh thay đổi theo chế độ, n giữa các đoạn thay đổi theo. Mục II mô tả cách thứ nhất; bản phân tích không thay bằng cách thứ hai. [Mục II, tr. 2]

### 4.2. Nhánh tái diễn: dựng RP và tính MRT của từng đoạn

Định nghĩa ma trận tái diễn trong bài được viết cho một chuỗi vô hướng. Kết hợp với câu mô tả rằng MRT được tính từ dãy cực đại của từng đoạn, có thể biểu diễn lại như sau:

$$
R_{ab}^{(j)}=
\begin{cases}
1,&\|e_a^{(j)}-e_b^{(j)}\|_2\leq\epsilon_R,\\
0,&\|e_a^{(j)}-e_b^{(j)}\|_2>\epsilon_R.
\end{cases}
$$

a và b là chỉ số các cực đại trong đoạn j. Đây là đổi chỉ số để tránh nhầm với chỉ số đoạn; không phải một ma trận mới do tác giả đề xuất. Bài chọn chuẩn Euclid và ngưỡng bằng 30% độ lệch chuẩn của tín hiệu. Ký hiệu ε có chỉ số R là cách bản phân tích phân biệt ngưỡng tái diễn với ε của mô hình laser; bài dùng cùng chữ ε cho hai ý nghĩa. [Định nghĩa RP, Mục II.A, tr. 2–3]

$$
\epsilon_R=0.30\,\sigma.
$$

σ là độ lệch chuẩn được dùng để định cỡ ngưỡng. PDF chưa xác định đầy đủ σ lấy từ tín hiệu gốc hay từ dãy cực đại, từ cả chuỗi hay tính lại cho từng đoạn. Không nên mặc định tái chuẩn hóa mỗi đoạn hoặc giữ một ngưỡng chung cho mọi điều kiện nếu chưa có mã gốc. Bài cũng không mô tả phép nhúng trễ; không tự bổ sung phép nhúng nhiều chiều vào quy trình được báo cáo. [Mục II.A, tr. 2–3]

Tiếp theo, thống kê những vệt trắng thẳng đứng, tức các đoạn liên tiếp có giá trị tái diễn bằng 0, theo độ dài ℓ. MRT của đoạn được tính bằng trung bình có trọng số:

$$
M_j=\operatorname{MRT}(E^{(j)})
=\frac{\sum_{\ell=1}^{N}\ell\,p_j(\ell)}
{\sum_{\ell=1}^{N}p_j(\ell)}.
$$

Đây là Phương trình (1), tr. 3, với chỉ số j được bổ sung để làm rõ phép tính từng đoạn. p là phân bố độ dài vệt trắng; tỷ số trên dùng được cả khi p được biểu diễn bằng tần suất đếm hoặc xác suất tương ứng. N là giới hạn tổng theo ký hiệu gốc; PDF không đặc tả đầy đủ cách đặt giới hạn này theo kích thước từng đoạn.

MRT trong quy trình này gắn với **bước trong dãy cực đại**. Vì các cực đại không nhất thiết cách đều theo thời gian vật lý, không thể tự coi giá trị MRT là số giây chờ giữa các biến cố. PDF không mô tả một phép đổi từ độ dài vệt sang thời gian vật lý, không quy định chi tiết xử lý vệt chạm mép, vùng quanh đường chéo chính hoặc trường hợp không có vệt trắng hợp lệ. [Phương trình (1); Mục II.A, tr. 3]

### 4.3. Nhánh entropy: phân bố biên độ của từng đoạn

$$
\begin{aligned}
\Delta_j&=\frac{\max E^{(j)}-\min E^{(j)}}{m},\\
H_j&=-\sum_{i=1}^{m}p_i^{(j)}\log_2 p_i^{(j)},\\
A_j&=\operatorname{ENT}(E^{(j)})=\frac{H_j}{\log_2 m}.
\end{aligned}
$$

Δ là độ rộng khoảng chia biên độ, m là số khoảng bằng nhau trong từng đoạn, còn p có chỉ số i, j là tỷ lệ cực đại của đoạn j rơi vào khoảng i. H là entropy Shannon; ENT là entropy đã chuẩn hóa. Ký hiệu A được bản phân tích đặt để viết gọn công thức phương sai bên dưới. Đây là quy tắc chia khoảng và Phương trình (2)–(3), Mục II.B, tr. 3.

Điểm quan trọng là **biên khoảng được xác định lại theo miền biên độ của từng đoạn**. Phương sai ENT vì vậy so sánh những phân bố có thể nằm trên các miền biên độ khác nhau. Không được diễn giải nó như phương sai của entropy tính trên một hệ biên cố định nếu chưa đổi thiết kế phân tích. PDF không nêu giá trị số m, quy tắc xử lý dãy cực đại hằng hoặc số cực đại ít hơn số khoảng chia. Đóng góp của xác suất 0 cần được hiểu bằng giới hạn bằng 0 khi triển khai. [Mục II.B, tr. 3]

ENT chỉ đo phân bố biên độ trong đoạn, không phải tốc độ sinh thông tin theo thời gian. ENT không dùng thứ tự cực đại bên trong đoạn, mặc dù việc chia theo thời gian vẫn giữ được thông tin đoạn nào có phân bố khác đoạn nào. [Suy ra từ Phương trình (2)–(3)]

### 4.4. Lấy phương sai giữa các đoạn tại một điều kiện tham số

$$
\begin{aligned}
\bar M&=\frac{1}{k}\sum_{j=1}^{k}M_j,\qquad
V_{\mathrm{MRT}}=\frac{1}{k-1}\sum_{j=1}^{k}(M_j-\bar M)^2,\\
\bar A&=\frac{1}{k}\sum_{j=1}^{k}A_j,\qquad
V_{\mathrm{ENT}}=\frac{1}{k-1}\sum_{j=1}^{k}(A_j-\bar A)^2.
\end{aligned}
$$

Phương sai MRT là Phương trình (4), Mục II.C, tr. 3, dùng mẫu số k − 1. Bài nói phương sai ENT được tính tương tự; dòng thứ hai viết tường minh thao tác đó, không phải bổ sung một chỉ số khác. Cần ít nhất hai đoạn có đại lượng hợp lệ. Cả hai đều là **phương sai của thống kê theo đoạn**, không phải phương sai biên độ của tín hiệu gốc và không phải phương sai của đường chỉ số theo tham số.

Bài thường vẽ MRT hoặc ENT bằng màu xanh, phương sai tương ứng bằng màu đỏ, trên **hai trục tung có thang khác nhau**. Không so chiều cao hai đường như các đại lượng cùng đơn vị. Văn bản chưa xác định đủ chi tiết cách tổng hợp thành từng điểm màu xanh — chẳng hạn tính trên toàn bộ dãy cực đại hay lấy trung bình các đoạn — dù phép lấy phương sai giữa các đoạn đã được nêu rõ. [Hình 1–2, 4, 6–7; Mục II.C]

Đây là phép tính thống kê trực tiếp: không có hàm mất mát, thuật toán tối ưu hoặc mô hình phải huấn luyện. Những lựa chọn cần thiết là T, k, m, ngưỡng tái diễn và cách lấy cực trị. [Mục II]

### 4.5. Ngưỡng cực đoan và biến đếm làm tham chiếu

Với các cực đại được đánh dấu bằng một ngưỡng, cấu trúc chung của quy tắc trong bài là:

$$
Q_{\mathrm{th}}=\langle a_{\max}\rangle+c_Q\sigma_{\max},\qquad
C_{\mathrm{exc}}=\sum_{r=1}^{n}\mathbf{1}\{a_r>Q_{\mathrm{th}}\}.
$$

Trong khối này, a là biên độ cực đại, c có chỉ số Q là hệ số ngưỡng và C có chỉ số exc là số lần vượt ngưỡng; các tên này do bản phân tích đặt để tránh nhầm với tham số mô hình. Công thức thứ hai diễn đạt bằng ký hiệu toán cách tác giả mô tả đại lượng đếm, không phải một phương trình được bài đánh số. Bài dẫn tài liệu 16 cho mô tả chi tiết hơn. [Mục III.B, tr. 4–5]

Brusselator và laser dùng trung bình cực đại cộng sáu lần độ lệch chuẩn; hệ siêu dẫn dùng bốn lần. Với hệ nơron, bài viết trung bình của tổng hai biến x cộng sáu lần độ lệch chuẩn, không ghi chỉ số cực đại trong chính công thức; cần xác minh tập mẫu dùng tính ngưỡng ở trường hợp này. [Mục III.B–C, tr. 4, 6; Mục IV.A–B, tr. 8–9]

Ngưỡng không xuất hiện trong hai công thức phương sai. Tuy nhiên, kết luận rằng phương sai cao ứng với “cực đoan” được đánh giá so với nhãn miền tạo từ ngưỡng này. Đổi hệ số ngưỡng có thể đổi nhãn đối chiếu dù không đổi chỉ số đã tính trên cùng chuỗi. Số lần vượt ngưỡng là số đếm trong chuỗi hữu hạn, chưa phải xác suất biến cố đã hiệu chuẩn; các thang màu lôgarit trong hình phục vụ trình bày. [Hình 2–7; Mục III.B, tr. 5]

### 4.6. Vì sao phương sai có thể tăng khi xuất hiện biến cố hiếm?

**Diễn giải của người phân tích, không phải mô hình được tác giả khớp:** Gọi Z là chỉ báo một đoạn có chứa biến cố, q là xác suất của loại đoạn đó và M là một thống kê theo đoạn. Khi phân biệt hai loại đoạn, phân rã phương sai có dạng:

$$
\operatorname{Var}(M)
=(1-q)\sigma_0^2+q\sigma_1^2
+q(1-q)(\mu_1-\mu_0)^2.
$$

μ và σ có chỉ số 0, 1 là trung bình và độ lệch chuẩn có điều kiện theo hai loại đoạn. Thành phần cuối cho thấy sự chênh lệch giữa đoạn nền và đoạn có biến cố có thể làm phương sai tăng. Đây là giải thích thống kê cho ý tưởng ở Mục I–II, chưa phải kết quả mô phỏng hay quan hệ định lượng do bài chứng minh.

Cách giải thích này cũng cho thấy T quan trọng: đoạn quá dài có thể chứa nhiều loại hành vi cùng lúc; đoạn quá ngắn có thể không đủ cực đại để ước lượng ổn định. Nếu biến cố quá hiếm đến mức chưa xuất hiện trong dữ liệu, hoặc hầu như mọi đoạn đều có biến cố, phần chênh lệch giữa hai loại đoạn có thể nhỏ. Vì thế không có bảo đảm tổng quát rằng cứ có biến cố cực đoan thì hai phương sai luôn cao.

## 5. Bốn mô hình và thiết kế kiểm chứng

### 5.1. Brusselator có cưỡng bức: đối chiếu tuần hoàn, hỗn loạn và biến cố cực đoan

$$
\begin{aligned}
\frac{du_1}{dt}&=\mu-(\alpha+1)u_1+u_1^2u_2+I\sin(\omega t),\\
\frac{du_2}{dt}&=\alpha u_1-u_1^2u_2.
\end{aligned}
$$

Đây là Phương trình (5), Mục III.A, tr. 3. μ và α là các tham số phản ứng được tác giả liên hệ với nồng độ ban đầu và tốc độ suy giảm của chất tự xúc tác; I và ω là biên độ và tần số cưỡng bức. Bài cố định μ = 0,2; α = 1,114; ω = 0,69 và tăng I. Hình dùng ký hiệu x cho đại lượng quan sát; PDF không viết tường minh phép đồng nhất x với một trong hai biến u của phương trình.

Thí nghiệm thứ nhất quét I trong khoảng 0,051–0,0518 để quan sát nhân đôi chu kỳ tới hỗn loạn, trước khi xét biến cố cực đoan. Đây là đối chiếu nền để kiểm tra các chỉ số phản ứng với chế độ tuần hoàn và hỗn loạn thông thường như thế nào. [Mục III.A, tr. 3–4; Hình 1]

Thí nghiệm tiếp theo mở rộng tới I = 0,056. Văn bản phân các miền: hỗn loạn bị giới hạn khoảng 0,051–0,0519; cực đoan khoảng 0,0520–0,0545; dao động lớn thường xuyên khoảng 0,0546–0,056. Miền đầu được gọi chung là miền hỗn loạn trong Mục III.B, nhưng Hình 1 và chính ghi chú ở tr. 4 cho thấy vẫn có các nhánh tuần hoàn ở phần thấp của khoảng này; không nên coi toàn bộ khoảng 0,051–0,0519 là thuần hỗn loạn. Các khoảng được báo cáo không xác định chính xác những khoảng hở nhỏ ở ranh giới. [Mục III.B, tr. 4; Hình 1–2]

Cơ chế khởi phát được tác giả quy cho **khủng hoảng nội tại** (*interior crisis*): tập hút hỗn loạn tương tác với quỹ đạo tuần hoàn bất ổn, mở ra những chuyến đi xa. Bài dẫn nguồn cho cơ chế; nghiên cứu hiện tại không trình bày lại một kiểm chứng quỹ đạo bất ổn độc lập. Ngoài quét một tham số, Hình 3 khảo sát miền I từ 0,05 đến 0,07 và ω từ 0,66 đến 0,72. [Mục III.B, tr. 4–5; Hình 3]

### 5.2. Laser CO₂: kiểm tra một cơ chế được mô tả là không trơn

$$
\begin{aligned}
\dot{x}&=x\left[l_1\left(y-1.0-k_1\sin^2 z\right)
-l_3\epsilon\cos(l_2t)\right],\\
\dot{y}&=-(y-n)-2l_1xy,\\
\dot{z}&=-l_4\left(z-b+\frac{rx}{1+\zeta x}\right).
\end{aligned}
$$

Đây là Phương trình (6), Mục III.C, tr. 5. Quan sát của các hình là y; ngưỡng cực đoan dùng các cực đại của y. Bài quét ε từ 1,625 đến 1,685; giản đồ hai tham số ở Hình 5 dùng ε từ 1,62 đến 1,66 và r từ 199 đến 201. Các tham số được nêu ở tr. 6 gồm n = 4,0; b = 4,5; η = 25,57; r = 200 và:

$$
l_1=28.57,\qquad l_2=30.0,\qquad
l_3=25.0,\qquad l_4=6.452.
$$

**Chi tiết chưa nhất quán:** Phương trình chứa ζ và k có chỉ số 1, nhưng danh sách giá trị in η = 25,57 mà không xác định rõ η tương ứng với hệ số nào trong phương trình. Không tự gán η cho ζ hoặc cho hệ số k. PDF hiện tại chưa đặc tả đủ các giá trị cần thiết để cài đặt duy nhất Phương trình (6). [Phương trình (6), tr. 5; danh sách tham số Mục III.C, tr. 6]

Tác giả diễn giải biến cố lớn bằng **phân nhánh tiếp xúc–trượt** (*grazing–sliding bifurcation*): quỹ đạo tới gần biên không liên tục x = 0, sau đó có giai đoạn trượt gần biên và lệch xa biên độ thông thường. Tuy nhiên, hệ phương trình được in chưa kèm các nhánh vectơ trường, điều kiện chuyển nhánh hoặc quy tắc trượt để triển khai rõ một hệ không trơn. Cơ chế và chi tiết mô hình được dẫn tới tài liệu 30, 38; chưa đọc các tài liệu đó nên bản phân tích không bổ sung quy tắc từ bên ngoài. [Mục III.C, tr. 5–6]

### 5.3. Bộ ba thiết bị giao thoa lượng tử siêu dẫn

Bài sử dụng ba **thiết bị giao thoa lượng tử siêu dẫn** (*Superconducting Quantum Interference Devices*, SQUID) ghép qua tương tác từ. Phương trình chuẩn hóa được in như sau:

$$
\begin{bmatrix}
\ddot{\phi}_1+\gamma\dot{\phi}_1+\beta\sin(2\pi\phi_1)\\
\ddot{\phi}_2+\gamma\dot{\phi}_2+\beta\sin(2\pi\phi_2)\\
\ddot{\phi}_3+\gamma\dot{\phi}_3+\beta\sin(2\pi\phi_3)
\end{bmatrix}
=\frac{1}{D}F
\begin{bmatrix}
\phi_1-\phi_{\mathrm{ext}}\\
\phi_2-\phi_{\mathrm{ext}}\\
\phi_3-\phi_{\mathrm{ext}}
\end{bmatrix}.
$$

Đây là Phương trình (7), Mục IV.A, tr. 7. Các biến φ là từ thông chuẩn hóa; γ liên quan suy giảm và Λ bên dưới là hệ số ghép từ. Ma trận F và hệ số D được bài cho ngay sau phương trình:

$$
\begin{aligned}
F&=
\begin{bmatrix}
1-\Lambda^2 & -\Lambda+\Lambda^2/8 & \Lambda^2-\Lambda/8\\
-\Lambda+\Lambda^2/8 & 1-\Lambda^2/64 & -\Lambda+\Lambda^2/8\\
\Lambda^2-\Lambda/8 & -\Lambda+\Lambda^2/8 & 1-\Lambda^2
\end{bmatrix},\\
D&=\det(\widehat{\Lambda})
=1-\frac{129}{64}\Lambda^2+\frac{1}{4}\Lambda^3.
\end{aligned}
$$

D ở đây là định thức của ma trận ghép theo ký hiệu mô hình, không phải một chỉ số độ lệch xác suất. Bản phân tích giữ đúng dấu ở vế phải và vectơ chênh lệch từ thông của Phương trình (7); không sửa dấu dựa vào một phiên bản mô hình chưa được đọc. Tín hiệu cưỡng bức được cho bởi:

$$
\phi_{\mathrm{ext}}=\phi_{\mathrm{dc}}
+\phi_{\mathrm{ac}}\cos(\omega\tau),\qquad
\beta=0.1384,\qquad \phi_{\mathrm{dc}}=0.
$$

Đây là dạng cưỡng bức và các giá trị được nêu tại Mục IV.A, tr. 7. PDF chưa cung cấp giá trị số đầy đủ cho Λ, biên độ cưỡng bức và tần số dùng tạo Hình 6. Cần bổ sung chúng trước khi tái lập mô phỏng.

Đại lượng quan sát là từ thông của thiết bị thứ nhất. Hình 6 quét γ từ 0,006 đến 0,028; quá trình khởi phát được mô tả theo **chiều giảm γ**, với vùng gần tuần hoàn từ khoảng 0,028 xuống 0,0235 và mốc bùng phát khoảng 0,0234. Cơ chế được gọi là **gián đoạn gần tuần hoàn** (*quasiperiodic intermittency*): những đợt bùng phát hiếm xen vào dao động gần tuần hoàn. Tác giả dẫn phân nhánh Neimark–Sacker cho nguồn gốc miền gần tuần hoàn nhưng nói rõ không trình bày phân nhánh đó trong bài. Ngưỡng cực đoan dùng trung bình cực đại cộng bốn lần độ lệch chuẩn. [Mục IV.A, tr. 8; Hình 6]

### 5.4. Hai nơron Hindmarsh–Rose ghép qua khớp thần kinh

$$
\begin{aligned}
\dot{x}_i&=y_i+bx_i^2-ax_i^3-z_i+I
-k_i(x_i-v_s)\Gamma(x_j),\\
\dot{y}_i&=c-dx_i^2-y_i,\\
\dot{z}_i&=r\left[s(x_i-x_R)-z_i\right],\\
\Gamma(x)&=\frac{1}{1+\exp[-\lambda(x-\Theta)]},
\qquad i,j\in\{1,2\},\quad i\ne j.
\end{aligned}
$$

Đây là Phương trình (8) và hàm ghép trong Mục IV.B, tr. 8. Hai nơron có tổng cộng sáu biến trạng thái. Bài cho a = 1,0; b = 3,0; c = 1,0; d = 5,0; λ = 10,0 và:

$$
x_R=-1.6,\qquad v_s=2.0,\qquad \Theta=-0.25,\qquad
k_1=k_2=k>0,\qquad x_{\parallel}=x_1+x_2.
$$

Tác giả gọi ghép dương này là kích thích hoặc hút; các phép tính dùng tổng hai biến x làm quan sát. Bài không cho giá trị số r, s, I trong phần đặc tả mô hình; không dùng các giá trị của một công trình khác để lấp chỗ trống. [Mục IV.B, tr. 8–9]

Hình 7 quét k từ 0,0525 đến 0,0545 và nêu mốc k = 0,0532. Cơ chế được gọi là **gián đoạn Pomeau–Manneville** (*Pomeau–Manneville intermittency*, PM): các pha gần tuần hoàn bị ngắt bởi những bùng phát lớn hiếm gặp. Ngưỡng in trong văn bản dùng trung bình tổng hai biến x cộng sáu lần độ lệch chuẩn; cách tính từ cực đại hay từ toàn bộ tín hiệu chưa được xác định nhất quán như ở các ví dụ khác. [Mục IV.B, tr. 9; Hình 7]

### 5.5. Các nhóm chuyển tiếp và những điều kiện kiểm chứng còn thiếu

Tác giả tổ chức nghiên cứu thành **ba nhóm chuyển tiếp**: từ hỗn loạn, từ gần tuần hoàn và từ tuần hoàn tới biến cố cực đoan. Riêng nhóm từ hỗn loạn có hai cơ chế được nêu: khủng hoảng nội tại trong Brusselator và tiếp xúc–trượt trong laser. Vì vậy, không nên diễn đạt thành bốn mô hình cùng minh họa đúng ba cơ chế vật lý đồng nhất. [Mục III–V, tr. 3–10]

| Thành phần kiểm chứng | PDF cung cấp | Giới hạn của bằng chứng hoặc thông tin chưa báo cáo |
| --- | --- | --- |
| Mô hình và can thiệp | Quét một tham số trên bốn mô hình; thêm hai giản đồ hai tham số cho Brusselator và laser | Các mô hình chưa được đặc tả số đầy đủ như đã nêu; không có can thiệp trên hệ đo thực |
| Điều kiện đối chiếu | Tuần hoàn, gần tuần hoàn, hỗn loạn bị giới hạn và dao động lớn thường xuyên | Là các miền đối chiếu nội tại, chưa phải tập đối chứng âm có thiết kế độc lập |
| Cách lấy mẫu | Chia tín hiệu theo những đoạn không chồng lấn và lấy cực đại | Thiếu T, k, tổng số mẫu, bước lấy mẫu và số cực đại dùng tại từng điều kiện |
| Cấu hình mô phỏng | Phương trình và một phần tham số | Thiếu điều kiện đầu, loại bỏ quá độ, bộ tích phân, bước thời gian, dung sai và cách theo nhánh khi quét |
| So sánh thành phần | MRT và ENT gốc so với phương sai tương ứng trong cùng hình | Không chạy chỉ số của tài liệu 28 hoặc một tập phương án đối chiếu rộng trên cùng chuỗi |
| Thước đo đối chiếu | Ngưỡng cực đại; số lần vượt ngưỡng trong giản đồ; tương ứng với biểu đồ phân nhánh | Không có quy tắc phân loại từ phương sai, sai số định vị mốc, độ nhạy phát hiện hoặc tỷ lệ cảnh báo sai |
| Độ nhạy tham số phân tích | Chọn ngưỡng tái diễn 30% độ lệch chuẩn | Không khảo sát thay T, k, m, ngưỡng tái diễn, nhiễu hoặc cách trích cực trị |
| Tín hiệu thay thế | Không báo cáo | Chưa tách ảnh hưởng của thay đổi phân bố, số cực đại và cấu trúc thời gian khỏi tính cực đoan |
| Độ bất định | Các đường chỉ số và giản đồ màu | Không báo cáo số lần chạy độc lập, thanh sai số, khoảng tin cậy hoặc kiểm định thống kê |
| Huấn luyện và kiểm tra | Không có mô hình phải huấn luyện | Không có đánh giá ngoài mẫu hoặc đánh giá dự báo theo thời gian |
| Khả dụng dữ liệu | Tác giả tuyên bố dữ liệu hỗ trợ nằm trong bài | PDF không nêu kho chuỗi thời gian gốc hoặc kho mã; không đồng nghĩa chúng không tồn tại ở nơi khác |

Nguồn: Mục II–V, tr. 2–10; Hình 1–9; phần khả dụng dữ liệu, tr. 10. Độ dài đoạn tín hiệu vẽ ở phụ lục không xác định được tổng lượng dữ liệu đã dùng cho từng điểm phương sai.

## 6. Kết quả và bằng chứng theo từng hình

### 6.1. Hình 1 — Đối chiếu nền trước khi có biến cố cực đoan

Hình 1 dùng quá trình nhân đôi chu kỳ của Brusselator để cho thấy MRT gốc có thể nhận các mức gần hằng khác nhau ở các nhánh tuần hoàn, còn ENT tăng khi vào hỗn loạn. Phương sai được tác giả diễn giải là bằng không hoặc rất nhỏ cho tuần hoàn và dao động nhỏ hơn ở miền hỗn loạn bị giới hạn. Trong hình vẫn có những đỉnh phương sai gần các vùng thay đổi nhánh; không nên biến mô tả định tính đó thành quy tắc chính xác rằng phương sai mọi chuỗi tuần hoàn đều bằng không. [Mục III.A, tr. 3–4; Hình 1, tr. 4]

**Hình kiểm tra điều gì?** Hai thống kê và phương sai của chúng phản ứng ra sao với những chế độ thông thường trước khởi phát cực đoan. **Không chứng minh điều gì?** Phương sai dương là dấu hiệu đặc hiệu cho cực đoan hoặc có thể dùng một ngưỡng duy nhất phân loại mọi chế độ. Hai trục tung của mỗi ô có thang khác nhau; những đỉnh nhỏ cũng cần đọc theo thang của phương sai.

### 6.2. Hình 2 — Bằng chứng chính cho lợi ích của phương sai theo đoạn

Ở Brusselator, MRT gốc tăng từ nền hỗn loạn sang miền cực đoan nhưng vẫn tương đối cao trong miền dao động lớn thường xuyên. Phương sai MRT lại cao ở miền cực đoan và giảm về phía dao động lớn thường xuyên. ENT gốc không tách được toàn bộ miền cực đoan bằng một mức đơn giản; phương sai ENT có dạng miền tăng rõ hơn. [Mục III.B, tr. 4–5; Hình 2, tr. 5]

**Bằng chứng hỗ trợ:** Xét sự biến đổi giữa các đoạn bổ sung thông tin mà chỉ đọc mức của thống kê gốc chưa thể hiện rõ trong ví dụ này. **Không chứng minh:** Mức tăng đã có trước biến cố đầu tiên, phép phân loại đạt một độ chính xác nhất định hoặc hai phương sai tốt hơn chỉ số của Das và cộng sự trên cùng dữ liệu. Mốc khởi phát và vị trí cực đại phương sai cũng không phải cùng một khái niệm. [Hình 2; Mục III.B]

### 6.3. Hình 3 — Mở rộng sang miền hai tham số của Brusselator

Ba ô đối chiếu số lần vượt ngưỡng với hai phương sai trên mặt phẳng I–ω. Các dải có biến cố cực đoan và các dải có phương sai cao tương ứng về mặt hình ảnh. Điều này mở rộng kiểm chứng từ một lát cắt sang một miền tham số. [Mục III.B, tr. 5; Hình 3, tr. 6]

**Giới hạn:** Bài không lượng hóa độ trùng miền bằng một thước đo, không báo cáo tỷ lệ dương tính giả hoặc âm tính giả và không cho một ngưỡng phương sai để dựng lại nhãn. Hai bản đồ chỉ số không trùng khít từng điểm màu trong toàn bộ hình; tương ứng trực quan không đồng nghĩa với hiệu năng phân loại hoàn hảo. Đặc biệt, số đếm và phương sai khác đơn vị và cách định cỡ thang màu. [Hình 3]

### 6.4. Hình 4 — Laser: xu hướng phương sai còn xuất hiện khi cơ chế được mô tả khác

Ở laser CO₂, MRT gốc tăng trong miền biến cố hiếm rồi giảm dần khi đỉnh lớn thường xuyên hơn. ENT gốc khá cao trước khởi phát và giảm qua miền cực đoan. Hai phương sai đều tăng trong miền xuất hiện bùng phát hiếm và thấp hơn ở các miền đối chiếu. [Mục III.C, tr. 6–7; Hình 4, tr. 6]

**Bằng chứng hỗ trợ:** Xu hướng không chỉ xuất hiện trong mô hình phản ứng hóa học. **Không chứng minh:** Một cơ chế tiếp xúc–trượt đã được suy ra từ chính hai phương sai; cơ chế vẫn dựa trên phân tích và tài liệu nguồn mà tác giả dẫn. Việc tái lập đầy đủ còn vướng đặc tả tham số và quy tắc không trơn của mô hình laser. [Mục III.C, tr. 5–6]

### 6.5. Hình 5 — Miền hai tham số của laser

Giản đồ ε–r cho thấy một dải nghiêng có số đếm biến cố và phương sai cao hơn, trong khi miền không có biến cố có mức thấp hơn. Đây là phép đối chiếu hình thái miền giống Hình 3 trên một hệ khác. [Mục III.C, tr. 7; Hình 5]

**Giới hạn:** Không có kiểm định định lượng về mức khớp giữa các bản đồ, cũng không có khảo sát lưới tham số và sai số do chuỗi hữu hạn. Có cấu trúc nền và dao động cục bộ trong bản đồ phương sai; không nên xem màu thấp/cao tự nó là một bộ phân loại đã được hiệu chuẩn. [Hình 5]

### 6.6. Hình 6 — Khởi phát từ dao động gần tuần hoàn

Với SQUID, cần đọc quá trình khởi phát theo chiều giảm γ, từ phải sang trái trên trục ngang. Tác giả báo cáo mốc khoảng 0,0234; phương sai nhỏ trong miền gần tuần hoàn, tăng trong miền bùng phát gián đoạn rồi giảm khi bùng phát lớn thường xuyên. Đường chỉ số có những chỗ lõm, cửa sổ và dao động cục bộ; không phải một hàm đơn điệu trơn trên toàn bộ miền cực đoan. [Mục IV.A, tr. 8; Hình 6]

**Bằng chứng hỗ trợ:** Khảo sát phương sai có thể làm nổi bật miền gián đoạn trên một hệ ghép với nền gần tuần hoàn. **Không chứng minh:** Mốc 0,0234 được ước lượng với sai số xác định, mọi điều kiện đầu đều cho cùng kết quả, hoặc phương sai đã phát hiện được phân nhánh Neimark–Sacker chưa được vẽ. [Mục IV.A; Hình 6]

### 6.7. Hình 7 — Khởi phát từ nền tuần hoàn trong hệ nơron

Gần k = 0,0532, bùng phát lớn xuất hiện từ nền tuần hoàn. MRT gốc **giảm** qua khởi phát, khác với chiều tăng được quan sát trong một số ví dụ khác; ENT gốc tăng. Hai phương sai có bước tăng rồi giảm dần ở phía các bùng phát lớn thường xuyên hơn. Đây là lý do hữu ích để đọc phương sai như mức dao động giữa các đoạn thay vì đòi hỏi MRT trung bình luôn tăng khi có cực đoan. [Mục IV.B, tr. 9; Hình 7]

**Bằng chứng hỗ trợ:** Xu hướng phương sai còn được minh họa cho nền tuần hoàn và quan sát tổng hợp của hai nơron. **Không chứng minh:** Hai chỉ số đã được kiểm chứng trên tín hiệu nơron đo được hoặc có giá trị dự báo lâm sàng. Cách quy cơ chế PM được mô tả và dẫn nguồn, không phải kết luận duy nhất có thể suy từ đường phương sai. [Mục IV.B; Hình 7]

### 6.8. Hình 8–9 — Xác nhận dạng tín hiệu và phân bố biên độ

Phụ lục đặt chuỗi thời gian cạnh **hàm mật độ xác suất** (*probability density function*, viết tắt PDF trên hình) để minh họa các đỉnh hiếm vượt ngưỡng. Hình 8 gồm Brusselator và laser; Hình 9 gồm SQUID và hệ nơron. Các ngưỡng nằm trên đường ngang hoặc đường đứng đứt nét. [Phụ lục, tr. 10–11; Hình 8–9]

**Tác giả khẳng định:** Ba ví dụ đầu có phân bố đuôi nặng, còn hệ nơron có **phân bố với nhóm cực trị ngoại lệ nổi bật ở đuôi** (*dragon-kings-like distribution*), biểu hiện bằng phần gồ ở đuôi. Đây là tên mô tả của bài; không được thay bằng một loại phân bố tham số cụ thể. [Phụ lục, tr. 11]

**Bằng chứng hỗ trợ:** Đồ thị có các cực đại ở xa miền thường gặp, có quan sát vượt ngưỡng và ở hệ nơron có cấu trúc gồ ở phía biên độ lớn. **Không chứng minh:** Tính chất đuôi nặng theo định nghĩa tiệm cận, quy luật lũy thừa, tính tối ưu của ngưỡng hoặc kiểm định thống kê cho một lớp cực trị ngoại lệ. Bài không báo cáo khớp đuôi, mô hình phân bố đối chiếu hay khoảng bất định của xác suất hiếm. [Hình 8–9; Phụ lục]

## 7. Đóng góp thực sự và giới hạn khái quát

Kết quả đáng giữ lại là **thay mức của một thống kê bằng mức biến động của thống kê đó giữa các đoạn** có thể giúp phân biệt các miền động lực học trong những ví dụ được khảo sát. Đóng góp không nằm ở entropy mới hay công thức phương sai mới, mà ở cách triển khai hai nhánh thống kê hữu hạn theo thời gian và khảo sát sự tương ứng của chúng với biến cố hiếm trên bốn mô hình. [Mục I–V; Hình 1–7]

**Tác giả khẳng định:** Chỉ số độc lập mô hình và nhất quán qua các cơ chế khởi phát. **Bằng chứng hỗ trợ:** Hai phương sai cho xu hướng tương tự trong bốn mô hình và các miền tham số đã trình bày. Không có định lý cho mọi mô hình, chuẩn hóa chung giữa các hệ hoặc kiểm chứng ngoài mẫu để suy ra tính độc lập mô hình theo nghĩa phổ quát. [Mục V, tr. 9–10]

Những tình huống có thể làm phương pháp không đạt mục đích dưới đây là **suy luận của người phân tích**, chưa phải các phép thử thất bại do bài báo cáo:

- **Cửa sổ không phù hợp với thang bùng phát.** T thay đổi có thể làm số đoạn chứa biến cố đổi mạnh, làm trộn nền và bùng phát hoặc gây thiếu cực đại; không có một giá trị T được chứng minh phù hợp chung. [Quy trình Mục II; giải thích thống kê ở Mục 4.6 của bản phân tích]
- **Biến động không do cực đoan.** Trôi nền, thay đổi chế độ không có biến cố lớn, nhiễu hoặc thay đổi số cực đại cũng có thể tạo phương sai giữa các đoạn; thiếu đối chứng âm nên chưa xác lập tính đặc hiệu. [Phương trình (4); thiết kế Mục III–IV]
- **Sai khác độ dài dãy cực đại.** Các đoạn có cùng thời lượng có thể có số cực đại khác nhau; sai số ước lượng ENT và MRT có thể thay đổi theo số cực đại. Bài chưa tách phần dao động ước lượng khỏi phần thay đổi động lực học. [Mục II, tr. 2–3]
- **Tái chuẩn hóa ngầm theo từng đoạn.** Miền chia biên độ thay đổi cho ENT, còn phạm vi tính độ lệch chuẩn để đặt ngưỡng RP chưa rõ. Một phần kết quả có thể phụ thuộc quy tắc tiền xử lý, không chỉ vào sự hiện diện của đỉnh hiếm. [Mục II.A–B]
- **Không thể quy cơ chế chỉ từ một phương sai cao.** Khủng hoảng, gián đoạn hoặc tiếp xúc–trượt được nêu từ hiểu biết mô hình và các nguồn được dẫn; cùng một mức phương sai có thể xuất hiện vì nhiều nguyên nhân. [Mục III–V]
- **Thông tin thời gian được giữ có chọn lọc.** MRT sử dụng cấu trúc tái diễn theo thứ tự cực đại, còn ENT trong đoạn chỉ dùng phân bố biên độ. Bản thân phép lấy phương sai không giữ thứ tự của các giá trị thống kê giữa các đoạn; đảo thứ tự những đoạn đã phân tích sẽ giữ hai phương sai. Điều đó chưa đủ để mô tả tính tụ cụm hoặc định vị lần bùng phát kế tiếp. [Suy ra từ Phương trình (1)–(4)]

### Khả năng chuyển sang tín hiệu y sinh

**Giả thuyết mở rộng, chưa được kiểm chứng:** Có thể khảo sát hai phương sai trên các đặc trưng cực trị của điện não đồ (*electroencephalography*, EEG), điện tâm đồ (*electrocardiography*, ECG) hoặc tín hiệu quang thể tích (*photoplethysmography*, PPG). Câu hỏi có ý nghĩa là các thống kê theo đoạn có phản ánh sự xen kẽ giữa nền và các đợt bất thường hay chủ yếu phản ánh nhiễu, số đỉnh và cách chọn cửa sổ.

Mô hình Hindmarsh–Rose trong bài là bằng chứng mô phỏng hệ động lực, không phải dữ liệu EEG hoặc kiểm chứng bệnh nhân. Không mặc định một biến cố y sinh bắt nguồn từ các cơ chế phân nhánh được chọn trong bài hoặc từ chậm dần tới hạn. Việc chuyển giao cần xác định cực trị có ý nghĩa sinh lý, kiểm soát nhiễu đo, có nhãn độc lập và đánh giá theo người bệnh hoặc phiên đo. [Phạm vi kiểm chứng Mục IV.B, tr. 8–9; phần mở rộng do người phân tích đề xuất]

Nếu mục tiêu là cảnh báo sớm, phương sai chỉ được tính từ các đoạn đã quan sát trước mốc dự báo; phải định nghĩa thời gian báo trước và đánh giá cảnh báo sai trên dữ liệu chưa dùng để chọn tham số. Đây là yêu cầu của một thiết kế nghiên cứu mới, chưa phải khả năng đã được chứng minh và chưa phải khoảng trống y sinh đã xác lập qua tổng quan lĩnh vực.

## 8. Hồ sơ phương pháp (Methodological Fingerprint)

| Trường | Hồ sơ của nghiên cứu |
| --- | --- |
| **Bài toán (Problem)** | Phân biệt chế độ có bùng phát lớn hiếm gặp với dao động nền và dao động lớn thường xuyên; nhận diện miền chuyển tiếp theo tham số. [Mục I] |
| **Đầu vào (Input)** | Một chuỗi quan sát một chiều cho mỗi điều kiện, chia thành k đoạn không chồng lấn; trích dãy cực đại của mỗi đoạn. [Mục II] |
| **Thông tin biết trước (Known information)** | Biến quan sát, độ dài đoạn, số khoảng chia, quy tắc RP và cực trị; khi kiểm chứng còn biết tham số điều khiển và ngưỡng đối chiếu. Một số cấu hình chưa được báo cáo. [Mục II–IV] |
| **Đầu ra (Output)** | Phương sai MRT và phương sai ENT giữa các đoạn; đường hoặc giản đồ chỉ số theo tham số, chưa phải dự báo thời điểm hay biên độ biến cố. [Phương trình (4); Hình 1–7] |
| **Phương án đối chiếu (Existing baseline)** | MRT và ENT gốc; biểu đồ phân nhánh và số đếm vượt ngưỡng làm tham chiếu. Không chạy chỉ số entropy–độ lệch của tài liệu 28 trên cùng chuỗi. [Mục I, III; Hình 1–7] |
| **Thành phần mới (New component)** | Mở rộng khảo sát phương sai theo đoạn sang chuyển tiếp từ hỗn loạn, bổ sung nhánh phương sai ENT và kiểm chứng trên bốn mô hình; phương sai MRT đã có tiền lệ ở tài liệu 27. [Mục I–V] |
| **Giả định (Assumptions)** | Dữ liệu đủ dài và đủ cực đại; cách chia đoạn làm lộ sự khác biệt giữa nền với bùng phát; quy tắc ngưỡng và thống kê nhất quán; miền vượt ngưỡng là tham chiếu có ý nghĩa. Đây là điều kiện của cách diễn giải, chưa được kiểm tra độ nhạy đầy đủ. [Mục II–IV] |
| **Kiểm chứng (Validation)** | Quét một tham số trên bốn hệ, thêm hai giản đồ hai tham số cho Brusselator và laser; đối chiếu chuỗi và phân bố trong phụ lục. [Hình 1–9] |
| **Kết quả chính (Main finding)** | Hai phương sai thường cao trong miền bùng phát lớn hiếm và thấp hơn ở các chế độ đối chiếu trong những ví dụ đã vẽ; thống kê gốc riêng lẻ chưa phân biệt rõ mọi miền. [Mục III–V] |
| **Câu hỏi còn mở (Unresolved questions)** | Cấu hình T, k, m; ngưỡng RP; tính đặc hiệu, độ bất định, độ nhạy với nhiễu và độ dài chuỗi; tham số mô hình còn thiếu; quy tắc phân loại và dự báo ngoài mẫu. [Mục II–IV] |
| **Khả năng tái lập (Reproduction feasibility)** | Có thể viết khung tính toán, nhưng chưa tái tạo duy nhất các hình từ PDF: thiếu cấu hình phân tích, dữ liệu gốc và nhiều giá trị mô hình. Chưa chạy tái lập ở bước này. [Mục II–IV; khả dụng dữ liệu, tr. 10] |

## 9. Tài liệu đọc tiếp và quyết định tái lập

### 9.1. Phần cần chốt trước tiên

Ưu tiên **Mục II, tr. 2–3** để xác định T, k, m, phạm vi tính độ lệch chuẩn đặt ngưỡng RP, cách xử lý vệt trắng và cách tổng hợp đường chỉ số gốc. Sau đó đối chiếu **Hình 1–2 và Phương trình (5)** để chọn Brusselator làm trường hợp tái lập ban đầu. Phương trình và tham số của hệ này được mô tả đầy đủ hơn ba hệ còn lại; vẫn cần chốt biến x trong hình tương ứng với biến nào của phương trình.

Với laser, cần làm rõ ánh xạ ký hiệu η, ζ, hệ số k và quy tắc động lực học không trơn. Với SQUID, cần các giá trị số còn thiếu của ghép từ và cưỡng bức. Với hệ nơron, cần r, s, I và tập mẫu tính ngưỡng. Không thay thế các thông tin này bằng cấu hình từ nghiên cứu đã đọc trước mà không kiểm tra. [Mục III.C–IV.B, tr. 5–9]

### 9.2. Tài liệu đọc tiếp từ danh mục của bài

Các nguồn sau **chưa được truy cập trong bước này**. Nhan đề tiếng Anh được giữ để nhận diện, kèm bản dịch hoặc diễn giải tiếng Việt; thông tin thư mục lấy từ tr. 11–12 của PDF.

| Nguồn được bài dẫn | Mục đích đọc tiếp |
| --- | --- |
| S. Vinoth và cộng sự (2025), *Extreme events in gene regulatory networks with time-delays* — “Biến cố cực đoan trong mạng điều hòa gen có trễ”, *Sci. Rep.* **15**, 13064, tài liệu 27 | Xác định chính xác phần phương sai MRT đã có và giới hạn mà bài hiện tại muốn mở rộng |
| D. Das và cộng sự (2024), *Complexity measure of extreme events* — “Thước đo độ phức tạp của biến cố cực đoan”, *Chaos* **34**, 121104, tài liệu 28 | Kiểm tra căn cứ của tuyên bố khắc phục hạn chế và thiết kế so sánh trên cùng chuỗi |
| S. Schinkel, O. Dimigen và N. Marwan (2008), *Selection of recurrence threshold for signal detection* — “Chọn ngưỡng tái diễn để phát hiện tín hiệu”, *Eur. Phys. J. Spec. Top.* **164**, 45–53, tài liệu 33 | Kiểm tra căn cứ chọn ngưỡng theo độ lệch chuẩn, tránh coi 30% là một hằng số phổ quát |
| E. Ngamga và cộng sự (2007), *Recurrence analysis of strange nonchaotic dynamics* — “Phân tích tái diễn của động lực kỳ dị nhưng không hỗn loạn”, *Phys. Rev. E* **75**, 036222, tài liệu 35 | Làm rõ quy ước vệt trắng và thời gian tái diễn được kế thừa |
| P. Gray, S. K. Scott và J. H. Merkin (1988), *The Brusselator model of oscillatory reactions. Relationships between two-variable and four-variable models with rigorous application of mass conservation and detailed balance* — “Mô hình Brusselator của phản ứng dao động: quan hệ giữa mô hình hai và bốn biến với bảo toàn khối lượng và cân bằng chi tiết”, *J. Chem. Soc., Faraday Trans. 1* **84**, 993–1011, tài liệu 37 | Kiểm tra đặc tả mô hình phản ứng làm trường hợp tái lập nền |
| S. L. Kingston (2024), *Grazing-sliding bifurcation induced extreme large-intensity pulses in CO₂ laser* — “Xung cường độ rất lớn do phân nhánh tiếp xúc–trượt trong laser CO₂”, *Eur. Phys. J. Plus* **139**, 447, tài liệu 30 | Làm rõ quy tắc không trơn và tham số của hệ laser |
| S. Dinesh Vijay và cộng sự (2024), *Extreme events in SQUID trimer* — “Biến cố cực đoan trong bộ ba thiết bị SQUID”, *Appl. Phys. Lett.* **125**, 014101, tài liệu 20 | Tìm cấu hình số và diễn giải chuyển tiếp gần tuần hoàn của hệ siêu dẫn |
| S. Leo Kingston và cộng sự (2023), *Impact of time varying interaction: Formation and annihilation of extreme events in dynamical systems* — “Ảnh hưởng của tương tác biến thiên theo thời gian tới sự hình thành và triệt tiêu biến cố cực đoan”, *Chaos* **33**, 123134, tài liệu 32 | Đối chiếu nguồn mô hình nơron và các giá trị số chưa nêu trong bài hiện tại |

Các mục đích đọc ở cột phải không phải tóm tắt kết quả của những nguồn đã được đọc độc lập.

### 9.3. Quyết định tái lập

**Lựa chọn: ứng viên tái lập (Reproduction candidate), có điều kiện.** Điểm hấp dẫn là giả thuyết thống kê rõ, hai nhánh chỉ số có thể triển khai và có các hình mục tiêu để đối chiếu. Rào cản lớn nhất không phải công thức phương sai mà là thiếu đặc tả phân đoạn và số liệu đầu vào. Chưa đủ cơ sở chọn đây làm phương pháp nền tảng cho dự báo biến cố hoặc ứng dụng lâm sàng. [Mục II–V]

**Lộ trình đề xuất, chưa thực hiện:** Chốt quy ước phân tích trước, rồi tái lập Brusselator ở ba loại chế độ và kiểm tra Hình 1–2. Nếu chọn một biến u làm x, phải ghi rõ đó là giả định triển khai cho tới khi xác minh nguồn. Sau khi xu hướng cơ bản được tái tạo, thay độ dài đoạn, số cực đại và ngưỡng RP; đối chiếu phương sai với chỉ số gốc và một thước đo đuôi trên cùng chuỗi. Mục tiêu là xác định liệu tăng phương sai phản ánh động lực bùng phát hay sai số ước lượng và quy tắc tiền xử lý.

Thông tin còn cần để tái lập chính xác gồm cấu hình T, k, m; toàn bộ chuỗi hoặc mã tạo chuỗi; bước tích phân, điều kiện đầu và phần quá độ; quy ước tái diễn; lưới tham số; cách tính và chọn ngưỡng cực đoan; các hằng số mô hình còn thiếu. Phần khả dụng dữ liệu viết rằng dữ liệu hỗ trợ nằm trong bài, nhưng PDF không nêu liên kết tới mã hay chuỗi thời gian gốc. Không đồng nhất việc có hình kết quả với việc đã có đủ dữ liệu số để tái lập. [Mục II–IV; phần khả dụng dữ liệu, tr. 10]

Phân tích này chưa chạy mô phỏng, chưa cài đặt thử các chỉ số trên dữ liệu, chưa liên hệ tác giả và chưa truy cập nguồn ngoài.

## 10. Ghi nhận kiểm tra bản phân tích

- Đã đọc toàn bộ 13 trang PDF, gồm phụ lục và danh mục tài liệu; đối chiếu trực quan Hình 1–9, công thức MRT, entropy, phương sai và Phương trình (5)–(8). Đã giữ các chi tiết chưa rõ của nguồn thay vì tự sửa mô hình.
- Đã rà soát tiếng Việt, thuật ngữ và viết tắt; phân biệt lời tác giả, bằng chứng và suy luận. Hồ sơ có đủ 11 trường và quyết định tái lập có điều kiện.
- Đã kiểm tra tệp lưu trên đĩa về dấu phân cách toán, ngoặc nhọn, môi trường nhiều dòng và ký tự điều khiển. Môi trường chưa có trình xem Markdown hỗ trợ toán sẵn dùng để xem toàn bộ công thức; xác nhận ở mức đối chiếu nội dung và cú pháp, không tuyên bố đã kiểm tra hiển thị bằng MathJax/KaTeX.
