# Dakos và cộng sự (2012) — Phương pháp phát hiện cảnh báo sớm trong chuỗi thời gian

**Bài báo:** *Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data* — “Các phương pháp phát hiện cảnh báo sớm của chuyển tiếp tới hạn trong chuỗi thời gian, minh họa bằng dữ liệu sinh thái mô phỏng”. **Tác giả:** Vasilis Dakos, Stephen R. Carpenter, William A. Brock, Aaron M. Ellison, Vishwesha Guttal, Anthony R. Ives, Sonia Kéfi, Valerie Livina, David A. Seekell, Egbert H. van Nes và Marten Scheffer. **Công bố:** *PLoS ONE* **7**(7), e41010, ngày 17/7/2012. **DOI ghi trong PDF:** 10.1371/journal.pone.0041010.

**Nguồn và quy ước trang:** Chỉ sử dụng [PDF được chỉ định](<../paper/4 Methods for Detecting Early Warnings of Critical Transitions in Time Series Illustrated Using Simulated Ecological Data.pdf>). Đã đọc toàn bộ **20 trang**, gồm danh mục tài liệu và mô tả tài liệu bổ sung; đã đối chiếu trực quan các công thức trọng tâm, Hình 1–12 và Bảng 1–3. Số trang in trong bài trùng trang PDF 1–20, không có bìa riêng. Không sử dụng web, tải mã hoặc đọc tài liệu ngoài trong bước này. PDF chỉ **liệt kê** Hình S1–S4, không chứa các ảnh bổ sung đó; không coi chúng là đã được xem.

Bài tổ chức các phương pháp thành một quy trình năm bước: chuẩn bị dữ liệu → xử lý xu hướng → khảo sát chỉ báo → kiểm tra độ nhạy → kiểm định ý nghĩa. Đóng góp thực hành nằm ở việc áp dụng nhiều nhóm phương pháp lên **cùng hai chuỗi mô phỏng** và cho thấy lựa chọn xử lý dữ liệu có thể thay đổi kết luận. Đây là hướng dẫn so sánh phương pháp và giới thiệu công cụ, chưa phải một đánh giá dự báo trên quần thể nhiều hệ hoặc một thuật toán báo động duy nhất đã được hiệu chuẩn. [Tóm tắt, tr. 1; Giới thiệu, tr. 2; Kết quả, tr. 15–17; Thảo luận, tr. 17–18; Hình 12]

**Quy ước mức phát biểu:** **Tác giả khẳng định (Authors claim)** là điều bài nêu; **Bằng chứng hỗ trợ (Evidence supports)** là điều công thức, mô phỏng hoặc phép so sánh trực tiếp cho phép kết luận; **Diễn giải của người phân tích (Analyst interpretation)** là đánh giá và đề xuất bổ sung. Những bất nhất của bản in được ghi ngay cạnh nội dung liên quan để tránh sao chép sai. Đây chưa phải phần kiểm định phản biện đầy đủ của Prompt 02.

## 1. Bài toán và động cơ: từ danh sách chỉ báo đến quy trình có thể kiểm tra

Tác giả đặt vấn đề trong các hệ có thể chuyển sang trạng thái khác khi điều kiện nền biến đổi chậm, như hồ, quần thể sinh vật, nhịp sinh lý hoặc khí hậu. Khi không biết rõ tác nhân điều khiển và ngưỡng tới hạn, một chuỗi trạng thái có thể là nguồn thông tin chính. Các **dấu hiệu cảnh báo sớm** (*early-warning signals*, EWS) được kỳ vọng phản ánh sự thay đổi trí nhớ động lực học, mức dao động hoặc chuyển đổi giữa những trạng thái ổn định. [Giới thiệu, tr. 1–2]

Hai nút thắt được tác giả nêu là thiếu dữ liệu thích hợp và thiếu một khung áp dụng thống nhất. Dữ liệu có thể quá ngắn, lấy mẫu quá thưa hoặc được thiết kế để tránh tự tương quan, trong khi chính cấu trúc tương quan lại chứa thông tin cần đo. Các phương pháp cũng xuất phát từ những lĩnh vực và giả định khác nhau: một số xét dao động nhỏ quanh cân bằng; một số xử lý chế độ nhiễu mạnh và chuyển đổi giữa các miền hút. So sánh trên các dữ liệu thực khác nhau khó tách ảnh hưởng của phương pháp khỏi ảnh hưởng của hệ, chất lượng dữ liệu và sự không chắc chắn về cơ chế chuyển tiếp. [Giới thiệu, tr. 2]

Câu hỏi chính là: **nếu cùng áp dụng các phương pháp hiện có vào những chuỗi có cơ chế chuyển tiếp đã biết, chúng cho thông tin gì, cần xử lý dữ liệu thế nào và bằng chứng về xu hướng có đáng tin dưới một mô hình không hay không?** Việc dùng dữ liệu mô phỏng là lựa chọn nhằm kiểm soát một phần sự không chắc chắn về cơ chế, không phải bằng chứng rằng kết quả đã khái quát sang dữ liệu thực. [Giới thiệu và phần Dữ liệu, tr. 2, 11, 14–15]

**Tác giả khẳng định:** chưa có nghiên cứu so sánh phù hợp và cần một bộ hướng dẫn thực hành; kết hợp phương pháp có thể giúp nhận diện tín hiệu đáng tin hơn. **Bằng chứng hỗ trợ:** các phương pháp quả thực cho kết quả khác nhau trên hai chuỗi, và nhiều kết quả phụ thuộc xử lý dữ liệu. **Diễn giải của người phân tích:** đây là so sánh có ví dụ thực hiện, chưa phải bảng xếp hạng hiệu năng với tỷ lệ cảnh báo sai, bỏ sót và thời gian báo trước trên nhiều lần mô phỏng độc lập. [Tóm tắt; Hình 2–11; Thảo luận, tr. 17–18]

## 2. Đặt bài toán, đầu vào và đầu ra

Bài giả định người áp dụng chỉ có một chuỗi đáp ứng, chưa biết rõ phương trình sinh dữ liệu, tác nhân chậm hoặc ngưỡng chuyển tiếp. Tuy nhiên, **người thiết kế thí nghiệm lại biết mô hình, tham số và lịch thay đổi tác nhân** để tạo dữ liệu và đối chiếu kết quả. Hai vai trò này cần được tách biệt: biết sự thật nền để minh họa phương pháp không chứng minh sự thật đó có thể được nhận dạng từ một chuỗi bất kỳ. [Phương pháp, tr. 2–3; Dữ liệu, tr. 11, 14–15; mở đầu Kết quả, tr. 15]

Mô hình khái quát dùng làm nền cho lập luận là:

$$
dx=f(x,\theta)\,dt+g(x,\theta)\,dW.
$$

x là trạng thái, θ là điều kiện điều khiển thay đổi chậm, f là phần trôi tất định và g điều chỉnh tác động nhiễu. W là quá trình Brown; bài diễn đạt phần ngẫu nhiên bằng nhiễu trắng. Đây là Phương trình (1), tr. 2. Không phải tất cả phương pháp đều cần khớp chính xác f và g, nhưng cách diễn giải EWS vẫn dựa trên giả định về loại động lực học.

| Thành phần                                                          | Cách bài báo thiết lập                                                                                                                                                             |
| --------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Đầu vào tính chỉ báo                                            | Một chuỗi một biến, hoặc phần dư/phiên bản biến đổi của chuỗi đó; không có bộ phân loại được huấn luyện bằng nhãn                                           |
| Thông tin cần chọn khi áp dụng                                   | Khoảng lấy mẫu, đoạn phân tích, phép biến đổi, bộ lọc, cửa sổ; với mô hình còn có bậc tự hồi quy, hạt nhân làm trơn hoặc dạng phương trình trạng thái |
| Thông tin không cần biết tường minh trong nhiều phương pháp | Toàn bộ phương trình cơ chế và giá trị của tác nhân chậm                                                                                                                  |
| Thông tin biết trước để kiểm chứng                            | Mô hình sinh khối bị khai thác, các tham số, lịch tăng mức khai thác và nhánh cân bằng của hệ tất định                                                              |
| Đầu ra dựa trên đại lượng thống kê                          | Chuỗi chỉ báo theo thời gian; xu hướng Kendall; độ nhạy theo lựa chọn xử lý; giá trị p dưới mô hình không được chọn                                             |
| Đầu ra dựa trên mô hình                                         | Trôi, khuếch tán, bước nhảy, phương sai có điều kiện; hệ số tự hồi quy biến thiên; đại lượng hồi phục; chế độ hoặc số giếng thế ước lượng            |
| Đầu ra chưa được xây dựng đầy đủ                          | Một quy tắc báo động thống nhất có ngưỡng được hiệu chuẩn và đánh giá thời gian báo trước, cảnh báo sai, bỏ sót ngoài mẫu                                  |

Nguồn bảng: Phương pháp, tr. 2–11; Kết quả, tr. 15–17; Hình 12 và Bảng 3, tr. 14.

