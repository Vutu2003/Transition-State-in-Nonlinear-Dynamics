# Farazmand và Sapsis — Biến cố cực đoan: cơ chế và dự báo

**Bài báo:** *Extreme Events: Mechanisms and Prediction* — “Biến cố cực đoan: cơ chế và dự báo”. **Tác giả:** Mohammad Farazmand và Themistoklis P. Sapsis. **Tạp chí ghi trong PDF:** *Applied Mechanics Reviews*. **DOI:** 10.1115/1.4042065.

**Phiên bản và quy ước trang:** [PDF được chỉ định](<../paper/8 Extreme Events: Mechanisms and Prediction.pdf>) là **bản thảo được chấp nhận, chưa biên tập bản in**, ghi nhận bài ngày 15/3/2018 và đăng bản thảo ngày 22/11/2018. Mã file dùng năm **2018 theo bản thảo này**; không suy ra năm, tập hoặc số bài của phiên bản xuất bản chính thức từ ngày tải PDF. Số trang in **1–25** trùng số trang PDF; không có bìa riêng. Đã đọc toàn bộ 25 trang, gồm 198 mục tài liệu tham khảo, và đối chiếu trực quan Hình 1–20 cùng các công thức trọng tâm. Chỉ sử dụng PDF này; không dùng web, không đọc các công trình được dẫn và không tải mã hoặc dữ liệu ngoài.

**Định vị nghiên cứu:** Đây là **bài tổng quan phương pháp**, không phải một thuật toán dự báo duy nhất mới được đề xuất và kiểm tra trên nhiều bộ dữ liệu độc lập. Mạch chính là: hình học và vật lý sinh biến cố → tìm trạng thái tiền triệu có ý nghĩa động lực học → chọn chỉ báo đo được → ước lượng xác suất biến cố trong một khoảng tương lai → đánh giá đồng thời cảnh báo sai và bỏ sót. Phương pháp biến phân ở Mục 4 được tác giả trình bày lại từ công trình trước [136]; hướng tự động tìm chỉ báo từ dữ liệu ở Mục 5.3 mới là đề cương nghiên cứu, chưa phải thuật toán đã được giải và kiểm chứng trong bài. [Tóm tắt; Mục 1, tr. 1–3; Mục 4, tr. 9–15; Mục 5.3–6, tr. 17–19]

**Quy ước mức phát biểu:** **Tác giả khẳng định (Authors claim)** là điều bài nêu; **Bằng chứng hỗ trợ (Evidence supports)** là điều công thức, hình hoặc kết quả được trình bày thực sự cho phép kết luận; **Diễn giải của người phân tích (Analyst interpretation)** là kiểm tra toán học, đánh giá hoặc giả thuyết bổ sung. Những bất nhất của bản thảo được đánh dấu tại chỗ, không âm thầm sửa thành công thức được gán cho tác giả. Phần kiểm định phản biện của Prompt 02 được để chờ cuối file.

## 1. Câu chuyện nghiên cứu: vì sao biết thống kê cực trị vẫn chưa đủ?

Bài mở đầu bằng sóng biển bất thường, thời tiết cực đoan, động đất và sự cố lưới điện. Các lĩnh vực này cùng quan tâm đến những diễn biến ít gặp nhưng có thể gây hậu quả lớn. Tuy nhiên, biết tần suất hoặc phân bố đuôi của một đại lượng chưa trả lời được **trạng thái hiện tại nào đang chuẩn bị sinh ra một biến cố cụ thể**. Đó là sự khác nhau giữa thống kê dài hạn và dự báo một sự kiện theo thời gian. [Mục 1, tr. 1–3; Hình 1]

Tác giả chia lĩnh vực thành bốn phần liên hệ nhau: cơ chế hình thành, dự báo theo thời gian, giảm thiểu và thống kê. Cơ chế được đặt ở trung tâm vì có thể giúp chọn chỉ báo, thiết kế can thiệp và hiểu xác suất xuất hiện biến cố. Bài tập trung vào **cơ chế và dự báo**, không thực hiện một nghiên cứu kiểm soát can thiệp hoặc một đánh giá toàn diện các phương pháp thống kê cực trị. [Hình 1, tr. 1; Mục 1, tr. 2–3; Mục 6, tr. 19]

### 1.1. Những khó khăn được tác giả nêu

| Khó khăn | Hệ quả phương pháp | Mức bằng chứng trong PDF |
| --- | --- | --- |
| Biến cố có thể xuất hiện khi tín hiệu quan sát trực tiếp chưa có dấu hiệu rõ | Không thể chỉ nhìn biên độ hiện tại của đại lượng cần dự báo | Động cơ ở tr. 1–2; hai ứng dụng sau cho ví dụ về chỉ báo khác đại lượng đích |
| Biết phương trình không có nghĩa đã hiểu cơ chế | Nhiều bậc tự do và hỗn loạn che khuất các tương tác quan trọng | Mục 1, 4.2; mạng tương tác Fourier là ví dụ cụ thể |
| Quan sát thiếu trạng thái và dữ liệu cực đoan khan hiếm | Khó hiệu chỉnh mô hình và ước lượng độ tin cậy ở vùng đuôi | Được thảo luận ở Mục 1; không có một thí nghiệm đồng hóa dữ liệu mới trong bài |
| Các phương pháp hình học có điều kiện áp dụng và chi phí lớn | Đa tạp chậm hoặc đường chuyển tiếp khó tính ở số chiều cao | Mục 3.1 và 3.3; những giới hạn số chiều là nhận xét theo tài liệu tại thời điểm bản thảo |
| Một chỉ báo có thể bỏ sót hoặc báo động liên tục | Cần đánh giá cả hai loại sai, không chỉ số lần báo trúng | Mục 5.1–5.3; Hình 18–20 |

**Tác giả khẳng định:** cần một cách kết hợp phương trình vật lý với thông tin thống kê của tập hút để phát hiện cơ chế ở hệ nhiều chiều. **Bằng chứng hỗ trợ:** cách tối ưu có ràng buộc tạo được một cấu trúc tiền triệu gọn trong ví dụ dòng Kolmogorov; cấu trúc này gợi ra chỉ báo dự báo ngắn hạn. **Diễn giải của người phân tích:** các ví dụ không chứng minh có một phương pháp duy nhất giải được mọi loại biến cố cực đoan, hoặc mọi chỉ báo dựa trên cơ chế đều vượt mọi phương pháp từ dữ liệu. [Mục 4.1–4.2; Mục 5.2; Mục 6]

## 2. Đặt bài toán: trạng thái, đại lượng quan sát và biến cố

### 2.1. Mô hình động lực học và thông tin biết trước

Khung chính bắt đầu từ một bài toán giá trị ban đầu:

$$
\partial_t u=N(u),\qquad u(\mathbf{x},0)=u_0(\mathbf{x}),\qquad
u(t)=S^{t}(u_0).
$$

u là trạng thái của hệ, có thể là một trường theo không gian; N là toán tử do vật lý quy định; S là ánh xạ nghiệm đưa trạng thái ban đầu tới trạng thái sau thời gian t. Nguồn: Phương trình (1)–(2), Mục 2, tr. 3. Bài cũng xét hệ phương trình vi phân thường hữu hạn chiều, chẳng hạn các bộ dao động FitzHugh–Nagumo. Đây không phải thiết lập chỉ có một chuỗi vô hướng và hoàn toàn không biết mô hình. [Mục 2, tr. 4]

Không gian trạng thái được trang bị độ đo xác suất bất biến μ. Một **đại lượng quan sát** là hàm f đưa trạng thái sang một số thực, ví dụ tốc độ tiêu tán năng lượng hoặc biên độ bao sóng cực đại. Sự ngẫu nhiên của chuỗi quan sát có thể đến từ việc chọn trạng thái ban đầu theo μ dù phương trình tiến hóa là tất định. Trong nhánh chuyển tiếp do nhiễu ở Mục 3.3, bài dùng một mô hình ngẫu nhiên riêng. [Mục 2, tr. 3; Mục 3.3, tr. 8–9]

### 2.2. Biến cố cực đoan không đồng nghĩa với mọi chuyển tiếp hiếm

Tập trạng thái cực đoan được định nghĩa bằng một ngưỡng:

$$
E_f(f_e)=\{u\in\mathcal{U}:f(u)>f_e\}.
$$

Nguồn: Định nghĩa 1, Phương trình (3), tr. 3; minh họa ở Hình 2, tr. 4. Không gian trạng thái là 𝒰; ngưỡng của đại lượng quan sát được ký hiệu f có chỉ số e. Một cực tiểu bất thường có thể xét bằng cách đổi f thành −f.

**Diễn giải của người phân tích:** điều kiện vượt ngưỡng này tự nó chưa ràng buộc xác suất biến cố phải rất nhỏ. Ngưỡng cần có ý nghĩa với ứng dụng và thống kê của hệ. Các đợt bùng phát tuần hoàn ở Hình 6 minh họa cơ chế tăng biên độ, không tự chứng minh tính hiếm hoặc tính khó dự báo. Tác giả cũng nói rõ chuyển tiếp hiếm giữa hai trạng thái tồn tại lâu không nhất thiết thuộc định nghĩa cực đoan theo biên độ này. [Mục 2, tr. 3–4; Hình 3, 6]

Muốn tìm trạng thái **chưa cực đoan nhưng sẽ đi vào vùng cực đoan** trong một khoảng hữu hạn, bài định nghĩa:

$$
A_f(\tau,f_e)=
\left\{u\in\mathcal{U}\setminus E_f(f_e):
\exists t\in(0,\tau],\ S^{t}(u)\in E_f(f_e)\right\}.
$$

τ là giới hạn thời gian tìm biến cố. Nguồn: Định nghĩa 2, Phương trình (16), tr. 9. Bài gọi đây là miền hút hữu hạn thời gian của biến cố cực đoan; nó **không phải miền hút tiệm cận của một cân bằng ổn định**. Ký hiệu nghịch ảnh xuất hiện ở dạng thứ hai của (16) không yêu cầu S có ánh xạ nghịch toàn cục.

### 2.3. Đầu vào và đầu ra khác nhau theo từng phần

