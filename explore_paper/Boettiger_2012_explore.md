# Boettiger và Hastings (2012) — Định lượng giới hạn phát hiện cảnh báo sớm của chuyển tiếp tới hạn

**Bài báo:** *Quantifying limits to detection of early warning for critical transitions* — “Định lượng các giới hạn trong phát hiện cảnh báo sớm của chuyển tiếp tới hạn”. **Tác giả:** Carl Boettiger và Alan Hastings. **Công bố:** *Journal of the Royal Society Interface* **9**, 2527–2539; công bố trực tuyến ngày 16/5/2012. **DOI ghi trong PDF:** 10.1098/rsif.2012.0125.

**Nguồn và quy ước trang:** Chỉ sử dụng [PDF được chỉ định](<../paper/5 Quantifying limits to detection of early warning for critical transitions.pdf>). Đã đọc toàn bộ **13 trang**, gồm danh mục tài liệu tham khảo; đã đối chiếu trực quan các công thức trọng tâm, Hình 1–8 và Bảng 1–2. Trong tài liệu này, “tr.” là số trang in **2527–2539**; trang PDF tương ứng bằng số trang in trừ 2526. Không có bìa riêng. Không dùng web, không tải hay đọc mã nguồn, dữ liệu hoặc các tài liệu được trích dẫn. Các đường dẫn và tài liệu đọc tiếp dưới đây chỉ được ghi nhận theo PDF.

**Luận điểm xuyên suốt:** một chỉ báo tăng trước một biến cố chưa đủ chứng minh khả năng cảnh báo. Cần biết cùng chỉ báo ấy tăng thường xuyên đến đâu khi hệ vẫn ổn định, và bao nhiêu trường hợp thực sự tiến gần chuyển tiếp vẫn bị bỏ sót. Bài chuyển câu hỏi này thành so sánh hai mô hình, mô phỏng lặp dưới cả hai mô hình, rồi biểu diễn sự đánh đổi bằng đường đặc tính hoạt động của bộ phát hiện. Kết quả là một khung **đánh giá năng lực phân biệt có điều kiện theo mô hình và dữ liệu**, chưa phải bảo đảm dự báo biến cố ngoài thực địa. [Tóm tắt; Mục 1, tr. 2527; Mục 3.5–3.8, tr. 2530–2532; Mục 6, tr. 2536–2537]

**Quy ước mức phát biểu:** **Tác giả khẳng định (Authors claim)** chỉ điều bài nêu; **Bằng chứng hỗ trợ (Evidence supports)** chỉ điều công thức, hình và phép thử trực tiếp cho phép kết luận; **Diễn giải của người phân tích (Analyst interpretation)** chỉ suy luận hoặc kế hoạch bổ sung. Những chỗ bản in chưa nhất quán được đánh dấu tại nội dung liên quan. Phân tích này thực hiện Prompt 01; phần kiểm định phản biện của Prompt 02 được để chờ ở cuối file.

## 1. Bài toán: cảnh báo đáng tin đến đâu khi chỉ có một chuỗi?

Bối cảnh là nguy cơ suy sụp của hệ sinh thái như hồ, quần thể khai thác, rạn san hô và hệ bán khô hạn. Một mô hình cơ chế chi tiết có thể hỗ trợ quản lý, nhưng thường không sẵn có. Khi đó, các **dấu hiệu cảnh báo sớm** (*early warning signals*, EWS), chẳng hạn phương sai hoặc tự tương quan tăng, được dùng như dấu hiệu chung của hệ đang mất ổn định. Bài đặt trọng tâm vào trường hợp một chuỗi quan sát đơn lẻ phải cung cấp bằng chứng, thiếu các lần lặp và đối chứng thực sự. [Mục 1, tr. 2527]

Tác giả phân biệt rõ mục tiêu phát hiện một chuyển tiếp **đang tới gần** với phân tích điểm thay đổi để xác định **sau sự kiện** rằng chuyển tiếp đã xảy ra. Tuy vậy, cách kiểm chứng trong bài chủ yếu vẫn dùng những đoạn dữ liệu và trường hợp đã được lựa chọn hồi cứu. Cần giữ đồng thời hai ý: mục tiêu phương pháp hướng tới cảnh báo trước, còn mức kiểm chứng thực tế là phân tích chuỗi đã có và mô phỏng dưới mô hình khớp từ chuỗi đó. [Mục 1, tr. 2527; Mục 4.1–4.2, tr. 2533–2535]

### 1.1. Những giới hạn trước đó mà tác giả nêu

| Giới hạn | Vì sao liên quan đến độ tin cậy? | Mức bằng chứng trong bài |
| --- | --- | --- |
| Giả định cơ chế bị che khuất | Phương sai tăng có thể do nguyên nhân khác; một số chuyển tiếp không có dấu hiệu chậm dần tương ứng | Lập luận và dẫn tài liệu ở Mục 2.1; bài không tự kiểm tra mọi cơ chế được liệt kê |
| Cửa sổ tính thống kê phải lựa chọn | Cửa sổ dài cho nhiều điểm nhưng dễ trộn động lực học đang thay đổi; cửa sổ ngắn cho ước lượng nhiễu hơn | Mục 2.2; thí nghiệm chính chỉ dùng cửa sổ bằng nửa chuỗi, không khảo sát đầy đủ độ nhạy |
| Xu hướng chưa được hiệu chuẩn | Một đường chỉ báo tăng không tự cho biết xác suất cảnh báo sai | Mục 2.3; Hình 6–8 minh họa và định lượng trực tiếp |
| Đối chứng theo giả thuyết không chưa phù hợp | Kiểm định hạng giả định độc lập hoặc xáo trộn thứ tự có thể phá cấu trúc phụ thuộc thời gian | Mục 2.4; bài thay bằng mô hình động lực học ổn định, không thực hiện một so sánh thực nghiệm đầy đủ với mọi cách tạo tín hiệu thay thế |
| Thiếu đánh giá lực kiểm định | Không rõ bao nhiêu dữ liệu là đủ, bỏ sót bao nhiêu và chỉ báo nào tốt hơn tại cùng tỷ lệ cảnh báo sai | Mục 2.5; được xử lý bằng mô phỏng và Hình 5, 8, Bảng 1–2 |

Nguồn: Mục 2.1–2.5, tr. 2528–2529; Mục 5, tr. 2535–2536.

Một điểm tinh tế của Mục 2.2 là việc dùng trung bình theo thời gian trong một cửa sổ để thay cho trung bình qua nhiều hiện thực. Điều đó đòi hỏi hệ đủ ổn định trong cửa sổ, trong khi giả thuyết cần phát hiện lại là động lực học đang thay đổi. Đây là sự căng thẳng giữa yêu cầu có đủ dữ liệu và yêu cầu gần dừng cục bộ; không nên diễn đạt thành kết luận rằng mọi phép dùng cửa sổ đều vô hiệu. [Mục 2.2, tr. 2528; diễn giải của người phân tích]

### 1.2. Câu hỏi nghiên cứu có thể kiểm tra

Với độ dài, lịch lấy mẫu và cường độ thay đổi được suy ra từ một chuỗi cụ thể, **phân bố của chỉ báo dưới hệ ổn định khác đến đâu so với dưới hệ tiến gần phân nhánh?** Tại một mức cảnh báo sai chấp nhận được, ta phát hiện được bao nhiêu trường hợp; nếu muốn phát hiện phần lớn trường hợp, phải chịu bao nhiêu cảnh báo sai? Câu hỏi này đưa chất lượng cảnh báo về hai phân bố có thể mô phỏng, thay vì chỉ đọc một đường xu hướng. [Mục 3.5–3.8, tr. 2530–2532]

## 2. Đầu vào, thông tin biết trước và ý nghĩa đầu ra