Phần tiền xử lý chọn chuỗi **chậm dần tới hạn** (*critical slowing down*, CSD) tới khoảng bước 970 vì đã biết vị trí chuyển đổi trong mô phỏng. Chuỗi chuyển đổi qua lại được dùng toàn bộ do khó chọn một mốc chuyển tiếp rõ. Vì vậy, phép tính ở đây kết hợp **mô tả động lực học, phát hiện hồi cứu và kiểm tra xu hướng trên đoạn được chọn**, chưa phải một thí nghiệm dừng trực tuyến trước một sự kiện chưa biết. Một cửa sổ trượt có thể tính khi dữ liệu đến dần; riêng đặc điểm đó không làm toàn bộ quy trình, gồm chọn đoạn, lọc và khớp mô hình, trở thành kiểm chứng dự báo trước sự kiện. [Bước 1–3, tr. 15; Thảo luận, tr. 18]

Ước lượng ngưỡng phân chế độ của mô hình tự hồi quy cũng khác ước lượng ngưỡng điều khiển gây phân nhánh. Một ngưỡng trên **giá trị trạng thái đã biến đổi** không phải giá trị mức khai thác làm nhánh cân bằng biến mất. [Phương trình (6a–b), tr. 10–11; Hình 8; Dữ liệu, tr. 14]

## 3. Dữ liệu mô phỏng: hai đường tiếp cận cùng một phân nhánh

### 3.1. Mô hình sinh dữ liệu và sai số quan sát

Sinh khối x tăng trưởng logistic và bị khai thác theo hàm bão hòa:

$$
dx=\left[rx\left(1-\frac{x}{K}\right)
-c\frac{x^{2}}{x^{2}+h^{2}}\right]dt+\sigma x\,dW.
$$

r là tốc độ tăng trưởng, K là sức chứa, h là hằng số nửa bão hòa và c là mức khai thác. Đây là Phương trình (8), tr. 11. Hình 1A cho hai nhánh cân bằng hút và một nhánh không ổn định ở giữa, tạo vùng hai trạng thái ổn định cùng tồn tại. Tác giả ghi ngưỡng nếp gấp làm sụp đổ nhánh sinh khối cao xấp xỉ c bằng 2,604. Khôi phục nhánh cũ khi giảm c xảy ra tại một ngưỡng khác, thể hiện tính trễ phụ thuộc lịch sử. [Hình 1A, tr. 3; Dữ liệu, tr. 14]

Quan sát được thêm sai số đo:

$$
x_{\mathrm{obs},t}=x_t+\sigma_{\mathrm{obs}}\epsilon_t,\qquad
\sigma_{\mathrm{obs}}=0.1.
$$

ε là biến ngẫu nhiên có phân phối chuẩn theo mô tả của bài; cùng độ lệch chuẩn sai số đo được dùng cho cả hai chuỗi. Nguồn: Dữ liệu, tr. 15. Ký hiệu σ có chỉ số obs là cách viết ngắn của bản phân tích cho hệ số được bài gọi là sai số quan sát; không phải nhiễu động lực trong (8).

### 3.2. Hai chuỗi được dùng

| Thiết lập                | Chuỗi chậm dần tới hạn                               | Chuỗi chuyển đổi qua lại                                                                                 |
| -------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Cách gọi                 | Chậm dần tới hạn (CSD)                                | **Chuyển đổi qua lại giữa các trạng thái** (*flickering*)                                     |
| Độ dài mô phỏng       | 1.000 bước                                              | 10.000 bước                                                                                                 |
| Mức khai thác            | Tăng tuyến tính từ 1 tới 2,6771                      | Cùng khoảng tăng nhưng qua 10.000 bước                                                                  |
| Tham số chung             | r = 1; h = 1; K = 10                                      | r = 1; h = 1; K = 10                                                                                          |
| Hệ số nhiễu động lực | σ = 0,03                                                 | σ = 0,15                                                                                                     |
| Nguồn nhiễu thêm        | Không nêu dòng vào có tương quan như ở cột bên | Có dòng vào sinh khối với tương quan thời gian; T = 20, β = 0,07                                     |
| Sai số đo                | Độ lệch chuẩn 0,1                                     | Độ lệch chuẩn 0,1                                                                                         |
| Diễn biến                | Chuyển sang khai thác quá mức khoảng bước 970      | Qua lại nhiều lần giữa hai trạng thái, rồi dành thời gian dài hơn ở trạng thái sinh khối thấp |
| Đoạn phân tích chính  | Chọn tới bước 970; cửa sổ 50% là 485 điểm        | Dùng toàn bộ chuỗi; cửa sổ 50% là 5.000 điểm                                                         |

Nguồn: Hình 1, tr. 3; Dữ liệu, tr. 14–15; Bước 1 và 3, tr. 15. Các con số là bước quan sát/mô phỏng theo bài, không tự gán thành đơn vị thời gian vật lý.

Biểu thức dòng vào có tương quan thời gian được in ở tr. 14 là:

$$
i_{t+1}=\left[\left(1-\frac{1}{T}\right)i_t+\beta\eta_t\right]x_t.
$$

η là biến ngẫu nhiên chuẩn theo văn bản. Công thức được giữ đúng vị trí ngoặc và thừa số x của bản in. **Lưu ý khi tái lập:** không được tự chuyển x vào chỉ một hạng hoặc thay bằng một quá trình nhiễu đỏ chuẩn khác; cần đối chiếu mã sinh dữ liệu để xác định cách dòng vào được tạo và đưa vào phương trình. PDF chưa trình bày đầy đủ thuật toán tích phân và cách cập nhật đồng thời các biến. [Dữ liệu, tr. 14–15]

**Diễn giải của người phân tích:** hai kịch bản thay đổi đồng thời độ dài chuỗi, tốc độ tăng tác nhân theo bước, cường độ nhiễu và sự có mặt của dòng vào có tương quan. Vì vậy, khác biệt giữa kết quả hai cột không thể quy riêng cho một thành phần “chuyển đổi qua lại” bằng một thí nghiệm loại bỏ từng yếu tố. Tác giả thừa nhận dùng những hiện thực đơn lẻ để minh họa, chưa đánh giá độ tin cậy trên nhiều hiện thực. [Thảo luận, tr. 18]

Một chi tiết quan trọng của (8) là nhiễu **nhân với trạng thái**: dù σ cố định, biên độ nhiễu tức thời vẫn thay đổi theo x. Do đó, “hệ số nhiễu được giữ cố định” không đồng nghĩa phương sai nhiễu động lực dọc toàn quỹ đạo là hằng. Điều này cần được nhớ khi diễn giải các ước lượng khuếch tán ở Hình 5–6.

## 4. Hai họ phương pháp và phạm vi tính mới

**Mô hình tự hồi quy** (*autoregressive model*, AR) bậc p được ký hiệu AR(p); AR(1) chỉ trường hợp bậc một. Bài phân biệt **chỉ báo dựa trên đại lượng thống kê** (*metric-based indicators*) với **chỉ báo dựa trên mô hình** (*model-based indicators*). Nhóm đầu đo các thuộc tính của chuỗi mà không khớp một cấu trúc động lực cụ thể; nhóm sau ước lượng các thành phần của một mô hình tổng quát. “Dựa trên mô hình” ở đây không có nghĩa phải biết sẵn toàn bộ phương trình sinh dữ liệu: một số mô hình được khớp chính vì f, g và tác nhân chậm chưa biết. [Phương pháp, tr. 2–3, 6–11]

| Nhóm công cụ                                  | Công cụ được bài tổng hợp                                                                                        | Nguồn gốc và cách dùng                                                                                                     |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Trí nhớ và phổ                               | Tự tương quan trễ 1; hệ số AR(1); đại lượng hồi phục; mật độ phổ, tỷ số phổ, số mũ phổ             | Bảng 1 dẫn các nguồn [19]–[25]; không phải toàn bộ các công cụ này được phát minh trong bài                   |
| Dao động theo thang                            | **Phân tích dao động sau loại xu hướng** (*detrended fluctuation analysis*, DFA)                          | Kế thừa [7], [26]–[27], với một chỉ báo được đổi thang                                                              |
| Phân bố giá trị                              | Độ lệch chuẩn, hệ số biến thiên, bất đối xứng và độ nhọn                                                 | Kế thừa [25], [28]–[29]                                                                                                      |
| Phụ thuộc của độ biến thiên               | **Phương sai có điều kiện thay đổi** (*conditional heteroskedasticity*, CH)                              | Kế thừa các kiểm định [30]–[32], áp dụng cho phần dư trong cửa sổ                                                  |
| Phụ thuộc chưa được mô hình giải thích | Kiểm định Brock–Dechert–Scheinkman, viết tắt BDS                                                                  | Công cụ có trước [33], dùng như chẩn đoán bổ sung, không phải chỉ báo được thiết kế riêng cho phân nhánh |
| Trôi, nhiễu và bước nhảy                   | **Mô hình trôi–khuếch tán–bước nhảy phi tham số** (*nonparametric drift–diffusion–jump model*, DDJ) | Kế thừa [16], [34]–[36]                                                                                                      |
| Động lực tự hồi quy                         | Mô hình tự hồi quy hệ số biến thiên theo thời gian và mô hình tự hồi quy phân ngưỡng                    | Kế thừa [38]; có cấu trúc trạng thái và thành phần sai số đo                                                        |
| Cấu trúc nhiều trạng thái                   | Phân tích thế và số giếng thế                                                                                     | Kế thừa [43]–[44]                                                                                                            |

Nguồn: Bảng 1, tr. 2; các mô tả phương pháp, tr. 3–11; danh mục tài liệu, tr. 19–20.