| Tầng phân tích | Đầu vào và điều đã biết | Đầu ra thực sự |
| --- | --- | --- |
| Giải thích hình học | Hệ phương trình, tham số; khi phù hợp có phân chia nhanh–chậm hoặc các tập bất biến | Cơ chế bùng phát, cấu trúc hút–đẩy, đường chuyển tiếp có xác suất đáng kể |
| Thăm dò biến phân | Phương trình và điều kiện biên; đại lượng f; thời gian τ; các ràng buộc thống kê từ tập hút | Một hoặc một số trạng thái ban đầu tối ưu và quỹ đạo tiếp theo |
| Chọn chỉ báo dựa trên cơ chế | Cấu trúc tối ưu và các đại lượng có thể đo, như hệ số Fourier của trường vận tốc | Hàm chỉ báo g, không nhất thiết là chính f |
| Hiệu chuẩn dự báo | Các cặp giá trị chỉ báo hiện tại và cực đại tương lai; ngưỡng biến cố; khoảng dự báo | Mật độ có điều kiện, xác suất sắp có biến cố, quy tắc báo động |
| Tìm chỉ báo hoàn toàn từ dữ liệu | Một lớp hàm chỉ báo và một hàm mục tiêu sai số cần được định nghĩa nhất quán | Được phác thảo ở Mục 5.3; chưa có thuật toán tối ưu đã giải trong PDF |

Nguồn: Mục 2–5, tr. 3–19.

Trong ví dụ chất lưu, đầu vào để tính chỉ báo là **thông tin không gian của trường vận tốc đủ để lấy một hệ số Fourier**, không chỉ chuỗi tiêu tán năng lượng. Trong ví dụ sóng, cần biết ít nhất các nhóm sóng hoặc một phép chiếu của bao sóng. Bài không chứng minh có thể suy ra các chỉ báo này từ bất kỳ một cảm biến điểm nào. [Mục 4.2–4.3; Mục 5.2; Mục 6]

## 3. Nguồn gốc phương pháp và cách hiểu tính mới

Ba lớp đóng góp phải được phân biệt:

1. **Kiến thức tổng hợp:** lý thuyết hệ nhanh–chậm, quỹ đạo đồng liên và dị liên, lý thuyết đường chuyển tiếp, phương trình sóng phi tuyến và thống kê có điều kiện. Các công cụ này được dẫn về tài liệu nền; chúng không phải phát minh của bài tổng quan. [Mục 3; Mục 4.3; Mục 5.1]
2. **Phương pháp đã có từ công trình trước của nhóm tác giả:** phương pháp biến phân được ghi rõ là đề xuất trong Farazmand và Sapsis (2017), tài liệu [136]. Ứng dụng dòng Kolmogorov cũng được trình bày lại từ nguồn này. Dự báo sóng bậc thấp được dẫn về Cousins và Sapsis (2016), [188], và mở rộng hai chiều về Farazmand và Sapsis (2017), [189]. [Mục 4.1–4.3; danh mục, tr. 24–25]
3. **Tổng hợp khái niệm và đề xuất hướng nghiên cứu trong bản thảo:** nối tìm cơ chế với chọn chỉ báo và đánh giá xác suất; phác thảo tìm chỉ báo bằng tối thiểu hóa một hàm sai số. Phần tối ưu chỉ báo được tác giả nói sẽ xử lý ở nơi khác. [Mục 5.3–6, tr. 17–19]

**Tác giả khẳng định:** có triển vọng về một khung toán học chung để tìm cơ chế ở nhiều hệ. **Bằng chứng hỗ trợ:** bài trình bày một cách đặt bài toán tối ưu có thể chuyển giữa ứng dụng, cùng hai ví dụ có vật lý khác nhau. **Diễn giải của người phân tích:** nên phân loại đây là **bài tổng quan định hướng phương pháp và tổng hợp một khung phân tích**, không gán toàn bộ đóng góp của [136], [188], [189] thành phương pháp mới công bố lần đầu trong bản thảo này.

Việc những tài liệu ấy xuất hiện trong danh mục không có nghĩa đã đọc chúng. Các chi tiết không được trình bày lại trong PDF vẫn là thông tin cần kiểm tra tiếp, không được tự khôi phục bằng suy đoán.

## 4. Ba lớp cơ chế được tổng quan

### 4.1. Hệ nhanh–chậm: bùng phát khi rời vùng hút theo phương ngang

Một quỹ đạo có thể đi chậm gần đa tạp chậm, rồi bùng phát khi gặp vùng đẩy theo các phương ngang với đa tạp. Tốc độ tăng biên độ đến từ động lực nhanh khi rời vùng đó; sau đó quỹ đạo trở lại vùng hút. Cơ chế này được minh họa bằng sơ đồ Hình 4 và một dạng chuẩn của **phân nhánh Hopf kỳ dị** (*singular Hopf bifurcation*) trong hệ nhanh–chậm:

$$
\begin{aligned}
\varepsilon\dot{x}&=y-x^{2}-x^{3},\\
\dot{y}&=z-x,\\
\dot{z}&=-\nu-ax-by-cz.
\end{aligned}
$$

Nguồn: Phương trình (4), tr. 5. ε nhỏ tạo tách biệt thang thời gian; a, b, c, ν là các tham số cố định. Bài dùng a = −0,3872; b = −0,3251; c = 1,17; ν = 0,0072168. Ở giới hạn ε bằng 0, đa tạp tới hạn được xác định bởi:

$$
\mathcal{M}_0=\{(x,y,z):y=x^{2}+x^{3}\}.
$$

Đây là Phương trình (6), tr. 5. Dòng chậm trên đa tạp và dòng nhanh ngoài đa tạp được mô tả riêng bằng (5) và hệ đổi thời gian (7). Hình 5 chỉ các nhánh hút, nhánh đẩy và hai điểm gấp. Với ε = 0,001, Hình 6 cho một quỹ đạo tuần hoàn ổn định gồm các dao động nhỏ xen đợt bùng phát. [Mục 3.1, tr. 5–6]

**Điều kiện toán học:** lý thuyết nhiễu suy biến hình học được bài viện dẫn cần các điều kiện, đặc biệt **tính hút hoặc đẩy trội theo phương ngang** (*normal hyperbolicity*): động lực theo phương ngang mạnh hơn động lực bên trong đa tạp. Không nên hiểu mô tả “đa tạp tới hạn tồn tại sau nhiễu” là một bảo đảm áp dụng nguyên vẹn ngay tại các điểm gấp, nơi điều kiện này mất đi. Đây là lưu ý của người phân tích khi diễn giải đoạn tr. 6; bài không trình bày chứng minh chi tiết qua vùng gấp.

Để minh họa bùng phát không tuần hoàn, bài xét các phần tử FitzHugh–Nagumo ghép với nhau:

$$
\begin{aligned}
\dot{x}_i&=x_i(a_i-x_i)(x_i-1)-y_i
+k\sum_{j=1}^{n}A_{ij}(x_j-x_i),\\
\dot{y}_i&=b_ix_i-c_iy_i,\\
\bar{x}&=\frac{1}{n}\sum_{i=1}^{n}x_i.
\end{aligned}
$$

Hai dòng đầu là Phương trình (8), tr. 6; dòng cuối là đại lượng quan sát dùng trong Hình 7. A là ma trận kề, k là cường độ ghép, n là số phần tử. Với hai phần tử, bài dùng a ở cả hai phần tử bằng −0,025794; c ở cả hai bằng 0,02; hai b lần lượt là 0,0065 và 0,0135; k = 0,128; đường chéo A bằng 0, hai phần tử ngoài đường chéo bằng 1. [Chú thích Hình 7, tr. 7]

Hình 7 cho các đỉnh lớn không có chu kỳ lặp đều trên nền dao động nhỏ. Đây là minh họa cơ chế và hiện tượng, **chưa phải một thí nghiệm kiểm tra chỉ báo dự báo cho mô hình thần kinh**. Bài cũng lưu ý tính toán các đa tạp bất biến trở nên tốn kém khi số chiều tăng; nhận xét rằng các phương pháp được dẫn còn giới hạn ở khoảng bốn hoặc năm chiều phải được hiểu theo tài liệu tại thời điểm bản thảo. [Mục 3.1, tr. 7]

### 4.2. Quỹ đạo đồng liên và dị liên

**Quỹ đạo đồng liên** (*homoclinic orbit*) tiến về cùng một tập bất biến khi xét thời gian tiến và lùi; ví dụ được bàn là quỹ đạo Shilnikov của một điểm cân bằng kiểu yên–tiêu. **Quỹ đạo dị liên** (*heteroclinic orbit*) nối các tập bất biến khác nhau. Chuyển động có thể gồm một đoạn xoắn chậm gần điểm cân bằng và một đoạn bị đẩy nhanh ra xa; các quỹ đạo tuần hoàn không ổn định lân cận tạo khung cho bùng phát hỗn loạn. [Mục 3.2, tr. 7; Hình 8]

Bài tóm tắt kết quả Shilnikov và các ứng dụng đã được báo cáo, không tự chứng minh định lý hoặc xây một chỉ báo dự báo mới từ Hình 8. Không nên đồng nhất cơ chế này với yêu cầu tham số điều khiển đang trôi dần tới một ngưỡng phân nhánh: hệ có thể bùng phát lặp lại trong một chế độ với tham số giữ cố định. [Mục 3.2; diễn giải của người phân tích]

### 4.3. Chuyển tiếp do nhiễu và lý thuyết đường chuyển tiếp

Một hệ có nhiều cân bằng ổn định vẫn có thể chuyển giữa chúng nhờ nhiễu. Bài giới thiệu **lý thuyết đường chuyển tiếp** (*transition-path theory*) để tính cấu trúc xác suất của các quỹ đạo chuyển tiếp, thay vì chỉ tần suất nhảy giữa các vùng. Sau mô hình Langevin bậc hai (9), bài xét giới hạn ma sát lớn:

$$
\dot{u}=-\nabla V(u)+\sqrt{2}\,\sigma(u)\eta(t),\qquad
a(u)=\sigma(u)\sigma(u)^{\dagger}.
$$

Đây là Phương trình (10) và định nghĩa ma trận khuếch tán trước đó, tr. 8. V là thế, η là nhiễu trắng trung bình 0, σ điều chỉnh nhiễu; dấu † trên ma trận biểu thị liên hợp chuyển vị. Căn chỉ bao quanh số 2, không bao quanh toàn bộ σ. Bài đã chuẩn hóa khối lượng và đổi thời gian để loại hệ số ma sát.

Với hai vùng trạng thái đã chọn, mật độ trạng thái tham gia chuyển tiếp được biểu diễn:

$$
\rho_{12}(u)=q_{+}(u)q_{-}(u)\rho(u).
$$