| Thành phần | Thiết lập thực tế trong bài |
| --- | --- |
| Đơn vị đầu vào | Một chuỗi trạng thái một biến cùng thời điểm quan sát; ba ví dụ được phân tích riêng, không ghép thành một tập huấn luyện |
| Thông tin mô hình đã chọn trước | Dạng gần phân nhánh nút–yên, quy luật tham số thay đổi tuyến tính, cấu trúc nhiễu và mô hình ổn định để đối chiếu |
| Tham số được ước lượng | Các tham số của từng mô hình từ chính chuỗi đang phân tích, bằng cực đại hóa hàm hợp lý |
| Thông tin kiểm chứng trong ví dụ mô phỏng | Phương trình sinh–tử, tham số và lịch tăng tác nhân gây suy giảm do người thiết kế biết |
| Thông tin kiểm chứng trong ví dụ thực nghiệm | Chuỗi Daphnia H6 thuộc một thí nghiệm thao tác tiến tới suy sụp; chuỗi băng hà III đã được phân tích trong nghiên cứu trước |
| Đầu ra trực tiếp | Hai mô hình đã khớp; thống kê chênh lệch độ phù hợp; phân bố thống kê dưới hai giả thuyết; đường đánh đổi cảnh báo sai–phát hiện đúng |
| Đầu ra so sánh chỉ báo | Hiệu năng của thống kê dựa trên mô hình so với xu hướng Kendall của phương sai và tự tương quan |
| Đầu ra chưa được kiểm chứng | Thời điểm báo động trực tuyến, phân bố thời gian còn lại tới biến cố, thời gian báo trước trên các sự kiện độc lập, hoặc hiệu quả can thiệp |

Nguồn: Mục 3.1–3.5, tr. 2529–2531; Mục 4.1–5, tr. 2533–2536.

Phương pháp không cần biết chính xác mô hình sinh thái của hệ đang quan sát, nhưng **cần giả định một lớp mô hình gần chuyển tiếp**. “Chưa biết phương trình cơ chế cụ thể” khác với “không cần thông tin tiên nghiệm”. Các giả thuyết đều chứa tham số chưa biết, nên đây là lựa chọn giữa các **giả thuyết hợp thành**: mỗi giả thuyết đại diện cho một họ phân bố, không phải một phân bố đã biết hoàn toàn. [Mục 3.1, tr. 2529; Mục 3.4, tr. 2530]

Đầu ra khớp mô hình có thể chứa tham số biểu diễn tốc độ tiến gần phân nhánh, nhưng bài không báo cáo một thí nghiệm đánh giá sai số ước lượng điểm tới hạn hoặc thời gian xảy ra chuyển tiếp. Do đó, không được đổi tên kết quả phân biệt “ổn định hay đang thay đổi” thành dự báo chính xác ngày xảy ra biến cố. [Mục 3.2–3.5; Mục 4.2–6]

## 3. Nguồn gốc và phần đóng góp phương pháp

Các công cụ nền đều được kế thừa: dạng chuẩn phân nhánh từ lý thuyết hệ động lực; **phương trình vi phân ngẫu nhiên** (*stochastic differential equation*, SDE) và tính mômen từ lý thuyết quá trình ngẫu nhiên; so sánh hàm hợp lý, mô phỏng lấy mẫu lại có tham số từ thống kê; **đường đặc tính hoạt động của bộ phát hiện** (*receiver-operating characteristic*, ROC) từ lý thuyết phát hiện tín hiệu. Chính bài dẫn Guckenheimer và Holmes [25], Kuehn [39], Gardiner [44], van Kampen [45], Cox [41,48], McLachlan [42] và các nguồn ROC [23,24] cho những thành phần này. Đây là mô tả nguồn gốc **theo bài báo**, không phải xác nhận đã đọc các tài liệu đó. [Mục 3–3.8, tr. 2529–2532]

**Tác giả khẳng định:** trực tiếp khớp và mô phỏng các mô hình để so sánh giả thuyết chưa được dùng theo cách này trong các nghiên cứu EWS mà họ xem xét. Tác giả đặc biệt nêu phần mở rộng là sinh **cả phân bố dưới mô hình đối thuyết lẫn phân bố dưới mô hình không**, giúp định lượng bỏ sót cùng với cảnh báo sai. [Mở đầu Mục 3, tr. 2529; cuối Mục 3.4, tr. 2530]

**Bằng chứng hỗ trợ:** bài thực hiện được một quy trình nhất quán: khớp hai mô hình → sinh các hiện thực mới → khớp lại cả hai mô hình trên từng hiện thực → tính phân bố chênh lệch hàm hợp lý → dựng ROC; sau đó áp dụng cùng khung đánh giá cho các chỉ báo thống kê. Hình 2–8 và Bảng 1–2 cho thấy quy trình này làm lộ ra những đánh đổi không thể đọc từ một xu hướng tăng đơn lẻ.

**Diễn giải của người phân tích:** đóng góp thực sự là đưa **hiệu chuẩn sai số theo mô hình** thành bộ phận của nghiên cứu cảnh báo sớm, đồng thời dùng các giả định cơ chế để xây dựng một chỉ báo khai thác toàn chuỗi. Bài không phát minh ROC, phép lấy mẫu lại hoặc lý thuyết phân nhánh; cũng chưa đủ cơ sở để tuyên bố thống kê hàm hợp lý luôn tối ưu trước mọi loại dữ liệu. Bản thân Mục 3.4 đã thừa nhận bài toán hợp thành khó hơn trường hợp hai giả thuyết đơn của bổ đề Neyman–Pearson.

## 4. Hai mô hình động lực học và các giả định đi kèm

### 4.1. Từ dạng chuẩn tới hệ đang mất ổn định

Bài bắt đầu bằng **phân nhánh nút–yên** (*saddle–node bifurcation*): một cân bằng hút và một cân bằng không ổn định tiến lại rồi cùng biến mất. Dạng chuẩn được viết:

$$
\frac{dx}{dt}=r_t-x^{2}.
$$

x là trạng thái; r có chỉ số t là tham số phân nhánh có thể thay đổi chậm. Đây là Phương trình (3.1), tr. 2529. Không phải mọi chuyển tiếp đột ngột đều thuộc cơ chế này. Mục 2.1 phân biệt các trường hợp nhiễu đẩy qua biên miền hút, cú sốc ngoại sinh hoặc tham số biến đổi quá nhanh.

Để cho phép mức trạng thái trung bình tùy ý, bài dịch trạng thái bằng θ và định nghĩa vị trí cân bằng hút:

$$
\frac{dx}{dt}=r_t-(\theta-x)^{2},
\qquad
\widehat{x}=\theta+\sqrt{r_t}=:\phi(r_t).
$$

θ là hằng số dịch trạng thái; φ là vị trí cân bằng hút khi tham số còn ở phía tồn tại cân bằng. Nguồn: đầu Mục 3.2, tr. 2530. Các biểu thức có căn bậc hai đòi hỏi miền tham số thích hợp; bản PDF chưa cung cấp đầy đủ các ràng buộc dùng khi tối ưu.

Phương trình ngẫu nhiên tuyến tính theo trạng thái được **in nguyên văn về cấu trúc toán** như sau:

$$
dX_t=\sqrt{r_t}\bigl[\phi(r_t)-X_t\bigr]dt
+\sigma\sqrt{\phi(r_t)}\,dB_t.
$$

Đây là Phương trình (3.2), tr. 2530; chỉ thống nhất cách ghi chỉ số của X trong bản phân tích. B là chuyển động Brown chuẩn, σ là hệ số nhiễu. Bài giải thích biên độ nhiễu căn bậc hai theo mức quần thể bằng giả định nhiễu nội sinh từ các sự kiện nhân khẩu học. Với nhiễu môi trường ngoại sinh, tác giả nêu có thể bỏ căn đó. Việc chọn cấu trúc nhiễu là giả định cần kiểm tra, không phải thuộc tính đã được nhận dạng chắc chắn từ ba chuỗi. [Đoạn sau Phương trình (3.2), tr. 2530]

Tham số tiến gần ngưỡng được xấp xỉ tuyến tính:

$$
r_t=r_0-mt.
$$

Đây là Phương trình (3.3), tr. 2530. r có chỉ số 0 là mức ban đầu, m là tốc độ giảm. Khi m dương, tham số đi về phía mất cân bằng hút. Giả định này mã hóa một quá trình tiến gần ngưỡng từ từ và đơn điệu. Những đường tiến gần ngưỡng tăng tốc hoặc phi tuyến mạnh không được khảo sát bằng một hệ thí nghiệm riêng trong PDF. [Mục 2.1; Mục 3.2]

### 4.2. Mô hình không: một hệ hồi phục ổn định

Nếu tham số không thay đổi, bài dùng **quá trình Ornstein–Uhlenbeck** (OU):

$$
dX_t=r(\theta-X_t)\,dt+\sigma\,dB_t.
$$