Một chi tiết tính mới cần đọc chính xác: Bảng 1 ghi số mũ phổ với nguồn “bài này”, trong khi phần diễn giải phép khớp số mũ phổ vẫn dẫn [24]. Có thể ghi nhận tác giả đưa cách dùng số mũ phổ vào danh mục EWS của công trình, nhưng không đủ căn cứ gọi phép tính số mũ phổ hoặc phân tích phổ là mới. Kết quả hình riêng của nhánh này được dẫn tới Hình S3 ngoài PDF hiện có, nên chưa thể đánh giá trực tiếp đồ thị bổ sung. [Bảng 1; tr. 4; mô tả Hình S3, tr. 19]

**Đóng góp được hỗ trợ rõ nhất:** so sánh cách thực hiện trên cùng dữ liệu; liên kết tiền xử lý, lựa chọn mô hình, độ nhạy và mô hình không thành quy trình năm bước; cung cấp các ví dụ và chỉ dẫn công cụ. Không có một bộ ước lượng hay hàm mục tiêu tối ưu hóa hoàn toàn mới bao trùm mọi phương pháp. Việc phối hợp nhiều chỉ báo được đề xuất như cách tăng độ tin cậy, chưa được kiểm chứng bằng một bộ quy tắc kết hợp có tỷ lệ lỗi đo trên tập kiểm tra. [Hình 12; Bảng 3; Thảo luận, tr. 17–18]

## 5. Quy trình năm bước: điều gì thật sự được thực hiện?

### 5.1. Bước 1 — Chọn đoạn, kiểm tra lấy mẫu và biến đổi dữ liệu

Đầu tiên, tác giả chọn đoạn CSD trước chuyển tiếp và giữ toàn bộ chuỗi chuyển đổi qua lại. Dữ liệu mô phỏng không có giá trị thiếu và được lấy mẫu đều. Bài lưu ý nội suy có thể giải quyết dữ liệu thiếu nhưng cũng tạo tương quan giả; gộp dữ liệu có thể đổi thang thời gian quan sát nhưng phải hiểu thang động lực học phù hợp. Đây là lưu ý phương pháp, không phải các thử nghiệm mất dữ liệu hoặc lấy mẫu không đều được thực hiện trên hai chuỗi chính. [Bước 1, tr. 15]

Phép biến đổi được chọn khác nhau theo phương pháp. Chuỗi chuyển đổi qua lại có giá trị gần 0 và giá trị lớn nên có trường hợp dùng log cộng 1 rồi chuẩn hóa. Mô hình AR theo thời gian và AR phân ngưỡng dùng dữ liệu biến đổi log và chuẩn hóa; DDJ dùng chuỗi biến đổi log; phân tích thế dùng dữ liệu không biến đổi. Không nên gọi tất cả các đường kết quả là được tính trên một đầu vào số học giống hệt nhau. [Bước 1, tr. 15; Bước 3, tr. 15–17]

Để làm rõ ý nghĩa, các biến đổi có thể viết bằng ký hiệu của bản phân tích:

$$
u_t=\log(z_t+1),\qquad
v_t=\frac{u_t-\bar{u}}{s_u}.
$$

z là chuỗi ban đầu, u là chuỗi sau log, còn v được chuẩn hóa bằng trung bình và độ lệch chuẩn của u. Nguồn là mô tả Bước 1, tr. 15; ký hiệu u, v và thanh trung bình được dùng ở đây cho rõ, không phải ký hiệu nguyên bản. Công thức này không khẳng định mọi nhánh đều dùng cùng một phép log cộng 1: cần xem đúng mã và quy ước của từng nhánh trước tái lập.

### 5.2. Bước 2 — Loại xu hướng, nhưng không loại mất động lực học cần đo

Tác giả dùng làm trơn Gaussian để tạo phần dư khi tính tự tương quan, độ lệch chuẩn và bất đối xứng của chuỗi CSD. Lựa chọn minh họa là độ rộng bộ lọc bằng 10% độ dài chuỗi. DFA loại xu hướng tuyến tính; CH làm việc trên phần dư của AR được chọn. Bộ lọc quá linh hoạt có thể lấy mất chính biến thiên chậm mà chỉ báo cần phát hiện; chu kỳ mùa vụ còn sót có thể tạo cấu trúc tương quan không liên quan đến CSD. [Bước 2–3, tr. 15; Hình 2, 10]

Do đó, loại xu hướng không chỉ là một thao tác làm đẹp dữ liệu. Nó quyết định đại lượng quan sát đang phản ánh nhiễu quanh một nền ổn định hay sự di chuyển của chính nền đó. PDF không nêu đầy đủ cách xử lý biên bộ lọc hoặc bảo đảm mọi phép làm trơn chỉ dùng quá khứ; chưa thể coi toàn bộ quy trình là một phép thử dự báo trực tuyến, cũng không được tự kết luận đã có lỗi dùng dữ liệu tương lai chỉ từ tên bộ lọc.

### 5.3. Bước 3 — Tính chỉ báo và lượng hóa xu hướng

Các cửa sổ chính của tự tương quan, độ lệch chuẩn và bất đối xứng có độ dài 50%: 485 điểm cho CSD và 5.000 điểm cho chuyển đổi qua lại. CH dùng cửa sổ 10%; mô hình DDJ được khớp cả chuỗi; mô hình AR phân ngưỡng dùng riêng một đoạn 500 điểm. Các khác biệt này là một phần của quy trình, không phải cùng một phép đo chỉ thay tên thuật toán. [Bước 3, tr. 15–17]

Xu hướng được lượng hóa bằng **tương quan thứ hạng Kendall**. Trong trường hợp không có đồng hạng, một dạng minh họa của hệ số là:

$$
\tau=\frac{2}{M(M-1)}
\sum_{1\leq i<j\leq M}\operatorname{sgn}(I_j-I_i).
$$

I là chuỗi giá trị chỉ báo theo thời gian và M là số giá trị. Đây là diễn giải công thức của người phân tích cho thống kê được bài dùng; PDF không đặc tả cách điều chỉnh đồng hạng trong triển khai. τ dương nghĩa là tăng theo thời gian, τ âm nghĩa là giảm; độ lớn không phải độ chính xác dự báo. Đối với chỉ báo tăng rồi giảm hoặc dao động mạnh, một τ chung có thể che cấu trúc quan trọng. [Hình 2–3; Bước 4, tr. 17]

### 5.4. Bước 4 — Độ nhạy là thay lựa chọn phân tích, không phải thêm hiện thực dữ liệu

Với CSD, tác giả quét độ dài cửa sổ từ 25% tới 75% chuỗi, bước 10 điểm, và độ rộng Gaussian từ 5 tới 200, bước 20 theo mô tả văn bản. Hình 10 cho τ trên lưới lựa chọn và phân bố tần suất τ tương ứng. DFA cũng được kiểm tra theo độ dài cửa sổ cho cả hai chuỗi. Những phân bố này phản ánh **thay đổi tham số phân tích trên cùng dữ liệu**, không phải phân bố qua nhiều chuỗi độc lập hay khoảng tin cậy. [Bước 4, tr. 17; Hình 3E–F, 10]

Tự tương quan giữ xu hướng tăng trong lưới CSD. Độ lệch chuẩn có thể cho xu hướng âm khi độ rộng bộ lọc nhỏ, được tác giả giải thích là lọc quá sát làm mất biến thiên. Bất đối xứng cho xu hướng âm nhưng yếu hơn. Kết quả này ủng hộ việc khảo sát độ nhạy; không chứng minh mọi phương pháp đều bền với mọi loại dữ liệu hoặc mọi bộ lọc. [Hình 10; Bước 4, tr. 17]

### 5.5. Bước 5 — Kiểm định ý nghĩa phụ thuộc mô hình không

Với các chỉ báo cửa sổ không có kiểm định tích hợp, tác giả khớp **mô hình tự hồi quy–trung bình trượt** (*autoregressive moving average model*, ARMA) vào phần dư, chọn bậc bằng **tiêu chuẩn thông tin Akaike** (*Akaike information criterion*, AIC), rồi sinh **1.000 chuỗi thay thế** (*surrogate time series*) có cùng độ dài. τ quan sát được so với phân bố τ từ các chuỗi tuyến tính dừng này cho từng lựa chọn cửa sổ/bộ lọc. Các phương pháp có kiểm định hoặc cơ chế chọn mô hình riêng được xử lý theo nhánh của chúng. [Bước 5, tr. 17; Hình 11]

Ý nghĩa của phép thử là: xu hướng quan sát có bất thường so với **mô hình tuyến tính dừng đã khớp** hay không. Nó không trực tiếp kiểm định “có một phân nhánh nếp gấp sắp xảy ra” đối lại với mọi cơ chế khác. 1.000 chuỗi thay thế không phải 1.000 lần mô phỏng hệ sinh thái tiếp cận ngưỡng, và giá trị p không phải xác suất một cảnh báo đúng. Đây là giới hạn diễn giải của người phân tích, nhất quán với lưu ý của tác giả rằng kết luận phụ thuộc mô hình không. [Bước 5, tr. 17]

Không có bước chia huấn luyện/kiểm tra độc lập trong quy trình này. Cụm “đối chiếu chéo” giữa các chỉ báo trong Thảo luận được hiểu là kiểm tra sự phù hợp giữa các phương pháp, không phải bằng chứng tác giả đã thực hiện kiểm định chéo bằng chia dữ liệu. PDF cũng không báo cáo hiệu chỉnh chung cho việc khảo sát nhiều lựa chọn, nhiều chỉ báo hoặc kiểm định lặp trên cửa sổ chồng lấn. [Hình 10–12; Thảo luận, tr. 17–18]