Nguồn: Phương trình (11), tr. 8. ρ là mật độ bất biến duy nhất. Bài giả định hệ có tính ergodic, nghĩa là trung bình theo thời gian phù hợp trung bình theo độ đo bất biến cho các đại lượng thích hợp. Hai **hàm xác suất đến miền đích** (*committor functions*) có ý nghĩa khác nhau: q có chỉ số + là xác suất tương lai tới vùng thứ hai trước vùng thứ nhất; q có chỉ số − mô tả việc quỹ đạo đến trạng thái hiện tại sau lần rời vùng thứ nhất thay vì vùng thứ hai. Không nên hiểu ρ có chỉ số 12 là một mật độ đã được chuẩn hóa có tổng khối lượng bằng 1 trên toàn không gian; công thức mô tả phần mật độ gắn với quỹ đạo chuyển tiếp. [Mục 3.3; diễn giải về chuẩn hóa]

Quy trình là giải các bài toán Kolmogorov lùi cho hai hàm xác suất và phương trình Fokker–Planck dừng cho ρ, rồi tính mật độ cùng dòng xác suất chuyển tiếp bằng (11), (15). Các điều kiện biên cố định giá trị 0 hoặc 1 trên hai vùng. Trong (13), toán tử liên hợp được xác định theo tích vô hướng có trọng số ρ; không tự thay bằng toán tử Fokker–Planck không trọng số. [Phương trình (12)–(15), tr. 8–9]

Hình 9 của thế Mueller gồ ghề cho mật độ, hàm xác suất đến miền đích và các đường dòng chuyển tiếp. Hình được tái bản từ [127], không phải thí nghiệm mới do bài tổng quan thực hiện. Bài nhấn mạnh chi phí giải ba phương trình vi phân riêng phần tăng mạnh theo số chiều; không báo cáo một giải pháp mới vượt giới hạn này. [Mục 3.3, tr. 8–9; chú thích Hình 9]

## 5. Trọng tâm biến phân: tìm trạng thái tiền triệu có ý nghĩa vật lý

### 5.1. Không tìm toàn bộ miền tiền triệu, mà tìm các đại diện

Tập trạng thái có thể dẫn đến cực đoan trong (16) có hình học phức tạp. Ý tưởng ở Mục 4 là tìm một số trạng thái ban đầu tạo **mức tăng lớn của đại lượng quan sát**, rồi kiểm tra cấu trúc vật lý của chúng để suy ra cơ chế. Bài không khẳng định đã tính được toàn bộ miền tiền triệu hoặc phân bố xác suất đầy đủ của nó. [Mục 4.1, tr. 9–10]

Bài toán trung tâm là:

$$
\sup_{u_0\in\mathcal{A}}
\left[f\bigl(S^{\tau}(u_0)\bigr)-f(u_0)\right].
$$

Nguồn: Phương trình (17), tr. 10. τ là thời gian tăng trưởng đã chọn, 𝒜 là tập trạng thái khả dĩ gần tập hút. Hàm mục tiêu đo **mức tăng sau một khoảng thời gian**, không phải giá trị cực đại trên mọi thời điểm, không phải xác suất biến cố, cũng không phải sai số dự báo của một bộ phân loại.

**Diễn giải của người phân tích:** tối đa hóa mức tăng chưa tự bảo đảm giá trị cuối vượt ngưỡng; cũng chưa tự loại trạng thái vốn đã cực đoan ở thời điểm đầu. Định nghĩa (16) có điều kiện loại trạng thái cực đoan ban đầu, còn (17)–(19) không viết điều kiện này thành một ràng buộc riêng. Chính bài sau đó chỉ xét một nghiệm tối ưu **có** giá trị cuối vượt ngưỡng. Muốn triển khai cần kiểm tra điều kiện đó, không đồng nhất mọi nghiệm tối ưu với một tiền triệu hợp lệ. [Cuối tr. 10–đầu tr. 11]

### 5.2. Vì sao phải ràng buộc theo thông tin tập hút?

Trong toàn không gian trạng thái có thể tồn tại các trạng thái tạo bùng phát rất mạnh nhưng hầu như không bao giờ được động lực học dài hạn ghé qua. Tối ưu không ràng buộc có thể tìm chính các trạng thái ngoại lệ này. Tác giả dùng thông tin thống kê để xấp xỉ miền trạng thái liên quan:

$$
\mathcal{A}=
\left\{u_0\in\mathcal{U}:
\underline{c}_i\leq C_i(u_0)\leq\overline{c}_i,
\quad i=1,\ldots,k\right\}.
$$

Nguồn: Phương trình (18), tr. 10. Các hàm C và cận dưới, cận trên phụ thuộc ứng dụng; k là số ràng buộc. 𝒜 là **xấp xỉ khả dĩ** cho tập hút hoặc lân cận của nó, không mặc nhiên bằng chính tập hút. Các ràng buộc thống kê bậc thấp cũng không tự bảo đảm mọi trạng thái thỏa chúng đều có xác suất xuất hiện đáng kể. [Mục 4.1; diễn giải của người phân tích]

Ví dụ được tác giả nêu là hệ FitzHugh–Nagumo có các quỹ đạo quá độ ở ngoài tập hút tạo giá trị trung bình lớn hơn 1,5, vượt những đỉnh điển hình ở Hình 7. Các quỹ đạo đó không được duy trì trong chế độ dài hạn; dùng chúng làm cơ chế đại diện có thể sai mục tiêu. [Tr. 10]

### 5.3. Tối ưu có ràng buộc phương trình động lực học

Viết tường minh, bài toán trở thành:

$$
\begin{aligned}
&\sup_{u_0\in\mathcal{U}}
\left[f\bigl(u(\tau)\bigr)-f(u_0)\right],\\
&\partial_t u=N(u),\qquad u(0)=u_0,\\
&\underline{c}_i\leq C_i(u_0)\leq\overline{c}_i,
\qquad i=1,\ldots,k.
\end{aligned}
$$

Nguồn: Phương trình (19a–c), tr. 10. Dòng thứ hai bảo đảm quỹ đạo tuân theo vật lý; dòng thứ ba gắn với khả năng xuất hiện của trạng thái. Đây là chỗ phương trình và dữ liệu đóng hai vai trò bổ sung: **phương trình xác định tăng trưởng, dữ liệu xác định miền tìm kiếm**.

Bài nêu điều kiện miền khả dĩ 𝒜 có tính compact — điều kiện tôpô dùng để bảo đảm đạt cực trị — và các ánh xạ đủ trơn để có nghiệm, nhưng nghiệm có thể không duy nhất và có nhiều cực đại địa phương. Cần đánh giá ý nghĩa của từng nghiệm sau tối ưu. PDF không cung cấp một thuật toán tối ưu thống nhất, các bước tính đạo hàm, khởi tạo đa điểm hoặc tiêu chí dừng cho toàn bộ các ứng dụng; tác giả dẫn tài liệu tối ưu có ràng buộc [141–144]. [Tr. 10]

Nếu nghiệm tìm được đi vào vùng vượt ngưỡng với một biên vượt dương và ánh xạ nghiệm liên tục, các trạng thái đủ gần cũng dẫn tới biến cố. Hình 10 minh họa lập luận liên tục này. Nó chưa cho kích thước vùng lân cận, xác suất quỹ đạo thực ghé vùng ấy, hoặc mức chịu nhiễu đo của chỉ báo suy ra. [Tr. 10–11; Hình 10]

### 5.4. Quy trình có thể tái dựng từ bài

1. Chọn mô hình, đại lượng quan sát, ngưỡng biến cố và thời gian tăng trưởng thích hợp.
2. Mô phỏng hoặc quan sát đủ lâu để mô tả chế độ dài hạn; loại giai đoạn quá độ nếu mục tiêu là biến cố trên tập hút.
3. Chọn các hàm ràng buộc và cận của chúng từ thông tin vật lý, thống kê.
4. Giải bài toán tăng trưởng có ràng buộc; kiểm tra hội tụ, các cực trị địa phương và điều kiện thực sự vượt ngưỡng.
5. Phân tích cấu trúc nghiệm tối ưu để đề xuất một cơ chế và đại lượng tiền triệu đơn giản.
6. Đánh giá chỉ báo bằng giá trị hiện tại và cực đại trong khoảng tương lai; không dùng tương quan đồng thời làm bằng chứng dự báo.
7. Kiểm tra độ tin cậy, thời gian báo trước và khả năng đo chỉ báo trong điều kiện ứng dụng.

Các bước 1–5 tổng hợp Mục 4; bước 6 dựa trên Mục 5.1–5.2. Các yêu cầu về hội tụ, kiểm tra ngoài dữ liệu đã dùng và khả năng đo là tiêu chí triển khai của người phân tích; PDF không báo cáo đầy đủ một thí nghiệm theo tất cả các bước kiểm tra này.

## 6. Ứng dụng thứ nhất: truyền năng lượng trong dòng Kolmogorov

### 6.1. Hệ và đại lượng cần dự báo

Bài dùng phương trình Navier–Stokes không nén được trong hai chiều:

$$
\partial_t\mathbf{u}
=-\mathbf{u}\cdot\nabla\mathbf{u}-\nabla p
+\nu\Delta\mathbf{u}+\mathbf{F},
\qquad \nabla\cdot\mathbf{u}=0.
$$

Nguồn: Phương trình (20), tr. 11. Miền là hình xuyến có hai chiều dài đều bằng 2π, tức điều kiện biên tuần hoàn. p là áp suất; ν là độ nhớt động học. Bản phân tích in đậm vận tốc để phân biệt trạng thái trường với các đại lượng vô hướng, không thay đổi mô hình của bài.

Ngoại lực Kolmogorov và số Reynolds được quy định:

$$
\mathbf{F}=\sin(k_f x_2)\mathbf{e}_1,\qquad
k_f=4,\qquad \mathrm{Re}=\nu^{-1}=40.
$$

Nguồn: Mục 4.2 và Hình 11–13, tr. 11–12. Các mô phỏng khởi tạo ngẫu nhiên, chạy qua quá độ rồi mới thu thập dữ liệu trên tập hút. PDF không nêu đủ độ dài loại quá độ, số quỹ đạo, lưới không gian và bước tích phân để tái lập nguyên các hình. [Mục 4.2]

Hai đại lượng quan sát là:

$$
\begin{aligned}
D(\mathbf{u})
&=\frac{\nu}{(2\pi)^{2}}
\int_{\mathbb{T}^{2}}|\nabla\mathbf{u}|^{2}\,d\mathbf{x},\\
I(\mathbf{u})
&=\frac{1}{(2\pi)^{2}}
\int_{\mathbb{T}^{2}}\mathbf{u}\cdot\mathbf{F}\,d\mathbf{x}.
\end{aligned}
$$

