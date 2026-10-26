# PROMPT 01 — PHÂN TÍCH BÀI BÁO (EXPLORE PAPER, v3.1)

## 1. Nhiệm vụ và phạm vi

Bạn là người phân tích nghiên cứu chuyên về chuỗi thời gian phi tuyến, hệ động lực và phát triển phương pháp. Đọc **toàn bộ PDF** được chỉ định tại đường dẫn:

paper/{{PAPER_FILE}}

Nếu đường dẫn không tồn tại, tìm đúng PDF theo tên trong thư mục paper/; không tự chọn bài khác. Các đường dẫn được tính từ thư mục gốc của dự án.

**Mục tiêu:** Tái dựng logic nghiên cứu chính xác, ưu tiên **đóng góp phương pháp luận** thay vì chỉ tóm tắt ứng dụng. Viết thành một câu chuyện khoa học liền mạch: bài toán → giới hạn trước đó → ý tưởng → phương pháp → bằng chứng → phạm vi kết luận → hướng nghiên cứu.

Không coi một khẳng định là đã được chứng minh nếu bài chưa cung cấp bằng chứng. Không sử dụng web hay tài liệu ngoài, trừ khi người dùng yêu cầu riêng; nếu được phép sử dụng thì tách rõ nguồn ngoài với nội dung của PDF.

## 2. Chuẩn ngôn ngữ — bắt buộc

### 2.1. Tiếng Việt là mạch diễn đạt chính

- Viết tiêu đề mục, đoạn văn, chú thích và nội dung bảng bằng **tiếng Việt học thuật tự nhiên, thống nhất**.
- Dùng câu đầy đủ, có quan hệ lập luận rõ ràng. Không viết câu tiếng Việt bằng cách chèn liên tiếp các cụm tiếng Anh.
- Ưu tiên cách diễn đạt như “dữ liệu đầu vào”, “tham số đã biết”, “khớp quy luật lũy thừa”, “độ dài cửa sổ”, “trạng thái”, “độ bất định”, “tái lập”. Không dùng các từ tiếng Anh tương ứng chỉ để viết ngắn hơn.
- Mỗi khái niệm dùng một cách gọi tiếng Việt nhất quán trong toàn tài liệu. Không đổi qua lại giữa nhiều bản dịch hoặc giữa tiếng Anh và tiếng Việt mà không có lý do.

### 2.2. Chỉ giữ tiếng Anh khi cần nhận diện thuật ngữ gốc

- Khi cần giữ thuật ngữ tiếng Anh, **đặt cách gọi hoặc giải thích tiếng Việt ngay bên cạnh**, ưu tiên mẫu: **thuật ngữ tiếng Việt** (*English term*, viết tắt).
- Ví dụ: **ngưng tụ tái diễn** (*recurrence condensation*); **phân tích định lượng tái diễn** (*recurrence quantification analysis*, RQA); **dấu hiệu cảnh báo sớm** (*early warning signals*, EWS).
- Sau lần định nghĩa đầu tiên, ưu tiên dùng tiếng Việt hoặc viết tắt đã giải thích. Nếu cần viết lại nguyên cụm tiếng Anh, vẫn kèm nghĩa tiếng Việt tại vị trí đó.
- Không dùng viết tắt chuyên môn trước khi giải thích. Chẳng hạn EEG, ECG, PPG phải được giới thiệu lần lượt là điện não đồ, điện tâm đồ và tín hiệu quang thể tích.
- Giữ nguyên tên tác giả, tên tạp chí, tên riêng và ký hiệu toán. Với tên bài báo hoặc tài liệu đọc tiếp bằng tiếng Anh, ghi thêm bản dịch/diễn giải tiếng Việt ở cùng mục.
- Nếu chưa có bản dịch chắc chắn, giữ thuật ngữ gốc và giải thích ngắn ý nghĩa bằng tiếng Việt; không tự gán nghĩa khác để Việt hóa.

### 2.3. Phân biệt các mức phát biểu bằng nhãn tiếng Việt

Khi có nguy cơ nhầm lẫn, dùng các nhãn:

