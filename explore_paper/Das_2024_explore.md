# Das và cộng sự (2024) — Đo độ phức tạp của biến cố cực đoan

**Tên bài báo:** *Complexity measure of extreme events* — “Thước đo độ phức tạp của biến cố cực đoan”.

**Tác giả:** Dhiman Das, Arnob Ray, Chittaranjan Hens, Dibakar Ghosh, Md. Kamrul Hassan, Artur Dabrowski, Tomasz Kapitaniak và Syamal K. Dana. **Công bố:** *Chaos* **34**, 121104 (2024), công bố trực tuyến ngày 2/12/2024. **DOI:** [10.1063/5.0232645](https://doi.org/10.1063/5.0232645).

**Phạm vi nguồn và quy ước trang:** Chỉ sử dụng [PDF được chỉ định](<../paper/11 Complexity measure of extreme events.pdf>), đã đọc toàn bộ 10 trang PDF, gồm bìa, nội dung, hai phụ lục và danh mục tài liệu; đã đối chiếu trực quan các công thức trọng tâm và Hình 1–6. Không sử dụng web hay đọc các tài liệu được bài báo dẫn. Trong phân tích này, “tr. 1–9” chỉ trang bài báo 121104-1 đến 121104-9, tương ứng trang PDF 2–10; trang PDF 1 là bìa. Dấu thời gian tải năm 2026 trên bản PDF không phải năm công bố.

Bài báo đặt câu hỏi: có thể phân biệt hỗn loạn chứa những biến cố biên độ lớn hiếm gặp với hỗn loạn không có biến cố cực đoan bằng một đại lượng độ phức tạp hay không? Ý tưởng là tính entropy Shannon trên phân bố biên độ các cực trị, kết hợp với độ lệch của chính phân bố đó khỏi phân bố đều. Kết quả chính là sự tương ứng giữa biến đổi của tích hai đại lượng và sự xuất hiện biến cố cực đoan khi quét tham số của ba mô hình. Đây là nghiên cứu mô tả và nhận diện chế độ động lực học hồi cứu, chưa phải phương pháp dự báo thời điểm hay độ lớn của biến cố tương lai. [Tóm tắt, tr. 1; Mục I–III, tr. 2–6]

## 1. Bài toán, động cơ và giới hạn mà nghiên cứu muốn giải quyết

Biến cố cực đoan được tác giả mô tả là độ lệch biên độ lớn, xuất hiện không thường xuyên và tồn tại ngắn so với hành vi thông thường dài hạn. Bối cảnh được nêu trải từ sóng biển, khí hậu, kinh tế đến laser và mạch điện tử. Tuy nhiên, dữ liệu trực tiếp của nghiên cứu này đều được sinh bằng mô phỏng; các ứng dụng thực tế là động cơ, không phải những bộ dữ liệu đã được kiểm chứng trong bài. [Mục I, tr. 1–2; Mục III, tr. 3–6]

Các đại lượng như số mũ Lyapunov, chiều fractal và entropy đã được dùng để đặc trưng hỗn loạn. Tác giả tập trung vào một phân biệt tinh hơn: một tín hiệu có thể đã hỗn loạn ở biên độ nhỏ nhưng đôi lúc xuất hiện các chuyến đi xa của quỹ đạo, tạo đỉnh lớn hiếm gặp; khi các đỉnh lớn trở nên thường xuyên, tác giả lại gọi chế độ đó là hỗn loạn biên độ lớn không cực đoan. Vì vậy, “cực đoan” ở đây liên quan cả biên độ tương đối và sự hiếm gặp, không đồng nghĩa với mọi dao động biên độ lớn. [Mục I, tr. 2; Mục III.A–B, tr. 4–5; Hình 2, 4]

**Tác giả khẳng định (Authors claim):** Các nghiên cứu được dẫn trước đó chủ yếu phân biệt tuần hoàn với hỗn loạn hoặc hỗn loạn biên độ nhỏ với biên độ lớn, chưa xử lý độ phức tạp của các biến cố lớn hiếm gặp. **Entropy hoán vị** (*permutation entropy*, PE) dựa trên thứ tự tương đối nên làm mất thông tin về độ lớn của những biến cố này; entropy Shannon tính từ biên độ được chọn để giữ chúng trong phân bố xác suất. [Mục I, tr. 2; Mục IV, tr. 7; Phụ lục A, tr. 8]

**Bằng chứng hỗ trợ (Evidence supports):** Hình 1 đối chiếu trực tiếp entropy Shannon chuẩn hóa, độ lệch khỏi phân bố đều và tích của chúng trong hai cơ chế chuyển tiếp của cùng một mô hình. Bài không tính PE trên cùng các chuỗi để so sánh hiệu năng, cũng không báo cáo một đánh giá có hệ thống với các phương án khác. Nhận định về ưu thế so với PE vì vậy chủ yếu dựa trên lập luận biểu diễn và cách tác giả diễn giải công trình trước, không phải một phép so sánh thực nghiệm tương đương. [Hình 1, tr. 4; Mục I, tr. 2]

**Diễn giải của người phân tích (Analyst interpretation):** Câu hỏi phương pháp luận phù hợp nhất là: phân bố biên độ các cực trị có thay đổi theo một cách giúp nhận diện chế độ chứa biến cố cực đoan trong những mô hình này không? Không nên mở rộng câu hỏi thành “đã tìm ra thước đo duy nhất của độ phức tạp” hoặc “đã giải quyết dự báo biến cố cực đoan”; chính tác giả nhấn mạnh tính định tính của kết quả. [Mục III, tr. 3; Mục IV, tr. 7]

## 2. Đầu vào, thông tin biết trước và đầu ra

Một phép tính độ phức tạp dùng **một chuỗi cực trị biên độ tại một giá trị tham số cố định**. Để tái tạo kết quả chính của bài, cần **nhiều chuỗi**, mỗi chuỗi gắn với giá trị tham số điều khiển đã biết; sau đó so sánh đường độ phức tạp với biểu đồ phân nhánh và ngưỡng cực đoan. Không có tập nhãn lâm sàng hoặc dữ liệu huấn luyện cho một mô hình học máy. [Mục II–III, tr. 3; Hình 1, 3, 5]

| Thành phần                               | Nội dung trong bài                                                                                                                                                      |
| ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Tín hiệu quan sát                       | Biến y của hệ Liénard; biến y của ánh xạ Ikeda; tổng hai biến x của hệ Hindmarsh–Rose                                                                        |
| Chuỗi đưa vào thống kê               | Cực đại địa phương của y trong Liénard; cực tiểu địa phương của y trong Ikeda; cực đại địa phương của tổng hai biến x trong hệ Hindmarsh–Rose |
| Thông tin biết trước để kiểm chứng | Phương trình mô hình, các tham số cố định, tham số đang quét và các cơ chế chuyển tiếp mà tác giả dẫn từ nghiên cứu trước                     |
| Lựa chọn phân tích                     | Số khoảng chia biên độ m; hướng cực trị; ngưỡng tham chiếu để đánh dấu biến cố cực đoan                                                              |
| Đầu ra tại một điều kiện            | Entropy Shannon chuẩn hóa S, độ lệch khỏi phân bố đều D và độ phức tạp C                                                                                   |
| Đầu ra khi quét tham số                | Đường S, D, C theo tham số; nhận diện trực quan sự thay đổi chế độ và vị trí khởi phát tương ứng với biểu đồ phân nhánh                        |

Nguồn: Mục II–III.C, tr. 3–6; Phương trình (1)–(10); Hình 1–5. Mặc dù phần mở đầu Mục III nói chung về cực đại, ví dụ Ikeda thực tế sử dụng cực tiểu; lựa chọn đó phải được giữ khi tái lập.

Phép tính S, D, C tự nó không cần biết phương trình chuyển động hay tham số điều khiển. Những thông tin này cần cho thiết kế mô phỏng và diễn giải đường C theo tham số trong nghiên cứu. Ngưỡng cực đoan không đi vào công thức C, nhưng được dùng để đối chiếu xem chế độ nào được gọi là cực đoan. [Mục II–III, tr. 3]

Cần phân biệt bốn mức đầu ra:

1. **Mô tả động lực học:** đặc trưng phân bố biên độ ở từng chế độ; đây là phần được thực hiện trực tiếp.
2. **Nhận diện hồi cứu:** quan sát C đổi khi các biến cố lớn đã có trong chuỗi; có bằng chứng minh họa qua Hình 1–5.
3. **Định vị điểm chuyển tiếp trong không gian tham số:** sự thay đổi của C tương ứng với mốc phân nhánh trong các ví dụ, nhưng bài chưa đưa thuật toán chọn điểm tự động, sai số ước lượng hoặc khoảng bất định.
4. **Dự báo trước một biến cố:** dự đoán thời điểm hoặc biên độ tương lai từ dữ liệu quá khứ; bài không kiểm chứng mức này, không báo cáo thời gian báo trước, tỷ lệ cảnh báo sai hoặc kết quả ngoài mẫu.

Phân biệt trên dựa vào quy trình quét tham số ở Mục I–III, tr. 2–6. “Tăng khi khởi phát” không tự đồng nghĩa với “tăng đủ sớm trước khi khởi phát”.

## 3. Nguồn gốc phương pháp và đóng góp có thể xác định

| Thành phần                                                          | Nguồn được chính bài báo dẫn                               | Vai trò và phạm vi tính mới                                                                                                        |
| --------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------- |
| Entropy Shannon                                                       | Shannon, tài liệu 32 và 37; Mục II                             | Công cụ kế thừa để đo mức phân tán xác suất                                                                                 |
| Chuẩn hóa theo entropy của phân bố đều                         | Phương trình (1); Phụ lục A                                   | Đưa entropy về thang chuẩn hóa theo số khoảng chia; bài không chứng minh đây là phép chuẩn hóa mới                     |
| Độ lệch khỏi phân bố đều bằng tổng bình phương sai khác | Tài liệu 46, 59, 60; Phương trình (2)                         | Công cụ kế thừa; tác giả gọi là khoảng cách Euclid, còn biểu thức sử dụng bình phương khoảng cách, không lấy căn |
| Tích entropy và độ lệch khỏi phân bố đều                    | Lopez-Ruiz, Mancini và Calbet, tài liệu 46; Phương trình (3) | Có tiền lệ được dẫn ngay khi định nghĩa; không thể coi phép nhân hai đại lượng là phát minh của bài               |
| Giữ thông tin biên độ bằng phân bố của toàn bộ cực trị   | Mục I–II; Phụ lục A                                            | Lựa chọn biểu diễn được nhấn mạnh cho bài toán biến cố lớn hiếm gặp                                                     |
| Quét tham số và diễn giải dạng tăng–đạt đỉnh–giảm       | Mục III–IV; Hình 1–6                                           | Đóng góp chính của công trình: khảo sát và diễn giải chỉ số kế thừa trong ba mô hình có biến cố cực đoan         |

Nguồn: Mục I–II, tr. 2–3; Mục IV, tr. 7; danh mục tài liệu 32, 37, 46, 59–60, tr. 9. Các tài liệu này chỉ được nhận diện từ PDF hiện tại, chưa được đọc độc lập.

Điểm đáng chú ý không nằm ở một hàm mục tiêu cần tối ưu hay một mô hình phải huấn luyện. Đây là một **thống kê của phân bố biên độ**, được đánh giá bằng sự tương ứng với các chế độ động lực học. Tính mới nên phát biểu ở mức áp dụng và diễn giải đó; tuyên bố ưu tiên tuyệt đối cần tổng quan tài liệu ngoài phạm vi Prompt 01. [Phương trình (1)–(3), tr. 3; Mục IV, tr. 7]

## 4. Tái dựng quy trình từ chuỗi thời gian đến độ phức tạp

### 4.1. Trích cực trị và xây dựng phân bố biên độ

Tại mỗi điều kiện tham số, sinh một chuỗi đủ dài rồi lấy các cực đại hoặc cực tiểu địa phương theo biến quan sát đã chọn. Để tránh nhầm với biến trạng thái x của mô hình, bản phân tích gọi chuỗi cực trị là a; đây chỉ là đổi ký hiệu so với dãy x ở Mục II:

$$
\{a_k\}_{k=1}^{n},\qquad
\Delta a=\frac{a_{\max}-a_{\min}}{m},\qquad
p_i=\frac{n_i}{n},\qquad
\sum_{i=1}^{m}p_i=1.
$$

Ở đây n là số cực trị đã thu được, m là số khoảng chia biên độ bằng nhau, Δa là độ rộng mỗi khoảng, còn nᵢ là số cực trị nằm trong khoảng thứ i. Các biên được xác định từ giá trị nhỏ nhất và lớn nhất của chính dãy đang phân tích. Công thức trên diễn đạt lại quy trình bằng lời của Mục II, tr. 3 và Phụ lục A, tr. 8; không phải một phương trình mới do tác giả đánh số. Bài dùng m = 50 trong kết quả chính.

Cách làm này đưa cả các cực trị lớn hiếm gặp vào tần suất của những khoảng ở xa miền biên độ thường gặp. Tuy nhiên, **đưa mọi cực trị vào thống kê không đồng nghĩa bảo toàn toàn bộ thông tin của tín hiệu**: phép chia khoảng bỏ chi tiết biên độ bên trong từng khoảng, còn S, D, C không sử dụng thứ tự xuất hiện hay khoảng thời gian giữa các cực trị. Nhận xét sau là suy ra từ định nghĩa, không phải kết quả thử nghiệm bổ sung của bài. [Mục II, tr. 3; Phương trình (1)–(3); Phụ lục A, tr. 8]

PDF không cho quy tắc tìm cực trị khi có nhiễu, cách xử lý đỉnh bằng nhau, khoảng cách tối thiểu giữa các đỉnh hay quy ước gán giá trị nằm đúng biên. Nếu tất cả cực trị bằng nhau, công thức độ rộng cho giá trị không; Phụ lục A minh họa phân bố dồn vào một khoảng nhưng không cung cấp mã xử lý trường hợp suy biến này. [Mục II, tr. 3; Phụ lục A, tr. 7–8]

### 4.2. Entropy Shannon chuẩn hóa

$$
H=-\sum_{i=1}^{m}p_i\log_{2}p_i,\qquad
H_{\max}=\log_{2}m,\qquad
S=\frac{H}{H_{\max}}
=-\frac{1}{\log_{2}m}\sum_{i=1}^{m}p_i\log_{2}p_i.
$$

H là entropy của phân bố cực trị, tính theo bit; entropy cực đại ứng với xác suất bằng nhau ở tất cả m khoảng. S là entropy đã chuẩn hóa, thuộc đoạn từ 0 đến 1. Đây là định nghĩa H và Phương trình (1), Mục II, tr. 3. Phụ lục A, tr. 7–8 minh họa S bằng 1 với bảy giá trị đồng xác suất và bằng 0 với dãy hằng; đóng góp của khoảng có xác suất bằng 0 được hiểu theo giới hạn bằng 0.

S ở đây là entropy của **phân bố biên độ**, không phải tốc độ sinh thông tin theo thời gian hay entropy Kolmogorov–Sinai. S dương chỉ cho biết xác suất trải trên nhiều khoảng; riêng điều đó không xác nhận tín hiệu hỗn loạn. Đây là giới hạn suy ra từ định nghĩa, cần giữ khi diễn giải từ “mất trật tự” mà tác giả dùng. [Mục I–II, tr. 2–3]

### 4.3. Độ lệch khỏi phân bố đều

$$
D=\frac{m}{m-1}\sum_{i=1}^{m}
\left(p_i-\frac{1}{m}\right)^{2}.
$$

D đo mức tập trung xác suất so với phân bố đều, tức **độ mất cân bằng phân bố** (*disequilibrium*). Hệ số chuẩn hóa đưa D về 1 khi toàn bộ xác suất nằm trong một khoảng; D bằng 0 khi các khoảng đồng xác suất. Đây là Phương trình (2), Mục II, tr. 3. Trong toàn bản phân tích, “độ lệch khỏi phân bố đều” chỉ đại lượng D này; không hàm ý hệ vật lý đã được chứng minh ở xa cân bằng nhiệt động lực học.

D là tổng bình phương sai khác xác suất đã chuẩn hóa. Không được thêm căn bậc hai vì tên gọi “khoảng cách Euclid”, cũng không thay bằng độ phân kỳ Jensen–Shannon vốn chỉ xuất hiện trong tổng quan các phương pháp khác. [Mục I–II, tr. 2–3]

### 4.4. Kết hợp thành độ phức tạp

$$
C=S\,D
=\left(-\frac{1}{\log_{2}m}
\sum_{i=1}^{m}p_i\log_{2}p_i\right)
\left(\frac{m}{m-1}\sum_{i=1}^{m}
\left(p_i-\frac{1}{m}\right)^{2}\right).
$$

C là tích của S và D, đúng Phương trình (3), Mục II, tr. 3. Không có bước khớp hệ số, tối ưu hàm mất mát hay học tham số trong công thức. m là lựa chọn phân tích, không phải một đại lượng được huấn luyện.

Ở hai giới hạn, C đều bằng 0: phân bố dồn vào một khoảng có S bằng 0; phân bố đều có D bằng 0. C có thể dương khi vừa có sự phân tán vừa có sự không đồng đều. Chuẩn hóa riêng S và D không có nghĩa C chắc chắn đạt 1, và tác giả không cung cấp một ngưỡng C chung để phân loại mọi hệ. [Phương trình (1)–(3), tr. 3; Mục III và IV, tr. 3, 7]

**Diễn giải của người phân tích:** Sau một chuyển tiếp làm mở rộng miền biên độ, nhiều cực trị thông thường có thể tập trung trong một phần của miền mới, trong khi một số ít cực trị lớn nằm ở xa. S và D có thể phản ứng ngược chiều, còn tích của chúng có thể tăng. Đây là cách hiểu phù hợp với Hình 1, không phải một định lý bảo đảm C luôn tăng với mọi phân bố có đuôi hiếm. Bài chưa có thí nghiệm tách riêng ảnh hưởng của việc miền chia khoảng mở rộng và ảnh hưởng của xác suất biến cố. [Hình 1(c)–(f), tr. 4; Mục II, tr. 3]

### 4.5. Ngưỡng đánh dấu biến cố cực đoan và đối chiếu theo tham số

$$
T=\mu\pm d_{T}\sigma,\qquad d_{T}\in[4,8].
$$

T là ngưỡng biên độ tham chiếu, μ là trung bình và σ là độ lệch chuẩn. Ký hiệu d có chỉ số T là cách bản phân tích phân biệt hệ số ngưỡng với tham số d trong mô hình nơron; PDF gọi cả hai là d. Tác giả cho biết hệ số ngưỡng được chọn tùy ý trong khoảng 4–8. Dùng dấu cộng và xét vượt lên đối với cực đại; dùng dấu trừ và xét vượt xuống đối với cực tiểu. [Mục III, tr. 3]

Hệ Liénard dùng ngưỡng cộng sáu lần độ lệch chuẩn; Ikeda dùng ngưỡng trừ năm lần độ lệch chuẩn. Mục III.C và chú thích Hình 5 không nêu riêng giá trị hệ số ngưỡng của hệ Hindmarsh–Rose. Định nghĩa chung viết “trung bình độ cao của chuỗi thời gian”, trong khi quy trình làm việc với cực trị; PDF không mô tả đủ thao tác để xác định không nhập nhằng μ, σ được tính từ toàn bộ mẫu tín hiệu hay từ dãy cực trị trong mọi ví dụ. Đây là chi tiết cần xác minh khi tái lập. [Mục III, tr. 3; Hình 1, tr. 4; Mục III.B–C, tr. 5–6; Hình 5]

Sau khi tính tại từng giá trị tham số, vẽ C cùng biểu đồ phân nhánh và T để đối chiếu. T không nằm trong công thức C: thay hệ số ngưỡng không trực tiếp đổi C của cùng một chuỗi, nhưng có thể đổi việc chuỗi ấy được gắn là “có biến cố cực đoan”. Tính độc lập về công thức vì thế cần phân biệt với tính độc lập của kết luận phân loại. [Phương trình (3); Mục III, tr. 3]

## 5. Thiết kế mô phỏng và các mô hình kiểm chứng

### 5.1. Hệ Liénard có cưỡng bức tuần hoàn

$$
\begin{aligned}
\dot{x}&=y,\\
\dot{y}&=-\alpha xy-\gamma x-\beta x^{3}+F\sin(\omega t).
\end{aligned}
$$

Đây là Phương trình (4), Mục III.A, tr. 3. α điều khiển thành phần tắt dần phi tuyến, β điều khiển thành phần phi tuyến bậc ba; γ liên quan tần số nội tại; F và ω là biên độ, tần số cưỡng bức. Bài cố định α = 0,45; β = 0,50; γ = −0,50; F = 0,2 và quét ω. Quan sát là y, sau đó lấy cực đại địa phương.

Hai miền quét kiểm tra hai cơ chế khác nhau:

- Trong khoảng ω từ 0,642 đến 0,643, tăng ω dẫn từ dao động chu kỳ một sang các đợt bùng phát hỗn loạn gián đoạn tại khoảng 0,642212. Tác giả gọi cơ chế này là **gián đoạn Pomeau–Manneville** (*Pomeau–Manneville intermittency*, PM): các đoạn gần tuần hoàn bị ngắt bởi bùng phát lớn.
- Trong khoảng ω từ 0,727 đến 0,735, phải đọc quá trình khởi phát theo **chiều giảm ω**, từ hỗn loạn biên độ nhỏ sang biến cố lớn ở khoảng 0,73242. Tác giả gọi đây là **khủng hoảng nội tại** (*interior crisis*), sự mở rộng đột ngột của tập hút hỗn loạn.

Nguồn: Mục III.A, tr. 3–5; Hình 1–2; bài dẫn tài liệu 4 và 54 cho diễn giải cơ chế. Không nên đọc cả hai đường theo chiều tăng ω rồi kết luận xu hướng trái ngược.

Đây là phép kiểm tra hữu ích vì cùng một mô hình tạo hai đường đi tới biến cố cực đoan. Tuy nhiên, việc quy cơ chế cho PM hoặc khủng hoảng nội tại dựa một phần vào công trình được dẫn; bài hiện tại không trình bày lại đầy đủ phân tích ổn định hay va chạm với quỹ đạo bất ổn. [Mục III.A, tr. 4]

### 5.2. Ánh xạ Ikeda hai chiều

$$
\begin{aligned}
z_{n+1}&=A+Bz_n\exp\left(\mathrm{i}k-
\frac{\mathrm{i}p}{1+|z_n|^{2}}\right),\\
z_n&=x_n+\mathrm{i}y_n.
\end{aligned}
$$

Đây là Phương trình (5), Mục III.B, tr. 5; chữ i thẳng biểu diễn đơn vị ảo. Mô hình mô tả tiến triển của laser trong một cộng hưởng quang phi tuyến. Bài cũng cho dạng hai chiều thực tương đương:

$$
\begin{aligned}
w_n&=1+x_n^{2}+y_n^{2},\\
x_{n+1}&=A+Bx_n\cos\left(k-\frac{p}{w_n}\right)
-By_n\sin\left(k-\frac{p}{w_n}\right),\\
y_{n+1}&=By_n\cos\left(k-\frac{p}{w_n}\right)
+Bx_n\sin\left(k-\frac{p}{w_n}\right).
\end{aligned}
$$

Đây là Phương trình (6), tr. 5, kèm định nghĩa w trong phần giải thích. A là biên độ laser đầu vào, B là hệ số phản xạ của gương, k và p là các tham số lệch cộng hưởng. Bài cố định A = 0,85; B = 0,9; k = 0,4 và tăng p. Dãy dùng cho phân tích là **cực tiểu địa phương của y**, vì các biến cố lớn xuất hiện theo hướng âm. [Mục III.B, tr. 5; Hình 3–4, tr. 6]

Mốc khủng hoảng được báo cáo là p xấp xỉ 7,26884894. Hình 4 chọn p = 7,265 cho hỗn loạn trước khủng hoảng, 7,275 cho biến cố lớn hiếm gặp và 7,295 cho các biến cố lớn thường xuyên hơn sau khủng hoảng. Số chữ số của mốc p là cách tác giả báo cáo, không phải bằng chứng cho độ chính xác ước lượng tương ứng; bài không cho độ phân giải quét và sai số của mốc. [Mục III.B, tr. 5; Hình 3–4, tr. 6]

### 5.3. Hai nơron Hindmarsh–Rose ghép qua khớp thần kinh

$$
\begin{aligned}
\dot{x}_i&=y_i+bx_i^{2}-ax_i^{3}-z_i+I
-\epsilon(x_i-v_s)\Gamma(x_j),\\
\dot{y}_i&=c-dx_i^{2}-y_i,\\
\dot{z}_i&=r\left[s(x_i-x_R)-z_i\right],\\
\Gamma(x)&=\frac{1}{1+\exp[-\lambda(x-\theta)]},
\qquad i,j\in\{1,2\},\quad i\ne j.
\end{aligned}
$$

Đây là Phương trình (7)–(10), Mục III.C, tr. 5. Mỗi nơron có ba biến, tạo thành hệ ghép sáu chiều; Γ là hàm dạng chữ S của tương tác khớp thần kinh, ε là hệ số ghép. Các hằng số được cho ở tr. 6: a = 1; b = 3; c = 1; d = 5; r = 0,01; s = 5; I = 4; λ = 10. Các giá trị còn lại được viết thành khối để giữ rõ ký hiệu:

$$
x_R=-1.6,\qquad v_s=2.0,\qquad \theta=-0.25.
$$

Giá trị ngưỡng −0,25 được ghi bằng chữ Θ hoa trong phần tham số tr. 6, trong khi hàm Γ ở Phương trình (10) dùng θ thường; ở đây thống nhất θ để chỉ tham số đó. Không thay đổi dấu hay độ lớn. [Phương trình (10), tr. 5; Mục III.C, tr. 6]

Đại lượng quan sát mà tác giả gọi gắn với đa tạp đối pha là:

$$
x_{\parallel}=x_1+x_2.
$$

Bài lấy cực đại địa phương của tổng này và quét ε. Sự xuất hiện bùng phát lớn được diễn giải là các lần quỹ đạo rời vùng đối pha; sau đó những bùng phát trở nên thường xuyên khi giảm ε. Định nghĩa tổng ở trên là một đại lượng quan sát; tự nó không thay thế việc chứng minh cấu trúc bất biến hay độ ổn định của toàn bộ đa tạp trong không gian sáu chiều. [Mục III.C, tr. 6–7; Hình 5]

**Bất nhất cần giữ nguyên khi tái lập:** Văn bản tr. 6 viết hệ số ghép được giả sử “dương” và diễn giải là ghép đẩy/ức chế, nhưng trục ε và chú thích Hình 5 đều dùng giá trị âm, trong đó A = −0,07127 và B = −0,1431. Phương trình (7) vẫn có dấu trừ trước ε. Chưa đủ căn cứ để tự đổi dấu phương trình hoặc đổi dấu các điểm khảo sát. Cần hỏi tác giả hoặc đối chiếu mã nguồn trước khi coi ví dụ này đã được đặc tả nhất quán. [Phương trình (7), tr. 5; Mục III.C và Hình 5, tr. 6]

### 5.4. Các điều kiện kiểm chứng đã có và thông tin còn thiếu

Can thiệp chính là thay đổi một tham số điều khiển trong từng mô hình; những chế độ trước chuyển tiếp và chế độ có biến cố lớn thường xuyên hơn đóng vai trò đối chiếu nội tại. Việc có ba mô hình và hai cơ chế giúp kiểm tra tính lặp lại về định tính. Đây không phải nghiên cứu can thiệp trên hệ sinh học thực hoặc đánh giá dự báo trên tập kiểm tra. [Mục III.A–C, tr. 3–7]

| Nội dung thiết kế                      | Điều PDF cung cấp                                                                                                          | Giới hạn cần giữ khi diễn giải                                                                                                                                     |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Phương trình và tham số              | Ba mô hình, tham số cố định và đại lượng quan sát; các giá trị minh họa trên hình                           | Có bất nhất dấu ε trong hệ Hindmarsh–Rose                                                                                                                         |
| Cách lấy mẫu và thời lượng         | Một số đoạn chuỗi được vẽ với trục thời gian hoặc số vòng lặp                                                 | Không báo cáo đầy đủ bước tích phân, phương pháp và dung sai tích phân, chu kỳ lấy mẫu, số mẫu hoặc số cực trị dùng cho mỗi điểm C         |
| Điều kiện đầu và quá độ          | Mô tả chuỗi được sinh bằng mô phỏng và cần đủ dài                                                               | Không cho đầy đủ điều kiện đầu, thời gian loại quá độ, quy tắc chọn nhánh hay cách nối tiếp điều kiện đầu giữa các giá trị tham số        |
| Lưới tham số                           | Các miền quét và mốc chuyển tiếp điển hình                                                                          | Không báo cáo đầy đủ bước quét và quy tắc chọn mốc; số chữ số được in không thay cho sai số ước lượng                                          |
| So sánh từng thành phần               | Hình 1 vẽ riêng S, D và tích C                                                                                           | Có giá trị như kiểm tra vai trò kết hợp; chưa phải đánh giá hiệu năng có cùng tiêu chí quyết định cho nhiều phương pháp                        |
| Phương án đối chiếu ngoài          | Thảo luận PE và các cách đo độ phức tạp trước đây                                                               | Không báo cáo PE, độ phân kỳ Jensen–Shannon hay phương pháp cảnh báo sớm trên cùng các chuỗi                                                           |
| Độ nhạy số khoảng chia               | m = 25, 50, 75, 100 trong Hình 6                                                                                             | Có kiểm tra này; chưa kiểm tra hệ thống độ dài chuỗi, nhiễu, cách phát hiện cực trị hoặc biên chia khoảng cố định so với biên theo từng chuỗi |
| Chia dữ liệu                            | Không huấn luyện mô hình; không báo cáo chia huấn luyện/kiểm tra                                                   | Không thể suy ra kết quả ngoài mẫu hoặc khả năng khái quát của bộ phân loại                                                                               |
| Tín hiệu thay thế và đối chứng âm | Không báo cáo phép thử với chuỗi thay thế, nhiễu ngẫu nhiên có phân bố phù hợp hoặc hoán vị dãy cực trị | Chưa xác định tính đặc hiệu của C đối với cơ chế động lực học của biến cố cực đoan                                                                |
| Độ bất định                          | Trình bày đường chỉ số, biểu đồ phân nhánh và phân bố biên độ                                               | Không báo cáo số lần chạy độc lập, thanh sai số, khoảng tin cậy hoặc kiểm định thống kê của mức tăng C                                              |
| Dữ liệu và mã                         | Dữ liệu được cung cấp từ tác giả liên hệ khi có yêu cầu hợp lý                                                | PDF không nêu kho dữ liệu hoặc kho mã công khai; không đủ căn cứ kết luận chúng không tồn tại ở nơi khác                                            |

Nguồn: Mục II–III, tr. 3–7; Hình 1–6; Phụ lục B, tr. 8; phần khả dụng dữ liệu, tr. 7. Các chi tiết “không báo cáo” trong bảng là phạm vi của PDF đã đọc. Độ dài đoạn vẽ trên hình không được dùng thay cho độ dài chuỗi thực sự đưa vào thống kê.

## 6. Kết quả: từng hình cho phép kết luận đến đâu?

### 6.1. Hình 1 — Vì sao cần kết hợp S và D?

Đây là hình then chốt cho lập luận phương pháp. Hai hàng trên đối chiếu biểu đồ phân nhánh với S và D; hàng dưới cho C. Trong đường PM, chế độ chu kỳ một có các cực đại bằng nhau nên S bằng 0 và D bằng 1. Khi bùng phát xuất hiện theo chiều tăng ω, S tăng còn D giảm. Trong đường khủng hoảng nội tại, đi theo chiều giảm ω từ hỗn loạn biên độ nhỏ đến biến cố lớn hiếm gặp, S lại giảm đột ngột trong khi D tăng. C tăng tại khởi phát trong cả hai trường hợp. [Hình 1(a)–(f), Mục III.A, tr. 4]

**Bằng chứng hỗ trợ:** Nếu mục tiêu là một chỉ số đổi cùng chiều khi khởi phát trong hai ví dụ này, tích S và D đáp ứng tốt hơn việc chỉ đọc S. C tiếp tục biến đổi, đạt cực đại rồi giảm dần khi những biến cố lớn trở nên thường xuyên. Đối với PM, tác giả nêu rõ không có ranh giới sắc nét khi chuyển từ cực đoan sang hỗn loạn không cực đoan. [Mục III.A, tr. 4]

**Không chứng minh:** C có độ chính xác phân loại cao hơn PE, có một ngưỡng phổ quát hoặc có thể cảnh báo trước lần bùng phát đầu tiên. Hình không cung cấp quy tắc phân loại, thống kê lặp hoặc chỉ tiêu dự báo. Mốc tăng C cũng không nhất thiết trùng vị trí cực đại của C. [Hình 1; Mục III.A, tr. 4]

### 6.2. Hình 2 — Biên độ lớn phải được đặt cùng mức hiếm gặp

Hình này ghép chuỗi y với **hàm mật độ xác suất** (*probability density function*, trong hình viết tắt PDF) của các cực đại trên thang bán lôgarit. Với PM, ω = 0,642236 có các đỉnh hiếm vượt T, còn ω = 0,643 có đỉnh lớn thường xuyên hơn nhưng không vượt ngưỡng trong minh họa. Với khủng hoảng nội tại, hai điểm tương ứng là ω = 0,731693 và 0,73007. [Hình 2(a)–(h), tr. 5; Mục III.A, tr. 4–5]

**Bằng chứng hỗ trợ:** Các chế độ được gọi là cực đoan thực sự có những cực đại hiếm vượt ngưỡng do bài chọn, còn các minh họa không cực đoan không thể hiện đỉnh vượt ngưỡng. Điều này giúp diễn giải vì sao biên độ lớn hơn hoặc xuất hiện nhiều đợt lớn hơn chưa chắc làm C tiếp tục tăng. [Hình 2]

**Không chứng minh:** Đuôi phân bố tuân theo một quy luật lũy thừa, một họ phân bố cực trị cụ thể hay xác suất rủi ro đã được hiệu chuẩn. Bài chỉ trình bày phân bố thực nghiệm trên thang bán lôgarit; không báo cáo phép khớp đuôi, kiểm định phân bố hoặc độ bất định của xác suất biến cố hiếm. Ngưỡng T dựa vào chính mức trung bình và độ phân tán của chuỗi, nên việc không vượt T không đồng nghĩa không có rủi ro biên độ lớn theo một ngưỡng vật lý cố định. [Hình 2; định nghĩa T ở Mục III, tr. 3]

### 6.3. Hình 3 — Kiểm tra cùng ý tưởng trên ánh xạ Ikeda

Biểu đồ cực tiểu của y mở rộng đột ngột về phía âm tại p xấp xỉ 7,26884894; C đồng thời chuyển từ mức thấp sang mức cao hơn. Sau bước nhảy, đường C có một miền gần bằng phẳng hoặc cực đại rộng, rồi giảm khi p tăng thêm. Vì vậy, trường hợp này phù hợp với xu hướng tổng quát của tác giả, nhưng không nên mô tả như một đỉnh nhọn được xác định chính xác. [Hình 3, tr. 6; Mục III.B, tr. 5]

**Bằng chứng hỗ trợ:** Hiện tượng không chỉ xuất hiện trong hệ vi phân Liénard; nó còn có ở một ánh xạ hai chiều và với cực trị theo hướng âm. **Không chứng minh:** Có thể ước lượng mốc khủng hoảng với sai số ở chữ số thập phân cuối được báo cáo, hay một bộ phân loại sử dụng C sẽ giữ cùng độ chính xác giữa hai hệ. [Hình 3; Mục III.B]

### 6.4. Hình 4 — Đối chiếu ba chế độ của Ikeda

Ba chuỗi và ba phân bố tương ứng cho thấy hỗn loạn biên độ nhỏ trước khủng hoảng ở p = 7,265; biến cố âm lớn hiếm gặp ở p = 7,275; và biến cố âm lớn thường xuyên hơn ở p = 7,295. Hình giải thích sự giảm C sau miền cực đại bằng thay đổi tần suất xuất hiện biến cố lớn. [Hình 4(a)–(f), tr. 6; Mục III.B, tr. 5]

**Bằng chứng hỗ trợ:** Đường C có thể được diễn giải cùng thay đổi quan sát được của tín hiệu, thay vì chỉ dựa vào một đường thống kê đơn lẻ. **Không chứng minh:** Quan hệ nhân quả hoặc đơn điệu giữa C và tần suất biến cố trên mọi phân bố. Hình chưa phải thí nghiệm giữ nguyên phần còn lại của phân bố rồi chỉ thay đổi xác suất ở đuôi. [Hình 4; Phương trình (3)]

### 6.5. Hình 5 — Mở rộng sang hệ ghép sáu chiều

Hình ghép biểu đồ phân nhánh của tổng hai biến x, C theo ε và hai cặp chuỗi–phân bố tại A và B. Theo quá trình được tác giả mô tả, giảm ε dẫn tới các bùng phát lớn và sau đó tới bùng phát thường xuyên hơn. C đạt mức cao trong miền khởi phát rồi giảm dần về phía các giá trị ε âm hơn. [Hình 5(a)–(f), tr. 6; Mục III.C, tr. 6–7]

**Bằng chứng hỗ trợ:** Dạng biến đổi của C còn xuất hiện trong một hệ ghép nhiều chiều với một đại lượng quan sát tổng hợp. Tuy nhiên, hai điểm A và B chủ yếu minh họa thay đổi tần suất bùng phát; không nên tự khẳng định điểm B tuyệt đối không còn cực trị vượt T nếu chỉ dựa vào cách tác giả mô tả chúng. [Hình 5(c)–(f); Mục III.C]

**Không chứng minh:** Tính đúng với mọi điều kiện đầu, mọi miền hút hoặc tín hiệu nơron thực. Cũng không giải quyết bất nhất dấu ε đã nêu ở Mục 5.3 của bản phân tích; hình và văn bản không thể đồng thời được dùng như một đặc tả số hoàn toàn nhất quán. [Mục III.C, tr. 6; Hình 5]

### 6.6. Hình 6 và các phụ lục — Độ nhạy với cách chia khoảng

Phụ lục A giải thích entropy cực đại, cực tiểu và cách giữ các cực trị lớn trong những khoảng có xác suất nhỏ. Phụ lục B kiểm tra m = 25, 50, 75, 100 trên hai miền của Liénard, Ikeda và hệ Hindmarsh–Rose. Hình 6 cho thấy vị trí thay đổi chế độ tương tự về mặt trực quan trong phạm vi những lựa chọn này, trong khi giá trị C thay đổi rõ theo m. [Phụ lục A–B, tr. 7–8; Hình 6(a)–(d), tr. 8]

**Tác giả khẳng định:** Các điểm chuyển tiếp không thay đổi theo những số khoảng chia đã thử và các đặc điểm định tính được giữ. **Bằng chứng hỗ trợ:** Các đường C được vẽ có bước chuyển ở những vị trí tương ứng; không có ước lượng sai khác vị trí hoặc khoảng bất định. Phụ lục B nói đến tính ổn định của S, D, C, nhưng Hình 6 trực tiếp trình bày C, không vẽ lại riêng S và D. [Phụ lục B; Hình 6]

**Không chứng minh:** Bất biến với mọi độ phân giải, mọi cách chọn biên hoặc mọi độ dài mẫu. Kết quả này chính là lý do không lấy một ngưỡng C cố định để so sánh trực tiếp các cấu hình m khác nhau. [Hình 6; Mục III, tr. 3; Mục IV, tr. 7]

## 7. Đóng góp thực sự, phạm vi kết luận và các giới hạn

Đóng góp thuyết phục nhất là một quy trình đơn giản, có thể giải thích từng bước: trích cực trị → xây dựng phân bố biên độ → tính entropy và độ lệch khỏi phân bố đều → nhân hai đại lượng → đối chiếu với sự thay đổi chế độ khi quét tham số. Điểm có bằng chứng trực tiếp là S riêng lẻ có hai chiều biến đổi khác nhau tại khởi phát trong Liénard, còn C cho xu hướng tăng ở cả hai cơ chế. Ba mô hình mở rộng phạm vi minh họa, và Phụ lục B cho một kiểm tra độ nhạy hữu ích. [Mục II–IV; Hình 1, 3, 5–6]

**Tác giả khẳng định:** Xu hướng tăng–đạt cực đại–giảm là tính chất chung, độc lập với ba hệ đã chọn, và có thể còn xuất hiện ở những hệ khác, gồm mô hình Hindmarsh–Rose có phần tử nhớ điện trở. **Bằng chứng hỗ trợ:** Xu hướng xuất hiện trong các ví dụ đã khảo sát; bài không có định lý cho mọi phân bố hoặc mọi hệ, cũng không mô phỏng hệ mở rộng được nêu. Chính kết luận tr. 7 thừa nhận chưa có một thước đo định lượng duy nhất. Do đó, “tính chung” nên hiểu là tính lặp lại trong ba mô hình và những miền tham số đã khảo sát. [Mục IV, tr. 7]

Những giới hạn dưới đây là **diễn giải của người phân tích từ công thức và thiết kế**, chưa phải các thí nghiệm thất bại đã được thực hiện:

- **Không đo cấu trúc thời gian của dãy cực trị.** Hoán vị thứ tự các cực trị sau khi đã trích xuất, giữ nguyên tập biên độ, sẽ giữ nguyên S, D, C. Vì vậy, chỉ số không phân biệt hai dãy có cùng phân bố nhưng khác tính tụ cụm, trật tự bùng phát hoặc thời gian chờ. Hoán vị toàn bộ mẫu tín hiệu thô là phép khác, vì có thể làm đổi tập cực trị. [Suy ra từ Phương trình (1)–(3)]
- **Không nhận diện duy nhất đuôi cực đoan.** C phụ thuộc vào toàn bộ các xác suất, không trực tiếp trọng số hóa khoảng ở xa theo mức nguy hiểm. Nhiều phân bố khác nhau có thể cho cùng C; C dương cũng có thể xuất hiện trong chuỗi không hỗn loạn. Không có chứng minh C cao là điều kiện đủ cho biến cố cực đoan. [Phương trình (3); thiết kế kiểm chứng ở Mục III]
- **Không đo độ lớn tuyệt đối.** Với phép đổi thang biên độ tuyến tính dương và chia lại miền nhỏ nhất–lớn nhất theo cùng quy tắc, tần suất các khoảng không đổi nên C không đổi, bỏ qua sai số số học và quy tắc xử lý biên. Một ngưỡng nguy hiểm theo đơn vị vật lý vì thế cần thông tin riêng. [Quy tắc chia khoảng ở Mục II và Phụ lục A]
- **Có thể nhạy với mẫu hiếm và ngoại lai.** Một cực trị rất xa làm đổi cả miền chia khoảng; chuỗi quá ngắn có thể chưa chứa biến cố cần đặc trưng. Nhiễu có thể tạo nhiều cực trị giả. Bài mới kiểm tra số khoảng chia, chưa định lượng các tác động này. [Mục II, tr. 3; Phụ lục A–B, tr. 8]
- **Không cho nhãn chung xuyên hệ.** Giá trị C thay đổi theo m, dạng phân bố, biến quan sát và điều kiện tham số. Ngay trong một hệ, tăng–giảm sau cực đại không xác lập một ranh giới duy nhất giữa mọi chế độ. Việc chọn tổng hai biến ở hệ ghép còn làm kết quả phụ thuộc vào đại lượng quan sát. [Hình 1, 3, 5–6]

Một lưu ý về phạm vi ngôn ngữ: D là độ lệch khỏi phân bố xác suất đều, không phải độ lệch khỏi giá trị trung bình của tín hiệu. Mục III.A, tr. 4 có câu diễn giải hai khái niệm gần như tương đương; bản phân tích bám vào Phương trình (2), vì hai phép đo không tương đương về toán học.

### Khả năng chuyển sang tín hiệu y sinh

**Giả thuyết mở rộng, chưa được kiểm chứng:** Có thể khảo sát C trên biên độ các đợt bùng phát hoặc các cực trị đã được xác định nhất quán trong điện não đồ (*electroencephalography*, EEG), điện tâm đồ (*electrocardiography*, ECG) hoặc tín hiệu quang thể tích (*photoplethysmography*, PPG). Lý do hợp lý về mặt biểu diễn là những tín hiệu này có thể cung cấp dãy biên độ cực trị; điều đó không bảo đảm cùng một ý nghĩa sinh lý hoặc cùng dạng đường C.

Mô hình nơron trong bài là bằng chứng từ hệ động lực mô phỏng, chưa phải kiểm chứng trên bệnh nhân, dữ liệu sinh lý đo được hoặc một biến cố lâm sàng. Để diễn giải C trên dữ liệu y sinh, cần phân biệt thay đổi sinh lý với nhiễu đo, chuyển động, thay đổi khuếch đại và thay đổi cách phát hiện đỉnh. Không mặc định mọi biến cố y sinh bắt nguồn từ khủng hoảng nội tại, phân nhánh hoặc chậm dần tới hạn. [Phạm vi dữ liệu của Mục III.C, tr. 5–7; phần mở rộng là đề xuất của người phân tích]

Nếu mục tiêu là dự báo, cần một thiết kế mới chỉ dùng dữ liệu đã có trước mốc dự báo, chọn độ dài cửa sổ trước khi đánh giá, tách người bệnh hoặc phiên đo giữa các tập dữ liệu và báo cáo thời gian báo trước cùng tỷ lệ cảnh báo sai. Với tiêu chí nguy hiểm theo biên độ tuyệt đối, cần giữ thêm biên độ và ngưỡng sinh lý. Đây là điều kiện cho một nghiên cứu tiếp theo, chưa phải kế hoạch đã chạy hoặc khoảng trống lâm sàng đã được xác lập từ PDF này.

## 8. Hồ sơ phương pháp (Methodological Fingerprint)

| Trường                                                  | Hồ sơ của nghiên cứu                                                                                                                                                                                                                                                                                                                                    |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Bài toán (Problem)**                            | Đặc trưng và phân biệt chế độ hỗn loạn có biến cố biên độ lớn hiếm gặp với hỗn loạn không cực đoan; khảo sát chuyển tiếp giữa chúng. [Mục I]                                                                                                                                                                                |
| **Đầu vào (Input)**                              | Một dãy biên độ cực đại hoặc cực tiểu cho mỗi điều kiện; nhiều dãy có tham số đi kèm để dựng đường chuyển tiếp. [Mục II–III]                                                                                                                                                                                                  |
| **Thông tin biết trước (Known information)**    | Chọn biến quan sát, hướng cực trị và số khoảng chia; trong kiểm chứng còn biết phương trình, tham số điều khiển và mốc/chế độ từ biểu đồ phân nhánh. Ngưỡng T dùng để đối chiếu, không để tính C. [Mục III]                                                                                                     |
| **Đầu ra (Output)**                               | S, D, C tại từng điều kiện; đường C theo tham số và sự tương ứng trực quan với khởi phát, miền biến cố hiếm và biến cố lớn thường xuyên. [Phương trình (1)–(3); Hình 1, 3, 5]                                                                                                                                              |
| **Phương án đối chiếu (Existing baseline)**   | S và D riêng lẻ trong Hình 1; biểu đồ phân nhánh, chuỗi và phân bố biên độ làm tham chiếu. PE được thảo luận nhưng không chạy so sánh trực tiếp. [Mục I; Hình 1–5]                                                                                                                                                           |
| **Thành phần mới (New component)**               | Khảo sát chỉ số tích entropy–độ lệch đã có trên phân bố biên độ cực trị để mô tả biến cố cực đoan; diễn giải xu hướng qua ba mô hình và hai cơ chế. Không phải phát minh tích S và D. [Mục II–IV; tài liệu 46]                                                                                                 |
| **Giả định (Assumptions)**                       | Chuỗi tại mỗi tham số đại diện đủ tốt cho chế độ; lấy đủ cực trị để quan sát biến cố hiếm; trích cực trị và chia khoảng nhất quán; biến quan sát phản ánh hiện tượng cần khảo sát. Đây là các điều kiện ngầm của quy trình, không phải giả định đã được kiểm chứng đầy đủ. [Mục II–III] |
| **Kiểm chứng (Validation)**                       | Liénard với PM và khủng hoảng nội tại; Ikeda và hai nơron Hindmarsh–Rose với khủng hoảng nội tại; thay m qua bốn giá trị. Không có kiểm chứng ngoài mẫu hoặc trên dữ liệu thực. [Hình 1–6]                                                                                                                                    |
| **Kết quả chính (Main finding)**                 | C tăng trong miền khởi phát, đạt cực đại hoặc miền cao rồi giảm khi biến cố lớn thường xuyên hơn; mốc thay đổi định tính giữ tương tự khi đổi m trong phạm vi thử. [Mục III–IV; Hình 1, 3, 5–6]                                                                                                                        |
| **Câu hỏi còn mở (Unresolved questions)**       | Tính đặc hiệu của C; độ nhạy với độ dài chuỗi, nhiễu và biên khoảng; quy tắc chọn điểm chuyển tiếp; dấu ε; cách tính μ, σ và hệ số ngưỡng trong hệ ghép; giá trị cho dự báo trước biến cố. [Các thông tin thiếu ở Mục III và Phụ lục B]                                                                  |
| **Khả năng tái lập (Reproduction feasibility)** | Có thể cài đặt chỉ số và phương trình từ PDF; tái lập xu hướng khả thi hơn tái lập chính xác hình. Cần bổ sung cấu hình số, dữ liệu/mã và làm rõ bất nhất dấu ghép. Chưa thực hiện mô phỏng tái lập trong bước này. [Mục II–III; khả dụng dữ liệu, tr. 7]                                              |

## 9. Tài liệu đọc tiếp và quyết định tái lập

### 9.1. Thứ tự kiểm tra nguồn

Trước tiên cần đọc lại **Mục II, tr. 3**, **Phụ lục A–B, tr. 7–8** và **Hình 6** để chốt đúng cách chia khoảng, chuẩn hóa D và giới hạn định lượng. Tiếp theo kiểm tra **Mục III.B và Hình 3–4** để chọn ví dụ Ikeda ít phụ thuộc vào chi tiết tích phân hơn. Cuối cùng, kiểm tra **Phương trình (7), Mục III.C và Hình 5** để giải quyết dấu ε trước khi mở rộng sang hệ ghép.

Những tài liệu dưới đây là **đề xuất đọc tiếp từ danh mục của bài**, chưa được truy cập trong phân tích này. PDF không in tên của phần lớn các tài liệu tham khảo; vì vậy chỉ ghi thông tin thư mục được cung cấp cùng mục đích đọc, không tự đặt nhan đề:

| Tài liệu được bài dẫn                                                                                                                                  | Mục đích đọc tiếp                                                                                                           |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| Lopez-Ruiz, Mancini và Calbet (1995), *Phys. Lett. A* **209**, 321, tài liệu 46                                                                    | Xác định nguồn gốc của cách kết hợp entropy và độ lệch khỏi phân bố đều, cũng như các lựa chọn chuẩn hóa |
| Bandt và Pompe (2002), *Phys. Rev. Lett.* **88**, 174102, tài liệu 44                                                                              | Kiểm tra biểu diễn thứ tự của PE và phạm vi thực sự của nhận định “mất thông tin biên độ”                    |
| Xiong, Shang, He và Zhang (2020), *Nonlinear Dyn.* **100**, 1673, tài liệu 51                                                                      | Kiểm tra phép kết hợp PE và độ phân kỳ Jensen–Shannon mà bài dùng làm đối chiếu trong tổng quan                 |
| Manneville và Pomeau (1980), *Physica D* **1**, 219, tài liệu 52; Grebogi và cộng sự (1987), *Phys. Rev. A* **36**, 5365, tài liệu 53 | Làm rõ cơ chế gián đoạn và khủng hoảng, tránh suy cơ chế chỉ từ bước nhảy của C                                |
| Kingston và cộng sự (2017), *Phys. Rev. E* **96**, 052204, tài liệu 54                                                                           | Tìm đặc tả và kiểm chứng cơ chế của hệ Liénard được bài kế thừa                                                 |
| Ray, Rakshit, Ghosh và Dana (2019), *Chaos* **29**, 043131, tài liệu 55                                                                            | Kiểm tra nguồn mô hình Ikeda, tham số và quy trình sinh biến cố cực đoan                                               |
| Mishra và cộng sự (2018), *Phys. Rev. E* **97**, 062311, tài liệu 57                                                                             | Kiểm tra quy ước dấu ghép và cơ chế bùng phát của hệ Hindmarsh–Rose                                                  |

Nguồn thông tin thư mục: danh mục tài liệu, tr. 9. Các chủ đề trong cột phải là lý do đọc, không phải bản tóm tắt những tài liệu đã được đọc.

### 9.2. Quyết định và các điều kiện tái lập

**Lựa chọn: ứng viên tái lập (Reproduction candidate), có điều kiện.** Lý do là công thức ngắn, đầu vào rõ ở mức khái niệm, có mô hình xác định và các hình đích để đối chiếu. Giá trị của việc tái lập là kiểm tra một thống kê phân bố có diễn giải được, không phải xác nhận sẵn một bộ dự báo biến cố cực đoan. Chưa đủ cơ sở xếp phương pháp này thành phương pháp nền tảng cho cảnh báo sớm hoặc ứng dụng lâm sàng. [Mục II–IV; Hình 1–6]

**Bước đầu hợp lý, chưa thực hiện:** Bắt đầu bằng Ikeda ở ba điểm p của Hình 4 rồi quét quanh miền Hình 3. Tính đúng C từ cực tiểu của y với m = 50, sau đó thử bốn giá trị m của Hình 6. Vì là ánh xạ, lựa chọn này tránh được một nguồn bất định là bộ tích phân phương trình vi phân, nhưng vẫn cần chốt điều kiện đầu, số vòng lặp, phần quá độ và quy tắc lấy cực tiểu. Mốc p được in trong bài là mục tiêu đối chiếu, không phải kết quả đã tái lập.

Để tái lập chính xác hơn, thông tin cần lấy từ tác giả hoặc mã gốc gồm:

1. Điều kiện đầu, thời gian loại quá độ, tổng thời lượng, số mẫu hoặc số cực trị cho mỗi điều kiện; cách chuyển điều kiện đầu khi quét tham số.
2. Phương pháp tích phân, bước thời gian, dung sai, lịch lấy mẫu và cách tìm cực trị cho Liénard và hệ Hindmarsh–Rose.
3. Lưới tham số và cách xác định điểm chuyển tiếp; quy tắc chia khoảng, xử lý dãy hằng và các giá trị nằm ở biên.
4. Tập mẫu dùng tính μ, σ, quy tắc ước lượng độ lệch chuẩn và hệ số ngưỡng của hệ Hindmarsh–Rose.
5. Quy ước đúng của dấu ε và dữ liệu/mã tạo Hình 5; làm rõ ký hiệu θ/Θ nếu cần.

PDF cho biết dữ liệu hỗ trợ kết quả được cung cấp từ tác giả liên hệ khi có yêu cầu hợp lý; không nêu kho mã hoặc kho dữ liệu công khai. Phân tích này chưa liên hệ tác giả, chưa tải nguồn ngoài và chưa chạy mô phỏng. [Phần khả dụng dữ liệu, tr. 7]

Sau khi tái tạo được xu hướng cơ bản, các phép kiểm tra bổ sung có giá trị là thay độ dài chuỗi, đổi điều kiện đầu, so sánh biên chia khoảng theo từng chuỗi với biên chung, và dùng chuỗi thay thế để tách cấu trúc thời gian khỏi phân bố biên độ. Nếu chuyển sang mục tiêu dự báo, cần thiết kế đánh giá nhân quả theo thời gian riêng. Đây là gợi ý của người phân tích cho giai đoạn sau, không phải thí nghiệm mà bài đã báo cáo hoặc công việc đã chạy ở bước đọc bài.

## 10. Ghi nhận kiểm tra bản phân tích

- Đã đối chiếu toàn bộ nội dung 10 trang PDF, gồm danh mục tài liệu; kiểm tra trực quan Hình 1–6, Phương trình (1)–(10) và các ký hiệu dễ lỗi khi trích xuất như Γ, θ/Θ, ε.
- Đã dùng tiếng Việt làm mạch diễn đạt, giải thích thuật ngữ và viết tắt khi xuất hiện; phân biệt lời tác giả, bằng chứng và suy luận của người phân tích. Bảng hồ sơ có đủ 11 trường và quyết định tái lập có điều kiện.
- Đã kiểm tra lại tệp Markdown lưu trên đĩa về cặp dấu toán, vị trí dòng phân cách, ngoặc nhọn, môi trường nhiều dòng và ký tự điều khiển; các công thức quan trọng nằm trong khối toán riêng. Môi trường hiện tại không có trình xem Markdown hỗ trợ toán sẵn dùng để kiểm tra toàn bộ bản hiển thị; mức xác nhận là đối chiếu nội dung và kiểm tra cú pháp, chưa xác nhận biên dịch hoặc hiển thị bằng MathJax/KaTeX.

Phần kiểm định phản biện tiếp theo được dành cho Prompt 02; chưa thực hiện ở bước này.

## Critical Audit (chờ Prompt 02)