D là tốc độ tiêu tán năng lượng, I là tốc độ năng lượng được ngoại lực đưa vào hệ. Nguồn: Phương trình (21), tr. 11. Mục tiêu vật lý là dự báo đợt D tăng mạnh; I thuận tiện để phân tích vì tuyến tính theo vận tốc. Hình 11 cho D bùng phát và mật độ chung của I, D tập trung dọc một miền tương quan dương. Tương quan này là lý do tác giả tìm cơ chế chung, chưa tự là phép chứng minh nhân quả. [Hình 11; Mục 4.2]

### 6.2. Từ hai khả năng tăng năng lượng tới một bộ ba Fourier

Với quy ước khai triển Fourier (23), bài viết:

$$
I\bigl(\mathbf{u}(t)\bigr)
=-\operatorname{Im}a(0,k_f,t)
=-r(0,k_f,t)\sin\phi(0,k_f,t).
$$

a là hệ số Fourier phức; r và φ là môđun và pha của nó. Nguồn: phần sau Phương trình (23), tr. 11. Hai khả năng là pha làm trường vận tốc thẳng hàng hơn với ngoại lực, hoặc môđun của thành phần bị cưỡng bức tăng. Tác giả cho biết quan sát số bác khả năng thứ nhất và ủng hộ khả năng thứ hai, nhưng chi tiết kiểm tra pha được dẫn về [136], không trình bày đầy đủ trong PDF này.

Hình 12 cho nghiệm tối ưu tập trung vào ba thành phần Fourier chính, có các véc-tơ sóng:

$$
(1,k_f)=(1,0)+(0,k_f).
$$

Đây là quan hệ tương tác **bộ ba** được phân tích ở tr. 12. Các thành phần có véc-tơ đối dấu được liên hệ bởi điều kiện trường vận tốc thực, không được đếm thành những cơ chế độc lập mới. Ngoài các thành phần chính vẫn có tương tác với các bộ ba khác; sơ đồ Hình 12b dùng nét đứt để chỉ phần mạng chưa vẽ.

Hình 13 cho môđun ở véc-tơ sóng (1,0) giảm sâu gần lúc thành phần (0,4) tăng mạnh. Tác giả diễn giải đó là năng lượng chuyển từ thành phần số sóng nhỏ sang thành phần bị cưỡng bức. Phần phi tuyến và áp suất bảo toàn năng lượng tổng trong điều kiện đang xét, nhưng các thành phần riêng có thể trao đổi năng lượng. [Phương trình (24); Hình 12–13; tr. 12–13]

Đóng góp của các thành phần vào tiêu tán được viết:

$$
D(\mathbf{u})
=\nu\sum_{\mathbf{k}\in\mathbb{Z}^{2}}
|\mathbf{k}|^{2}|a(\mathbf{k})|^{2}.
$$

Nguồn: Phương trình (25), tr. 13. Với cùng lượng năng lượng chuyển sang thành phần số sóng lớn hơn, trọng số tiêu tán tăng: bài so sánh trọng số 1 của (1,0) với trọng số 16 của (0,4). Đây là cơ sở vật lý cho chuỗi giải thích: truyền năng lượng → thành phần bị cưỡng bức tăng → I và D tăng.

**Bằng chứng hỗ trợ:** nghiệm tối ưu, hai chuỗi môđun và quan hệ trọng số tiêu tán cùng ủng hộ một tương tác chủ đạo. **Chưa được chứng minh trong PDF:** chỉ ba thành phần này đủ thay thế mọi động lực học của hệ, hoặc tắt riêng tương tác đó làm mất toàn bộ biến cố. Không có thí nghiệm loại bỏ tương tác được trình bày để xác lập tính cần và đủ. Bài cũng nói phép tối ưu sử dụng ở [136] là “tương tự (19)” và bỏ qua chi tiết, nên chưa đủ cơ sở khẳng định mọi lựa chọn hàm mục tiêu, τ và ràng buộc của ứng dụng đều chính xác như công thức tổng quát. [Mục 4.2, tr. 12–13]

## 7. Ứng dụng thứ hai: sóng bất thường và dự báo bậc thấp

### 7.1. Vì sao chuyển từ mô hình mặt tự do sang phương trình bao sóng?

Trong mô hình sóng nước sâu, một chiều truyền sóng, dòng không xoáy, phương trình đầy đủ cần cả mặt nước lẫn thế vận tốc dưới mặt nước. Mặt nước có thể đo, còn đo đầy đủ trường thế vận tốc khó hơn. Bài dùng điều này để giải thích động cơ của phương trình bao sóng, thay vì giả định đã biết đầy đủ trạng thái thủy động lực học ngoài thực địa. [Hình 14; Phương trình (26)–(28); Mục 4.3, tr. 13]

Đến bậc xấp xỉ được xét, bao sóng phức u thỏa **phương trình Schrödinger phi tuyến** (*nonlinear Schrödinger equation*, NLS):

$$
\frac{\partial u}{\partial t}
+\frac{1}{2}\frac{\partial u}{\partial x}
+\frac{\mathrm{i}}{8}\frac{\partial^{2}u}{\partial x^{2}}
+\frac{\mathrm{i}}{2}|u|^{2}u=0.
$$

Nguồn: Phương trình (29), tr. 13. Ở đây u là **bao sóng phức**, khác trường vận tốc ở ứng dụng trước; số ảo được viết thẳng. Không gian và thời gian được chuẩn hóa bằng các đại lượng của sóng mang như bài giải thích ở tr. 14. Xấp xỉ cần các điều kiện, gồm độ dốc sóng nhỏ; một phương trình sửa đổi bậc cao hơn được ký hiệu MNLS và được dẫn về [169]. Không tự áp dụng NLS cho biển bất kỳ, sóng đa hướng hoặc độ dốc rất lớn. [Mục 4.3, tr. 13–14]

Bài nhắc quy ước thường dùng của sóng bất thường: độ cao sóng vượt hai lần độ cao sóng có nghĩa; độ cao sóng có nghĩa được mô tả bằng bốn lần độ lệch chuẩn cao độ mặt nước. Tuy nhiên, đại lượng dự báo về sau là **biên độ bao sóng cực đại theo không gian**. Cần xác nhận phép đổi chuẩn hóa và ngưỡng trước khi đồng nhất hai đại lượng; không lấy một ngưỡng độ cao đỉnh–đáy rồi tự dùng nguyên cho bao sóng. [Mục 4.3, tr. 13; Mục 5.2 và chú thích Hình 20, tr. 17–18]

### 7.2. Không phải mọi sóng bất thường đều là nghiệm Peregrine

Hình 15 minh họa các **nghiệm thở** (*breather solutions*), tức nghiệm có cấu trúc tập trung rồi biến đổi theo không gian và thời gian: Ma, Akhmediev và Peregrine. Peregrine tập trung theo cả hai chiều, nên có hình thái giống một đợt sóng bất thường sinh ra rồi tan đi. Bài dẫn các quan sát thực nghiệm từ công trình khác, nhưng nhấn mạnh nghiệm thở chính xác **không phải cơ chế duy nhất** tạo sóng bất thường trong trường sóng không đều. [Mục 4.3, tr. 14; Hình 15]

### 7.3. Phân rã nhóm sóng và kết hợp khả năng lớn lên với tần suất xuất hiện

Một trường bao sóng được xấp xỉ bằng các nhóm cục bộ:

$$
|u(x)|\simeq
\sum_{i=1}^{n}A_i\operatorname{sech}
\left(\frac{x-x_i}{L_i}\right).
$$

Nguồn: Phương trình (30), tr. 14. A là biên độ nhóm, L là độ dài đặc trưng, x có chỉ số i là vị trí tâm. Các tham số được chọn để giảm sai số xấp xỉ; PDF chưa nêu chuẩn sai số, cách chọn số nhóm hoặc thuật toán tối ưu phân rã. Hàm sech là nghịch đảo của cosh.

Sau khi phân rã nhiều hiện thực sóng ngẫu nhiên, tác giả dùng mật độ chung của A và L để biết những nhóm nào thường xuất hiện. Một phép khảo sát tiến hóa theo mô hình xác định miền các nhóm sẽ lớn thành sóng bất thường. Hình 16b chồng hai thông tin: mật độ xuất hiện và đường biên khả năng lớn lên. Nhóm thường gặp nhất không nhất thiết nguy hiểm; nhóm “nguy hiểm nhất” trong cách trình bày là nhóm **có khả năng xuất hiện cao trong miền sẽ phát triển thành biến cố**, không phải nhóm có biên độ ban đầu lớn nhất. [Hình 16; tr. 14–15]

Đường đen và đỏ nét đứt lần lượt là biên dựa trên NLS và MNLS. Đây là so sánh độ nhạy theo mô hình sóng trong minh họa, không phải một phép so sánh hiệu năng với tất cả các thuật toán cảnh báo sớm. [Chú thích Hình 16, tr. 14]

**Điểm cần tránh khi kể phương pháp:** nhóm sóng nguy hiểm ở Hình 16 được tìm trực tiếp bằng khảo sát và mật độ trên không gian tham số thấp chiều. Mục 4.3 nói có thể tìm chúng bằng tối ưu có ràng buộc, nhưng ở ví dụ này **không cần giải chính bài toán (17)** vì chi phí khảo sát không quá lớn. Không được viết như thể cả hai ứng dụng đều đã dùng cùng một bộ giải biến phân. [Đầu tr. 15]

Dự báo bậc thấp theo [188] dùng cấu trúc nhóm sóng hoặc phép chiếu vào miền độ dài–biên độ nguy hiểm để suy ra chỉ báo. Theo bài, bước dự báo này không cần tích phân lại NLS cho mỗi lần quan sát. Điều đó khác với việc không cần mô hình hoặc không cần mô phỏng trong giai đoạn khám phá và hiệu chuẩn. [Tr. 15, 17]

## 8. Từ tiền triệu đến xác suất biến cố trong tương lai

### 8.1. Xác định đúng mục tiêu dự báo

Bài chọn cực đại của đại lượng quan sát trong một khoảng tương lai:

$$
f_m(u;t_1,t_2)
=\max_{t_1\leq\tau\leq t_2}f\bigl(S^{\tau}(u)\bigr),
\qquad 0<t_1\leq t_2.
$$