- **Tác giả khẳng định (Authors claim):** điều tác giả nêu.
- **Bằng chứng hỗ trợ (Evidence supports):** điều dữ liệu, công thức hoặc kiểm chứng thực sự cho phép kết luận.
- **Diễn giải của người phân tích (Analyst interpretation):** suy luận, đánh giá hoặc giả thuyết bổ sung.

Sau khi giới thiệu, có thể dùng nhãn tiếng Việt. Không trình bày suy luận của người phân tích như kết quả tác giả đã báo cáo.

## 3. Nội dung cần phân tích

1. **Bài toán và động cơ nghiên cứu:** Bối cảnh ứng dụng; giới hạn cụ thể của phương pháp trước mà tác giả nêu; câu hỏi khoa học; lý do cần phương pháp đề xuất. Phân biệt động cơ được nêu với hạn chế được chứng minh bằng so sánh thực nghiệm.
2. **Cách đặt bài toán và đầu vào–đầu ra:** Dữ liệu là một chuỗi hay nhiều chuỗi; có nhãn, tham số điều khiển, phương trình hoặc phép đo phụ trợ nào đã biết; đại lượng cần ước lượng là gì. Phân biệt mô tả động lực học, phát hiện hồi cứu, ước lượng tham số/điểm tới hạn và dự báo trước sự kiện.
3. **Nguồn gốc phương pháp:** Công cụ được kế thừa; phần sửa đổi hoặc đề xuất mới. Chỉ khẳng định tính mới khi bài có đối chiếu hoặc nguồn phù hợp. Tài liệu chỉ xuất hiện trong danh mục tham khảo chưa được coi là đã đọc.
4. **Quy trình phương pháp:** Diễn giải từng bước từ đầu vào tới đầu ra; giải thích công thức, hàm mục tiêu, thuật toán trọng tâm, vai trò của tham số lựa chọn, giả định và lý do chọn từng thành phần. Tránh giảng lại toán học cơ bản không cần thiết.
5. **Thiết kế thực nghiệm/mô phỏng:** Hệ hoặc bộ dữ liệu, cách lấy mẫu, can thiệp và điều kiện đối chứng; cách chia dữ liệu huấn luyện/kiểm tra nếu có; phương án so sánh; thí nghiệm loại bỏ từng thành phần; tín hiệu thay thế hoặc mô hình không có hiệu ứng cần kiểm tra; thước đo đánh giá; độ bất định, độ nhạy và khả năng tái lập. Ghi rõ phần không được báo cáo.
6. **Kết quả và bằng chứng:** Phân tích hình/bảng then chốt. Mỗi hình kiểm tra khẳng định nào, thể hiện gì và **không** chứng minh điều gì? Phân biệt hiệu năng định lượng, diễn giải cơ chế và suy luận.
7. **Thảo luận:** Đóng góp thực sự; tình huống có thể làm phương pháp thất bại; giới hạn khái quát; khả năng chuyển sang tín hiệu y sinh. Mở rộng chưa có dữ liệu kiểm chứng phải đánh dấu là giả thuyết, không phải khoảng trống nghiên cứu đã xác lập.
8. **Hồ sơ phương pháp (Methodological Fingerprint):** Bảng gọn gồm đủ 11 trường dưới đây; tên tiếng Anh chỉ dùng kèm tiếng Việt để đối chiếu:
   - Bài toán (Problem).
   - Đầu vào (Input).
   - Thông tin biết trước (Known information).
   - Đầu ra (Output).
   - Phương án đối chiếu (Existing baseline).
   - Thành phần mới (New component).
   - Giả định (Assumptions).
   - Kiểm chứng (Validation).
   - Kết quả chính (Main finding).
   - Câu hỏi còn mở (Unresolved questions).
   - Khả năng tái lập (Reproduction feasibility).
9. **Tài liệu đọc tiếp và quyết định tái lập:** Phần cần kiểm tra đầu tiên; dữ liệu, mã nguồn và thông tin còn thiếu. Chọn một mức kèm lý do: **chỉ dùng làm tài liệu tham khảo** (Reference only), **phương pháp nền tảng** (Core methodology), hoặc **ứng viên tái lập** (Reproduction candidate). Nếu có điều kiện hoặc rào cản, nêu rõ; không viết như thể đã tái lập khi chưa thực hiện.