Đây là Phương trình (3.4), tr. 2530. r dương là tốc độ hồi phục, θ là mức cân bằng và σ là cường độ nhiễu. Bài liên hệ OU với mô hình tự hồi quy bậc một trong thời gian rời rạc. Đây là đối chứng động lực học còn giữ phụ thuộc thời gian, thay cho xáo trộn ngẫu nhiên thứ tự quan sát. [Mục 2.4; Mục 3.2]

**Lưu ý ký hiệu:** r trong (3.4) là hệ số hồi phục; r trong (3.1)–(3.3) là tham số của dạng chuẩn. Khi m bằng 0, mô hình thay đổi trở thành một OU sau khi đổi cách tham số hóa tốc độ, mức cân bằng và nhiễu. Không được đồng nhất số học mọi tham số cùng tên của hai phương trình. Tính lồng nhau của hai họ mô hình được tác giả dùng ở Mục 3.5; miền tham số triển khai thực tế vẫn cần đối chiếu mã. [Tr. 2530–2531; diễn giải của người phân tích]

### 4.3. Chậm dần tới hạn là ý nghĩa cơ chế, không phải kết luận chung

Trong mô hình tuyến tính này, khi tham số tiến về ngưỡng, hệ số kéo về cân bằng suy giảm. Hệ phục hồi chậm hơn sau nhiễu; đó là **chậm dần tới hạn** (*critical slowing down*). Phương sai hoặc trí nhớ thời gian có thể phản ánh sự suy giảm ấy, nhưng phải xét cả cấu trúc nhiễu và lịch biến đổi tham số. Tác giả đã nêu ngay từ Mục 2.1 rằng cùng một xu hướng thống kê không nhận diện duy nhất cơ chế, và không phải mọi chuyển tiếp đều có cùng kiểu cảnh báo. [Mục 2.1, tr. 2528; Mục 3.2, tr. 2529–2530; Mục 6, tr. 2537]

## 5. Tính hàm hợp lý và thống kê so sánh

### 5.1. Khai thác phân bố chuyển tiếp thay vì cắt chuỗi thành nhiều cửa sổ

Do hai mô hình tuyến tính theo trạng thái với hệ số nhiễu chỉ phụ thuộc thời gian, phân bố chuyển tiếp là phân bố chuẩn (Gaussian), được xác định bởi trung bình và phương sai có điều kiện. Bản phân tích viết rõ khoảng thời gian giữa hai quan sát là Δ để tránh nhầm với thời điểm tuyệt đối:

$$
\ell_M(\vartheta_M;X)
=\sum_{i=2}^{n}
\log p_M\!\left(x_i\mid x_{i-1},\Delta_i;\vartheta_M\right),
\qquad
\Delta_i=t_i-t_{i-1}.
$$

Đây là cách viết tường minh của Phương trình (3.5), tr. 2530. M là mô hình; ϑ là véc-tơ tham số của mô hình đó; n là số quan sát. Bài dùng P cho xác suất/hàm hợp lý; ở đây dùng p cho mật độ chuyển tiếp liên tục và ℓ cho logarit hàm hợp lý. Ký hiệu ϑ và Δ do người phân tích đặt, không phải thành phần phương pháp mới. Tổng này điều kiện theo quan sát ban đầu; PDF chưa giải thích chi tiết cách khởi tạo mô phỏng và xử lý phân bố ban đầu trong mã.

Với OU, các mômen chuyển tiếp có công thức đóng:

$$
\begin{aligned}
\mu_i
&=x_{i-1}e^{-r\Delta_i}+\theta\bigl(1-e^{-r\Delta_i}\bigr),\\
v_i
&=\frac{\sigma^{2}}{2r}\bigl(1-e^{-2r\Delta_i}\bigr).
\end{aligned}
$$

μ và v lần lượt là trung bình và phương sai có điều kiện của quan sát thứ i. Nguồn: Phương trình (3.8)–(3.9), tr. 2530; chỉ đổi ký hiệu khoảng thời gian. Mô hình thời gian liên tục đưa khoảng cách quan sát vào hàm hợp lý trực tiếp, nên về cấu trúc có thể tiếp nhận khoảng lấy mẫu không đều. Bài không trình bày một thí nghiệm đánh giá riêng khả năng này. [Mục 3.3; diễn giải của người phân tích]

Với mô hình thay đổi, bài gọi mô hình tuyến tính gần nút–yên là **LSN**, từ *linear saddle–node*; trình bày phương trình mômen và dùng thủ tục tích phân số `lsoda` trong R để tính chúng trên từng khoảng quan sát. [Phương trình (3.10)–(3.11), Mục 3.3, tr. 2530]

### 5.2. Những bất nhất toán học phải kiểm tra trước khi triển khai

Các chi tiết dưới đây đã được đối chiếu với ảnh trang 2530, không chỉ dựa trên chữ trích xuất. Chúng chưa xác định mã nguồn của tác giả đã sử dụng phiên bản nào.

**Thứ nhất, hệ số của phương trình trung bình chưa thống nhất với SDE.** Phương trình (3.10) được in:

$$
\frac{d}{dt}E(x_i\mid M=\mathrm{LSN})
=2\sqrt{r(t)}\bigl(\sqrt{r(t)}+\theta-x_i\bigr).
$$

Vế phải có hệ số 2, trong khi phần trôi ở (3.2) chỉ có căn của r. Hơn nữa, vế phải dùng chính ký hiệu x có chỉ số i thay vì một ký hiệu trung bình riêng. Nguồn: Phương trình (3.2), (3.10), tr. 2530.

**Kiểm tra đại số của người phân tích:** đạo hàm phần trôi tất định đã dịch trạng thái tại cân bằng hút là:

$$
\left.
\frac{\partial}{\partial x}\bigl[r-(\theta-x)^{2}\bigr]
\right|_{x=\theta+\sqrt{r}}
=-2\sqrt{r}.
$$

Vì vậy, tuyến tính hóa trực tiếp dạng chuẩn đã in cho hệ số hồi phục bằng hai lần căn của r. Điều này phù hợp với hệ số trong (3.10), nhưng chưa giải thích hệ số của (3.2). Có thể có một quy ước đổi tham số hoặc lỗi trình bày; PDF không làm rõ để quyết định.

**Thứ hai, phương trình phương sai cũng không thể ghép tùy ý với các công thức trên.** Bài in:

$$
\frac{d}{dt}V(x_i\mid M=\mathrm{LSN})
=-2\sqrt{r(t)}V(x_i)
+\sigma^{2}\bigl(\sqrt{r(t)}+\theta\bigr).
$$

Đây là Phương trình (3.11), tr. 2530. Hệ số suy giảm phương sai này tương ứng với phần trôi có hệ số hồi phục bằng căn của r ở (3.2), trong khi hệ số của phương trình trung bình (3.10) gợi ra hai lần giá trị ấy.

**Thứ ba, công thức mômen tổng quát (3.7) có vấn đề về dấu và hệ số nếu f là phần trôi.** Bản in ghi:

$$
\frac{d}{dt}V(x\mid M)
=-\partial_x f(x)\,V(x\mid M)+g(x)^{2}.
$$

f và g là các hàm trôi và nhiễu trong cách trình bày của Mục 3.3. Nếu thay phần trôi OU vào biểu thức này, nó không khôi phục phương sai OU của (3.9).

Để thấy điểm cần đối chiếu, **người phân tích** viết lại quan hệ mômen nhất quán cho một SDE tuyến tính tổng quát, không coi đây là công thức tác giả đã báo cáo:

$$
\begin{aligned}
dX_t&=a(t)\bigl[b(t)-X_t\bigr]dt+c(t)\,dB_t,\\
\frac{d\mu}{dt}&=a(t)\bigl[b(t)-\mu(t)\bigr],\\
\frac{dv}{dt}&=-2a(t)v(t)+c(t)^{2}.
\end{aligned}
$$

a là tốc độ hồi phục, b là mức hút tức thời, c là biên độ nhiễu; μ và v là trung bình và phương sai chuyển tiếp. Nếu chọn a bằng căn của r thì phương sai khớp (3.11), còn nếu chọn a bằng hai lần căn của r thì hệ số suy giảm phương sai phải thay đổi tương ứng. **Quyết định tái lập phải dựa trên một bộ SDE–mômen nhất quán và đối chiếu mã gốc; không âm thầm sửa một phương trình rồi gọi đó là nguyên bản của tác giả.** Các bất nhất bản in chưa đủ để kết luận các kết quả số đã sai.