## 6. Các chỉ báo thống kê: công thức, giả định và bằng chứng

### 6.1. Tự tương quan, đại lượng hồi phục và phổ

Với chuỗi quanh trung bình ổn định, bài trình bày:

$$
\rho_1=\frac{\mathbb{E}[(z_t-\mu)(z_{t+1}-\mu)]}{\sigma_z^{2}},\qquad
z_{t+1}=a_1z_t+e_t.
$$

ρ là tự tương quan trễ 1, μ là trung bình, phương sai của z nằm ở mẫu số và e là nhiễu mới Gaussian. Nguồn: phần Tự tương quan, tr. 3. Sự tương đương giữa ρ và hệ số AR(1) được hiểu trong mô hình dừng, với cách xử lý trung bình và nhiễu thích hợp; không bảo đảm hai ước lượng hữu hạn giống hệt trên mọi chuỗi có xu hướng.

Bài còn gọi nghịch đảo hệ số AR(1), hoặc một trừ hệ số đó, là đại lượng hồi phục:

$$
R_{1}=\frac{1}{a_1},\qquad R_{2}=1-a_1.
$$

Hai ký hiệu R có chỉ số sẽ được dùng trong bản phân tích để phân biệt **hai quy ước khác nhau** được nêu ở tr. 3, không phải hai đại lượng bằng nhau. Nghịch đảo tiến về 1 khi a tiến về 1, còn hiệu tiến về 0; không được đồng nhất chúng với cùng một tốc độ hồi phục có đơn vị thời gian hoặc suy ra cùng một điểm cắt báo động. Khi tái lập cần kiểm tra định nghĩa được mã thực sự dùng.

**Sự đỏ hóa phổ** (*spectral reddening*) là tăng đóng góp của các tần số thấp khi động lực học chậm đi. Bài liệt kê mật độ phổ, tỷ số giữa mật độ phổ tần số thấp/cao và số mũ khớp trên đồ thị log–log. Đây là các biểu diễn có liên hệ với tự tương quan, không phải những bằng chứng độc lập hoàn toàn về cơ chế. Minh họa phổ và phân tích wavelet, tức phân tích theo thang thời gian–tần số, được dẫn tới Hình S3–S4 không nằm trong PDF này. [Tr. 3–4, 16, 18–19]

### 6.2. DFA và ý nghĩa của ngưỡng sau đổi thang

DFA loại xu hướng trong các đoạn và đo quan hệ giữa độ dao động với kích thước đoạn:

$$
F(s)\propto s^{\alpha}.
$$

F là hàm dao động, s là kích thước đoạn và α là số mũ DFA. Nguồn: phần DFA, tr. 4. Không nên nhầm s ở đây với độ dài cửa sổ ngoài dùng để quét dọc toàn chuỗi. Bài nêu khoảng thang thường dùng 10–100 đơn vị và yêu cầu hơn 100 điểm để có ước lượng vững hơn; chỉ báo được đổi thang để mốc 1 tương ứng số mũ 1,5. Công thức đổi thang không được viết đầy đủ trong PDF.

Hình 3 cho xu hướng tăng trong cả hai chuỗi, với CSD tiến về phía mốc chỉ báo 1 còn chuyển đổi qua lại dao động quanh hoặc vượt 1. Đó là bằng chứng về hai ví dụ sau quy trình DFA đã chọn, chưa phải một ngưỡng phân loại trạng thái tới hạn được hiệu chuẩn phổ quát. Phân bố τ ở Hình 3E–F là theo lựa chọn cửa sổ, không phải độ chính xác qua nhiều hiện thực độc lập. [Hình 3; Bước 3–4, tr. 16–17]

### 6.3. Độ lệch chuẩn, hệ số biến thiên, bất đối xứng và độ nhọn

**Độ lệch chuẩn** (*standard deviation*, SD), **hệ số biến thiên** (*coefficient of variation*, CV), **độ bất đối xứng** (*skewness*) và **độ nhọn** (*kurtosis*) mô tả những khía cạnh khác nhau của phân bố. **Lưu ý nguồn quan trọng:** bản in tr. 4 viết biểu thức mang nhãn SD nhưng không có căn bậc hai. Ở tr. 5, biểu thức bất đối xứng chỉ chia cho căn của mômen bậc hai, còn mẫu số độ nhọn là bình phương của chính căn ấy. Các biểu thức in này không phù hợp với phần văn bản gọi chúng là độ lệch chuẩn, mômen chuẩn hóa bậc ba và bậc bốn. Đã đối chiếu trực quan ở độ phân giải cao; đây không chỉ là lỗi trích xuất chữ.

Để không sao chép sai, các định nghĩa tương ứng với ý nghĩa thống kê được giải thích riêng bằng ký hiệu của người phân tích:

$$
\begin{aligned}
\bar z&=\frac{1}{n}\sum_{t=1}^{n}z_t,\qquad
m_k=\frac{1}{n}\sum_{t=1}^{n}(z_t-\bar z)^{k},\\
SD&=\sqrt{\frac{1}{n-1}\sum_{t=1}^{n}(z_t-\bar z)^{2}},\qquad
CV=\frac{SD}{\bar z},\\
\gamma_1&=\frac{m_3}{m_2^{3/2}},\qquad
\kappa=\frac{m_4}{m_2^{2}}.
\end{aligned}
$$

n là số điểm trong cửa sổ; các m là mômen trung tâm; κ là độ nhọn chưa trừ 3. Đây là **làm rõ theo các định nghĩa bằng lời của tr. 4–5**, không phải chép nguyên công thức PDF hay khẳng định mã sử dụng đúng từng hiệu chỉnh mẫu ở trên. CV khó diễn giải khi trung bình gần 0. Không có mã đã kiểm tra trong bước này, nên không suy từ lỗi biểu thức in rằng những đường SD hoặc bất đối xứng tác giả tính cũng sai.

Các chỉ báo phân bố không chỉ thay đổi bởi CSD. Khi chuỗi trộn hai trạng thái, độ phân tán tăng khi cả hai trạng thái được quan sát nhiều, rồi có thể giảm khi phần lớn điểm đã thuộc trạng thái mới. Hướng bất đối xứng còn phụ thuộc trạng thái đích cao hay thấp. Hình 2 minh họa rõ tình huống này: chuỗi chuyển đổi qua lại có SD tăng tới khoảng bước 8.000 rồi giảm, trong khi bất đối xứng tăng. [Tr. 4–5, 15–16; Hình 2H, J]

### 6.4. CH: phát hiện cụm biến thiên lớn trong phần dư

CH không đơn thuần hỏi phương sai có tăng theo thời gian hay không; nó hỏi độ biến thiên ở một bước có liên quan với độ biến thiên ở các bước trước hay không. Trong từng cửa sổ 10%, tác giả chọn AR(p) theo AIC, lấy phần dư, bình phương phần dư rồi hồi quy lên bình phương trễ một bước. [Phần CH, tr. 5; Bước 3, tr. 16]

Một biểu diễn làm rõ phép thử trong bài là:

$$
u_t^{2}=b_0+b_1u_{t-1}^{2}+v_t,\qquad
LM=N_{\mathrm{reg}}R^{2}.
$$

u là phần dư của AR, N là số quan sát thực dùng trong hồi quy phụ và R bình phương là hệ số xác định. Bài mô tả kiểm định nhân tử Lagrange (LM) và so sánh R bình phương với ngưỡng chi bình phương chia cỡ mẫu; công thức LM ở đây viết cách tương đương về quy mô, với một độ trễ nên ngưỡng tiệm cận có một bậc tự do. Không gọi R bình phương tự nó là một đại lượng có phân bố chi bình phương. [Tr. 5; Hình 4]

Hình 4 dùng **mức ý nghĩa 0,1**, không có nghĩa mọi điểm có giá trị p đúng bằng 0,1. CH có ý nghĩa ở nhiều đoạn CSD và trở nên rõ ở phần cuối; ở chuỗi chuyển đổi qua lại nó có ý nghĩa trong toàn bộ đoạn chỉ báo được vẽ. Tuy nhiên, có cụm biến thiên lớn chưa xác định được duy nhất cơ chế phân nhánh hoặc một thời điểm nhảy tương lai. [Bước 3, tr. 16; Hình 4]

### 6.5. BDS: kiểm tra cấu trúc còn sót, không phải xác nhận phân nhánh

BDS kiểm tra giả thuyết phần dư **độc lập và cùng phân phối** (*independent and identically distributed*, i.i.d.) sau khi loại cấu trúc bằng một mô hình trước đó. Bài dùng sai phân bậc nhất, AR(1) và **mô hình phương sai có điều kiện tự hồi quy tổng quát** (*generalized autoregressive conditional heteroskedasticity*, GARCH). Mô hình GARCH liên quan tới họ **phương sai có điều kiện tự hồi quy** (*autoregressive conditional heteroskedasticity*, ARCH). [Phần BDS, tr. 5–6; Bước 3, tr. 16]

Trong thí nghiệm, BDS được tính trên cả đoạn dữ liệu đã chọn và biến đổi log, với chiều nhúng 2 hoặc 3, bán kính bằng 0,5; 0,75; 1 lần độ lệch chuẩn; kiểm tra ý nghĩa bằng 1.000 lần lấy mẫu lại. Phần lớn trường hợp bác bỏ giả thuyết độc lập. Ngoại lệ cụ thể là phần dư GARCH(0,1) của chuỗi chuyển đổi qua lại ở chiều nhúng 2; tại chiều 3, các giá trị vẫn được đánh dấu có ý nghĩa trong Bảng 2. [Bảng 2, tr. 7; Bước 3, tr. 16]