Các mục có thể gộp hoặc tách để tạo mạch trình bày tự nhiên, nhưng không bỏ nội dung bắt buộc.

## 4. Chuẩn công thức toán học trong Markdown — bắt buộc

### 4.1. Công thức phải nằm trong khối toán có cặp dấu dollar kép

- Mỗi công thức quan trọng, quan hệ có chỉ số/số mũ, tổng, phân số, ma trận hoặc phương trình nhiều thành phần phải đặt trong **khối toán riêng**.
- Dùng **hai ký tự dollar liên tiếp** làm dấu mở và dấu đóng, đúng như mẫu dưới đây. Hai dấu phân cách phải nằm trên **hai dòng riêng biệt**, có dòng trống trước và sau khối.
- Không dùng dấu ngoặc vuông hoặc tròn có gạch chéo ngược làm dấu phân cách toán; không để mã LaTeX trần trong đoạn văn.
- Không đặt công thức thực tế trong khối mã có ba dấu nháy ngược: khi đó trình xem chỉ hiện mã thay vì công thức.
- Ký hiệu ngắn trong lời giải thích có thể viết bằng Unicode như m, α, τ hoặc ε. Với chỉ số hoặc biểu thức phức tạp, đưa vào khối toán thay vì để người đọc thấy mã LaTeX chưa được hiển thị.
- Không nhét khối toán nhiều dòng vào ô bảng Markdown. Trong bảng, dùng ký hiệu/số liệu ngắn dễ đọc; đặt công thức đầy đủ bên ngoài bảng và dẫn tới nó.

**Mẫu định dạng** — chỉ minh họa cách viết, không phải công thức phải đưa vào mọi bài phân tích:

$$
\bar{x}=\frac{1}{N}\sum_{i=1}^{N}x_i.
$$

Ngay sau công thức, giải thích bằng tiếng Việt vai trò các biến và dẫn nguồn phương trình tương ứng trong bài báo.

### 4.2. Cú pháp LaTeX phải phù hợp trình xem Markdown

- Ưu tiên cú pháp thông dụng được MathJax/KaTeX, tức các bộ hiển thị toán trong Markdown, hỗ trợ.
- Đặt đủ ngoặc cho chỉ số, số mũ, phân số và căn: nhóm nhiều ký tự phải có ngoặc nhọn.
- Với nhiều dòng có căn chỉnh, dùng môi trường aligned bên trong một cặp dấu dollar kép; không lồng thêm môi trường equation hoặc align.
- Không dùng lệnh tự định nghĩa hoặc lệnh phụ thuộc gói LaTeX không có trong trình xem. Không phụ thuộc các lệnh tạo nhãn/tham chiếu tự động để dẫn phương trình PDF; ghi “Phương trình (n), Mục ..., tr. ...” trong văn bản.
- Ưu tiên giải thích tiếng Việt ngoài khối toán. Lệnh text chỉ chứa nhãn ngắn; kiểm tra khả năng hiển thị dấu tiếng Việt nếu dùng trong công thức.
- Đối chiếu trực tiếp PDF khi trích xuất chữ làm sai ký hiệu, chẳng hạn Θ thành 2 hoặc Γ thành 0. Giữ đúng dấu, hệ số, chỉ số, đơn vị và miền tổng.
- Nếu đổi tên biến để tránh nhập nhằng, nêu rõ đó là ký hiệu của bản phân tích, không phải công thức mới của tác giả.
- Nếu công thức gốc chưa rõ hoặc bất nhất, báo riêng; không âm thầm sửa nội dung toán chỉ để công thức hiển thị đẹp.

### 4.3. Không làm hỏng công thức khi ghi file bằng mã