### 5.3. Chênh lệch logarit hàm hợp lý

Sau khi cực đại hóa riêng cho mỗi mô hình, thống kê so sánh là:

$$
\begin{aligned}
\widehat{\vartheta}_j
&=\underset{\vartheta_j}{\operatorname{arg\,max}}\,
\ell_j(\vartheta_j;X),\qquad j\in\{0,1\},\\
\delta(X)
&=2\left[
\ell_1(\widehat{\vartheta}_1;X)
-\ell_0(\widehat{\vartheta}_0;X)
\right].
\end{aligned}
$$

Mô hình 0 là OU ổn định, mô hình 1 là LSN thay đổi. Đây là Phương trình (3.12) và định nghĩa ước lượng ngay trước đó, tr. 2530. δ lớn biểu thị mức cải thiện độ phù hợp khi cho phép hệ tiến gần chuyển tiếp. Vì mô hình 0 được coi là lồng trong mô hình 1, tác giả nhận định δ không âm về nguyên tắc; việc tối ưu thực tế phải đạt nghiệm phù hợp mới bảo toàn tính chất này. [Mục 3.5, tr. 2531; diễn giải bổ sung về tối ưu]

δ là thống kê so sánh, **không phải xác suất hệ sắp suy sụp**. Bài không biến hai phân bố δ thành xác suất hậu nghiệm bằng một mô hình xác suất tiên nghiệm về tần suất biến cố. Tương tự, nhận định rằng tiêu chí thông tin Akaike (AIC) ưu tiên mô hình thay đổi trong cả ba ví dụ chỉ là kết quả lựa chọn mô hình; AIC tự nó không cung cấp hai tỷ lệ sai cần cho quyết định cảnh báo. [Mục 3.4–3.7; Mục 4.2, tr. 2535]

## 6. Quy trình mô phỏng, khớp lại và hiệu chuẩn chỉ báo

### 6.1. Quy trình trung tâm

1. **Chọn và chuẩn bị một chuỗi.** Giữ các thời điểm quan sát; xử lý riêng chuỗi băng hà như mô tả ở Mục 7. Các lựa chọn đoạn và tiền xử lý là một phần của điều kiện phân tích.
2. **Khớp hai mô hình vào chuỗi gốc.** Ước lượng tham số bằng cực đại hóa hàm hợp lý và tính δ quan sát.
3. **Sinh hai nhóm chuỗi mới.** Mô phỏng **500 chuỗi từ OU đã khớp** và **500 chuỗi từ LSN đã khớp**. Các hiện thực này là đối chứng và trường hợp có tín hiệu theo mô hình, không phải những thí nghiệm thực nghiệm độc lập.
4. **Khớp lại cả hai mô hình trên từng chuỗi mới.** Tổng cộng mỗi bộ dữ liệu cần **2.000 lần khớp** cho các bản mô phỏng, vì có hai mô hình cần khớp cho hai nhóm, mỗi nhóm 500 chuỗi; ngoài ra còn hai lần khớp chuỗi gốc. Không giữ nguyên tham số đã ước lượng rồi chỉ thế vào hàm hợp lý của mọi chuỗi mới.
5. **Lập hai phân bố δ.** Một phân bố từ các chuỗi sinh bởi OU; một từ các chuỗi sinh bởi LSN. Độ chồng lấn biểu thị khó khăn phân biệt hai kịch bản.
6. **Quét ngưỡng và dựng ROC.** Với mỗi ngưỡng δ, đếm phần chuỗi OU bị báo động và phần chuỗi LSN được báo động; dùng chúng làm hai tọa độ ROC.
7. **Lặp cách đánh giá cho chỉ báo thống kê.** Trên các chuỗi mô phỏng dưới hai mô hình, tính phương sai hoặc tự tương quan trong cửa sổ bằng nửa độ dài chuỗi, rồi tính hệ số xu hướng Kendall; dựng ROC theo ngưỡng của hệ số này.

Nguồn: Mục 3.5, tr. 2530–2531; Mục 3.8, tr. 2531–2532; Mục 4.2–5, tr. 2535–2536. Các chi tiết triển khai như ràng buộc tối ưu, quy tắc khởi tạo, bước tích phân mô phỏng và cách làm tròn nửa độ dài khi số điểm lẻ không được cung cấp đầy đủ trong PDF.

Điểm phương pháp quan trọng ở bước 4 là tái tạo **toàn bộ thao tác ước lượng** dưới mỗi kịch bản. Phân bố cần đánh giá là phân bố của một quy trình đã khớp tham số từ dữ liệu, không chỉ phân bố của hàm hợp lý khi biết tham số thật. Tuy nhiên, tham số dùng để sinh hai nhóm vẫn được cố định tại giá trị khớp từ chuỗi gốc; bài không báo cáo một lớp mô phỏng ngoài nhằm bao phủ toàn bộ bất định về tham số sinh và sai dạng mô hình. [Mục 3.5; diễn giải của người phân tích]

### 6.2. Cách đọc ROC và một lỗi chú thích của Hình 1

Bản phân tích ký hiệu một chỉ báo chung là S và ngưỡng là c, quy ước báo động khi S lớn hơn c:

$$
\begin{aligned}
\operatorname{FPR}(c)
&=P(S>c\mid M_0),\\
\operatorname{TPR}(c)
&=P(S>c\mid M_1),\\
\operatorname{FNR}(c)
&=1-\operatorname{TPR}(c).
\end{aligned}
$$

FPR là **tỷ lệ cảnh báo sai** (*false positive rate*), TPR là **tỷ lệ phát hiện đúng**, hay độ nhạy (*true positive rate*), FNR là **tỷ lệ bỏ sót** (*false negative rate*). Mô hình 0 là ổn định, mô hình 1 là tiến gần chuyển tiếp. Đây là ký hiệu giải thích của người phân tích cho Mục 3.7–3.8 và Hình 1, không phải phương trình đánh số của bài.

Hạ ngưỡng thường làm tăng cả phát hiện đúng lẫn cảnh báo sai. Hai phân bố chỉ báo giống hệt nhau cho đường ROC trùng đường chéo; một điểm gần góc trên trái biểu thị phân biệt tốt tại ngưỡng tương ứng. Đường ROC cho biết các mức đánh đổi có thể đạt, nhưng không tự quyết định ngưỡng phù hợp với chi phí quản lý. [Mục 3.8, tr. 2531–2532]

**Bất nhất bản in:** chú thích Hình 1, tr. 2531, mô tả phát hiện đúng bằng phần diện tích của phân bố đối thuyết ở **bên trái** ngưỡng. Với quy ước chỉ báo lớn hơn là bằng chứng cảnh báo, và theo các điểm ROC được vẽ khi ngưỡng tăng, phát hiện đúng phải là diện tích **bên phải** ngưỡng. Bản phân tích ghi rõ khác biệt này để tránh đảo TPR thành tỷ lệ bỏ sót; không tự nhận đã xác minh cách tính trong mã.

Tỷ lệ cảnh báo sai ở đây là xác suất báo động **khi hệ được sinh từ mô hình ổn định**. Nó khác tỷ lệ báo động sai trong tất cả những lần đã báo động, vốn còn phụ thuộc tần suất gặp hệ tiến gần chuyển tiếp. Hai nhóm mô phỏng có cùng số lượng không có nghĩa ngoài thực tế hai kịch bản xảy ra ngang nhau. [Diễn giải của người phân tích từ định nghĩa ROC]

### 6.3. Đối chiếu phương sai và tự tương quan được thực hiện thế nào?

Trong mỗi chuỗi, bài tính phương sai và tự tương quan bằng cửa sổ trượt có độ dài bằng 50% chuỗi; sau đó đo xu hướng bằng **hệ số tương quan hạng Kendall** τ. τ dương lớn nghĩa là chỉ báo có xu hướng tăng theo thời gian; nó chưa tự trở thành bằng chứng cảnh báo đã hiệu chuẩn. Bài đưa chính τ vào hai phân bố mô phỏng để đo lực phân biệt. Như vậy, đóng góp đánh giá có thể dùng cho cả chỉ báo dựa trên mô hình lẫn chỉ báo thống kê. [Mục 5, tr. 2535–2536; Hình 6–8]