Nguồn: Phương trình (31), tr. 15. u là trạng thái hiện tại; t có chỉ số 1 là thời gian chờ tối thiểu trước khoảng dự báo, t có chỉ số 2 là đầu cuối khoảng. Khi hai mốc bằng nhau, mục tiêu trở thành giá trị tại đúng một thời điểm tương lai, theo (32). Hình 17 minh họa g hiện tại tăng trước khi f tăng trong khoảng đã chọn.

Đây là một bài toán dự báo **biến cố có xuất hiện trong một khoảng hay không**, chưa phải ước lượng chính xác thời điểm, vị trí hoặc biên độ lớn nhất của từng biến cố. Khoảng dự báo và ngưỡng là thành phần của bài toán, không phải các thông số có thể thay đổi sau khi nhìn kết quả mà vẫn giữ nguyên diễn giải hiệu năng. [Mục 5; diễn giải của người phân tích]

### 8.2. Chỉ báo là đại lượng khác, được chọn để mang thông tin tiền triệu

g là hàm đo được của trạng thái. Trong chất lưu, nó dựa trên một thành phần Fourier; trong sóng, nó dựa trên phép chiếu bao sóng. Mục tiêu là g hiện tại liên hệ với cực đại **tương lai**, không chỉ đồng biến với biên độ hiện tại. Bài đánh giá mối liên hệ bằng thống kê có điều kiện, không bằng một hệ số tương quan duy nhất. [Mục 5.1–5.2]

Khi tồn tại các mật độ chung và mật độ biên thích hợp:

$$
p_{f_m\mid g}(a,b)=
\frac{p_{f_m,g}(a,b)}{p_g(b)},\qquad p_g(b)>0.
$$

Nguồn: Phương trình (33)–(35), tr. 15; bản phân tích viết rõ đối số. a và b là các giá trị khả dĩ của mục tiêu tương lai và chỉ báo. Đây là **mật độ** của mục tiêu khi biết chỉ báo, không phải xác suất một biến liên tục nhận đúng một giá trị. Việc ước lượng từ mẫu cần đủ dữ liệu tại những giá trị b đang xét; bài chưa nêu đầy đủ phương pháp chia ô hoặc làm trơn. [Mục 5.1]

Từ đó, xác suất sắp có biến cố là:

$$
P_{\mathrm{ee}}(g_0)=
\int_{f_e}^{\infty}p_{f_m\mid g}(a,g_0)\,da
=P\!\left(f_m>f_e\mid g=g_0\right).
$$

Nguồn: Định nghĩa 3, Phương trình (36)–(37), tr. 16. Ký hiệu xác suất P ở vế phải là cách viết gọn của điều kiện theo độ đo μ mà bài dùng. Chỉ số ee nhận diện xác suất biến cố cực đoan; sau đây gọi là **xác suất biến cố tương lai**. Xác suất này phụ thuộc ngầm vào đại lượng f, ngưỡng và khoảng thời gian đã chọn.

### 8.3. Bốn tình huống báo động

| Giá trị hiện tại của chỉ báo | Khoảng tương lai không có biến cố | Khoảng tương lai có biến cố |
| --- | --- | --- |
| Chưa vượt ngưỡng báo động | Không báo động đúng — miền I | Bỏ sót — miền III |
| Vượt ngưỡng báo động | Cảnh báo sai — miền IV | Phát hiện đúng — miền II |

Nguồn: Mục 5.1, tr. 16; Hình 18. Bài dùng g có chỉ số e làm ngưỡng báo động. Các trường hợp đúng bằng ngưỡng không được quy định chi tiết; nếu triển khai cần chọn quy ước nhất quán.

Một chỉ báo báo động liên tục có thể không bỏ sót nhưng gây nhiều cảnh báo sai; chỉ báo không bao giờ báo động có thể không gây cảnh báo sai nhưng bỏ sót mọi biến cố. Hình 18 là **sơ đồ minh họa**, không phải dữ liệu kiểm tra của một bộ dự báo đã huấn luyện. Đặc biệt, mức màu của một mật độ có điều kiện không tự cho tổng khối lượng xác suất trong một miền hai chiều nếu chưa đưa mật độ biên của chỉ báo vào. Điểm này liên quan trực tiếp tới vấn đề (38)–(39) ở Mục 10 dưới đây. [Mục 5.1, 5.3; diễn giải của người phân tích]

## 9. Những kết quả dự báo thực sự được báo cáo

### 9.1. Dòng Kolmogorov: một thành phần Fourier làm chỉ báo ngắn hạn

Chỉ báo được chọn là:

$$
g(\mathbf{u})=-|a(1,0)|,\qquad
f(\mathbf{u})=D(\mathbf{u}).
$$

Nguồn: Mục 5.2, tr. 17; Hình 19, tr. 18. Dấu âm làm giá trị g lớn hơn — tức ít âm hơn — tương ứng với môđun của thành phần (1,0) nhỏ đi. Đây là cách biến sự giảm năng lượng của thành phần tiền triệu thành quy tắc “g tăng thì nguy cơ tăng”.

Hình 19a cho mật độ có điều kiện và các đường ngưỡng; Hình 19b cho xác suất biến cố tương lai tăng rõ khi g lớn hơn. Bài mô tả vùng g nhỏ hơn khoảng −0,5 có xác suất gần 0; vùng lớn hơn khoảng −0,3 có xác suất gần 1; mốc xác suất 0,5 nằm gần **g = −0,39**. Đây là các mô tả theo ví dụ, không phải ngưỡng phổ quát cho dòng chảy khác. [Tr. 17–18]

**Lưu ý ký hiệu bản thảo:** đoạn tr. 17 dùng ngưỡng báo động ở một số chỗ đang mô tả miền giá trị của chỉ báo, gồm câu viết g có chỉ số e lớn hơn −0,3. Hình 19b và câu tiếp theo cho thấy mốc dùng làm ngưỡng ở xác suất 0,5 là khoảng −0,39. Bản phân tích tách ba miền giá trị g với ngưỡng được chọn, thay vì biến −0,5 và −0,3 thành hai ngưỡng báo động đồng thời.

Mục 5.3, tr. 18, nêu **khoảng tương lai từ 1 tới 2 đơn vị thời gian** cho Hình 19. Hình 19c minh họa một lần xác suất báo động tăng trước đợt D tăng mạnh. Tr. 19 cho biết khi tăng thời gian chờ lên quá 4 đơn vị, chỉ báo mất năng lực dự báo trong trường hợp này. Tuy nhiên, PDF không trình bày đầy đủ một đường hiệu năng theo thời gian chờ hoặc khoảng bất định để định lượng phát biểu đó. Không gán các đơn vị mô phỏng này thành giây, chu kỳ sóng hoặc thời gian của hệ y sinh. [Mục 5.2–5.3]

**Bằng chứng hỗ trợ:** ví dụ thể hiện một chỉ báo có liên hệ tiền triệu và một phép hiệu chuẩn xác suất ngắn hạn. **Chưa được chứng minh:** một ngưỡng 0,5 có chi phí quyết định tối ưu, hoặc đây là tỷ lệ phát hiện trên một tập quỹ đạo kiểm tra được tách độc lập. Bài không cung cấp rõ thiết kế chia dữ liệu hiệu chuẩn và kiểm tra. [Hình 19; Mục 5.2]

### 9.2. Sóng bất thường: có cảnh báo trước nhưng vẫn còn xác suất bỏ sót

Mục tiêu của ví dụ sóng là:

$$
f(u)=\max_x|u(x,t)|.
$$

Nguồn: Mục 5.2 và Hình 20, tr. 17–18. Đây là cực đại biên độ bao sóng trên miền tại thời điểm đang xét; mục tiêu dự báo sau đó lại lấy cực đại theo thời gian tương lai bằng (31). Không nhầm hai phép cực đại này thành một cảm biến đo tại một điểm.

Chỉ báo g được mô tả bằng phép chiếu bao sóng lên không gian con bắt được miền độ dài–biên độ nguy hiểm. PDF dẫn [188] cho công thức chi tiết; không đủ thông tin để viết một phép chiếu cụ thể rồi gán là thuật toán hoàn chỉnh của bài này. [Mục 5.2, tr. 17]

Hình 20 cho một cấu trúc có điều kiện khác với chất lưu: tại những giá trị g nhỏ hơn 0,1 vẫn còn xác suất biến cố vào khoảng **0,05–0,2** theo phần văn bản. Điều đó cho thấy chỉ báo nhỏ không loại trừ hoàn toàn biến cố tương lai. Bài báo cáo các dự báo bỏ sót chiếm **5,9% số dự báo**, và dẫn [188] cho thời gian cảnh báo trung bình **25 chu kỳ sóng**. [Tr. 17; Hình 20]

**Giới hạn số liệu:** PDF không định nghĩa đủ mẫu số của con số 5,9%, số mẫu, cách gộp các thời điểm thành một biến cố hoặc mức bao phủ thống kê. Không tự đổi nó thành “độ nhạy 94,1%” hay “bỏ sót 5,9% tất cả biến cố thực”. Tương tự, 25 chu kỳ là kết quả được tổng quan dẫn từ một công trình khác, chưa được bản phân tích kiểm tra ở nguồn gốc hoặc tái lập. Nó không phải một bảo đảm cho biển bất kỳ. [Mục 5.2]

Tác giả liên hệ thời gian dự báo dài hơn của sóng với tính khả tích của NLS và kỳ vọng thời gian dự báo giảm khi số mũ Lyapunov lớn nhất tăng. PDF không trình bày một phép đo và khớp quy luật định lượng cho quan hệ Lyapunov này; nên coi đây là diễn giải cơ chế và kỳ vọng, không phải một định luật thực nghiệm được xác lập trong bài. [Cuối Mục 5.2, tr. 17]

## 10. Đề cương tìm chỉ báo từ dữ liệu và vấn đề của hàm sai số

### 10.1. Tác giả mới đặt mục tiêu, chưa giải bài toán học chỉ báo

Mục 5.3 hỏi liệu có thể tự tìm một hàm chỉ báo tốt từ dữ liệu thay cho phân tích phương trình hay không. Tác giả đề nghị tối thiểu hóa sai số khi lựa chọn đồng thời hàm g, ngưỡng báo động và hai mốc thời gian. Họ nói rõ sự phụ thuộc phi tuyến, không trơn làm bài toán khó; việc giải sẽ được trình bày ở nơi khác. Do đó, không được gọi (38)–(39) là một phương pháp học đã có bộ giải, huấn luyện hoặc kết quả thử nghiệm trong PDF. [Tr. 17–19]