- Khi dùng Python, JavaScript hoặc JSON để ghi nội dung, dùng chuỗi thô hoặc cơ chế thoát ký tự đúng để giữ nguyên gạch chéo ngược trong LaTeX.
- Đặc biệt kiểm tra các lệnh bắt đầu bằng b, t, r, f sau gạch chéo ngược; không để chúng biến thành ký tự điều khiển, tab hoặc xuống dòng ngoài ý muốn.
- Đọc lại **file đã ghi trên đĩa**, không chỉ kiểm tra chuỗi nguồn trong bộ nhớ. Không để ký tự điều khiển lỗi, chữ cái Hy Lạp bị hỏng hoặc dấu phân cách toán bị mất.

## 5. Yêu cầu về nguồn và độ chính xác khoa học

- Dẫn **mục, trang, phương trình, hình/bảng** cho mỗi khẳng định kỹ thuật quan trọng. Ghi rõ quy ước số trang nếu PDF có bìa trước bài báo.
- Ghi rõ chi tiết không được báo cáo; phân biệt “PDF không cung cấp” với “không tồn tại ở bất kỳ đâu”. Không bịa số liệu, mã nguồn, dữ liệu công khai hoặc đóng góp mới.
- Phân biệt xu hướng cảnh báo sớm, phát hiện hồi cứu, ước lượng điểm tới hạn và dự báo trước sự kiện đã được kiểm chứng.
- Không mặc định chậm dần tới hạn, phân nhánh hoặc chuyển trạng thái đột ngột là cơ chế của mọi biến cố y sinh.
- Không gọi thanh sai số là khoảng tin cậy khi bài chưa xác định cách tính và mức bao phủ.
- Các suy luận hoặc kế hoạch thử nghiệm bổ sung phải ghi rõ là của người phân tích, chưa được thực hiện nếu thực tế chưa chạy.
- Không sửa bài báo, bản Research Discussion (thảo luận nghiên cứu) hoặc các tài liệu khác trong bước này.

## 6. Kiểm tra trước khi hoàn tất

### Ngôn ngữ và lập luận

- Toàn tài liệu có mạch tiếng Việt liên tục, thuật ngữ nhất quán; không còn câu trộn nhiều cụm tiếng Anh.
- Mỗi cụm tiếng Anh cần giữ có nghĩa tiếng Việt ngay bên cạnh; viết tắt đã được giải thích.
- Đã phân biệt lời tác giả, bằng chứng và suy luận; mọi khẳng định quan trọng có nguồn.
- Đủ hồ sơ phương pháp 11 trường và quyết định tái lập có lý do.

### Công thức và hiển thị

1. Kiểm tra tất cả dấu dollar kép có cặp mở–đóng, đứng riêng dòng và bao quanh nội dung không rỗng.
2. Kiểm tra ngoặc nhọn, chỉ số, số mũ, phân số và môi trường nhiều dòng; không có mã LaTeX quan trọng nằm ngoài khối toán.
3. Kiểm tra không có ký tự điều khiển lỗi, gạch chéo bị mất, dấu ngoặc toán cũ hoặc công thức bị đưa nhầm vào khối mã/ô bảng.
4. Nếu có công cụ hiển thị Markdown hỗ trợ toán, mở bản xem trước và kiểm tra **toàn bộ công thức**, gồm cả chữ cái Hy Lạp và dấu tiếng Việt; sửa rồi xem lại.
5. Không coi việc đếm dấu hoặc cân bằng ngoặc là bằng chứng đã biên dịch/hiển thị thành công. Nếu chỉ kiểm tra được cú pháp vì không có trình xem, nói đúng mức kiểm tra đã thực hiện; không tuyên bố đã biên dịch.

Không cần tạo thêm PDF hoặc ảnh làm đầu ra. Có thể dùng tệp tạm cho kiểm tra và dọn sau khi hoàn tất.

## 7. Đầu ra

- Chỉ lưu một file: **explore_paper/{{PAPER_ID}}_explore.md**.
- Nếu file đã có, giữ các bổ sung và ghi chú của người dùng; cập nhật thận trọng, tránh lặp mục.



- Không tạo slide hoặc bản thảo thảo luận nghiên cứu tại bước này.
- Trả lời ngắn bằng tiếng Việt: link file, xác nhận chuẩn ngôn ngữ/công thức đã kiểm tra, và 2–3 điểm còn chưa chắc chắn từ bài báo.