Bác bỏ i.i.d. có thể do phi tuyến, không dừng hoặc cấu trúc bị mô hình trước bỏ sót, như tác giả đã nêu. Vì vậy không được chuyển thành chứng minh chắc chắn có một chuyển tiếp tới hạn. Tác giả đã thử BDS trên cửa sổ nhưng không thu được kết quả nhất quán; kết quả không được vẽ. BDS cần chuỗi dài, nhạy với tiền xử lý; Bảng 3 gợi ý cửa sổ hơn 500 điểm khi dùng theo cửa sổ. [Tr. 6, 14, 16]

## 7. Các phương pháp dựa trên mô hình

### 7.1. DDJ: tách trôi, khuếch tán và bước nhảy

DDJ không cần biết dạng tường minh của f, g hoặc quan sát tác nhân θ. Nó khớp một cấu trúc tổng quát gồm biến thiên trơn cục bộ, các nhiễu nhỏ và các cú nhảy gián đoạn:

$$
dx_t=\mu(x_{t-},\theta_t)\,dt
+\sigma_D(x_{t-},\theta_t)\,dW
+d\left(\sum_{n=1}^{N_t}Z_n\right).
$$

Đây là Phương trình (3), tr. 7. μ là trôi, σD là biên độ khuếch tán, N đếm số bước nhảy và Z là độ lớn bước nhảy; dấu trừ ở chỉ số thời gian nghĩa là giá trị ngay trước bước cập nhật. Bài giả định bước nhảy có trung bình 0, phương sai riêng, với xác suất xuất hiện trong một khoảng ngắn tỷ lệ với cường độ λ. Các thành phần được ước lượng bằng hồi quy phi tham số. [Phương trình (2)–(3), tr. 7]

Hai quan hệ được bài dùng là:

$$
\widehat{\sigma}_{D}^{2}
=\widehat{\sigma}_{T}^{2}-\widehat{\lambda}\,\widehat{\sigma}_{Z}^{2},\qquad
\widehat S=\widehat M^{2}-(\widehat M^{1})^{2}.
$$

Quan hệ đầu tách phần phương sai do các cú nhảy khỏi tổng đóng góp nhiễu; quan hệ sau là phương sai có điều kiện từ mômen có điều kiện bậc hai và bình phương mômen bậc một. Ký hiệu M với số mũ 1, 2 chỉ **bậc mômen**, không phải bình phương hai lần. Bản phân tích rút gọn các đối số của công thức ở tr. 7 để dễ đọc. Không được đồng nhất phương sai của gia số/đóng góp nhiễu với phương sai trạng thái hoặc với CH của phần dư.

DDJ được khớp toàn chuỗi sau log, không quét cửa sổ như SD. Ở CSD, tác giả thấy phương sai có điều kiện, phương sai tổng và cường độ nhảy tăng, trong khi khuếch tán giảm. Ở chuỗi chuyển đổi qua lại, các đường theo thời gian rất dao động; đồ thị theo giá trị sinh khối sau log cho hình dạng dễ đọc hơn nhờ làm trơn. Một biểu diễn được làm trơn dễ nhìn hơn không tự chứng minh dự báo trước thời gian tốt hơn. [Hình 5–6, tr. 8–9; Bước 3, tr. 16]

Tác giả gợi ý đối chiếu phương sai có điều kiện với khuếch tán có thể giúp phân biệt chuyển tiếp ở phần trôi với thay đổi ở phần nhiễu. Đây là triển vọng cơ chế, chưa có một thí nghiệm phân loại nhiều cơ chế độc lập để tính độ chính xác. Bài nêu khả năng sinh dữ liệu từ mô hình đã khớp rồi khớp lại bằng mô phỏng Monte Carlo để đánh giá sai số; không trình bày những dải sai số đó trong Hình 5–6. [Tr. 7, 17]

### 7.2. AR biến thiên theo thời gian: động lực và sai số đo

Cấu trúc mô hình là:

$$
\begin{aligned}
x(t)&=b_0(t-1)+\sum_{i=1}^{p}b_i(t-1)
\left[x(t-i)-b_0(t-1)\right]+e(t),\\
b_i(t)&=b_i(t-1)+\phi_i(t),\\
x^{*}(t)&=x(t)+a(t).
\end{aligned}
$$

Dòng đầu là Phương trình (4a), dòng hai là (4b), dòng cuối là phương trình quan sát (5), tr. 7–8. b₀ xác định mức trung bình, các b còn lại mô tả động lực quanh trung bình; φ cho hệ số biến thiên như bước ngẫu nhiên; e là nhiễu quá trình và a là sai số đo. Tác giả dùng khung trạng thái, lọc Kalman và ước lượng hợp lý cực đại. Không nên tự đồng nhất đường trạng thái ước lượng với quỹ đạo thật chỉ vì phần sai khác được mô hình quy vào sai số đo.

Hai lựa chọn được so sánh là chỉ cho trung bình đổi theo thời gian, hoặc cho cả trung bình và hệ số động lực thay đổi. Bài dùng **kiểm định tỷ số hợp lý** (*likelihood-ratio test*, LRT) và AIC để so sánh. Các phương sai của bước ngẫu nhiên có giả thuyết không bằng 0 nằm ở biên tham số; tr. 9 nêu một hiệu chỉnh hỗn hợp chi bình phương cho LRT. Cần xem điều kiện đầy đủ ở nguồn [38] trước khi áp dụng máy móc công thức hiệu chỉnh cho một mô hình khác.

Hàm chọn mô hình AIC có thể viết theo ký hiệu chuẩn để giải thích vai trò:

$$
AIC=2k-2\log\widehat L.
$$

k là số tham số và L có mũ là hợp lý tại nghiệm khớp. Đây là công thức giải thích của người phân tích cho tiêu chí được bài dùng, không phải một hàm mục tiêu mới của công trình. LRT trả lời sự khác biệt phù hợp giữa các mô hình đặt ra, còn AIC cân bằng mức khớp với độ phức tạp; cả hai không trực tiếp đo chất lượng dự báo sự kiện.

Đại lượng λ ở nhánh này là nghịch đảo nghiệm đặc trưng của AR rời rạc: tiến về 1 biểu thị hồi phục yếu, vượt 1 gợi ý mất tính dừng trong mô hình cục bộ. Nó khác trị riêng âm của một phương trình liên tục thường dùng trong giải thích CSD. Đừng dùng chung ký hiệu λ rồi tự suy ra hai đại lượng bằng nhau. [Phần AR theo thời gian, tr. 7, 9; Hình 7]

Tác giả thử p bằng 1, 2, 3 trên chuỗi CSD đã log và chuẩn hóa. Mô hình cho phép hệ số động lực đổi khớp tốt hơn mô hình chỉ cho trung bình đổi, với giá trị p nhỏ hơn 0,0001 theo các LRT được báo cáo. AR(1) có AIC tốt nhất, nhưng AR(3) chỉ kém 0,8059 đơn vị AIC; xu hướng λ lại khác đáng kể: τ bằng 0,736 ở AR(1), chỉ 0,164 ở AR(3). Điều này cho thấy kết luận động lực không ổn định hoàn toàn theo bậc mô hình dù mức khớp gần nhau. [Bước 3, tr. 16; Hình 7]

### 7.3. AR phân ngưỡng: xác định chế độ đã xuất hiện

Mô hình khớp hai quá trình tự hồi quy, chuyển qua lại khi trạng thái vượt một ngưỡng. Có thể viết gọn Phương trình (6a–b) bằng chỉ số chế độ j:

$$
\begin{aligned}
x(t)&=b_0^{(j)}+\sum_{i=1}^{p}b_i^{(j)}
\left[x(t-i)-b_0^{(j)}\right]+e(t),\\
j&=1\quad\text{if }x(t-1)\leq\kappa,\\
j&=2\quad\text{if }x(t-1)>\kappa.
\end{aligned}
$$

Hai bộ hệ số được bài ký hiệu bằng dấu phẩy trên; bản phân tích thay bằng chỉ số chế độ. κ thay tên ngưỡng c của mô hình AR để tránh nhầm với **mức khai thác c** trong phương trình sinh thái. Mô hình còn dùng phương trình sai số đo (5). Nguồn: tr. 10–11.

Thí nghiệm chỉ dùng chuỗi chuyển đổi qua lại đã log và chuẩn hóa, lấy khoảng bước 7.200–7.700, được bài gọi là 500 quan sát. AR phân ngưỡng bậc 3 khớp tốt nhất trong ba bậc được thử; so với AR(3) một chế độ, LRT được báo cáo là 27,79 với giá trị p nhỏ hơn 0,0001. Tuy vậy, bậc 2 chỉ kém bậc 3 khoảng 1,75 đơn vị AIC. Ngưỡng phân chế độ trong Hình 8 là 0,1 trên thang trạng thái đã biến đổi, không phải ngưỡng khai thác 2,604. [Hình 8; Bước 3, tr. 16]

Tác giả nói rõ AR phân ngưỡng và phân tích thế **không phải cảnh báo sớm theo nghĩa chặt**, vì việc chuyển qua lại chứng tỏ đã có các lần đổi trạng thái. Chúng có thể báo sự hiện diện nhiều chế độ trước khi hệ ổn định hẳn ở chế độ mới, nhưng không tự xác định khi nào lần chuyển vĩnh viễn sẽ xảy ra. [Tr. 11]

