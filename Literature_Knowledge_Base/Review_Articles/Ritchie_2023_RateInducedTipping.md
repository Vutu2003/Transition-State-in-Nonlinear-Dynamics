---
schema_version: "1.0"

paper_id: Ritchie_2023_RateInducedTipping
title: Rate-induced tipping in natural and human systems
authors:
  - Paul D. L. Ritchie
  - Hassan Alkhayuon
  - Peter M. Cox
  - Sebastian Wieczorek
year: 2023
journal: Earth System Dynamics
volume: "14"
issue: "3"
pages: "669–683"
doi: "10.5194/esd-14-669-2023"
url: "https://esd.copernicus.org/articles/14/669/2023/"
pdf_path: "paper/23 Rate-induced tipping in natural and human systems.pdf"

publisher_article_type: Review
article_type: hybrid
article_subtypes: [narrative-review, theoretical, computational]
classification_reason: "Bài tổng hợp và giải thích lý thuyết R-tipping cho độc giả nhiều lĩnh vực (§§1–3, 7), đồng thời báo cáo các thí nghiệm số và tipping diagrams do nhóm tác giả thực hiện (§§4–6, Appendix A). Mục tiêu tổng quan dẫn dắt bài, nên hồ sơ thuộc Review_Articles."
classification_confidence: high

research_group: methodological
research_topics: [critical-transitions, tipping-theory, nonlinear-dynamics, mechanistic-modeling, dynamical-characterization]
application_domains: [ecology, climate-dynamics, power-systems]
phenomena: [loss-of-tracking, return-tipping, safe-overshoot, multiple-critical-rates, phase-slip]
tipping_mechanisms: [R-tipping, B-tipping, B-R-interaction]
theoretical_concepts: [nonautonomous-dynamics, threshold-instability, basin-instability, edge-state, saddle-node-bifurcation, Hopf-bifurcation]
dynamical_models: [tilted-saddle-node, plant-herbivore, two-box-AMOC-reduction, three-bus-power-system]
research_methods: [narrative-synthesis, frozen-system-analysis, phase-plane-analysis, numerical-ODE-simulation, tipping-diagrams]

evidence_types: [literature-synthesis, mathematical-proof, analytical-result, numerical-simulation, computational-validation]
evidence_origin: [secondary, original]

reading_status: unknown
reading_depth: unknown
note_status: source-checked
source_review_scope: "Đọc PDF bản xuất bản (15 trang), §§1–7, Figs. 1–6, Appendix A1–A5 và References. Kiểm tra metadata Copernicus và danh mục GitHub/Zenodo, đọc các script chọn lọc. Video, dữ liệu kèm và full text các nghiên cứu được trích dẫn chưa được rà soát. Chưa chạy mô phỏng."
human_verified: false

date_first_read: null
date_reviewed: "2026-11-27"
last_updated: "2026-11-27"
discovery_source: null
inclusion_reason: "Cung cấp cơ sở hình học và thiết kế mô phỏng để nhận diện R-tipping, nghiên cứu tương tác B–R và phát triển giả thuyết EWS phụ thuộc cơ chế."

code_url: "https://github.com/hassanalkhayuon/rtippingreview"
data_url: "https://zenodo.org/records/7920243"
supplementary_materials:
  - "https://zenodo.org/records/7920243"
correction_or_erratum: null

tags: [rate-induced-tipping, basin-instability, edge-state, return-tipping, critical-rates, forcing-profiles]
---

# Ritchie et al. (2023) — Rate-induced tipping in natural and human systems

## 01. Research Overview

Một hệ mở có thể mất khả năng bám theo trạng thái ổn định đang dịch chuyển dù giá trị forcing luôn nằm trong miền mà trạng thái ấy tồn tại. Bài giải thích **rate-induced tipping (R-tipping)** bằng hình học của ngưỡng hoặc basin of attraction, rồi kiểm tra cách **biên độ, hình dạng và thang thời gian của forcing** cùng quyết định kết cục. Với một return pulse, thay đổi tốc độ có thể luân phiên đưa cùng một mô hình vào các miền tracking và tipping. (§§1–4, 7)