PDF không trình bày đầy đủ công thức ước lượng tự tương quan, quy tắc cửa sổ chồng lấn, cách xử lý các cặp hạng bằng nhau, hay một khảo sát nhiều độ dài cửa sổ. Vì thế, kết quả định lượng áp dụng cho cách triển khai được bài sử dụng, chưa là giới hạn tối ưu của mọi biến thể phương sai/tự tương quan. [Mục 5; diễn giải của người phân tích]

## 7. Thiết kế dữ liệu và mô phỏng

### 7.1. Mô hình sinh–tử phi tuyến làm nguồn dữ liệu mô phỏng

Chuỗi mô phỏng gốc được tạo bằng quá trình sinh–tử thời gian liên tục ở cấp cá thể, không dùng chính SDE tuyến tính làm mô hình sinh. Phương trình chủ là:

$$
\frac{dP(n,t)}{dt}
=b_{n-1}P(n-1,t)+d_{n+1}P(n+1,t)
-(b_n+d_n)P(n,t).
$$

P là xác suất có n cá thể tại thời điểm t. b và d là các cường độ chuyển trạng thái do sinh và tử. Nguồn: Phương trình (4.1), tr. 2533. Đoạn văn của bài gọi chúng là xác suất sự kiện, nhưng trong phương trình thời gian liên tục chúng đóng vai trò tốc độ/cường độ sự kiện.

Các tốc độ được quy định:

$$
\begin{aligned}
b_n&=\frac{eKn^{2}}{n^{2}+h^{2}},\\
d_n&=en+a_t,\\
a_t&=100+0.09t.
\end{aligned}
$$

Hai dòng đầu là Phương trình (4.2)–(4.3), tr. 2533. Dòng cuối viết tường minh lịch tăng a theo phần văn bản cuối tr. 2533 và đầu tr. 2534. e điều chỉnh tốc độ, K và h điều chỉnh sinh sản phụ thuộc mật độ; a tăng làm tăng tử vong. Tham số được báo cáo: trạng thái ban đầu 730; e = 0,5; K = 1.000; h = 200.

Tác giả nêu mô phỏng trên khoảng **0–500** và lấy **40 điểm cách đều**. Mục đích lựa chọn mật độ này là có đủ dữ liệu để thấy tín hiệu nhưng chưa quá nhiều đến mức hết sai số. Các sự kiện sinh–tử tạo nhiễu Poisson, còn phần trôi là phi tuyến; đây là phép minh họa khả năng làm việc khi mô hình suy luận Gaussian tuyến tính chỉ là xấp xỉ. [Mục 4.1, tr. 2533–2534]

**Điểm cần đối chiếu:** trục thời gian của Hình 2a và chuỗi mô phỏng ở Hình 6 lại trải tới khoảng **1.000**. PDF không giải thích sự khác nhau giữa khoảng mô phỏng 0–500 trong văn bản và thang thời gian trong hình. Không tự gán lại tốc độ 0,09 theo một thang khác để khớp hình. Ngoài ra, cách xử lý biên quần thể bằng 0 và thuật toán mô phỏng sự kiện không được mô tả đầy đủ. [Hình 2, tr. 2532; Hình 6, tr. 2536; Mục 4.1, tr. 2534]

**Phạm vi phép thử:** dữ liệu mô phỏng gốc đến từ một cơ chế phi tuyến khác mô hình khớp; tuy nhiên ROC được dựng từ các chuỗi **OU/LSN đã khớp**, không phải từ một tập lớn các chuỗi sinh–tử độc lập có nhãn sự kiện. Vì vậy, phép thử cho thấy quy trình có thể phân tích ví dụ sai dạng mô hình này, nhưng chưa đo trực tiếp mức hiệu chuẩn sai số trên toàn họ sinh–tử phi tuyến. [Mục 3.5, 4.1–4.2; diễn giải của người phân tích]

### 7.2. Hai chuỗi quan sát đã có

| Bộ dữ liệu | Số điểm và lựa chọn | Tiền xử lý hoặc thông tin phụ trợ | Giới hạn diễn giải |
| --- | --- | --- | --- |
| Daphnia, thiết bị nuôi liên tục H6 | 16 điểm trong đoạn bị thao tác tiến tới suy sụp; tác giả chọn trường hợp có phương sai tăng | Dữ liệu từ Drake và Griffen [5]; PDF không trình bày lại đầy đủ chế độ can thiệp hoặc đơn vị đo | Một hiện thực được lựa chọn, chưa là đánh giá trên toàn bộ các thiết bị và đối chứng |
| Băng hà III trong hồ sơ deuteri ở lõi băng Nam Cực | 121 điểm cho sự kiện băng hà thứ ba | Nội suy tuyến tính, rồi loại xu hướng bằng làm trơn hạt nhân Gaussian để gần cách phân tích của Dakos và cộng sự [16] | Đã tiền xử lý và chọn sự kiện hồi cứu; 121 điểm sau xử lý không được đồng nhất với 121 quan sát thô độc lập |

Nguồn: Mục 4.1, tr. 2534–2535; Hình 3–4. H6 được tác giả gọi là một hệ nuôi liên tục, từ gốc là *chemostat*. Tên sinh vật Daphnia và tên riêng được giữ nguyên.

Bài thừa nhận không khớp hoàn toàn kết quả xử lý băng hà của [16], vì độ dài cửa sổ loại xu hướng ở nghiên cứu đó được chọn thủ công. Tác giả cho biết tương quan của hệ số tự hồi quy bậc một vẫn gần với kết quả trước. Đây là một rào cản tái lập cụ thể, không phải bằng chứng rằng các kết quả của hai phân tích đồng nhất. [Mục 4.1, tr. 2535]

Có một căng thẳng cần lưu ý: Mục 2.2 cảnh báo nội suy có thể tạo tự tương quan nhân tạo, nhưng Mục 4.1 vẫn nội suy chuỗi băng hà để nhất quán với phân tích gốc. Bài không cung cấp thí nghiệm riêng so sánh có/không nội suy nhằm đo ảnh hưởng của quyết định này lên ROC. [Tr. 2528, 2534–2535]

### 7.3. Đối chứng, chia dữ liệu và những kiểm chứng chưa được báo cáo

Đối chứng chính là các chuỗi OU sinh từ mô hình không đã khớp. Hình 6 còn đưa một hiện thực hệ ổn định có tự tương quan tăng mạnh để minh họa cảnh báo giả. Các phương án đối chiếu định lượng là xu hướng của phương sai và tự tương quan dưới cùng khung mô phỏng. Đây là đối chứng có mô hình động lực học, không phải các nhóm thực nghiệm mới được thiết kế trong bài này. [Mục 3.5; Mục 5; Hình 6–8]

PDF **không báo cáo**: chia huấn luyện–kiểm tra độc lập trên nhiều sự kiện; đánh giá theo thời gian khi dữ liệu đến dần; kiểm chứng ngưỡng trên một tập bên ngoài; thí nghiệm loại bỏ từng thành phần; khảo sát đầy đủ cửa sổ, loại nhiễu, sai số đo và mật độ lấy mẫu; khoảng bất định của ROC; thời gian tính toán hoặc tỷ lệ tối ưu thất bại. Tác giả cho biết gói R có hàm để thay lịch lấy mẫu và tham số rồi chạy lại, nhưng điều đó chưa phải kết quả một khảo sát độ nhạy đã được trình bày. [Mục 3.5, 4.1–5; toàn bộ Hình 1–8 và Bảng 1–2]

## 8. Kết quả: mỗi hình hỗ trợ điều gì?

### 8.1. Bản đồ bằng chứng Hình 1–8