### 7.4. Phân tích thế và số trạng thái

Mô hình thế được bài viết:

$$
dZ=-\frac{dU}{dz}\,dt+\sigma\,dW.
$$

Đây là Phương trình (7), tr. 11. U là thế, độ dốc âm của thế xác định trôi; phương pháp khớp đa thức để suy số giếng thế, được diễn giải như những trạng thái. **Lưu ý nguồn:** câu ngay dưới (7) gán bậc chẵn cho đạo hàm dU/dz và gọi nó là thế; cách phân biệt nhất quán là U là thế còn dU/dz là đạo hàm. Bậc hai hoặc bậc bốn của thế không phải cùng bậc với đạo hàm. Bản phân tích không âm thầm chuyển câu đó thành một đặc tả thuật toán đầy đủ.

Phân tích được thực hiện trên dữ liệu không biến đổi với cửa sổ từ 10 điểm tới nửa chuỗi. Với CSD, một giếng chiếm ưu thế nhưng có vùng cho hai giếng, nhất là cửa sổ lớn. Với chuyển đổi qua lại, phần lớn chuỗi lại được nhận diện là một giếng; gần 2.000 điểm cuối xuất hiện nhiều giếng và có vùng vượt 5 giếng. Tác giả nhận xét khi đó dữ liệu ở ranh giới không có một thế rõ ràng. Đây không phải kết quả tái dựng chính xác hai trạng thái cho toàn chuỗi. [Hình 9; Bước 3, tr. 17]

## 8. Kết quả định lượng và cách đọc bằng chứng

### 8.1. Cùng một chỉ báo có thể đổi mức xu hướng theo đầu vào

Các giá trị τ đọc từ Hình 2 là:

| Chuỗi và chỉ báo                       | Dữ liệu gốc | Sau xử lý tương ứng              |
| ------------------------------------------ | -------------- | ------------------------------------- |
| CSD — tự tương quan                    | 0,911          | 0,944 sau loại xu hướng            |
| CSD — SD                                  | 0,939          | 0,705 sau loại xu hướng            |
| CSD — bất đối xứng                    | −0,436        | −0,475 sau loại xu hướng          |
| Chuyển đổi qua lại — tự tương quan | 0,937          | 0,618 sau biến đổi log/chuẩn hóa |
| Chuyển đổi qua lại — SD               | 0,208          | 0,656 sau biến đổi log/chuẩn hóa |
| Chuyển đổi qua lại — bất đối xứng | 0,969          | 0,978 sau biến đổi log/chuẩn hóa |

Nguồn: Hình 2E–J, tr. 4. Đây là xu hướng trên hai hiện thực, không phải trung bình của nhiều lần mô phỏng. τ dương của SD chuyển đổi qua lại không có nghĩa SD tăng đến hết chuỗi: đường SD đạt đỉnh rồi giảm. Sau xử lý, dữ liệu không còn cùng đơn vị nên không so sánh trực tiếp độ lớn SD giữa đường đen và đường xanh như một mức cải thiện hiệu năng.

### 8.2. Độ nhạy và ý nghĩa thống kê là hai câu hỏi khác nhau

Hình 10 cho thấy xu hướng AR(1) CSD bền hơn với lưới lựa chọn đã xét, SD nhạy với bộ lọc nhỏ, còn bất đối xứng có xu hướng âm. Bước kiểm định bằng chuỗi thay thế lại cho kết quả:

| Chỉ báo trên chuỗi CSD | Kết quả kiểm định được tác giả báo cáo                                                         |
| -------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Tự tương quan           | p nhỏ hơn 0,025 trên các tổ hợp được khảo sát; p không lớn hơn 0,001 ở lựa chọn minh họa |
| SD                         | Có ý nghĩa ở nhiều lựa chọn; lựa chọn minh họa có p bằng 0,073                                 |
| Bất đối xứng           | Không có ý nghĩa theo phép thử của bài; p bằng 0,8 ở lựa chọn minh họa                        |

Nguồn: Bước 5, tr. 17; Hình 11, tr. 13. p bằng 0,073 đạt mức 0,1 mà bài minh họa nhưng không đạt mức 0,05; không được thay ngưỡng mà vẫn gọi mọi kết quả là có ý nghĩa. p không lớn hơn 0,001 là mức báo cáo với 1.000 chuỗi thay thế, không phải một ước lượng vô hạn chính xác về xác suất.

**Điểm cần kiểm tra khi tái lập:** Hình 2I và văn bản cho τ bất đối xứng sau lọc bằng −0,475, trong khi tam giác chỉ giá trị quan sát ở Hình 11F nằm ở phía dương. PDF chưa giải thích rõ một quy ước đổi dấu giữa hai hình. Bản phân tích giữ riêng τ và p theo nơi chúng được báo cáo; không tự đảo dấu hay sửa giá trị p để làm hai hình khớp nhau.

### 8.3. Mỗi hình kiểm tra điều gì và không chứng minh điều gì?

| Hình/bảng                  | Bằng chứng chính                                                                      | Giới hạn cần giữ                                                                                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hình 1, tr. 3               | Mô hình có nhánh hút thay thế và hai chuỗi đi tới khai thác quá mức         | Không phải hai hệ độc lập; nhiều yếu tố thiết lập đổi đồng thời                                                                            |
| Hình 2, tr. 4               | Tự tương quan, SD, bất đối xứng phụ thuộc chế độ và tiền xử lý           | Không có bộ báo động; cửa sổ chồng lấn và đoạn kết thúc đã được chọn                                                                  |
| Hình 3, tr. 5               | DFA tăng trong hai ví dụ; có kiểm tra theo cửa sổ                                 | Phân bố τ theo cửa sổ không là khoảng tin cậy qua nhiều hiện thực                                                                              |
| Hình 4, tr. 6               | CH trên phần dư AR có cụm giá trị có ý nghĩa                                   | Ý nghĩa cục bộ không là tỷ lệ cảnh báo sai của một quy tắc sự kiện                                                                          |
| Bảng 2, tr. 7               | BDS thường bác bỏ độc lập, phụ thuộc mô hình phần dư và chiều nhúng      | Không bác bỏ ở một số trường hợp; bác bỏ cũng không nhận diện duy nhất phân nhánh                                                        |
| Hình 5–6, tr. 8–9         | DDJ cho cấu trúc theo thời gian và theo trạng thái khác nhau                      | Làm trơn theo trạng thái không chứng minh dự báo thời gian; chưa có xác suất phân loại cơ chế                                             |
| Hình 7, tr. 10              | Hệ số động lực biến thiên khớp tốt; λ tăng khác nhau theo bậc AR            | Chất lượng khớp gần nhau không bảo đảm kết luận hồi phục giống nhau; hình chỉ áp vào CSD dù tiêu đề chú thích nhắc cả hai chuỗi |
| Hình 8, tr. 10              | AR phân ngưỡng phù hợp đoạn chuyển đổi qua lại hơn AR một chế độ         | Nhận diện chế độ đã xuất hiện; không ước lượng ngưỡng khai thác hoặc thời gian đổi vĩnh viễn                                        |
| Hình 9, tr. 11              | Số giếng thế phụ thuộc thời điểm và độ dài cửa sổ                          | Có giếng phụ và số giếng rất lớn; chưa xác nhận số tập hút thật bằng chỉ báo này                                                        |
| Hình 10, tr. 12             | Độ nhạy của ba chỉ báo CSD với cửa sổ/bộ lọc                                  | Không quét đầy đủ mọi phương pháp và mọi loại dữ liệu                                                                                       |
| Hình 11, tr. 13             | Xu hướng so với mô hình tuyến tính dừng được khớp làm giả thuyết không   | Không đo dự báo ngoài mẫu; kết luận có điều kiện theo mô hình không, hướng kiểm định và lựa chọn tham số                           |
| Hình 12 và Bảng 3, tr. 14 | Quy trình và các lưu ý thực hành, gồm giám sát, nhiễu, tác nhân và xử lý | Các quy tắc kinh nghiệm không phải định lý hoặc bộ thông số mặc định bảo đảm hiệu năng                                                 |

## 9. Thảo luận: đóng góp, giới hạn và khả năng chuyển sang y sinh

### 9.1. Đóng góp thực chất

Bài làm cụ thể điều một danh sách EWS riêng lẻ chưa giải quyết: **cùng dữ liệu nhưng khác biến đổi, cửa sổ và mô hình có thể cho kết luận khác**. Bước độ nhạy và bước kiểm định ý nghĩa giúp phân biệt “có đường xu hướng” với “xu hướng bất thường so với một mô hình không”. Việc đưa cả phương pháp dựa trên đại lượng thống kê và dựa trên mô hình vào cùng một quy trình cũng giúp kiểm tra mức phù hợp giữa các diễn giải động lực học. [Hình 2, 7, 10–12; Thảo luận, tr. 17–18]

**Tác giả khẳng định:** không có một phương pháp tốt nhất và kết hợp các tiếp cận là cách tốt để nhận biết tín hiệu vững. **Bằng chứng hỗ trợ:** không phải mọi phương pháp đều cung cấp thông tin như nhau trong hai ví dụ; một số không nhất quán hoặc phụ thuộc lựa chọn. **Diễn giải của người phân tích:** chưa có phép kiểm định một bộ kết hợp cụ thể hoặc bảng tỷ lệ lỗi để định lượng lợi ích tăng thêm của việc kết hợp. Không nên coi “không có phương pháp tốt nhất trên hai ví dụ” là kết luận xếp hạng phổ quát.