**Phân loại.** Copernicus công bố bài dưới nhãn *Review*, ngày 14/06/2023, trong *Earth System Dynamics*, 14(3), 669–683. Nhãn `hybrid` của knowledge base phản ánh tổng quan lý thuyết (§§1–3) và đóng góp số riêng của tác giả (§§4–6 và Appendix A). Bốn thiết lập gồm tilted saddle-node dùng để giải thích cơ chế và ba mô hình ứng dụng về hệ thực vật–động vật ăn cỏ, AMOC và lưới điện. Kết quả ứng dụng là mô phỏng trên các mô hình đã có hoặc được điều chỉnh. [Bản xuất bản của Copernicus](https://esd.copernicus.org/articles/14/669/2023/)

**Quy ước nguồn.** Số trang trong hồ sơ là trang in 669–683, tương ứng PDF 1–15. Đã đọc bản xuất bản, kiểm tra bản hiển thị các hình và phương trình chính, đối chiếu danh mục tài liệu bổ trợ và một số script. Trạng thái video, tệp dữ liệu mô phỏng và full text của các bài dẫn là `Not reviewed`. Trang publisher và tra cứu theo DOI chưa cho thấy correction hoặc erratum chính thức. Các điểm khác nhau giữa bản in và script được ghi tại §06 của hồ sơ.

## 02. Scientific Background and Motivation

Ở cách giải thích theo **bifurcation-induced tipping (B-tipping)**, sự thay đổi của một tham số bên ngoài làm nhánh trạng thái đang được hệ bám theo mất ổn định hoặc biến mất. Các nghiên cứu mà bài dẫn cho thấy vượt ngưỡng trong thời gian ngắn có thể vẫn phục hồi, vì quỹ đạo chưa rời vùng có thể quay về khi forcing đảo chiều. (§1, pp. 669–670; §4, p. 673)

Theo tác giả, trong Anthropocene, nhiều forcing thay đổi đủ nhanh để việc giả định hệ luôn gần cân bằng tức thời trở nên thiếu tin cậy. Câu hỏi khi đó là liệu hệ có kịp thích nghi với đường đi của forcing hay sẽ vượt một ngưỡng trong không gian trạng thái. Bài đặt câu hỏi này trong bối cảnh nghiên cứu khí hậu, hệ sinh thái và hạ tầng. Nhận định rằng R-tipping có thể phổ biến là lập luận của tác giả từ cơ chế và các ví dụ. (§§1, 7)

## 03. Review Methodology

| Thành phần | Thông tin tác giả báo cáo |
|---|---|
| Loại review và nguồn tư liệu | Narrative/tutorial review. Dẫn lý thuyết của hệ không tự trị, nghiên cứu về ngưỡng và mô hình ứng dụng, cùng các công trình về vượt ngưỡng tạm thời. (§§1–3, 7; References) |
| Cơ sở dữ liệu, truy vấn, giai đoạn tìm kiếm | `Not reported` trong phần tổng quan hoặc Appendix A. |
| Tiêu chí chọn và loại, quy trình sàng lọc, đánh giá chất lượng nghiên cứu | `Not reported`. Tác giả mô tả các mô hình ứng dụng là ví dụ minh họa có độ phức tạp khác nhau. (Abstract; §1) |
| Khung phân loại | B-tipping, R-tipping và tương tác B–R dưới forcing không đơn điệu. Trọng tâm là regular thresholds. Quasithreshold, irregular thresholds và các cơ chế khác xuất hiện qua tài liệu dẫn. (§§1–2, 4, 7) |
| Phương pháp tổng hợp | Trực giác threshold/basin instability → định nghĩa rate khi giữ biên độ cố định → đối chiếu ramp và return → so sánh hình học và tipping diagrams qua các mô hình. (§§2–6; Appendix A) |

**Thiết kế original.** Chọn điều kiện đầu ở base state tại forcing nền. Xác định các cấu trúc frozen-system liên quan, sau đó tích phân ODE với các forcing có cùng mức đỉnh và khác rate. Mỗi mô hình được đánh giá bằng đáp ứng theo thời gian, phase portrait và/hoặc biên tracking–tipping trong mặt phẳng mức dịch chuyển–rate. Đối chiếu giữa các mô hình kiểm tra khả năng tái hiện định tính của tilted saddle-node. (§§4–6; Appendix A1–A5)

## 04. Theoretical Foundations

### Frozen system, tracking và các loại ngưỡng

Giữ forcing $\lambda$ tại một mức cố định để thu được **frozen system** của hệ $\dot{\mathbf{x}}=f(\mathbf{x},\lambda(t))$. Trong các ví dụ của bài, **base state** là cân bằng ổn định của frozen system tại từng mức forcing. Quỹ đạo thực có thể bị trễ so với cân bằng đang dịch chuyển. Base state tổng quát có thể là attractor phi tĩnh. Mô hình quả cầu trong stability landscape ở Fig. 1 diễn đạt trực giác về hướng phục hồi và vượt ngưỡng. Việc biểu diễn bằng một landscape chỉ thích hợp với một số lớp hệ. (§2, pp. 670–671, Fig. 1 và chú thích 1)

- **Threshold instability.** Sau một dịch chuyển forcing, vị trí base state ban đầu nằm phía bên kia của ngưỡng ứng với forcing mới. Nếu ngưỡng đó là biên basin của hai attractor, bài gọi trường hợp này là **basin instability**. Với ramp đủ nhanh, quỹ đạo còn gần vị trí ban đầu khi ngưỡng đã dịch chuyển. Với ramp đủ chậm trong các trường hợp minh họa, quỹ đạo bám theo base state. (§2, Fig. 1)
- **Phạm vi kết quả toán học.** Theo các định lý được bài dẫn, threshold/basin instability dưới các giả thiết tương ứng cho biết tồn tại forcing gây R-tipping. Necessary-and-sufficient là nhận định cho các ví dụ bài xem xét. Để quyết định kết cục cho một forcing profile cụ thể, còn phải phân tích quỹ đạo và rate. (§2; Kiers & Jones, 2020; Wieczorek et al., 2023, qua review)
- **Edge state.** Ở biên giữa tracking và tipping, quỹ đạo tới một invariant set không ổn định theo hướng tách hai kết cục. Fig. 4 báo cáo cân bằng không ổn định cho plant–herbivore và chu kỳ đẩy cho AMOC. Các quỹ đạo ở critical rate là minh họa số theo hình học này. (§5, Figs. 4c,f)
- **Critical level và critical rate.** Critical level là giá trị forcing của bifurcation trong frozen system, chẳng hạn fold hoặc Hopf. Critical rate là biên theo tham số thời gian giữa các kết cục tại một profile và mức dịch chuyển đã xác định. Một bifurcation có thể bị vượt qua tạm thời mà hệ vẫn phục hồi, như các return profile ở §4. (§§3–5)

### Tham số rate và forcing profiles

Đặt $u=rt$ không thứ nguyên, $r$ có đơn vị nghịch đảo thời gian và viết forcing là $\lambda(rt)$. Khi giữ hình dạng cùng biên độ forcing cố định, tăng $r$ nén profile theo trục thời gian. Đạo hàm vật lý là $d\lambda/dt=r\,d\lambda(u)/du$, có đơn vị của forcing trên đơn vị thời gian và thay đổi dọc profile. Ví dụ trong AMOC, forcing hosing $H$ đo bằng Sv còn $r$ đo bằng $\mathrm{yr}^{-1}$. (§3; Fig. 5b)

Với $t\geq 0$, thời điểm đỉnh $T$ và mức dịch chuyển $\Delta_\lambda$, các thiết lập dùng $\lambda(rt)=\lambda_-+\Delta_\lambda a(rt)$ hoặc dạng vector tương ứng, với

$$
a_{\mathrm{ramp}}(rt)=
\begin{cases}
\operatorname{sech}\bigl(r(t-T)\bigr), & 0\leq t\leq T,\\
1, & t>T,
\end{cases}
\qquad
a_{\mathrm{return}}(rt)=\operatorname{sech}\bigl(r(t-T)\bigr).
$$

Ramp giữ nguyên đỉnh sau $T$, còn return tiến về mức nền với pha giảm đối xứng pha tăng. Khi cùng một $r$ chi phối hai pha, thay đổi $r$ cũng thay đổi thời gian lưu gần hoặc vượt critical level. Trong các diagram, tác giả chọn $T$ để $a(0)$ nhỏ theo từng mô hình. (Appendix A1–A5, Eqs. (A1)–(A2))

### Tilted saddle-node

Phương trình một chiều bảo toàn trạng thái thay thế $x=0$ và cho phép dịch chuyển cả nhánh cân bằng lẫn ngưỡng basin theo forcing:

$$
\dot{x}=-x\left[(x-A-s\lambda(rt))^2+\lambda(rt)\right].
$$

**AI-generated interpretation, suy ra từ Eq. (A3).** Với $\lambda<0$ ở miền mà hai nghiệm dương, $x_\pm=A+s\lambda\pm\sqrt{-\lambda}$. Từ dấu $\partial_x f$ tại nghiệm, $x_+$ ổn định, $x_-$ đẩy và làm biên basin, còn $x=0$ ổn định trong miền này. Hai nhánh dương gặp nhau tại $\lambda=0$ trong các thiết lập của bài. Tilt $s$ thay đổi cách các nhánh dịch theo $\lambda$ và do đó thay đổi khả năng xảy ra basin instability. Điều kiện của một dịch chuyển nhanh dưới fold có thể đọc trực tiếp từ việc so $x_+(\lambda_-)$ với $x_-(\lambda_{\mathrm{new}})$. (§4, Fig. 2; Appendix A2)

## 05. Scientific Knowledge Synthesis

**Mức forcing và lịch sử forcing.** Fig. 2a,d minh họa B-tipping với ramp vượt fold rồi giữ mức mới. Fig. 2b,e giữ đỉnh dưới fold, trong vùng basin instability. Hai rate dẫn đến tracking hoặc rơi về $x=0$. Fig. 2c,f dùng cấu trúc tilted theo chiều ngược lại để minh họa **return tipping** trên pha giảm. Trở về mức forcing đã từng an toàn có thể gây tipping vì trạng thái ngay trước lúc trở về đã dịch chuyển. (Paper-reported, original; §4, Fig. 2, p. 672; A2)

**Ramp và return có thể tạo ra số lượng critical rates khác nhau.** Với tilted saddle-node, biên ramp trong Fig. 3c tiến tới fold ở giới hạn chậm và tiến tới basin-instability boundary ở giới hạn nhanh. Với return, một mức đỉnh ngay dưới fold có thể cho hai critical rates bao quanh một khoảng R-tipping. Với một overshoot nhỏ trong Fig. 3c, khi tăng $r$ ở cùng mức đỉnh, bài ghi nhận chuỗi **B-tipping → tracking → R-tipping → tracking**, tức tối đa ba critical rates trong kịch bản này. Pha chậm để duy trì tracking và pha đủ nhanh để vượt fold an toàn có yêu cầu khác nhau. Khi toàn bộ pulse rất ngắn, trạng thái dịch chuyển ít và có thể vẫn phục hồi. (Paper-reported, original; §4, pp. 673–674, Fig. 3)

**Cùng cơ chế hình học, khác cấu trúc ngưỡng.** Với ramp ở plant–herbivore và AMOC, Fig. 4 cho thấy base state ban đầu ở ngoài basin của base state cuối. Rate thấp bám theo trạng thái đồng tồn tại hoặc AMOC-On. Rate cao làm mất herbivore hoặc đưa mô hình tới AMOC-Off. Fig. 5a có tối đa hai critical rates cho return ở một biên độ cố định, với miền mất khả năng quay về kéo sang phía dưới fold. Fig. 5b có tới ba critical rates cho return, với miền này trong diagram nằm phía trên Hopf. Biên AMOC có các đoạn gợn nhỏ; bài chưa định lượng nguồn gốc hay độ bền của các gợn. (Paper-reported, original; §5, Figs. 4–5, pp. 675–676)

**Chuyển tiếp có thể phục hồi.** Ở mô hình lưới điện, các cân bằng có cùng $V$ và cách nhau $2\pi$ theo phase angle. Ramp ở cả ba rate được chọn đưa $V$ về 0 theo quy ước vật lý của mô hình. Với return pulse cùng đỉnh, rate chậm trong ba ví dụ vẫn dẫn tới blackout, rate trung bình gây sụt áp tạm thời cùng một $2\pi$ phase slip, và rate nhanh duy trì tracking. Phase slip là chuyển tiếp có phục hồi sang cân bằng lân cận cùng mức điện áp. Ba mẫu ở Fig. 6 nằm dưới fold. (Paper-reported, original; §6, pp. 677–678, Fig. 6, chú thích 4; A5)

## 06. Methodological Landscape

| Approach | Scientific purpose | Main assumptions | Strengths | Limitations | Primary reference |
|---|---|---|---|---|---|
| So sánh base state ban đầu với basin hoặc ngưỡng tại forcing mới | Sàng lọc mức dịch chuyển có khả năng gây R-tipping | Có frozen dynamics và ngưỡng có thể xác định. Các so sánh của bài bắt đầu ở cân bằng. | Phân tích được nguyên nhân mất tracking dù nhánh ổn định vẫn tồn tại | Suy ra tính dễ tổn thương dưới giả thiết của tiêu chí. Cần tích phân theo profile để ước lượng $r_c$. | O’Keeffe & Wieczorek (2020); Kiers & Jones (2020); Wieczorek et al. (2023), qua §2 |
| Tilted saddle-node và mô phỏng ramp/return cùng biên độ | Kiểm soát tác động của tốc độ và overshoot | ODE 1D xác định, forcing sech, base state cố định lúc bắt đầu | Có thể kiểm tra quan hệ giữa vị trí nhánh, basin boundary và điểm rơi $x=0$ | Kết cấu một chiều và pulse đối xứng giới hạn các tương tác có thể quan sát | Ritchie et al. (2023), §4, A1–A2 |
| Phase portrait và quỹ đạo gần critical rate | Nhận diện invariant set phân tách tracking và tipping | Quan sát được cả trạng thái mô hình và ngưỡng frozen hệ 2D | Phân biệt ngưỡng là stable manifold của saddle với ngưỡng là chu kỳ đẩy | Quỹ đạo số gần biên nhạy với rate, sai số tích phân và cửa sổ quan sát | Ritchie et al. (2023), Fig. 4 |
| Tipping diagram theo peak shift–rate | Xác định miền tracking, tipping, recovery và nhiều critical rates | Phân loại kết cục theo từng mô hình, dưới một họ forcing và điều kiện đầu đã chọn | Thấy được bất đối xứng giữa ramp/return và các vùng rủi ro không đơn điệu | Độ phân giải, thời gian tích phân và quy tắc phân loại ảnh hưởng các biên mảnh | Ritchie et al. (2023), Figs. 3c, 5, 6c |

### Mô hình nền và thiết kế original

**Plant–herbivore.** ODE của Scheffer et al. (2008), với tham số theo O’Keeffe & Wieczorek (2020), mô tả biomass $P,H$ theo $\mathrm{g\,m^{-2}}$. Đáp ứng tiêu thụ $g(P)$ không đơn điệu. Tác giả cố định sáu tham số và đồng biến đổi plant growth rate $\rho$ và herbivore mortality rate $m$, đều theo $\mathrm{d}^{-1}$. (§5; Appendix A3, Eqs. (A4)–(A10))

$$
\dot P=\rho(rt)P-CP^2-Hg(P),\qquad
\dot H=H\left[E e^{-bP}g(P)-m(rt)\right],\qquad
g(P)=c_{\max}\frac{P^2}{P^2+a^2}e^{-b_cP}.
$$

Đặt $\rho(rt)=\rho_-+\Delta_\rho a(rt)$ và $m(rt)=m_-+\Delta_m a(rt)$, với $m(rt)-m_-=(\rho(rt)-\rho_-)/30$. Độ dịch chuẩn hóa $\Delta_e=\Delta_\rho/\Delta_{\rho,\mathrm{Fold}}=\Delta_m/\Delta_{m,\mathrm{Fold}}$ đặt fold tại $\Delta_e=1$. Trạng thái theo dõi là cân bằng đồng tồn tại, đầu ra chính là biomass $H$. Cân bằng plant-only có $H=0$. (Appendix A3, p. 679)

**AMOC.** Mô hình năm hộp của Wood et al. (2019) được giản lược theo Alkhayuon et al. (2019). Giữ $S_S$ và $S_B$ cố định do biến thiên chậm trong mô hình nguồn, suy ra $S_{IP}$ từ bảo toàn độ mặn và giữ $\Delta T$ cố định. Trạng thái động là $(S_N,S_T)$, đo theo psu trên Fig. 4f. Quan sát lưu lượng AMOC $q=\lambda(\alpha\Delta T+\beta(S_N-S_S))/(1+\lambda\alpha\mu)$ đo bằng Sv, với $1\,\mathrm{Sv}=10^6\,\mathrm{m^3\,s^{-1}}$. Ký hiệu $\lambda$ trong Eq. (A11) là hệ số mô hình. Forcing nằm ở vector flux bề mặt trong Eq. (A16). Các phương trình ngân sách độ mặn đổi hạng vận chuyển theo dấu của $q$. Hosing $H(rt)=\Delta_H a(rt)$ điều biến bốn flux bề mặt theo quan hệ tuyến tính có tổng bằng 0. Fig. 5b đánh dấu Hopf và fold riêng. Biên tới hạn ramp tiến về Hopf ở phía rate chậm trong diagram. (§5; Figs. 4d–f, 5b; A4, Eqs. (A11)–(A16))

**Lưới điện.** Mô hình ba nút kế thừa từ Dobson et al. (1988), Dobson & Chiang (1989) và Budd & Wilson (2002), gồm bốn biến trạng thái $(\delta_m,\omega_m,\delta,V)$. Hai biến đầu là góc pha và vận tốc góc của máy phát. Hai biến sau là góc pha và độ lớn điện áp tải. Tác giả giữ real power demand $P_1=5$, khi đó đường thay đổi reactive power demand $Q_1(rt)=Q_{1-}+\Delta_{Q_1}a(rt)$ gặp fold và tránh Hopf thấy trong thiết lập $P_1=0$ của nghiên cứu dẫn. Tipping được phân loại theo $V$ và pha. Tác giả giới hạn diễn giải vật lý tại $V\geq0$ và dùng $V=0$ để mô tả blackout. (§6, chú thích 4; A5, Eqs. (A17)–(A19))

### Phương pháp số, kiểm chứng và điều kiện tái lập

- **Fig. 3.** Script vẽ time series dùng Euler tiến với bước $0.001$, đặt gốc thời gian tại đỉnh, dùng $\Delta_\lambda=0.48$ cho ba quỹ đạo, và đọc dữ liệu biên từ các tệp `.mat`. Script bisection đi kèm minh họa cách chia đôi biên độ tại $r$ cố định dựa vào trạng thái cuối. Bản script hiện có đặt $A=3$, $\lambda_-=-0.4$, khác $A=3.2$, $\lambda_-=-0.5$ trong bài và script vẽ. Cấu hình sinh các tệp biên ở Fig. 3c là `To verify`. [Script vẽ Fig. 3](https://github.com/hassanalkhayuon/rtippingreview/blob/main/Tilted_SN_plotting_time_series_critical_boundaries_regions_v3.py) · [Script bisection](https://github.com/hassanalkhayuon/rtippingreview/blob/main/Tilted_SN_bisection.py)
- **AMOC.** Script diagram công khai dùng `ode45`, thử biên theo $\Delta_H$ bằng `fzero` trên hàm phân loại từ thành phần trạng thái cuối và có minh họa giới hạn $r=\infty$ cho basin instability. Đây là tiêu chí số trên cửa sổ hữu hạn. Phase portrait của Fig. 4f cung cấp kiểm tra hình học cho cách đọc kết cục. [Script AMOC](https://github.com/hassanalkhayuon/rtippingreview/blob/main/tipping_diagram_AMOC.m)
- **Lưới điện.** Script bisection công khai dùng `solve_ivp` với event dừng tại $V=0$. `To verify` khi tái lập từ bản in, vì Eq. (A18) có ký hiệu $\sin(\delta-\delta_m\theta_m)$ trong $P_e$, còn script dùng $\sin(\delta-\delta_m-\theta_m)$. Hạng đầu của $P_l$ trong bản in cũng có ký hiệu $V T_0$ tại chỗ script dùng hệ số admittance ở nút nguồn. Hồ sơ dùng Eq. (A19) nguyên dạng cho forcing. [Bản in, p. 680](https://esd.copernicus.org/articles/14/669/2023/esd-14-669-2023.pdf) · [Script lưới điện](https://github.com/hassanalkhayuon/rtippingreview/blob/main/Power_grid_model_bisection_P5.py)
- **Validation original.** Các đối chiếu cùng đỉnh/khác rate, biên basin trên phase plane và so sánh diagram giữa các mô hình là kiểm chứng số theo cơ chế trong mô hình. Thí nghiệm kiểm soát trên hệ thực, dữ liệu kiểm định độc lập, và quy trình kiểm định EWS, detection hay forecasting là `Not reported` trong §§4–7 và Appendix A. `Reproduction status` là đã đọc chọn lọc script và đối chiếu tham số, chưa chạy lại. [Code và dữ liệu mô phỏng](https://zenodo.org/records/7920243)

## 07. Scientific Evidence and Citation Network

| Scientific claim | Supporting evidence | Primary reference | Evidence type | Source location in review |
|---|---|---|---|---|
| Threshold/basin instability dưới các giả thiết tương ứng cho phép tồn tại forcing gây R-tipping. | Review tóm tắt kết quả toán học đã công bố. Fig. 1 giải thích trực giác bằng ngưỡng dịch chuyển. | Kiers & Jones (2020); Wieczorek et al. (2023). Cả hai qua review. | Mathematical proof, secondary. | §2, pp. 670–671, Fig. 1 |
| Tipping có thể xảy ra trong một ramp dưới fold khi tăng $r$ ở biên độ cố định. | Hai quỹ đạo của tilted saddle-node gần cùng forcing endpoint. Rate thấp tracking, rate cao về $x=0$. | Ritchie et al. (2023), PDF đã đọc trực tiếp. | Numerical simulation, original. | §4, Fig. 2b,e; A2 |
| Có overshoot nhỏ cho ba critical rates dưới return forcing. | Đường biên chữ S phân chia hai khoảng tipping và hai khoảng tracking khi nhìn theo $r$ tại một mức đỉnh. | Ritchie et al. (2023), trực tiếp. Kết quả về safe overshoot được liên hệ với Ritchie et al. (2021), qua review. | Numerical simulation, original cho diagram. | §4, pp. 673–674, Fig. 3c |
| Hai mô hình ứng dụng có thể tiến gần các loại edge state khác nhau tại critical rate. | Quỹ đạo xanh dương tiếp cận cân bằng không ổn định ở plant–herbivore và chu kỳ đẩy ở AMOC. | Ritchie et al. (2023), trực tiếp. | Numerical simulation và dynamical characterization, original. | §5, Fig. 4c,f; A3–A4 |
| AMOC đã được mô phỏng là nhạy với rate trong các cấu trúc mô hình khác. | Review dẫn mô phỏng với thay đổi tốc độ phát thải CO₂ hoặc freshwater hosing và kết quả của box model. | Stocker & Schmittner (1997); Lohmann & Ditlevsen (2021); Alkhayuon et al. (2019), qua review. | Numerical simulation, secondary. | §5, pp. 675–676 |
| Return có thể dẫn đến blackout, phase slip có phục hồi hoặc tracking ở các rate khác nhau. | Phân loại đáp ứng điện áp và pha của mô hình ba nút. Fig. 6b hiển thị điện áp, còn §6 mô tả điều kiện pha. | Ritchie et al. (2023), trực tiếp. | Numerical simulation, original. | §6, Fig. 6; A5 |
| Tốc độ tăng công suất có thể góp phần vào sự cố suýt mất điện ở Anh sau trận Euro 1990. | Case được thuật lại như một khả năng giải thích trong bài. | Swarup (2007), qua review. | Tường thuật lịch sử thứ cấp và giả thuyết cơ chế của tác giả review. | §6, p. 677 |

### Kết quả định lượng theo thiết lập

| Mô hình / scenario | Thiết lập đã kiểm tra | Kết cục được báo cáo | Vị trí |
|---|---|---|---|
| Tilted saddle-node, ramp qua fold | $s=4$, $A=3.2$, $\lambda_-=-0.5$, $\Delta_\lambda=0.505$, $T=500$, $r=0.05$ | $\lambda$ đạt và giữ ở $0.005$, phía bên kia fold, rồi hệ B-tips. | Fig. 2a,d; A2, p. 679 |
| Tilted saddle-node, ramp dưới fold | $s=4$, $A=3.2$, $\lambda_-=-0.5$, $\Delta_\lambda=0.4$, $T=500$ | $r=1$ tracking, $r=3$ R-tipping. Đỉnh $\lambda=-0.1$. | Fig. 2b,e; A2 |
| Tilted saddle-node, pha giảm của forcing | $s=-4$, $A=1.5$, $\lambda_-=-0.1$, $\Delta_\lambda=-0.4$, $T=500$ | $r=1$ tracking, $r=3$ return tipping. A2 khởi tạo tại base state tương ứng $\lambda_-$. | Fig. 2c,f; A2 |
| Tilted saddle-node, so sánh ramp–return | $s=4$, $A=3.2$, $\lambda_-=-0.5$, $\Delta_\lambda=0.48$ (script Fig. 3), $r=0.5,\ 0.9,\ 1.7$ | Cả hai profile tracking tại $0.5$. Tại $0.9$, ramp tips và return phục hồi. Tại $1.7$, cả hai tips. | Fig. 3a–c; A2; script vẽ Fig. 3 |
| Plant–herbivore, ramp (các màu xanh lá, xanh dương, đỏ) | $T=200\,\mathrm{d}$, $\rho_-=0.5$, $m_-=0.125$, $\Delta_\rho=0.1$, $\Delta_m=0.0033$ theo $\mathrm{d}^{-1}$ sau làm tròn. $\Delta_e=0.51$. | $r=0.03\,\mathrm{d}^{-1}$ tracking, $r\approx0.0453\,\mathrm{d}^{-1}$ quỹ đạo gần edge state, $r=0.1\,\mathrm{d}^{-1}$ herbivore tiến về 0. | Fig. 4a–c; A3 |
| AMOC, ramp (cùng thứ tự màu) | $T=1000\,\mathrm{yr}$, $\Delta_H=0.365\,\mathrm{Sv}$ từ mức nền $H=0$. | $r=0.005\,\mathrm{yr}^{-1}$ tracking, $r\approx0.01645\,\mathrm{yr}^{-1}$ quỹ đạo gần chu kỳ đẩy, $r=0.017\,\mathrm{yr}^{-1}$ tiến về AMOC-Off (nhánh có $q<0$ trong Fig. 4e). | Fig. 4d–f, Fig. 5b cho đơn vị $r$; A4 |
| Lưới điện, ramp và return (xanh dương, cam, tím) | $P_1=5$, $Q_{1-}=5$, $\Delta_{Q_1}=5$, $T=0.15$, $r=50,\ 130,\ 400$ theo trục thời gian của mô hình. Đơn vị vật lý cho $Q_1$, $V$ và thời gian là `Not reported` tại Fig. 6 và A5. | Ramp blackout cả ba. Return lần lượt blackout, sụt áp tạm thời và phase slip, tracking. | Fig. 6a–c; A5 |

Các $r$ xấp xỉ ở Fig. 4 là ước lượng critical rate cho đúng biên độ và ramp nêu trong bảng. Các rate lấy mẫu ở Fig. 2, Fig. 3 và Fig. 6 minh họa từng miền kết cục. Thiết lập số của bài dùng điểm đầu tại base state của forcing nền, với thời điểm bắt đầu đủ xa đỉnh trong các diagram để forcing ban đầu xấp xỉ mức nền. (Appendix A)

## 08. Research Gaps and Open Problems

- **Tác giả nêu trực tiếp.** Để dự báo định lượng cần mô hình phức tạp hơn và forcing thực tế hơn, chẳng hạn mô hình hoàn lưu toàn cầu hiện đại. Các ví dụ hiện tại chủ đích mô tả hiện tượng định tính. (§7, p. 678)
- **Tác giả nêu trực tiếp.** Base state có thể là chu kỳ hoặc chaotic attractor. Khi đó pha và cấu trúc của attractor có thể ảnh hưởng kết cục, như trong P-tipping. Bài dẫn nghiên cứu liên quan và để mở việc tích hợp chúng vào các mô hình thực tế hơn. (§7, p. 678)
- **To revisit, theo phạm vi tác giả xác định.** Bài tập trung vào regular thresholds. Quasithreshold và irregular threshold được nêu thông qua các nghiên cứu khác. Hệ quả đối với khả năng định nghĩa một biên rate đủ ổn định để dự báo cần được xem theo từng hệ. (§1, p. 670)
- **AI-generated research question.** Khi cho pha tăng và giảm có rate độc lập, các miền return ở Figs. 3, 5 và 6 biến đổi ra sao? Chú thích 3 ở §4 nêu khả năng dùng pulse bất đối xứng. Phân tích độ bền của nhiều critical rates theo hình dạng pulse, nhiễu và lịch sử trạng thái là hướng mở rộng của hồ sơ.

## 09. Critical Evaluation

**Tác giả tự nêu.** Các mô hình tương đối đơn giản và forcing được lý tưởng hóa. Tác giả hướng tới so sánh định tính, đồng thời xác định mô hình phức tạp và forcing thực tế là điều kiện cho dự báo định lượng. (§7)

**AI-generated interpretation.**

- **Điểm mạnh về nhận diện trong mô hình.** So sánh cùng biên độ và khác rate ngay dưới bifurcation làm rõ trường hợp R-tipping. Thêm phase portrait và geometry của biên basin giúp xác định cơ chế trong mô hình. Fig. 4 minh họa bằng hai loại edge state nên kết luận định tính ít phụ thuộc vào việc chọn một saddle cân bằng làm ngưỡng.
- **Phạm vi bằng chứng.** Các mô hình cùng dùng forcing sech lý tưởng hóa và các regular thresholds. Sự lặp lại của cơ chế cho thấy khả năng xuất hiện trong nhiều cấu trúc mô hình. Tần suất, độ tin cậy định lượng và ngưỡng rate trong hệ thực chưa được ước lượng. Với tình huống suýt mất điện được nêu, độ trễ điều khiển, quá trình vận hành và các biến đồng thời vẫn là những giải thích cần dữ liệu để phân biệt. (§§1, 6–7)
- **Độ bao phủ của review.** Việc chọn minh họa có basin instability phù hợp mục tiêu sư phạm. Vì thiếu mô tả tìm kiếm và tiêu chí chọn, không thể ước lượng selection bias hoặc mức độ bao phủ các trường hợp phản ví dụ. Kết quả secondary theo từng bài dẫn cần được kiểm tra ở nguồn gốc trước khi dùng làm bằng chứng độc lập.
- **Độ bền và khả năng tái lập.** Với quỹ đạo gần edge state hoặc biên có gợn, cần xét sai số tích phân, thời gian theo dõi và quy tắc phân loại. Các ngưỡng theo trạng thái cuối trong script là xấp xỉ operational. Các khác biệt giữa bản in, script mẫu và dữ liệu biên nêu tại §06 ảnh hưởng việc tái tạo chính xác Fig. 3c hoặc triển khai lưới điện theo Eq. (A18).
- **Cơ chế thay thế trong dữ liệu quan sát.** Lag, một đáp ứng quá độ dài, thay đổi phase của base attractor hoặc stochastic escape có thể tạo tín hiệu giống tipping. Thiết kế xác định của bài cho phép khảo sát R-tipping khi nhiễu được giữ ngoài mô hình. Một đường ghi đơn lẻ thiếu forcing và trạng thái ẩn khó cung cấp cùng mức nhận diện. (§§2, 5–7; Appendix A)

## 10. Scientific and Methodological Insights

- **Dùng cả biên frozen và endpoint của quỹ đạo.** Bifurcation diagram cho biết cân bằng có tồn tại và ổn định ở mức forcing nào. Phase portrait cho biết quỹ đạo có thể đi đến đâu khi forcing thay đổi. Hai nguồn thông tin giúp phân biệt mất nhánh, mất tracking và transient excursion. (§§2, 4–6)
- **Gắn critical rate với profile và điều kiện đầu.** Khi gắn $r_c$ với peak shift, profile, trạng thái ban đầu và nhãn kết cục, có thể so sánh định tính giữa mô hình. Một đường biên trong mặt phẳng $(\Delta,r)$ thể hiện trực tiếp khả năng có nhiều $r_c$ cho một mức đỉnh. (§3; Figs. 3c, 5, 6c)
- **Tách kết cục và thời điểm.** AI-generated interpretation. Trong một mô phỏng dài, thời điểm crossing threshold, thời điểm tín hiệu quan sát bắt đầu biến đổi, thời điểm đạt một operational event và thời điểm xác nhận attractor đích có thể khác nhau. Thiết kế detection hay EWS cần khai báo rõ mốc tham chiếu. (Căn cứ: quỹ đạo gần edge state ở Fig. 4 và quá trình phục hồi ở Fig. 6)
- **Phân tích hai pha của return.** Đối chiếu các đáp ứng ramp–return với cùng pha tăng cho phép đánh giá điều gì thay đổi khi forcing được đảo chiều. Khi pulse đối xứng, thay $r$ đồng thời thay tốc độ tiến, thời gian quanh đỉnh và tốc độ lùi. Việc thay từng yếu tố riêng là một thiết kế mở rộng có thể kiểm tra các ảnh hưởng này. (§4, chú thích 3; A1)

## 11. Relevance to My Research

**AI-generated interpretation cho hướng Mechanistic Modeling and Early-Warning Indicators of Physiological State Transitions.** Bài cung cấp thiết kế đối chứng cho nghiên cứu mô phỏng sinh lý và cách lập ground truth theo cơ chế. Ứng dụng phù hợp để khảo sát là một mô hình excitability có trạng thái ẩn, input được ghi và tín hiệu quan sát liên quan đến state, chẳng hạn điện thế màng hoặc tín hiệu tổng hợp từ mô hình thần kinh. Bằng chứng của bài thuộc sinh thái, khí hậu và lưới điện. Mức tương ứng sinh lý của input, trạng thái và ngưỡng cần được thiết lập bằng mô hình hoặc dữ liệu của bài toán đích. (Căn cứ chuyển giao: §§2–5; tham chiếu neural excitability trong §1)

| Câu hỏi ứng viên | Thiết kế kiểm tra | Dữ liệu hoặc điều kiện |
|---|---|---|
| Một cơ chế mất tracking có thể tạo dấu hiệu quan sát phân biệt được với B-tipping và stochastic escape hay không? | Xây frozen bifurcation diagram. Tạo quỹ đạo đối chứng dưới fold với nhiều rate, qua fold và dưới forcing cố định với nhiều mức nhiễu. Dùng full state mô phỏng tạo nhãn, rồi tính feature từ tín hiệu quan sát đã giới hạn. | Mô hình sinh lý có justification cho input và state, observation model, tham số và time units hợp lý, có nhiều trajectory và điều kiện đầu. |
| Lag so với moving base state hoặc khoảng cách tới threshold có thêm giá trị cảnh báo hay không? | So sánh dự báo có horizon cố định dùng các đại lượng ước lượng được tại thời điểm dự báo với baseline chỉ dùng forcing hoặc tín hiệu. Có thể đưa variance và autocorrelation vào nhóm đối chứng. | Cần input đồng bộ thời gian, cách ước lượng base state hoặc basin từ dữ liệu hiện có, và kiểm tra độ nhạy khi chỉ đo được một phần trạng thái. |
| Có thể phân biệt excursion có hồi phục với chuyển sang chế độ bền khác từ tín hiệu quan sát hay không? | So sánh ramp và pulse có cùng đỉnh. Định nghĩa riêng onset của excursion, recovery và kết cục dài hạn. Kiểm tra độ bền qua các shape và rate khác nhau. | Cần đủ thời gian ghi sau sự kiện và tiêu chí phục hồi gắn với trạng thái hoặc tín hiệu sinh lý. |

Một benchmark mô phỏng xác định có thể kiểm tra nhận diện cơ chế trước khi thêm nhiễu và partial observability. Với dự báo pseudo-real-time, dùng lịch sử đã có đến từng thời điểm, giữ các trajectory hoặc người tham gia độc lập giữa các tập đánh giá, và báo lead time theo mốc sự kiện đã định, cùng false positives và false negatives. Khả năng áp dụng thực nghiệm phụ thuộc vào việc đo hoặc biện minh được external forcing, phân biệt measurement noise với process noise và thu đủ lần chuyển tiếp ở nhiều forcing profiles.

## 12. Literature Connections and Future Reading

Nguồn dưới đây xuất hiện trong References của bản xuất bản. Thông tin thư mục theo bibliography của bài và các liên kết được ghi kèm. Trạng thái full text của các nguồn là `Not reviewed` trong phiên này.

| Công trình | Lý do đọc |
|---|---|
| P. Ashwin, S. Wieczorek, R. Vitolo và P. Cox (2012), *Tipping points in open systems: bifurcation, noise-induced and rate-dependent examples in the climate system*. | Nền tảng để đối chiếu B-, N- và R-tipping trong hệ mở. |
| Claire Kiers và Christopher K. R. T. Jones (2020), *On Conditions for Rate-induced Tipping in Multi-dimensional Dynamical Systems*. | Kiểm tra giả thiết chính xác của các điều kiện đủ trong hệ nhiều chiều. [Bản preprint của tác giả](https://arxiv.org/abs/1810.02808) |
| P. E. O’Keeffe và S. Wieczorek (2020), *Tipping phenomena and points of no return in ecosystems: beyond classical bifurcations*. | Đọc cơ sở cho basin instability, return tipping, tilted fold và tham số plant–herbivore trong Table 2.1. |
| S. Wieczorek, C. Xie và P. Ashwin (2023), *Rate-induced tipping: thresholds, edge states and connecting orbits*. | Đi sâu vào regular thresholds, edge states và quan hệ với connecting orbits. [DOI](https://doi.org/10.1088/1361-6544/accb37) |
| H. Alkhayuon, P. Ashwin, L. C. Jackson, C. Quinn và R. A. Wood (2019), *Basin bifurcations, oscillatory instability and rate-induced thresholds for Atlantic meridional overturning circulation in a global oceanic box model*. | So sánh mô hình gốc, giản lược độ mặn và bifurcation structure. Tác giả review chỉ đến Tables 3–4. |
| P. Ritchie và J. Sieber (2016), *Early-warning indicators for rate-induced tipping*. | Khởi điểm để xem đánh giá EWS cho R-tipping trong nghiên cứu riêng. [DOI](https://doi.org/10.1063/1.4963012) |
| P. D. L. Ritchie, J. J. Clarke, P. M. Cox và C. Huntingford (2021), *Overshooting tipping point thresholds in a changing climate*. | Đối chiếu safe overshoot và thời gian ở trên critical level với tương tác B–R trong Fig. 3. [Bài báo](https://www.nature.com/articles/s41586-021-03263-2) |
| J. Lohmann và P. D. Ditlevsen (2021), *Risk of tipping the overturning circulation due to increasing rates of ice melt*. | Trường hợp so sánh về rate-sensitivity và threshold có hình học phức tạp hơn trong mô hình AMOC. |
| K. Slyman và C. K. Jones (2023), *Rate and noise-induced tipping working in concert*. | Đọc cho câu hỏi mở rộng về tương tác N–R và cơ chế thay thế dưới nhiễu. [DOI](https://doi.org/10.1063/5.0129341) |
| M. I. Maturana, C. Meisel, K. Dell, P. J. Karoly, W. D’Souza, D. B. Grayden, A. N. Burkitt, P. Jiruska, J. Kudlacek, J. Hlinka, M. J. Cook, L. Kuhlmann và D. R. Freestone (2020), *Critical slowing down as a biomarker for seizure susceptibility*. | Nguồn liên hệ sinh lý được §1 dẫn. Dùng để khảo sát tính quan sát được của biomarker và cách áp dụng critical slowing down trong nghiên cứu động kinh. [Bài báo](https://doi.org/10.1038/s41467-020-15908-3) |

## 13. Systematic Data Extraction

| Extraction field | Extracted information | Source location |
|---|---|---|
| Article type | Hybrid ưu tiên review. Publisher label là Review. | Trang Copernicus; §1, §§4–6; Appendix A |
| Study design | Narrative/tutorial synthesis và mô phỏng ODE xác định có đối chứng theo biên độ, rate và shape. | Abstract; §§1–6; A1–A5 |
| Research problem | Một hệ mở có thể mất tracking và chuyển trạng thái chỉ vì forcing thay đổi đủ nhanh hay không, và kết cục đổi thế nào khi forcing đảo chiều? | Abstract; §§1–4 |
| Research objectives | Giải thích tiêu chí susceptibility, minh họa R-tipping ở các mô hình khác nhau và khảo sát nhiều critical rates, return tipping, reversible tipping. | §1; §7 |
| Application domain | Sinh thái thực vật–herbivore, khí hậu AMOC và lưới điện. | §§5–6 |
| Investigated phenomenon | Loss of tracking, basin instability, return tipping, safe overshoot, phase slip có phục hồi. | §§2, 4–6 |
| Tipping mechanism | R-tipping, B-tipping và tương tác B–R dưới forcing không đơn điệu. N–R chỉ xuất hiện qua tài liệu dẫn. | §§1–2, 4, 7; References |
| Mechanism identification status | Kiểm tra cơ chế bằng frozen geometry và mô phỏng có đối chứng trong mô hình. Sự kiện thực được nêu như giả thuyết cơ chế. | §§4–6, Figs. 2–6 |
| Theoretical framework | Non-autonomous ODE, base state, threshold/basin instability, edge state, bifurcation của frozen system. | §§2–4 |
| Dynamical model | Tilted saddle-node 1D, plant–herbivore 2D, AMOC reduced box 2D, lưới điện ba nút 4D. | A2–A5 |
| Model origin | Fold normal form được tilt, Scheffer et al. (2008), Wood et al. (2019)/Alkhayuon et al. (2019), Dobson et al. (1988)/Dobson & Chiang (1989)/Budd & Wilson (2002). | A2–A5 |
| Model modifications | Tilt $s$ ở mô hình 1D, forcing đồng biến đổi $\rho,m$, dùng AMOC giản lược và hosing tuyến tính, đặt $P_1=5$ trong lưới điện. | A2–A5 |
| State variables | $x$; $(P,H)$; $(S_N,S_T)$; $(\delta_m,\omega_m,\delta,V)$. | A2–A5 |
| Observable variables | Đầu ra mô phỏng gồm $x$, biomass herbivore $H$, AMOC strength $q$, điện áp $V$ và biến đổi pha để phân loại phase slip. | Figs. 2–6; A2–A5 |
| Attractor type | Cân bằng ổn định là base state trong các ví dụ. Có cân bằng thay thế, edge equilibrium, repelling periodic orbit tại biên và transient excursion có phục hồi. | §2; §§4–6, Figs. 4, 6 |
| Control parameters | Rate $r$ và peak shift theo mô hình. Các tham số liên quan gồm $s$, $\rho,m$, hosing $H$ và $P_1,Q_1$. | §3; A2–A5 |
| External forcing | Dịch chuyển ramp theo sech và giữ đỉnh, hoặc return impulse đối xứng về forcing nền. | A1, Eqs. (A1)–(A2) |
| Stochastic noise | Không có hạng nhiễu trong các mô phỏng gốc. | A1–A5, Eqs. (A3)–(A19) |
| Transition definition | Mất tracking của base state đang dịch và chuyển tới trạng thái thay thế hoặc excursion có phục hồi. | §§2, 4–6 |
| Transition criterion | So sánh kết cục cuối và quỹ đạo gần ngưỡng. $x\to 0$, $H\to0$, AMOC-Off, hoặc $V$ về 0 hay sụt tạm kèm $2\pi$ phase slip theo từng mô hình. | Figs. 2–6; §6, chú thích 4; Appendix A |
| Analysis methodology | Frozen equilibria và basin, so sánh trajectory, phase portrait và tipping diagrams. Script chọn lọc có Euler, `ode45`, `solve_ivp` và tìm biên số. | §§2–6; A1–A5; script trong §06 của hồ sơ |
| EWS / Predictors | Basin instability là tiêu chí susceptibility dựa trên mô hình. Hiệu năng EWS từ chuỗi quan sát, lead time và validation forecasting là `Not reported`. | §2; §§4–7; Appendix A |
| Validation strategy | Đối chứng cùng biên độ, khác rate, và cùng pha tăng với hai lựa chọn sau đỉnh. Kiểm tra hình học và đối chiếu định tính giữa mô hình. | §§4–6; Figs. 2–6 |
| Evidence type | Literature synthesis và kết quả toán qua tài liệu dẫn. Numerical simulation, computational verification và hình học mô hình trong phần gốc. | §§1–7; A1–A5 |
| Evidence origin | Secondary cho định lý và nghiên cứu được tóm tắt. Original cho các thí nghiệm số được bài báo cáo. | §§1–3, 4–6; Author contributions, p. 680 |
| Main scientific findings | Tipping có thể xảy ra dưới critical level. Return có thể cứu hệ, gây tipping hoặc tạo nhiều critical rates. Loại kết cục có thể là chuyển tiếp có hồi phục. | §§4–7; Figs. 2–6 |
| Main quantitative results | Ở hai ramp minh họa, $r_c\approx0.0453\,\mathrm{d}^{-1}$ tại $\Delta_e=0.51$ và $r_c\approx0.01645\,\mathrm{yr}^{-1}$ tại $\Delta_H=0.365\,\mathrm{Sv}$. Tới hai hoặc ba critical rates dưới return trong một số diagram. Xem bảng ở §07 của hồ sơ. | Fig. 4; A3–A4; Figs. 3c, 5 |
| Authors' limitations | Mô hình tương đối đơn giản, forcing lý tưởng hóa và kết quả nhằm giải thích định tính. | §7, p. 678 |
| Alternative explanations | B-tipping hoặc tương tác B–R khi qua fold và giữ hoặc đảo forcing. Với ứng dụng thực, cơ chế khác gồm dao động, nhiễu và độ trễ điều khiển cần dữ liệu riêng để đánh giá (AI-generated interpretation). | §§4–7; References |
| Author-identified research gaps | Cần mô hình và forcing thực tế hơn để dự báo định lượng. Base state phi tĩnh có thể dẫn tới hiện tượng phức tạp hơn, như P-tipping. | §7, p. 678 |
| Code availability | Python/MATLAB trong GitHub và Zenodo, đã kiểm tra danh mục và đọc chọn lọc script. | Code and data availability, p. 680; [GitHub](https://github.com/hassanalkhayuon/rtippingreview) |
| Data availability | Dữ liệu mô phỏng và dữ liệu vẽ hình có trong archive. Đã kiểm tra danh mục tệp, trạng thái nội dung các tệp là `Not reviewed`. | Code and data availability, p. 680; [Zenodo v1](https://zenodo.org/records/7920243) |
| Reproduction status | Đã đối chiếu PDF, hình, script chọn lọc và tham số. Chưa chạy lại mô phỏng. Xem các điểm `To verify` ở §06 của hồ sơ. | Appendix A; code liên kết |
| Research relevance | Cung cấp benchmark, cơ sở phân biệt cơ chế và thiết kế forcing cho nghiên cứu tiếp theo về physiological state transitions và EWS. Liên hệ sinh lý là suy luận đề xuất. | §§2–6; §11 của hồ sơ |

## 14. Personal Research Notes

Awaiting personal research notes.

## Revision History

- 2026-11-27 — Tạo hồ sơ từ PDF bản xuất bản. Đối chiếu metadata, Figs. 1–6, Appendix A, danh mục bổ trợ và script chọn lọc. Ghi các tham số, kết quả theo từng mô hình, nguồn gốc evidence và các điểm cần xác minh khi tái lập.