| Hình và vị trí | Khẳng định được kiểm tra hoặc minh họa | Điều thực sự quan sát được | Điều hình chưa chứng minh |
| --- | --- | --- | --- |
| Hình 1, tr. 2531 | Ngưỡng biến hai phân bố chỉ báo thành một đường đánh đổi | Ví dụ giả định cho thấy thay ngưỡng đổi đồng thời hai tỷ lệ; cần lưu ý lỗi trái/phải trong chú thích | Không phải hiệu năng thực nghiệm của một chỉ báo cụ thể |
| Hình 2, tr. 2532 | Quy trình hoạt động trên chuỗi mô phỏng | Chuỗi gốc; các bản mô phỏng OU/LSN; hai phân bố δ chồng lấn đáng kể; đường dọc là δ quan sát | Không phải xác suất suy sụp của quần thể, không phải kiểm chứng trên nhiều mô phỏng sinh–tử độc lập |
| Hình 3, tr. 2533 | Quy trình áp dụng được cho đoạn H6 ngắn | Hai phân bố δ vẫn chồng lấn dù mô hình thay đổi khớp tốt hơn chuỗi gốc | Không chứng minh có thể cảnh báo chắc chắn từ 16 điểm bất kỳ |
| Hình 4, tr. 2534 | Chuỗi băng hà đã xử lý chứa dấu hiệu khác biệt mạnh giữa hai mô hình | Hai phân bố δ tách biệt rõ hơn; δ quan sát lớn | Không xác lập duy nhất cơ chế phân nhánh của khí hậu, không bảo đảm dự báo sự kiện băng hà mới |
| Hình 5, tr. 2535 | Năng lực phân biệt phụ thuộc ví dụ dữ liệu | ROC băng hà gần góc trên trái; mô phỏng và H6 đánh đổi mạnh, các đường có thể đổi thứ tự theo ngưỡng | Không tách riêng được tác động của số điểm khỏi cường độ thay đổi và tiền xử lý |
| Hình 6, tr. 2536 | Xu hướng tăng trên một chuỗi có thể gây nhầm | Hệ ổn định có τ tự tương quan 0,7; hệ mô phỏng tiến gần ngưỡng có τ tự tương quan −0,15 | Một ví dụ không định lượng được tần suất cảnh báo sai; cần Hình 7–8 |
| Hình 7, tr. 2536 | Phân bố xu hướng dưới hai kịch bản có thể chồng lấn | Các biểu đồ hộp của τ cho phương sai/tự tương quan chồng lấn mạnh, nhất là ở hai ví dụ thực | Hộp và râu không phải khoảng tin cậy; PDF không quy định đầy đủ quy tắc vẽ râu |
| Hình 8, tr. 2537 | So sánh ba chỉ báo tại nhiều mức cảnh báo sai | Thống kê hàm hợp lý vượt rõ ở hai ví dụ thực; với mô phỏng, phương sai cạnh tranh hơn ở một số vùng ngưỡng | Không có ưu thế đồng đều của chỉ báo hàm hợp lý trên mọi điểm ROC, mọi hệ hoặc mọi chỉ báo EWS |

### 8.2. Chênh lệch độ phù hợp quan sát

Các giá trị δ được báo cáo là **5,1** cho mô phỏng, **6,0** cho H6 và **83,9** cho băng hà. Theo bài, cả ba trường hợp đều được AIC ưu tiên mô hình thay đổi với một tham số bổ sung. Tuy nhiên, δ hoặc một quyết định chọn mô hình chưa cho biết khả năng bỏ sót và cảnh báo sai trên các lần lặp; đó là lý do cần các phân bố mô phỏng. [Mục 4.2, tr. 2535]

Không nên đọc δ lớn của băng hà thành mức mất ổn định lớn hơn theo một thang chung cho ba hệ. Độ dài chuỗi, tốc độ thay đổi, lịch lấy mẫu và cấu trúc sau xử lý đều khác. Mục 4.2 cũng lưu ý độ dài chuỗi ảnh hưởng chênh lệch hợp lý. **Diễn giải của người phân tích:** cách bài nhắc đến đơn vị của hàm hợp lý thô không nên được chuyển thành khẳng định rằng chỉ đổi đơn vị trạng thái đã làm thay đổi tỷ số hợp lý giữa hai mô hình; trọng tâm so sánh ở đây là điều kiện dữ liệu và phân bố thống kê tương ứng.

### 8.3. Khi cố định tỷ lệ cảnh báo sai ở 5%

| Dữ liệu | Phát hiện đúng bằng phương sai | Phát hiện đúng bằng hàm hợp lý |
| --- | ---: | ---: |
| Mô phỏng | 25% | 61% |
| H6 | 5,0% | 34% |
| Băng hà III | 5,4% | 100% |

Nguồn: **Bảng 1, tr. 2537**. Đây là tỷ lệ được ước lượng trong hai nhóm mô phỏng của từng mô hình khớp, không phải tỷ lệ các biến cố thực địa độc lập mà nghiên cứu đã dự báo.

Tại mức cảnh báo sai thấp này, phương pháp hàm hợp lý cải thiện rõ so với phương sai ở cả ba ví dụ. Nhưng độ nhạy 34% của H6 hoặc 61% của mô phỏng vẫn để lại nhiều trường hợp bỏ sót. Kết quả tốt hơn một đối chiếu không có nghĩa đã đủ tốt cho một quyết định quản lý cụ thể. [Bảng 1; diễn giải của người phân tích]

### 8.4. Khi muốn phát hiện đúng 90%

| Dữ liệu | Cảnh báo sai bằng phương sai | Cảnh báo sai bằng hàm hợp lý |
| --- | ---: | ---: |
| Mô phỏng | 49% | 55% |
| H6 | 81% | 35% |
| Băng hà III | 93% | 0% |

Nguồn: **Bảng 2, tr. 2537**. Các tỷ lệ trên dùng định nghĩa cảnh báo sai có điều kiện theo hệ ổn định, không phải tỷ lệ sai trong mọi lần báo động.

Chi tiết quan trọng là ở **mô phỏng**, khi ép độ nhạy lên 90%, phương sai có tỷ lệ cảnh báo sai **thấp hơn** chỉ báo hàm hợp lý: 49% so với 55%. Do đó, câu “hàm hợp lý luôn tốt hơn phương sai” trái với chính Bảng 2. Hình 8c cũng cho thấy cần so sánh theo vùng ngưỡng cụ thể. Với H6 và băng hà, ưu thế của mô hình rõ hơn trong các điểm vận hành được báo cáo. [Bảng 2; Hình 8, tr. 2537]

### 8.5. Xu hướng mạnh và kết quả hoàn hảo đều cần đọc đúng mức

Hình 6 cho thấy τ phương sai lần lượt là −0,7 ở hệ ổn định, 0,22 ở mô phỏng tiến gần chuyển tiếp, 0,72 ở H6 và 0,93 ở băng hà. τ tự tương quan tương ứng là 0,7; −0,15; 0; 0,64. Hai ví dụ mô phỏng đối lập cho thấy mức tăng của một chỉ báo trên một hiện thực không bảo đảm phân loại đúng. Hình 7 bổ sung bằng chứng phân bố để vượt qua hạn chế của việc chỉ chọn một ví dụ. [Hình 6–7, tr. 2536]

Tác giả báo cáo **không thấy sai phân loại trong 500 hiện thực mỗi loại** ở ví dụ băng hà khi dùng chỉ báo mô hình. Phát hiện đúng 100% hoặc cảnh báo sai 0% trong Bảng 1–2 phải đọc trong phạm vi đó: chúng không xác lập sai số tổng thể đúng bằng 0, không bao gồm mọi bất định tiền xử lý, cũng không phải kết quả kiểm tra trên 500 sự kiện băng hà độc lập. PDF không báo cáo khoảng bất định cho các điểm ROC hoặc tỷ lệ trong bảng. [Mục 4.2, tr. 2535; Bảng 1–2]

Với 500 bản mô phỏng, một quan sát tương ứng 0,2 điểm phần trăm trong tỷ lệ đếm trực tiếp. Đây là kiểm tra số học của người phân tích; bài không nói rõ mọi giá trị ở ngưỡng cố định được lấy bằng đếm trực tiếp, nội suy hay làm trơn. Vì vậy không gán một độ chính xác thống kê bổ sung cho các con số đã in.

## 9. Đóng góp, giới hạn và phạm vi kết luận

### 9.1. Điều bài thực sự bổ sung

Đóng góp mạnh nhất là làm rõ **năng lực phát hiện thuộc về cả chỉ báo, điều kiện dữ liệu và mô hình đối chứng**. Một τ lớn có thể xuất hiện trong hệ ổn định; một phương pháp có thể tốt tại mức cảnh báo sai 5% nhưng mất ưu thế khi người sử dụng yêu cầu độ nhạy 90%. Bài cung cấp một quy trình định lượng để hỏi những câu này, thay vì chỉ khẳng định có xu hướng tăng. [Mục 5–6, tr. 2535–2537; Hình 6–8; Bảng 1–2]