Phát biểu rằng chưa có một khung hệ thống tìm chỉ báo hoàn toàn từ dữ liệu là **đánh giá của tác giả tại thời điểm bản thảo**, không phải kết luận cập nhật về tình trạng tài liệu hiện nay. Bản phân tích không dùng web hoặc tổng quan thêm để xác lập một khoảng trống hiện hành.

### 10.2. Định nghĩa (38) không phải cặp tỷ lệ sai thông thường

Để đọc rõ cách lấy điều kiện, bản phân tích đặt hai ký hiệu phụ:

$$
E=\{f_m>f_e\},\qquad A=\{g>g_e\}.
$$

E là biến cố tương lai, A là báo động; đây là ký hiệu của người phân tích, không phải ký hiệu mới của tác giả. Trong các công thức dưới, bỏ qua trường hợp đúng bằng ngưỡng hoặc giả sử nó có xác suất 0.

Phương trình (38), tr. 18, tương đương với:

$$
\mathcal{L}(g;g_e,t_1,t_2)
=P(E\mid A^{c})+P(E^{c}\mid A).
$$

Hạng đầu là xác suất có biến cố **trong nhóm không báo động**; hạng sau là xác suất không có biến cố **trong nhóm có báo động**. Tác giả gọi chúng là hai loại dự báo sai. Chúng khác với các tỷ lệ điều kiện theo trạng thái thật thường dùng khi đánh giá bộ phát hiện:

$$
\begin{aligned}
\mathrm{FNR}&=P(A^{c}\mid E),\\
\mathrm{FPR}&=P(A\mid E^{c}).
\end{aligned}
$$

Trong bản phân tích, FNR được giải thích là **tỷ lệ bỏ sót trong các trường hợp có biến cố** (*false negative rate*), FPR là **tỷ lệ cảnh báo sai trong các trường hợp không có biến cố** (*false positive rate*). Đây là đối chiếu định nghĩa của người phân tích, không phải đổi lại cách tác giả đã định nghĩa (38).

Vì mỗi hạng của (38) có thể nằm giữa 0 và 1, tổng có thể tới 2; câu ngay sau đó ghi miền giá trị chỉ từ 0 tới 1 chưa được bảo đảm bởi định nghĩa. Hơn nữa, nếu chỉ báo luôn hoặc không bao giờ báo động thì một điều kiện có xác suất 0, cần một quy ước xử lý; PDF không nêu quy ước này. [Đối chiếu trực quan tr. 18; diễn giải toán học của người phân tích]

### 10.3. Tích phân (39) chưa suy ra được từ (35) và (38)

Bản in tiếp tục viết:

$$
\begin{aligned}
\mathcal{L}(g;g_e,t_1,t_2)
={}&\int_{f_e}^{\infty}\int_{-\infty}^{g_e}
p_{f_m\mid g}(a,b)\,db\,da\\
&+\int_{-\infty}^{f_e}\int_{g_e}^{\infty}
p_{f_m\mid g}(a,b)\,db\,da.
\end{aligned}
$$

Nguồn: Phương trình (39), tr. 18, đã đối chiếu trực tiếp PDF. Mật độ dưới dấu tích phân đúng là **mật độ có điều kiện**, không phải mật độ chung bị lỗi trích xuất chữ.

**Kiểm tra của người phân tích:** mật độ có điều kiện được chuẩn hóa theo giá trị a ở mỗi b, không được chuẩn hóa chung theo cả a và b. Muốn tính một xác suất gộp theo nhiều giá trị chỉ báo, phải đưa phân bố của b vào. Nếu giữ nguyên ý nghĩa của (38), biểu thức nhất quán phải có các trọng số và mẫu số điều kiện tương ứng:

$$
\begin{aligned}
\mathcal{L}_{38}
={}&\frac{\displaystyle
\int_{f_e}^{\infty}\int_{-\infty}^{g_e}
p_{f_m\mid g}(a,b)p_g(b)\,db\,da}
{P(A^{c})}\\
&+\frac{\displaystyle
\int_{-\infty}^{f_e}\int_{g_e}^{\infty}
p_{f_m\mid g}(a,b)p_g(b)\,db\,da}
{P(A)}.
\end{aligned}
$$

Đây là **phép viết lại của người phân tích**, chỉ dùng khi hai mẫu số dương; không phải công thức đã được tác giả trình bày. Nếu mục tiêu là xác suất dự báo sai trên toàn bộ quan sát, một lựa chọn khác là tổng hai xác suất giao của dự báo sai với tình trạng thật, không phải tổng hai xác suất có điều kiện trong (38). Các mục tiêu này có cách cân nhắc tần suất biến cố khác nhau và không nên trộn lẫn.

Hệ quả thực hành là không thể đưa nguyên (39) vào một thuật toán rồi tuyên bố đã tối ưu đúng “tỷ lệ sai” của (38). Cần xác định rõ mẫu số, trọng số và chi phí hai loại sai trước. **Bất nhất này không tự phủ định định nghĩa xác suất biến cố ở (36), cơ chế truyền năng lượng hoặc tất cả các hình dự báo**; nhưng nó là rào cản trực tiếp khi muốn tái lập đề cương tối ưu chỉ báo của Mục 5.3.

## 11. Bản đồ hình và mức bằng chứng

PDF có Hình 1–20, không có bảng kết quả tổng hợp tương đương một bộ đánh giá chuẩn. Các nhóm hình sau trả lời những câu hỏi khác nhau.

| Hình, trang | Vai trò và điều được thể hiện | Điều không được chứng minh |
| --- | --- | --- |
| **Hình 1, tr. 1** | Sơ đồ quan hệ cơ chế–thống kê–dự báo–giảm thiểu | Không phải thí nghiệm chứng minh biết cơ chế tất yếu kiểm soát được biến cố |
| **Hình 2–3, tr. 4** | Phân biệt đi vào tập vượt ngưỡng với chuyển giữa hai vùng tồn tại lâu | Không xác lập mọi chuyển tiếp hiếm đều là cực đoan theo biên độ |
| **Hình 4–5, tr. 5** | Hình học hút–đẩy của đa tạp chậm và dòng nhanh quanh đa tạp tới hạn | Không phải hiệu năng dự báo; không áp dụng không điều kiện cho hệ không tách thang thời gian |
| **Hình 6, tr. 6** | Quỹ đạo tuần hoàn ổn định có các đoạn dao động nhỏ và bùng phát | Không chứng minh biến cố hiếm hoặc bùng phát hỗn loạn ở chính cấu hình này |
| **Hình 7, tr. 7** | Hai phần tử FitzHugh–Nagumo cho đỉnh lớn không lặp theo chu kỳ đều | Chưa đánh giá dự báo cơn động kinh hoặc bất kỳ dữ liệu lâm sàng nào |
| **Hình 8, tr. 7** | Sơ đồ đồng liên và dị liên để giải thích bùng phát hình học | Không phải phép xác định các quỹ đạo này từ một chuỗi không biết mô hình |
| **Hình 9, tr. 8** | Thế, hàm xác suất đến miền đích, mật độ và dòng chuyển tiếp; hình tái bản từ [127] | Không chứng minh tính toán hiệu quả ở không gian trạng thái rất cao chiều |
| **Hình 10, tr. 10** | Lập luận các trạng thái gần nghiệm tối ưu cũng có thể vượt ngưỡng nhờ tính liên tục | Không cho xác suất gặp tiền triệu hoặc bán kính chịu nhiễu quan sát |
| **Hình 11, tr. 12** | D tăng gián đoạn; I và D có thống kê chung tương quan rõ | Tương quan đồng thời chưa đủ chứng minh hướng nhân quả hoặc năng lực báo trước |
| **Hình 12–13, tr. 12** | Nghiệm tối ưu tập trung vào bộ ba; môđun hai thành phần có biến đổi liên quan | Không phải loại bỏ từng tương tác để chứng minh bộ ba là cơ chế duy nhất |
| **Hình 14–15, tr. 13–14** | Thiết lập sóng mặt tự do và các nghiệm NLS có hình thái tập trung | Không xác nhận mọi sóng bất thường ngoài biển là nghiệm Peregrine |
| **Hình 16, tr. 14** | Phân rã nhóm sóng, mật độ A–L và biên phát triển theo NLS/MNLS | Không phải bằng chứng đã dùng bộ giải (19), hoặc đã có hiệu năng trên dữ liệu biển độc lập |
| **Hình 17–18, tr. 15–16** | Định nghĩa khoảng tương lai và bốn tình huống dự báo | Là sơ đồ khái niệm, không phải số liệu huấn luyện/kiểm tra |
| **Hình 19, tr. 18** | Chỉ báo Fourier, xác suất biến cố và một ví dụ cảnh báo trước cho dòng Kolmogorov | Không có bảng tỷ lệ sai theo sự kiện, khoảng bất định hoặc phân tách kiểm tra độc lập được mô tả rõ |
| **Hình 20, tr. 18** | Chỉ báo sóng có thông tin dự báo, nhưng g nhỏ vẫn còn nguy cơ biến cố | Không suy ra độ nhạy 94,1% chỉ từ câu nói 5,9% số dự báo là bỏ sót |

Những giới hạn suy luận trong cột phải là diễn giải của người phân tích. Các hình hỗ trợ những mảnh khác nhau của câu chuyện; không cộng các sơ đồ, nghiệm giải tích và ví dụ mô phỏng thành một bằng chứng dự báo ngoài mẫu duy nhất.

## 12. Thiết kế kiểm chứng, độ bất định và khả năng tái lập

### 12.1. Những điều có thể xác nhận từ PDF

- Hệ nhanh–chậm và hai phần tử FitzHugh–Nagumo có phương trình, các bộ tham số và đại lượng quan sát cụ thể; các hình minh họa lần lượt bùng phát tuần hoàn và không tuần hoàn. [Mục 3.1; Hình 5–7]
- Dòng Kolmogorov có phương trình, miền tuần hoàn, dạng cưỡng bức, số sóng cưỡng bức 4 và Reynolds 40. Có mô tả bỏ quá độ và lấy thống kê từ các mô phỏng dài trên nhiều quỹ đạo. [Mục 4.2, tr. 11–12]
- Dự báo chất lưu dùng khoảng tương lai 1–2 đơn vị thời gian và một chỉ báo Fourier cụ thể. [Mục 5.2–5.3; Hình 19]
- Ví dụ sóng dựa trên mô hình bao sóng và các công trình bậc thấp trước đó; có so sánh biên phát triển theo NLS và MNLS, nhưng chi tiết phép chiếu chỉ báo được dẫn ra ngoài. [Mục 4.3, 5.2]