### 9.2. Các giới hạn có ảnh hưởng trực tiếp tới suy luận

- **Quần thể kiểm chứng nhỏ:** hai chuỗi là hai hiện thực đơn lẻ của một họ mô hình sinh khối, không có khảo sát hiệu năng trên nhiều hạt giống hoặc nhiều họ cơ chế. Tác giả nêu chính việc kiểm tra nhiều hiện thực và thử mù là hướng cần làm. [Thảo luận, tr. 18]
- **Không có đánh giá âm tính độc lập:** chuỗi thay thế phục vụ mô hình không cho xu hướng, không thay thế một tập hệ không có chuyển tiếp để tính cảnh báo sai của quy tắc phát hiện sự kiện. [Bước 5, tr. 17]
- **Xử lý và chọn đoạn có điều kiện theo dữ liệu:** cắt CSD tới thời điểm chuyển đổi đã biết, dùng toàn bộ chuỗi chuyển đổi qua lại, và khớp nhiều mô hình trên đoạn đầy đủ. Điều này phù hợp minh họa hồi cứu nhưng chưa xác nhận năng lực trực tuyến. [Bước 1–3, tr. 15–17]
- **Phụ thuộc thống kê:** cửa sổ chồng lấn dùng lại điểm; các phương pháp cùng đo trí nhớ hoặc độ phân tán nên không là bằng chứng độc lập hoàn toàn. Giá trị τ và số điểm của đường chỉ báo không thay thế số lần lặp độc lập. Đây là diễn giải thống kê của người phân tích.
- **Giả định cơ chế:** các chỉ báo CSD gắn với điều kiện tiến chậm tới mất ổn định. Cú sốc lớn, động lực hỗn loạn xa phân nhánh cục bộ hoặc điều kiện thay đổi nhanh có thể gây bỏ sót. Việc nhận diện chuyển đổi qua lại có thể xảy ra sau nhiều lần đổi trạng thái. [Tr. 11; Thảo luận, tr. 18]
- **Không phải mọi sai khác đều do cùng một nguyên nhân:** σ, tốc độ tác nhân, độ dài và nguồn nhiễu thêm thay đổi giữa hai kịch bản; mô hình đã khớp cũng có các giả định phân bố và cấu trúc riêng. Chưa có thiết kế loại bỏ từng yếu tố để phân lập tất cả nguyên nhân khác biệt. [Dữ liệu, tr. 14–15]
- **Bản in chưa đủ để triển khai nguyên xi:** công thức SD và mômen chuẩn hóa, cách gán bậc đa thức thế và dấu τ giữa các hình cần được kiểm tra với mã. Đây không tự chứng minh kết quả tính toán gốc sai. [Tr. 4–5, 11; Hình 2I, 11F]

### 9.3. Liên hệ với tín hiệu y sinh — giả thuyết, chưa có dữ liệu kiểm chứng trong bài

Bài không phân tích dữ liệu người bệnh, nhưng trực tiếp bàn tới **điện não đồ** (*electroencephalography*, EEG) như ví dụ chuỗi tần số cao có chu kỳ, có thể cần phân tích Fourier hoặc wavelet. Tác giả đồng thời nói các kỹ thuật tách thành phần theo chu kỳ chưa được kiểm chứng đầy đủ cho phát hiện chuyển tiếp tới hạn. Minh họa wavelet mà bài dẫn tới Hình S4 vẫn là dữ liệu mô phỏng sinh thái, không phải dữ liệu EEG. [Thảo luận và Tài liệu bổ sung, tr. 18–19]

**Giả thuyết của người phân tích:** có thể dùng khung năm bước để thiết kế phép kiểm tra EWS trên EEG, **điện tâm đồ** (*electrocardiography*, ECG) hoặc **tín hiệu quang thể tích** (*photoplethysmography*, PPG), nhưng cần xác định biến trạng thái và cơ chế phù hợp. Không nên mặc định dao động mang nhịp của tín hiệu thô là dao động nhỏ quanh một cân bằng một chiều, hoặc mọi cơn bệnh đều là phân nhánh nếp gấp.

Một kế hoạch bổ sung sẽ phải: chọn đặc trưng quan sát và thang thời gian; tách nhiễu đo khỏi biến đổi động lực khi có thể; kiểm tra bộ lọc và cửa sổ theo cách chỉ dùng quá khứ; định nghĩa sự kiện và đoạn không có sự kiện; đánh giá trên những người/đoạn dữ liệu độc lập với giai đoạn phát triển. Các đại lượng cần báo cáo là thời gian báo trước, cảnh báo sai và bỏ sót ở mức cá thể. Đây là kế hoạch chưa thực hiện, không phải một khoảng trống tài liệu hoặc tính hợp lệ lâm sàng đã được xác lập.

## 10. Hồ sơ phương pháp

| Trường                                                  | Nội dung                                                                                                                                                                                                                                                                |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Bài toán (Problem)**                            | Phát hiện và diễn giải dấu hiệu của thay đổi trí nhớ, độ biến thiên hoặc nhiều chế độ trong chuỗi có khả năng tiến tới chuyển tiếp tới hạn.                                                                                               |
| **Đầu vào (Input)**                              | Một chuỗi sinh khối mô phỏng, có sai số đo; các phiên bản gốc, phần dư, log hoặc chuẩn hóa tùy phương pháp. Hai kịch bản CSD và chuyển đổi qua lại.                                                                                          |
| **Thông tin biết trước (Known information)**    | Người thiết kế biết phương trình, tham số và lịch tăng khai thác; người áp dụng được giả định chỉ có chuỗi. Cần xác định lựa chọn xử lý, bậc mô hình, cửa sổ và mô hình dùng làm giả thuyết không.                        |
| **Đầu ra (Output)**                               | Chuỗi chỉ báo và τ; bản đồ độ nhạy, p theo mô hình không; ước lượng DDJ, hệ số AR và đại lượng hồi phục, ngưỡng phân chế độ hoặc số giếng thế.                                                                                      |
| **Phương án đối chiếu (Existing baseline)**   | Dữ liệu gốc so với xử lý; nhiều chỉ báo trên cùng chuỗi; AR cố định/chỉ đổi trung bình so với đổi hệ số; AR một chế độ so với phân ngưỡng; chuỗi ARMA thay thế làm mô hình không.                                                  |
| **Thành phần mới (New component)**               | Tích hợp thành quy trình thực hành năm bước, các ví dụ so sánh và chỉ dẫn công cụ. Bảng 1 định vị số mũ phổ như chỉ báo trong bài, nhưng công cụ tính số mũ phổ được kế thừa.                                                   |
| **Giả định (Assumptions)**                       | Phần lớn diễn giải gắn với tiến chậm tới nếp gấp hoặc nhiều trạng thái; lấy mẫu phù hợp; gần dừng trong cửa sổ; dạng nhiễu và mô hình được chọn đủ thích hợp; phép biến đổi không làm mất cấu trúc quan tâm.               |
| **Kiểm chứng (Validation)**                       | Hai hiện thực đơn lẻ của một mô hình sinh thái; 1.000 chuỗi thay thế cho kiểm định xu hướng; 1.000 lần lấy mẫu lại cho BDS; so sánh AIC/LRT và lưới độ nhạy. Không có kiểm tra dự báo độc lập trên nhiều hệ.                      |
| **Kết quả chính (Main finding)**                 | AR(1) có xu hướng mạnh và có ý nghĩa trong ví dụ CSD; SD và bất đối xứng phụ thuộc xử lý/chế độ; mô hình AR và số giếng có độ nhạy riêng. Không có phương pháp được chứng minh là tốt nhất hoặc được hiệu chuẩn chung. |
| **Câu hỏi còn mở (Unresolved questions)**       | Tỷ lệ lỗi và thời gian báo trước trên nhiều hiện thực/hệ thực; chọn hoặc kết hợp chỉ báo; quan sát không đều; mô hình không và nhiều lựa chọn; phân loại cơ chế; thống nhất công thức và mã nguồn.                             |
| **Khả năng tái lập (Reproduction feasibility)** | Có mô hình, nhiều thông số và nguồn công cụ được nêu; khả thi để xây dựng bản tái lập có kiểm soát. Tái lập chính xác cần đúng dữ liệu, mã/phiên bản, hạt giống, bước số và quy ước xử lý chưa đủ trong PDF.           |

Nguồn hồ sơ: Phương pháp, tr. 2–11; Dữ liệu/Kết quả, tr. 14–17; Hình 1–12; Bảng 1–3; Thảo luận, tr. 17–18. Các đánh giá tính khả thi và giới hạn là nhận định của người phân tích.

## 11. Quyết định tái lập, nguồn công cụ và tài liệu đọc tiếp

**Quyết định: ứng viên tái lập (Reproduction candidate), có điều kiện.** Bài có lợi thế là cùng một mô hình sinh dữ liệu, các thông số chính, ví dụ từng bước và nguồn công cụ. Mục tiêu hợp lý là tái lập một nhánh rõ trước, chẳng hạn tự tương quan/SD CSD cùng kiểm tra độ nhạy và chuỗi thay thế; không nên tuyên bố tái lập toàn bộ bộ công cụ chỉ vì một đường chỉ báo giống về hình dạng. Chưa chạy mô phỏng hoặc tải mã trong bước hiện tại.