Việc mô hình hóa tường minh cũng làm lộ ra giả định: phân nhánh nào, tham số thay đổi ra sao, loại nhiễu gì và hệ ổn định đối chứng có cấu trúc nào. Chất lượng so sánh có thể cải thiện khi thông tin cơ chế phù hợp với dữ liệu, nhưng cái giá là độ phụ thuộc vào dạng mô hình và việc ước lượng tham số. [Mục 3.1–3.3; Mục 6]

### 9.2. Những kết luận cần giới hạn

- **Về “giới hạn”:** đây là giới hạn thực hành của các cấu hình và ví dụ đã khảo sát, không phải một định lý chặn trên phổ quát cho mọi bộ phát hiện chuyển tiếp.
- **Về tính tối ưu:** bổ đề Neyman–Pearson tạo động cơ dùng hàm hợp lý, nhưng không chứng minh ưu thế đồng đều sau khi khớp các giả thuyết hợp thành và có sai dạng mô hình. Bảng 2 đã cho một điểm vận hành nơi phương sai tốt hơn.
- **Về số lượng dữ liệu:** băng hà có nhiều điểm và tín hiệu rõ, nhưng so sánh ba bộ dữ liệu không phải thí nghiệm giữ mọi yếu tố khác cố định rồi chỉ tăng số điểm. Không suy ra một quy tắc chung rằng 121 điểm luôn đủ hay 16 điểm luôn không đủ.
- **Về dự báo:** phát hiện mô hình động lực học thay đổi trên một đoạn đã chọn khác đánh giá thời gian báo trước, tỷ lệ báo động theo thời gian hoặc dự báo mốc chuyển tiếp trên sự kiện mới.
- **Về độ bền trước sai mô hình:** một ví dụ sinh–tử phi tuyến là minh họa có giá trị, nhưng chưa bao phủ nhiễu màu, nhiều biến chậm, tham số không đơn điệu, sai số quan sát hoặc nhiều kiểu phân nhánh.

Nguồn và cơ sở: Mục 2.1, 3.1, 3.4, 4.1–6; Hình 5, 8; Bảng 2. Các giới hạn suy luận trong danh sách là diễn giải của người phân tích, không phải các thí nghiệm đã được thực hiện bổ sung.

### 9.3. Khi nào phương pháp có thể thất bại?

Tác giả nêu ba lớp quan trọng: cú sốc đẩy trạng thái sang miền hút khác, chuyển tiếp chủ yếu do nhiễu, và tiến gần phân nhánh quá nhanh hoặc quá phi tuyến để có xu hướng dần dần. Bài còn nhấn mạnh phải đánh giá **mức phù hợp của mô hình**: nếu cả hai mô hình đều mô tả kém, lựa chọn mô hình tốt hơn tương đối chưa xác nhận cơ chế. Tuy nhiên, PDF không cung cấp một bộ kiểm tra đầy đủ mức phù hợp và kết quả áp dụng cho cả ba ví dụ. [Mục 2.1, tr. 2528; Mục 3.1, tr. 2529; Mục 6, tr. 2537]

**Diễn giải của người phân tích:** các trường hợp nhiễu có tương quan, độ chính xác cảm biến thay đổi, thay đổi mức nền không liên quan đến mất ổn định, hoặc nhiều cơ chế cạnh tranh đều có thể làm OU trở thành đối chứng quá đơn giản. Khi ấy, một ROC đẹp dưới cặp OU/LSN chỉ cho thấy hai mô hình giả định dễ phân biệt, chưa bảo đảm tỷ lệ sai trên dữ liệu thật. Đây là điều kiện cần kiểm tra thêm, chưa phải các thất bại mà bài đã đo định lượng.

## 10. Khả năng chuyển sang chuỗi thời gian y sinh

Phần này là **diễn giải và giả thuyết của người phân tích**. Bài không có dữ liệu y sinh và không kiểm chứng cơ chế chuyển tiếp trong cơ thể người.

Thành phần có khả năng chuyển giao rõ nhất là **khung hiệu chuẩn hai loại sai số**. Chẳng hạn, nếu nghiên cứu một biến cố sinh lý, có thể hỏi chỉ báo phân biệt ra sao giữa một đoạn ổn định có các dao động nền và một đoạn tiến tới biến cố, thay vì chỉ báo cáo chỉ báo tăng ở những trường hợp đã biết có biến cố. Tuy nhiên, việc chọn hai mô hình phải dựa trên sinh lý của hiện tượng, không mặc định mọi biến cố là phân nhánh nút–yên hoặc đều có chậm dần tới hạn.

Một thử nghiệm mở rộng hợp lý, **chưa được thực hiện ở bước này**, gồm: xác định rõ biến cố và thời hạn cảnh báo; xây dựng đối chứng giữ nhịp nền, phụ thuộc thời gian và nhiễu đo phù hợp; tính chỉ báo chỉ bằng dữ liệu đã có tại thời điểm quyết định; đánh giá trên người hoặc lần ghi độc lập; báo cáo cảnh báo sai theo thời gian theo dõi, bỏ sót và thời gian báo trước. Các thay đổi do can thiệp, vận động, nhịp ngày đêm hoặc cảm biến cần được xét như những giải thích cạnh tranh.

Đây là một hướng kiểm chứng khả năng áp dụng, **không phải khoảng trống y sinh đã được xác lập chỉ từ PDF này**. Chỉ sau khi kiểm tra các giả định và dữ liệu thực mới có thể quyết định có dùng cặp OU/LSN hay chỉ kế thừa khung đánh giá sai số.

## 11. Hồ sơ phương pháp

**Hồ sơ phương pháp (Methodological Fingerprint)** dưới đây tóm tắt đúng đơn vị suy luận của nghiên cứu.

| Trường | Nội dung |
| --- | --- |
| **Bài toán (Problem)** | Định lượng khả năng phân biệt một hệ ổn định với hệ đang tiến gần chuyển tiếp, đặc biệt sự đánh đổi cảnh báo sai và bỏ sót từ một chuỗi |
| **Đầu vào (Input)** | Chuỗi trạng thái một biến cùng thời điểm quan sát; ba ví dụ riêng có 40, 16 và 121 điểm |
| **Thông tin biết trước (Known information)** | Chọn lớp phân nhánh nút–yên, tham số thay đổi tuyến tính, cấu trúc SDE và mô hình OU đối chứng; tham số được khớp từ chuỗi; mô hình sinh–tử và can thiệp chỉ biết ở mức thiết kế kiểm chứng tương ứng |
| **Đầu ra (Output)** | Tham số khớp, δ quan sát, hai phân bố chỉ báo mô phỏng, ROC và các tỷ lệ phát hiện/cảnh báo sai tại ngưỡng; không phải thời điểm biến cố đã được kiểm chứng |
| **Phương án đối chiếu (Existing baseline)** | Xu hướng Kendall của phương sai và tự tương quan trên cửa sổ nửa chuỗi; AIC được thảo luận như cách chọn mô hình chưa đủ cho mục tiêu định lượng sai số |
| **Thành phần mới (New component)** | Đặt EWS thành lựa chọn mô hình và mô phỏng dưới cả mô hình không lẫn đối thuyết, khớp lại trên từng hiện thực; đánh giá chung các chỉ báo bằng ROC. Tính mới được ghi theo phát biểu của tác giả |
| **Giả định (Assumptions)** | Mô hình gần cân bằng hút thuộc lớp nút–yên là xấp xỉ có ích; tiến gần ngưỡng chậm, đơn điệu, gần tuyến tính; dạng nhiễu phù hợp; mô hình OU thể hiện đủ động lực học ổn định; tối ưu và tích phân số đáng tin |
| **Kiểm chứng (Validation)** | Một ví dụ sinh–tử phi tuyến, H6, băng hà III; mỗi ví dụ sinh 500 chuỗi dưới mỗi mô hình khớp, khớp lại cả hai; không có kiểm tra độc lập theo sự kiện hay đánh giá trực tuyến |
| **Kết quả chính (Main finding)** | Tại cảnh báo sai 5%, độ nhạy phương sai/hàm hợp lý là 25/61%, 5,0/34%, 5,4/100% theo ba ví dụ; tại độ nhạy 90%, mô phỏng cho cảnh báo sai 49/55%, nên ưu thế không đồng đều |
| **Câu hỏi còn mở (Unresolved questions)** | Mức phù hợp của cả hai mô hình, hiệu chuẩn ngoài họ mô hình, bất định tham số, độ nhạy tiền xử lý/cửa sổ/lấy mẫu, dự báo trên sự kiện mới; cần giải quyết các bất nhất bản in trước khi tái lập chính xác |
| **Khả năng tái lập (Reproduction feasibility)** | Có phương trình, tham số ví dụ và địa chỉ mã/dữ liệu theo PDF; khả thi có điều kiện sau khi kiểm tra mã, phiên bản và các quy tắc triển khai. Chưa tải mã, chưa tái lập kết quả số |