### 12.2. Những thông tin PDF không báo cáo đủ

| Hạng mục | Thông tin còn thiếu và hệ quả |
| --- | --- |
| Dữ liệu và lấy mẫu | Không có đầy đủ số mẫu, khoảng lấy mẫu, số hiện thực, phân bố khởi tạo và độ dài loại quá độ cho các hình chính |
| Tích phân số | Chưa đủ lưới không gian, số thành phần Fourier, bước thời gian, xử lý sai số và kiểm tra hội tụ |
| Bài toán tối ưu chất lưu | Chưa đủ các hàm ràng buộc, cận, thời gian tối ưu, hàm mục tiêu ứng dụng cụ thể, đạo hàm, khởi tạo và điều kiện dừng |
| Hiệu chuẩn xác suất | Chưa đủ cách ước lượng mật độ chung/biên, chia ô hoặc băng thông, số mẫu trong các miền g hiếm |
| Huấn luyện và kiểm tra | Không mô tả rõ tập hiệu chuẩn, tập kiểm tra độc lập, hoặc cách tránh chồng lấn các cửa sổ tương lai |
| Đối chiếu | Không có đánh giá chuẩn với nhiều bộ dự báo đối chiếu, mô hình không hoặc tín hiệu thay thế trên cùng tập kiểm tra |
| Loại bỏ thành phần | Không báo cáo một chuỗi thử nghiệm loại bỏ ràng buộc tập hút, bộ ba hoặc từng thành phần chỉ báo để lượng hóa vai trò riêng |
| Độ bất định | Không có khoảng tin cậy hoặc khoảng sai số định lượng cho các đường xác suất, tỷ lệ 5,9% hay thời gian trung bình 25 chu kỳ trong bản tổng quan |
| Khả năng đo | Chưa kiểm chứng ảnh hưởng của nhiễu cảm biến, độ phân giải thiếu và số lượng điểm đo tới chỉ báo Fourier hoặc phép chiếu sóng |

Các nhận xét này nói về **mức thông tin có trong PDF được giao**. Chúng không xác nhận các công trình gốc [136], [188], [189] cũng thiếu những kiểm tra ấy. Những hình màu hoặc độ rộng một vùng mật độ không được gọi là khoảng tin cậy khi bài chưa định nghĩa như vậy.

### 12.3. Mức kiểm chứng dự báo cần gọi đúng tên

Bài có các hàm mục tiêu tương lai, thống kê có điều kiện và minh họa báo trước một biến cố trong mô phỏng; vì vậy không nên hạ toàn bộ nội dung xuống chỉ còn tương quan đồng thời. Tuy nhiên, **dự báo theo thời gian được minh họa trên mô phỏng** vẫn khác một nghiên cứu theo dõi tiến cứu có ngưỡng khóa trước và kiểm tra trên dữ liệu quan sát mới. Bản tổng quan chưa cung cấp thiết kế tách dữ liệu đủ rõ để xác nhận mức sau. [Mục 5.1–5.2]

Tương tự, đây không phải phương pháp ước lượng điểm tới hạn của một tham số điều khiển. Reynolds 40, số sóng 4 hay tham số của hai bộ dao động là những điều kiện của ví dụ, không phải ngưỡng được thuật toán suy ra từ một chuỗi. Nhiều biến cố được nghiên cứu xuất hiện lặp lại trong cùng một hệ tự trị với tham số cố định. [Mục 3.1; Mục 4.2; Mục 6]

## 13. Thảo luận: đóng góp thực sự và điều kiện có thể thất bại

### 13.1. Giá trị phương pháp luận

Thứ nhất, bài nối hai việc thường bị tách rời: **giải thích vì sao biến cố xảy ra** và **chọn một đại lượng đủ đơn giản để báo trước nó**. Chỉ cần biết một phần cơ chế cũng có thể hữu ích: một thành phần Fourier hoặc một miền độ dài–biên độ của nhóm sóng có thể mang thông tin dự báo, dù không thay thế toàn bộ mô hình. [Mục 4.2–5.2]

Thứ hai, phương pháp biến phân tránh tìm trạng thái kích thích mạnh nhưng xa điều kiện hệ thực thường ghé qua. Việc ghép ràng buộc thống kê với phương trình vật lý là điểm phương pháp đáng kế thừa. Nhưng chất lượng kết quả phụ thuộc mạnh vào cách xấp xỉ miền khả dĩ, và phần này không được biến thành một lựa chọn tự động phổ quát. [Mục 4.1; Phương trình (18)–(19)]

Thứ ba, định nghĩa mục tiêu bằng một khoảng tương lai và tính xác suất có điều kiện tạo ngôn ngữ rõ để đánh giá chỉ báo. Một đường xác suất tăng mạnh có giá trị hơn nhận xét mơ hồ “có tiền triệu”, nhưng vẫn phải được hiệu chuẩn bằng mẫu đủ lớn và xác nhận ở điều kiện khác. Hàm sai số được đề xuất sau đó có bất nhất riêng, cần giải quyết trước khi dùng để học chỉ báo. [Mục 5.1–5.3]

### 13.2. Khi nào cách tiếp cận có thể thất bại?

- **Sai hoặc thiếu mô hình:** tối ưu có thể tìm một đường tăng trưởng mạnh của mô hình nhưng không tồn tại trong hệ thật. Có phương trình xấp xỉ không tự bảo đảm đúng thống kê cực đoan.
- **Ràng buộc quá rộng hoặc quá hẹp:** miền tìm kiếm có thể chứa trạng thái phi thực tế, hoặc loại bỏ chính các tiền triệu hiếm cần tìm.
- **Nhiều cơ chế cùng sinh biến cố:** một chỉ báo gắn với một bộ ba hoặc một nhóm sóng có thể bỏ sót các tuyến tạo biến cố khác. Hình 20 đã cho thấy nguy cơ còn lại khi chỉ báo nhỏ.
- **Cực trị địa phương và thời gian tối ưu không thích hợp:** nghiệm tìm được có thể không đại diện, không vượt ngưỡng, hoặc chỉ mạnh tại một mốc thời gian hẹp.
- **Quan sát thiếu:** chỉ báo được phát hiện từ trạng thái mô phỏng đầy đủ có thể không đo được bằng thiết bị thực tế.
- **Dự báo quá xa hoặc phân bố thay đổi:** hỗn loạn làm mất liên hệ tiền triệu; hiệu chuẩn trên độ đo bất biến cũ có thể mất tác dụng khi điều kiện nền đổi.

Đây là tổng hợp và suy luận của người phân tích từ Mục 4.1, 5.2–6; không phải danh sách các thí nghiệm thất bại mà tác giả đã chạy.

### 13.3. Giới hạn khái quát theo chính tác giả

Mục 6 giới hạn thảo luận vào **hệ tự trị**, có quy luật tiến hóa cố định, và không tuyên bố áp dụng trực tiếp cho những hệ có quy luật thay đổi theo thời gian. Tác giả nêu tài chính và mạng xã hội như các ví dụ có thể nằm ngoài phạm vi đang xét. Đây là ranh giới của khung trong bài, không phải kết luận rằng mọi mô hình tài chính hoặc xã hội đều không thể nghiên cứu bằng hệ động lực. [Tr. 19]

Các phát biểu về hướng nghiên cứu còn thiếu trong Mục 6 phải được ghi nhận theo thời điểm bản thảo. Không chuyển một đánh giá năm 2018 thành một tuyên bố rằng hiện nay vẫn chưa có công trình liên quan nếu chưa đọc thêm tài liệu.

## 14. Liên hệ chuỗi thời gian y sinh: kế thừa câu hỏi, chưa kế thừa cơ chế

Bài có mô hình FitzHugh–Nagumo, dẫn các cơ chế phát xung thần kinh và nhắc cơn động kinh trong phần kết luận. Tuy nhiên, **không có dữ liệu điện não đồ, điện tâm đồ hoặc tín hiệu quang thể tích được kiểm tra trong PDF**. Một mô hình kích thích trừu tượng không tương đương với một phép xác thực dự báo lâm sàng. [Mục 3.1–3.2; Mục 6]

**Diễn giải và đề xuất của người phân tích, chưa thực hiện:** với **điện não đồ** (*electroencephalography*, EEG), **điện tâm đồ** (*electrocardiography*, ECG) hoặc **tín hiệu quang thể tích** (*photoplethysmography*, PPG), điểm chuyển giao rõ nhất là cách đặt mục tiêu và đánh giá chỉ báo:

1. Định nghĩa biến cố có ý nghĩa sinh lý, một khoảng báo trước và một khoảng thời gian dự báo rõ ràng; không dùng duy nhất “biên độ lớn” cho mọi loại bệnh lý.
2. Xác định biến trạng thái và đại lượng thực sự đo được. Không mặc định một kênh tín hiệu cho đủ thông tin để tính chỉ báo được khám phá từ toàn trường trạng thái.
3. Nếu có mô hình cơ chế, dùng nó để tìm trạng thái tiền triệu dưới các ràng buộc sinh lý thích hợp; nếu chưa có mô hình, xem việc học chỉ báo là một bài toán riêng cần kiểm chứng.
4. Ước lượng xác suất biến cố từ dữ liệu quá khứ và kiểm tra trên người hoặc lần ghi độc lập; tách rõ bỏ sót theo biến cố, cảnh báo sai theo thời gian và tỷ lệ báo động sai trong các báo động.
5. Kiểm tra ảnh hưởng của nhiễu, can thiệp, nhịp nền và thay đổi theo thời gian tới xác suất đã hiệu chuẩn.

Không mặc định mọi biến cố y sinh có đa tạp chậm, phân nhánh, chậm dần tới hạn hoặc cơ chế truyền năng lượng kiểu bộ ba Fourier. Đây là những giả thuyết cơ chế phải đánh giá theo hiện tượng, **không phải khoảng trống nghiên cứu y sinh đã xác lập bằng bài tổng quan này**.

## 15. Hồ sơ phương pháp

**Hồ sơ phương pháp (Methodological Fingerprint)** cần phản ánh đây là một tổng quan nhiều nhánh, với trọng tâm là tìm cơ chế và hiệu chuẩn dự báo.