### 11.1. Những nguồn công cụ mà PDF nêu

| Phần việc                              | Thông tin trong PDF                                                                                                              | Điều chưa xác nhận                                                                                                 |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| Sinh dữ liệu                           | MATLAB R2011a và GRIND                                                                                                           | Chưa có tệp hai chuỗi, hạt giống và cấu hình mô phỏng được tải/kiểm tra                                 |
| Phần lớn chỉ báo                     | R 2.12.0 và gói `earlywarnings`                                                                                               | Chưa xác nhận phiên bản gói tương ứng, mã đang hoạt động hoặc hành vi công thức của phiên bản đó |
| DFA và phân tích thế                 | MATLAB R2011a, các phần tính bằng Fortran/C và kịch bản dòng lệnh; PDF nói mã có thể được cung cấp từ tác giả | Không có những tệp đó trong PDF hiện tại; chưa liên hệ hay tải thêm                                        |
| AR theo thời gian và AR phân ngưỡng | MATLAB R2011a; PDF chỉ sang tài liệu bổ sung của [38]                                                                        | Chưa đọc mã, cách lọc hay cấu hình kiểm định cụ thể                                                        |
| Ví dụ thực hành                      | PDF nêu các địa chỉ của GRIND, R-Forge và trang hướng dẫn cảnh báo sớm                                               | Chỉ là địa chỉ được ghi năm 2012; chưa xác nhận khả năng truy cập hiện tại                             |

Nguồn: tr. 15. Tên phần mềm và gói được giữ nguyên để nhận diện. Các hình bổ sung S1–S4 chỉ được mô tả ở tr. 18–19; chúng không nằm trong tệp PDF đã đọc. Không khẳng định tài nguyên không tồn tại chỉ vì chưa được truy cập ở bước này.

### 11.2. Thứ tự tái lập được đề xuất

1. **Chốt định nghĩa và đầu vào.** Kiểm tra công thức SD, bất đối xứng, độ nhọn trong mã; xác định chuỗi nào được log hay log cộng 1, chuẩn hóa thế nào và lọc biên ra sao. Làm rõ dấu τ ở Hình 11F trước khi so sánh kiểm định.
2. **Khôi phục hai chuỗi hoặc tạo chuỗi thay thế có ghi rõ khác biệt.** Cần hạt giống, điều kiện đầu, bước tích phân, bước lưu mẫu, cách tạo và cộng dòng vào có tương quan. Không tự sửa ngoặc công thức dòng vào mà gọi đó là tái lập đúng bản gốc.
3. **Tái lập nhánh CSD của Hình 2, 10, 11.** Kiểm tra đoạn 970 điểm, cửa sổ 485 điểm và độ rộng lọc minh họa, rồi quét độ nhạy và chọn ARMA sinh 1.000 chuỗi thay thế. Ghi rõ hướng kiểm định, cách xử lý đồng hạng và quy tắc đếm giá trị p.
4. **Tách việc khớp mô hình khỏi đánh giá cơ chế.** Với AR theo thời gian, kiểm tra bậc 1–3 và λ; với AR phân ngưỡng, giữ ngưỡng trạng thái khác ngưỡng khai thác; với DDJ/thế, công bố độ rộng hạt nhân, bậc đa thức và tiêu chí chọn mô hình.
5. **Mở rộng đánh giá chỉ sau khi tái lập cơ bản.** Dùng nhiều hiện thực, các chuỗi không chuyển tiếp và quy tắc báo động chốt trước; báo thời gian báo trước, cảnh báo sai/bỏ sót và độ nhạy với dữ liệu thiếu, nhiễu đo, tốc độ tác nhân. Đây là nghiên cứu bổ sung, chưa thực hiện và không phải kết quả đã có của bài.

Các bước này là đề xuất của người phân tích, dựa trên phần Dữ liệu/Kết quả và những giới hạn tác giả nêu ở tr. 18. Thông tin còn thiếu đặc biệt gồm hạt giống, thuật toán và bước tích phân, đầy đủ điều kiện đầu, phiên bản công cụ, quy ước biến đổi theo từng nhánh, tham số hồi quy phi tham số và quy tắc so sánh nhiều phép thử. Không được suy ra một giá trị mặc định chỉ vì không thấy nó trong PDF.

### 11.3. Tài liệu cần đọc tiếp

Các mục dưới đây được dẫn theo danh mục và vai trò trong PDF hiện tại; chưa được đọc độc lập trong bước phân tích này. Tình trạng xuất bản, gồm chữ “đang in”, được giữ theo bài năm 2012, không phải xác minh trạng thái hiện nay.

| Ưu tiên | Nguồn được bài dẫn, kèm nghĩa tiếng Việt                                                                                                                                                                                                                              | Câu hỏi cần kiểm tra                                                                                               |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| 1         | [38] A. R. Ives, V. Dakos, *Detecting dynamical changes in nonlinear time series using locally linear state-space models* — “Phát hiện thay đổi động lực trong chuỗi phi tuyến bằng mô hình trạng thái tuyến tính cục bộ”, *Ecosphere*, ghi đang in   | Mã AR theo thời gian/phân ngưỡng, sai số đo, thuật toán lọc và điều kiện LRT ở biên tham số           |
| 2         | [16] S. R. Carpenter, W. A. Brock (2011), *Early warnings of unknown nonlinear shifts: a nonparametric approach* — “Cảnh báo sớm cho chuyển đổi phi tuyến chưa biết: tiếp cận phi tham số”                                                                     | Chi tiết ước lượng DDJ, băng thông hạt nhân, mômen có điều kiện và sai số Monte Carlo                  |
| 3         | [8] V. Dakos và cộng sự (2008), *Slowing down as an early warning signal for abrupt climate change* — “Chậm dần như dấu hiệu cảnh báo sớm cho biến đổi khí hậu đột ngột”                                                                                | Bộ lọc, cửa sổ và phương pháp chuỗi thay thế được kế thừa                                               |
| 4         | [27] T. M. Lenton và cộng sự (2012), *Early warning of climate tipping points from critical slowing down: comparing methods to improve robustness* — “Cảnh báo sớm điểm chuyển khí hậu từ chậm dần tới hạn: so sánh phương pháp để tăng độ vững” | DFA, đổi thang số mũ và ảnh hưởng xử lý/thang lấy mẫu                                                      |
| 5         | [32] D. A. Seekell, S. R. Carpenter, M. L. Pace (2011), *Conditional heteroscedasticity as a leading indicator of ecological regime shifts* — “Phương sai có điều kiện thay đổi như chỉ báo đi trước chuyển chế độ sinh thái”                           | Cách kiểm định CH, cỡ cửa sổ và giả định của thống kê                                                    |
| 6         | [33] W. A. Brock, W. Dechert, J. Scheinkman, B. LeBaron (1996), *A test for independence based upon the correlation dimension* — “Kiểm định độc lập dựa trên số chiều tương quan”                                                                              | Giả thuyết BDS, lựa chọn bán kính/chiều nhúng và ý nghĩa của bác bỏ độc lập                           |
| 7         | [43] V. N. Livina, F. Kwasniok, T. M. Lenton (2010), *Potential analysis reveals changing number of climate states during the last 60 kyr* — “Phân tích thế cho thấy số trạng thái khí hậu thay đổi trong 60 nghìn năm gần đây”                            | Chọn bậc đa thức thế, độ tin cậy số giếng và ảnh hưởng cửa sổ                                          |
| 8         | [51] J. Theiler và cộng sự (1992), *Testing for nonlinearity in time-series — the method of surrogate data* — “Kiểm định phi tuyến trong chuỗi thời gian bằng phương pháp dữ liệu thay thế”                                                               | Mô hình không nào được bảo toàn bởi một phép sinh thay thế và phép thử thực sự loại trừ điều gì |

Nguồn: danh mục tài liệu, tr. 19–20. Đây là kế hoạch đọc tiếp, không phải các bằng chứng ngoài đã được dùng để bổ sung kết quả của PDF.

## 12. Ghi nhận kiểm tra bản phân tích

Đã đọc toàn bộ PDF và đối chiếu hình, bảng, công thức trọng tâm. Đã phân biệt: hai hiện thực đơn lẻ với một quần thể nhiều lần lặp; 1.000 chuỗi thay thế với 1.000 lần đánh giá dự báo; SD với phương sai; phương sai có điều kiện DDJ với CH; ngưỡng phân chế độ với ngưỡng khai thác; so sánh AIC/LRT với kiểm chứng dự báo ngoài mẫu. Các biểu thức không nhất quán trong bản in được chỉ rõ, không âm thầm sửa hoặc suy ra mã cũng sai.

Đã kiểm tra tiếng Việt và định nghĩa viết tắt. Các công thức dùng khối dollar kép, với chú giải nguồn và ký hiệu; đã đọc lại tệp trên đĩa để kiểm tra cặp dấu, ngoặc, môi trường căn chỉnh và ký tự điều khiển lỗi. Đây là kiểm tra cú pháp, chưa phải xác nhận hiển thị toàn bộ bằng trình xem Markdown hỗ trợ toán. Chưa chạy tái lập, chưa tải mã hoặc tài liệu bổ sung; không sửa tài liệu khác và giữ phần kiểm định phản biện cho bước sau.

## Critical Audit (chờ Prompt 02)