Nguồn tổng hợp: Mục 3–6, tr. 2529–2537; Hình 1–8; Bảng 1–2. Những yêu cầu mở rộng và nhận xét về kiểm chứng ngoài mẫu là đánh giá của người phân tích.

## 12. Tài liệu đọc tiếp và quyết định tái lập

### 12.1. Thứ tự kiểm tra đầu tiên

**Ưu tiên đầu tiên là xác định phiên bản mô hình đã được chạy.** Cần đối chiếu SDE, mômen và hàm tính hợp lý trong mã với (3.2), (3.7), (3.10), (3.11); xác nhận miền tham số và phép đổi tham số về OU. Sau đó kiểm tra thời gian mô phỏng 0–500 hay 0–1.000, tốc độ tăng a trên cùng thang thời gian, và đoạn dữ liệu thực sự dùng cho các hình. Đây là các điểm quyết định tái lập chính xác, không chỉ vấn đề định dạng công thức.

PDF cho biết có gói R **`earlywarning`** và ghi địa chỉ dữ liệu/mã tại [kho mã được bài báo dẫn](https://github.com/cboettig/earlywarning), tr. 2533 và 2537. **Chưa truy cập địa chỉ này**, nên chưa xác nhận tình trạng tồn tại, phiên bản, cấu trúc, giấy phép hoặc khả năng chạy hiện nay. Không coi việc PDF ghi địa chỉ là bằng chứng đã có đầy đủ mã và dữ liệu trong môi trường làm việc.

Các thông tin cần thu thập tiếp gồm: phiên bản mã và phụ thuộc R; hạt giống ngẫu nhiên; thuật toán tối ưu, điểm bắt đầu và tiêu chí hội tụ; cách xử lý nghiệm biên/thất bại; phương pháp mô phỏng và bước thời gian; khởi tạo chuỗi; lưới nội suy và băng thông loại xu hướng băng hà; công thức tự tương quan, cửa sổ và quy tắc hạng; cách chọn ngưỡng hoặc nội suy các tỷ lệ trong bảng. Đây là những chi tiết **PDF chưa cung cấp đủ**, không phải khẳng định chúng không có ở bất cứ đâu.

### 12.2. Những nguồn nên đọc, theo danh mục của chính bài báo

| Nguồn được bài dẫn | Tên gốc kèm nghĩa tiếng Việt | Mục đích đọc tiếp |
| --- | --- | --- |
| Cox (1961), [41], và Cox (1962), [48] | *Tests of separate families of hypotheses* — “Kiểm định giữa các họ giả thuyết riêng”; *Further results on tests of separate families of hypotheses* — “Kết quả bổ sung về kiểm định giữa các họ giả thuyết riêng” | Hiểu nền tảng lựa chọn mô hình với tham số phải ước lượng |
| McLachlan (1987), [42] | *On bootstrapping the likelihood ratio test statistic for the number of components in a normal mixture* — “Lấy mẫu lại thống kê tỷ số hợp lý để kiểm định số thành phần của hỗn hợp chuẩn” | Hiểu vai trò mô phỏng phân bố kiểm định và thao tác khớp lại |
| Gardiner (2009), [44] | *Stochastic methods: a handbook for the natural and social sciences* — “Phương pháp ngẫu nhiên: cẩm nang cho khoa học tự nhiên và xã hội” | Kiểm tra mômen, phân bố chuyển tiếp và sự nhất quán SDE |
| Drake và Griffen (2010), [5] | *Early warning signals of extinction in deteriorating environments* — “Cảnh báo sớm tuyệt chủng trong môi trường suy giảm” | Xác định thiết kế can thiệp, các lần lặp và lý do chọn H6 |
| Dakos và cộng sự (2008), [16] | *Slowing down as an early warning signal for abrupt climate change* — “Chậm dần như dấu hiệu cảnh báo sớm biến đổi khí hậu đột ngột” | Xác định đoạn băng hà và tiền xử lý ban đầu |
| Lenton và cộng sự (2012), [32] | *Early warning of climate tipping points from critical slowing down: comparing methods to improve robustness* — “Cảnh báo sớm điểm tới hạn khí hậu từ chậm dần tới hạn: so sánh phương pháp để tăng độ vững” | Kiểm tra ảnh hưởng lựa chọn cửa sổ và phương pháp xử lý |
| Hastings và Wysham (2010), [30] | *Regime shifts in ecological systems can occur with no warning* — “Chuyển chế độ trong hệ sinh thái có thể xảy ra không có cảnh báo” | Xác định phạm vi cơ chế nằm ngoài cặp mô hình của bài |

Nguồn tên và thông tin tài liệu: danh mục tham khảo, tr. 2538–2539. Các tài liệu này **chưa được đọc** trong bước phân tích hiện tại; không dùng chúng như bằng chứng độc lập.

### 12.3. Quyết định

**Mức chọn: ứng viên tái lập (Reproduction candidate), có điều kiện.** Lý do là quy trình trung tâm rõ, chi phí mô phỏng có thể xác định, có các mốc số trong Bảng 1–2 để đối chiếu, và bài chỉ ra nơi cung cấp mã/dữ liệu. Giá trị nghiên cứu nằm ở việc tái lập **khung hiệu chuẩn sai số**, không chỉ dựng lại một đường chỉ báo tăng.

Rào cản trước mắt là các bất nhất công thức và thang thời gian, cùng thông tin triển khai chưa đầy đủ trong PDF. Một kế hoạch tái lập hợp lý của người phân tích là bắt đầu từ ví dụ mô phỏng: xác nhận mô hình nhất quán → khôi phục dữ liệu hoặc sinh đúng cấu hình gốc → kiểm tra δ khoảng 5,1 → khớp lại hai mô hình trên mỗi nhóm 500 chuỗi → đối chiếu Hình 2, 5, 8c và hai hàng mô phỏng trong bảng. Chỉ sau đó mới xử lý H6 và băng hà, nơi lựa chọn đoạn và tiền xử lý khó kiểm soát hơn. Toàn bộ kế hoạch này **chưa được chạy**.

Một bước mở rộng sau tái lập có thể dùng nhiều chuỗi sinh–tử độc lập, thay đổi có kiểm soát số điểm và tốc độ tiến gần ngưỡng, rồi kiểm tra tỷ lệ sai thực tế có khớp với ROC dự kiến hay không. Đây là đề xuất kiểm chứng của người phân tích, không phải kết quả hay khoảng trống đã được bài chứng minh.

## 13. Ghi nhận kiểm tra tài liệu

Đã đọc lại file trên đĩa, kiểm tra mạch tiếng Việt, định nghĩa các viết tắt, nguồn trang/hình/phương trình, hồ sơ 11 trường và quyết định tái lập. Cả **16 khối toán** đều có cặp dấu phân cách đứng riêng dòng, nội dung không rỗng, ngoặc nhọn và môi trường nhiều dòng cân bằng; không phát hiện ký tự điều khiển lỗi, dấu phân cách toán cũ hoặc công thức trong khối mã. Các công thức quan trọng đã được đối chiếu bản in; công thức hay ký hiệu do người phân tích đặt được phân biệt rõ.

Đã chuẩn bị bản xem trước tạm bằng bộ hiển thị MathJax cục bộ, nhưng trình duyệt không khởi chạy được do giới hạn môi trường. Vì vậy, mức kiểm tra đạt được là **kiểm tra cú pháp và đối chiếu PDF**, chưa xác nhận hiển thị trực quan của toàn bộ công thức Markdown và không tuyên bố đã biên dịch thành công. Không thực hiện tái lập kết quả số của bài báo.

## Critical Audit (chờ Prompt 02)