| Trường | Nội dung |
| --- | --- |
| **Bài toán (Problem)** | Giải thích cơ chế sinh biến cố cực đoan và tìm chỉ báo báo trước trong hệ động lực, đặc biệt hệ hỗn loạn nhiều chiều |
| **Đầu vào (Input)** | Phương trình và điều kiện biên khi tìm cơ chế; dữ liệu dài hạn hoặc thống kê tập hút; trường trạng thái/nhóm sóng để tính chỉ báo; các cặp chỉ báo hiện tại–cực đại tương lai để hiệu chuẩn |
| **Thông tin biết trước (Known information)** | Đại lượng đích, ngưỡng cực đoan, khoảng thời gian; mô hình vật lý và tham số trong các ứng dụng; dạng ràng buộc khả dĩ; không giả định chỉ có một chuỗi vô hướng bất kỳ |
| **Đầu ra (Output)** | Trạng thái tiền triệu tối ưu, tương tác chủ đạo, chỉ báo g, mật độ có điều kiện và xác suất biến cố tương lai; chưa phải ước lượng một điểm tới hạn điều khiển |
| **Phương án đối chiếu (Existing baseline)** | Các cơ chế hình học và đường chuyển tiếp được tổng hợp; hai khả năng tăng năng lượng; NLS/MNLS cho biên phát triển sóng. Không có bộ đánh giá chung với nhiều thuật toán dự báo độc lập |
| **Thành phần mới (New component)** | Đóng góp của bản tổng quan là tổ chức cơ chế–biến phân–chỉ báo–xác suất trong một câu chuyện phương pháp; biến phân đã có ở [136]; tối ưu chỉ báo từ dữ liệu mới được phác thảo |
| **Giả định (Assumptions)** | Mô hình mô tả đúng động lực liên quan; miền ràng buộc xấp xỉ hợp lý điều kiện trên tập hút; chỉ báo đo được; thống kê dùng để hiệu chuẩn còn phù hợp; mỗi nhánh có thêm điều kiện riêng |
| **Kiểm chứng (Validation)** | Ví dụ nhanh–chậm, hai phần tử kích thích, hình đường chuyển tiếp tái bản, mô phỏng dòng Kolmogorov, mô hình sóng và kết quả dẫn từ các công trình trước; không có thử nghiệm y sinh |
| **Kết quả chính (Main finding)** | Bộ ba Fourier gợi ra chỉ báo chất lưu; xác suất báo động 0,5 tương ứng g gần −0,39 trong ví dụ; ví dụ sóng vẫn có nguy cơ khi g nhỏ, dẫn con số bỏ sót 5,9% số dự báo và báo trước trung bình 25 chu kỳ với giới hạn mẫu số/phạm vi |
| **Câu hỏi còn mở (Unresolved questions)** | Cách chọn ràng buộc và tìm chỉ báo tự động; chuẩn hóa nhất quán (38)–(39); khả năng quan sát, độ bền với nhiễu/sai mô hình, hiệu năng ngoài mẫu và khi điều kiện nền đổi |
| **Khả năng tái lập (Reproduction feasibility)** | Có thể bắt đầu từ các hệ phương trình ít chiều có tham số; chưa đủ chi tiết trong PDF để tái lập chính xác tối ưu chất lưu và chỉ báo sóng. Chưa tải mã, chưa chạy tái lập |

Nguồn tổng hợp: Mục 2–6, tr. 3–19; Hình 1–20. Các giới hạn kiểm chứng và yêu cầu mở rộng là diễn giải của người phân tích.

## 16. Tài liệu đọc tiếp và quyết định tái lập

### 16.1. Những phần cần kiểm tra đầu tiên

**Để kế thừa phương pháp dự báo:** trước tiên phải tách ba đại lượng khác nhau: xác suất biến cố khi không báo động; tỷ lệ bỏ sót trên tất cả các biến cố thật; tỷ lệ dự báo sai trên toàn bộ quan sát. Sau đó đối chiếu (38)–(39) và xác nhận mẫu số của 5,9%. Không nên chọn một hàm mất mát từ tên gọi “tỷ lệ sai” khi công thức điều kiện chưa rõ.

**Để tái lập cơ chế chất lưu:** cần mở công trình [136] và phần hỗ trợ nếu có để xác nhận chính xác hàm mục tiêu, ràng buộc, bộ giải, độ phân giải và cách xây dựng thống kê. Với sóng, cần [188] để xác nhận phép chiếu, ngưỡng, miền mô phỏng, phân bố trường sóng và cách tính thời gian báo trước. PDF hiện tại **không cung cấp một kho mã hoặc dữ liệu gắn với toàn bộ quy trình**; điều này không có nghĩa các nguồn gốc không cung cấp ở nơi khác.

### 16.2. Các tài liệu được chính PDF chỉ ra

| Nguồn trong danh mục | Tên gốc kèm nghĩa tiếng Việt | Mục đích đọc tiếp |
| --- | --- | --- |
| **[136] Farazmand và Sapsis (2017)** | *A variational approach to probing extreme events in turbulent dynamical systems* — “Một cách tiếp cận biến phân để thăm dò biến cố cực đoan trong hệ động lực rối”; *Science Advances* 3(9), e1701533 | Nguồn gốc phương pháp biến phân và chi tiết tái lập dòng Kolmogorov |
| **[188] Cousins và Sapsis (2016)** | *Reduced-order precursors of rare events in unidirectional nonlinear water waves* — “Tiền triệu bậc thấp của biến cố hiếm trong sóng nước phi tuyến một chiều truyền”; *Journal of Fluid Mechanics* 790, 368–388 theo thông tin bài dẫn | Phép chiếu chỉ báo sóng, số liệu bỏ sót và thời gian cảnh báo |
| **[189] Farazmand và Sapsis (2017)** | *Reduced-order prediction of rogue waves in two-dimensional deep-water waves* — “Dự báo bậc thấp sóng bất thường trong sóng nước sâu hai chiều”; *Journal of Computational Physics* 340, 418–434 | Phạm vi mở rộng so với cấu hình một chiều |
| **[80] Ansmann và cộng sự (2013)** | *Extreme events in excitable systems and mechanisms of their generation* — “Biến cố cực đoan trong hệ kích thích và cơ chế hình thành”; *Physical Review E* 88, 052911 | Nguồn ví dụ FitzHugh–Nagumo và cơ chế kích thích |
| **[67]/[127] E và Vanden-Eijnden (2010)** | *Transition-path theory and path-finding algorithms for the study of rare events* — “Lý thuyết đường chuyển tiếp và thuật toán tìm đường để nghiên cứu biến cố hiếm” | Nguồn tổng quan đường chuyển tiếp và Hình 9; hai mục trong danh mục chỉ cùng một tên công trình |
| **[141] Hinze và cộng sự (2008)** | *Optimization with PDE constraints* — “Tối ưu với ràng buộc phương trình vi phân riêng phần” | Thuật toán và điều kiện của tối ưu có ràng buộc động lực học |
| **[191] Dematteis và cộng sự (2018)** | *Rogue waves and large deviations in deep sea* — “Sóng bất thường và độ lệch lớn ở biển sâu”; *Proceedings of the National Academy of Sciences* 115(5), 855–860 | Liên hệ tối ưu, xác suất trạng thái ban đầu và biến cố sóng |

Tên và thông tin được ghi theo danh mục tr. 21–25. **Chưa đọc các tài liệu này** trong bước hiện tại; không dùng chúng như nguồn xác nhận độc lập cho nội dung phân tích.

### 16.3. Quyết định sử dụng

**Mức chọn: phương pháp nền tảng (Core methodology).** Bài phù hợp để xây dựng tư duy **từ cơ chế tới chỉ báo, rồi tới xác suất biến cố trong một khoảng tương lai**. Các phần có thể kế thừa làm nền là cách định nghĩa bài toán, tối ưu tăng trưởng dưới ràng buộc vật lý–thống kê và xác suất có điều kiện (36). Không dùng nguyên hàm sai số (38)–(39) như một công thức triển khai đã nhất quán.

Không chọn toàn bộ bản tổng quan làm một mục tiêu tái lập duy nhất vì nó gom nhiều phương pháp, nhiều nguồn bằng chứng và để thiếu các chi tiết triển khai chính. Nếu chuyển sang tái lập, nên chọn **một bài toán con**: trước hết kiểm tra mô phỏng hai phần tử FitzHugh–Nagumo theo (8) và Hình 7 để xác nhận hiểu đúng cơ chế; hoặc, nếu mục tiêu là phương pháp biến phân, đọc [136] rồi tái lập riêng chuỗi tìm bộ ba–chỉ báo–xác suất ở dòng Kolmogorov. Đây là kế hoạch của người phân tích, **chưa được thực hiện**.

Một mở rộng có thể nghiên cứu sau đó là đo hiệu năng khi chỉ báo phải tính từ quan sát thiếu và điều kiện nền thay đổi, so với tình huống toàn trạng thái trong mô phỏng. Đây là hướng kiểm chứng được gợi ra bởi giới hạn bài, không phải khoảng trống tài liệu đã được xác lập chỉ từ một PDF năm 2018.

## 17. Ghi nhận kiểm tra tài liệu

Nội dung được viết bằng tiếng Việt, định nghĩa thuật ngữ và viết tắt tại chỗ, phân biệt kết quả được tổng quan dẫn lại với đề xuất chưa thực hiện. Những số liệu chủ chốt có nguồn hình/mục/trang; hồ sơ phương pháp có đủ 11 trường; quyết định sử dụng và điều kiện tái lập được nêu rõ. Bản thảo gốc, Explore của bài khác và các bản thảo thảo luận nghiên cứu không được sửa trong bước này.

Đã đọc lại file trên đĩa và kiểm tra **29 khối toán**: dấu dollar kép mở–đóng đứng riêng dòng, nội dung không rỗng, ngoặc nhọn và môi trường nhiều dòng cân bằng; không phát hiện ký tự điều khiển lỗi, dấu phân cách toán cũ hoặc công thức đặt trong khối mã. Các công thức trọng tâm đã được đối chiếu trực quan với PDF; công thức do người phân tích dùng để đối chiếu, đặc biệt phần xác suất ở Mục 10, được ghi rõ nguồn gốc.

Đã chuẩn bị bản xem trước tạm dùng MathJax cục bộ và thử render, nhưng trình duyệt gặp lỗi môi trường, không hoàn tất xuất ảnh. Vì vậy, mức kiểm tra đạt được là **kiểm tra cú pháp và đối chiếu PDF**, chưa xác nhận hiển thị trực quan toàn bộ công thức Markdown; không tuyên bố đã biên dịch thành công. Không chạy mô phỏng hoặc tái lập kết quả số trong bước này.

## Critical Audit (chờ Prompt 02)
