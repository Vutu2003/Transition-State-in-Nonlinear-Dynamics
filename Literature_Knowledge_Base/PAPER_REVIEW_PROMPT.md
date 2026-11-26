# Master Prompt — Literature Knowledge Base

## 1. Mục tiêu và cách sử dụng

Sử dụng tài liệu này để tạo hoặc cập nhật **một hồ sơ Markdown cho một nghiên cứu**. Trong một Codex session mới, đọc toàn bộ tài liệu này rồi đọc PDF được chỉ định. Hai đầu vào đủ để bắt đầu là đường dẫn đến `PAPER_REVIEW_PROMPT.md` và đường dẫn đến PDF gốc. Đọc các supplementary materials, correction, erratum hoặc ghi chú cá nhân nếu người dùng cung cấp. Tự xác định article type và chọn cấu trúc theo quy tắc bên dưới. Mọi thông tin điều phối cần thiết đều có trong tài liệu này.

Đề tài thạc sĩ đã đăng ký là **Nonlinear Time Series Analysis of Biomedical Signals**. Hướng đang cân nhắc là **Mechanistic Modeling and Early-Warning Indicators of Physiological State Transitions**. Các chủ đề nền gồm Nonlinear Dynamical Systems, Complex Systems, Dynamical Characterization, Early-Warning Signals, Detection và Prediction. Ưu tiên hiện tại là Critical Transitions, Tipping Theory, B-tipping, N-tipping, R-tipping và interacting mechanisms. Extreme Event Research và Physiological Research sẽ được mở rộng theo các paper được chỉ định.

Mỗi hồ sơ phục vụ học lý thuyết, trích xuất phương pháp, đánh giá bằng chứng, so sánh giữa các paper, phát triển câu hỏi nghiên cứu và viết luận án. Trong một lần xử lý, giới hạn công việc vào paper được chỉ định. Dành cross-paper synthesis hoặc systematic review hoàn chỉnh cho một yêu cầu riêng. Khi yêu cầu chỉ là khởi tạo knowledge base, tạo cấu trúc và master prompt, rồi dừng trước bước phân tích paper.

Thư mục chứa tài liệu này là gốc của knowledge base. Thư mục cha của nó là gốc workspace dùng để ghi `pdf_path` tương đối.

```text
Literature_Knowledge_Base/
├── PAPER_REVIEW_PROMPT.md
├── Review_Articles/
└── Original_Research_Articles/
```

Giữ nguyên PDF gốc và các hồ sơ ngoài phạm vi yêu cầu. Dùng hai thư mục article ở trên cho bản ghi chính thức và tạo thư mục còn thiếu khi cần. Phần tra cứu, kiểm tra hoặc trích xuất tạm thời thuộc phiên làm việc. Chỉ lưu hồ sơ được yêu cầu trong knowledge base.

## 2. Workflow cho mỗi paper

1. Đọc toàn bộ master prompt. Xác định PDF từ đường dẫn được giao và kiểm tra các tài liệu bổ sung đã được cung cấp.
2. Đọc full text trong phạm vi truy cập. Kiểm tra nội dung lý thuyết, Methods, Results, Discussion, hình, bảng, phụ lục và các reference liên quan đến claim chính.
3. Xác minh bibliographic metadata từ PDF. Dùng nguồn chính thức như trang publisher, DOI hoặc nơi lưu trữ chính thức khi cần xác minh trường còn thiếu hay mâu thuẫn. Ghi rõ nguồn và phiên bản nếu điều đó ảnh hưởng cách đọc.
4. Phân loại article type theo Mục 3. Ghi lý do, độ chắc chắn và thư mục đích. Với hybrid, xác định đóng góp chính và phần original evidence.
5. Kiểm tra cả hai thư mục để tìm bản ghi hiện có theo Mục 10. Xác định một đường dẫn lưu trước khi soạn.
6. Dùng cấu trúc phù hợp ở Mục 5 hoặc Mục 6. Trích xuất theoretical knowledge, methodology, results, evidence, limitations và tài liệu cần đọc tiếp. Dùng Mục 7 cho bảng dữ liệu chung và Mục 8 để kiểm tra mọi claim quan trọng.
7. Tích hợp ghi chú cá nhân đã được cung cấp theo Mục 11. Khi cập nhật, đối chiếu nội dung mới với hồ sơ cũ, bảo toàn các phần còn giá trị và ghi Revision History.
8. Kiểm tra chất lượng theo Mục 12. Lưu đúng một hồ sơ UTF-8 hoặc cập nhật hồ sơ hiện có. Kiểm tra lại đường dẫn và nội dung đã lưu rồi báo cáo theo Mục 13.

Nếu chỉ truy cập được abstract hoặc một phần PDF, ghi phạm vi và thiếu sót cụ thể. Chỉ lưu phần có căn cứ dưới trạng thái `draft` nếu vẫn có ích. Khi không đủ căn cứ để phân loại hoặc lập hồ sơ, báo trở ngại thay vì tạo một bản đầy đủ dựa trên abstract.

## 3. Phân loại article type

Dùng nhãn do publisher công bố nếu có, cùng với objective, cấu trúc, methodology, tính chất đóng góp và nguồn gốc của evidence trong full text. Xác định câu hỏi chính được trả lời bằng cách tổng hợp nghiên cứu đã có, bằng proof hoặc dữ liệu mới, hay bằng cả hai. Title và abstract chỉ giúp định hướng đọc.

| Article type | Bằng chứng để phân loại | Thư mục đích |
|---|---|---|
| `review` | Đóng góp chính là tổng hợp, hệ thống hóa, đánh giá hoặc giải thích kiến thức đã có. Evidence chủ yếu đến từ các nghiên cứu được trích dẫn. Bao gồm narrative, systematic, scoping và tutorial review, scientific overview và review-oriented perspective. | `Review_Articles/` |
| `original_research` | Đóng góp chính là kết quả nguyên gốc như mathematical framework, proof, analytical result, mô hình mới hoặc sửa đổi có mục đích, computational method, numerical experiment, thí nghiệm, phân tích dữ liệu mới hoặc application-driven modeling. Một paper có thể dùng dữ liệu hoặc mô hình sẵn có để tạo ra kết quả original. | `Original_Research_Articles/` |
| `hybrid` | Bài có phần tổng hợp tài liệu đáng kể và có các đóng góp lý thuyết, số hoặc thực nghiệm riêng có thể xác định. Phân biệt original findings với findings do bài tóm tắt lại. | Chọn một trong hai thư mục theo primary contribution và ghi lý do. |

Đối với hybrid, dùng cấu trúc của nhóm đóng góp chính và bổ sung các tiểu mục thích hợp của nhóm còn lại. Ghi rõ phần nào là literature synthesis, phần nào tạo original evidence và mục nào của paper hỗ trợ lựa chọn. Lưu chung trong một hồ sơ Markdown.

Khi phân loại chưa chắc chắn, dùng cách phân loại được full text hỗ trợ tốt nhất. Ghi `classification_confidence` và chỉ rõ căn cứ, thông tin còn thiếu hoặc lý do publisher label khác knowledge-base classification. Chỉ điền `publisher_article_type` khi xác minh được nhãn chính thức.

## 4. YAML Front Matter chung

Đặt khối YAML này ở đầu mọi hồ sơ. Giữ nguyên tên và thứ tự trường để hỗ trợ trích xuất có hệ thống.

```yaml
---
schema_version: "1.0"

paper_id: null
title: null
authors: []
year: null
journal: null
volume: null
issue: null
pages: null
doi: null
url: null
pdf_path: null

publisher_article_type: null
article_type: null
article_subtypes: []
classification_reason: null
classification_confidence: null

research_group: null
research_topics: []
application_domains: []
phenomena: []
tipping_mechanisms: []
theoretical_concepts: []
dynamical_models: []
research_methods: []

evidence_types: []
evidence_origin: []

reading_status: unknown
reading_depth: unknown
note_status: draft
source_review_scope: null
human_verified: false

date_first_read: null
date_reviewed: null
last_updated: null

discovery_source: null
inclusion_reason: null

code_url: null
data_url: null
supplementary_materials: []
correction_or_erratum: null

tags: []
---
```

### Quy tắc điền metadata

- `title` giữ exact English title đã xuất bản, kể cả subtitle. `authors` giữ đủ tên, dấu và thứ tự theo nguồn. `year` dùng năm của ấn bản được tổng hợp. Nếu ngày online-first và năm của số tạp chí khác nhau, ghi rõ sự khác biệt trong nội dung khi hữu ích. Xác minh DOI, tác giả, năm và tên tạp chí.
- `paper_id` là citation key ổn định, ưu tiên giống tên file bỏ đuôi `.md`. Ghi `doi` dưới dạng DOI thuần và `url` chỉ khi URL đã được xác minh. Giữ volume, issue và pages dưới dạng chuỗi nếu có chữ, khoảng trang hoặc article number. Giữ nguyên article number theo metadata nguồn.
- `pdf_path` ưu tiên đường dẫn tương đối từ gốc workspace, ví dụ `paper/ten-tep.pdf`. Dùng đường dẫn tuyệt đối khi PDF ở ngoài workspace và đã biết vị trí. `supplementary_materials` là danh sách đường dẫn hoặc URL đã xác minh. Ghi trong nội dung tài liệu nào thực sự đã đọc. `correction_or_erratum` là tham chiếu ngắn đã xác minh, kèm phần bị ảnh hưởng trong nội dung.
- `article_subtypes` là các nhãn mô tả thiết kế như `narrative-review`, `systematic-review`, `theoretical`, `computational`, `experimental` hoặc `observational`. `classification_reason` nêu mục tiêu, loại đóng góp, nguồn evidence và lý do chọn thư mục nếu là hybrid. `classification_confidence` dùng `high`, `medium` hoặc `low` theo mức độ đầy đủ và nhất quán của căn cứ.
- `source_review_scope` mô tả ngắn phần đã đọc, appendices hoặc supplementary đã kiểm tra và phần còn thiếu. Trạng thái đọc cá nhân dùng `unknown` nếu người dùng chưa cung cấp thông tin. Việc Codex kiểm tra paper chỉ cập nhật phạm vi nguồn và trạng thái hồ sơ. `human_verified` dùng `true` khi người dùng trực tiếp xác nhận đã kiểm tra hồ sơ.
- Ghi ngày ISO `YYYY-MM-DD`, ưu tiên đặt trong dấu nháy để giữ kiểu chuỗi. `date_first_read` chỉ điền theo thông tin của người dùng. `date_reviewed` ghi ngày thực hiện rà soát nguồn. `last_updated` ghi ngày thực sự sửa hồ sơ. Ghi `discovery_source` theo nguồn phát hiện paper nếu biết và `inclusion_reason` theo sự liên quan có thể giải thích.
- Dùng `null` cho trường scalar còn thiếu và `[]` cho danh sách rỗng hoặc chưa biết. Dùng kiểu YAML nhất quán và trích dẫn chuỗi có ký tự đặc biệt khi cần. Dùng nhãn ngắn, thống nhất. Chỉ gắn tags hoặc chủ đề đủ liên quan đến nội dung thực tế.

### Controlled vocabulary

| Trường | Giá trị |
|---|---|
| `article_type` | `review`, `original_research`, `hybrid` |
| `research_group` | `methodological`, `physiological`, `both` |
| `research_topics` | `critical-transitions`, `tipping-theory`, `extreme-events`, `nonlinear-dynamics`, `nonlinear-time-series-analysis`, `mechanistic-modeling`, `dynamical-characterization`, `early-warning-signals`, `detection`, `prediction`, `physiological-state-transitions`. Dùng các nhãn thích hợp và bổ sung nhãn nhất quán khi cần. |
| `tipping_mechanisms` | `B-tipping`, `N-tipping`, `R-tipping`, `B-N-interaction`, `B-R-interaction`, `N-R-interaction`, `B-N-R-interaction`, `unspecified`. Dùng `unspecified` khi bài có đề cập tipping nhưng cơ chế chưa rõ. |
| `evidence_types` | `mathematical-proof`, `analytical-result`, `numerical-simulation`, `computational-validation`, `controlled-experiment`, `observational-evidence`, `statistical-inference`, `literature-synthesis` |
| `evidence_origin` | `original`, `secondary` |
| `reading_status` | `unknown`, `unread`, `partial`, `completed` |
| `reading_depth` | `unknown`, `overview`, `selective`, `detailed` |
| `note_status` | `draft`, `source-checked`, `human-reviewed` |

Dùng `methodological` khi đóng góp trọng tâm là lý thuyết, phương pháp hoặc modeling, `physiological` khi trọng tâm là câu hỏi và bằng chứng sinh lý, và `both` khi cả hai là đóng góp trọng tâm. Dùng `source-checked` sau khi đã đối chiếu các claim trọng yếu với nguồn. Dùng `human-reviewed` theo xác nhận của người dùng.

Sau YAML, tạo H1 theo mẫu `# Author et al. (Year) — Exact Paper Title`. Dùng họ tác giả hoặc dạng trích dẫn phù hợp với số tác giả. Dùng đúng các heading H2 có số thứ tự và `## Revision History` trong cấu trúc được chọn. Các tiểu mục linh hoạt theo nội dung paper.

## 5. Cấu trúc cho Review Article

### 01. Research Overview

Tóm tắt điều cần biết, mục đích, phạm vi và mạch lập luận của review. Trình bày các thông điệp có vai trò định hướng cho phần còn lại.

### 02. Scientific Background and Motivation

Nêu quá trình phát triển, tình hình nghiên cứu vào thời điểm công bố, vấn đề khoa học chính, lý do tác giả thực hiện review và giới hạn kiến thức lúc đó.

### 03. Review Methodology

Nêu loại review, nguồn tư liệu, search strategy, tiêu chí chọn và loại, cách sàng lọc tài liệu, classification framework, synthesis methodology và phạm vi bao phủ. Chỉ ghi phương pháp tác giả báo cáo. Với narrative review thiếu thông tin về chiến lược tìm kiếm, ghi `Not reported` cho trường đó.

### 04. Theoretical Foundations

Ghi các khái niệm, định nghĩa, phân loại, framework và diễn giải động lực. Giữ các phương trình và giả định có giá trị sử dụng lại. Nêu điều kiện áp dụng và giới hạn.

### 05. Scientific Knowledge Synthesis

Tổ chức theo các chủ đề thật sự có trong bài. Với Critical Transitions, các chủ đề có thể là B-, N-, R-tipping, cơ chế tương tác, attractor dynamics, stability, resilience, EWS, detection và prediction. Mỗi chủ đề nêu luận điểm, bằng chứng và điều kiện hoặc tranh luận liên quan.

### 06. Methodological Landscape

Tổng hợp mô hình cùng các hướng analytical, computational, experimental và empirical. Nếu có nhiều phương pháp để đối chiếu, dùng bảng sau.

| Approach | Scientific purpose | Main assumptions | Strengths | Limitations | Primary reference |
|---|---|---|---|---|---|

### 07. Scientific Evidence and Citation Network

| Scientific claim | Supporting evidence | Primary reference | Evidence type | Source location in review |
|---|---|---|---|---|

Ghi rõ kết luận tổng hợp của review authors, kết quả mà review dẫn từ primary studies và original results nếu bài là hybrid. Đánh dấu primary reference theo tình trạng đã đọc trực tiếp hay chỉ biết qua review. Một bản tổng hợp lại cùng dữ liệu là secondary evidence, dùng chung nguồn với nghiên cứu gốc.

### 08. Research Gaps and Open Problems

Nêu kiến thức đã có căn cứ, vấn đề chưa giải quyết, kết quả mâu thuẫn, khoảng trống do tác giả nêu và hướng họ đề xuất. Gắn nguồn và mức chắc chắn cho từng vấn đề có ý nghĩa.

### 09. Critical Evaluation

Đánh giá phạm vi tài liệu, chất lượng evidence, selection bias, khả năng khái quát, điểm mạnh và hạn chế. Đánh dấu phần do AI đánh giá và phân biệt với limitations tác giả tự báo cáo.

### 10. Scientific and Methodological Insights

Rút ra theoretical, dynamical, methodological và modeling insights có thể tái sử dụng. Giải thích lý do lựa chọn phương pháp hoặc cách đặt vấn đề khi paper cung cấp đủ căn cứ.

### 11. Relevance to My Research

Nêu các lý thuyết, phương pháp và chiến lược modeling có thể chuyển giao, ứng dụng sinh lý tiềm năng, câu hỏi và khoảng trống ứng viên, yêu cầu dữ liệu và tính khả thi. Gắn nhãn cho suy luận và điều kiện cần kiểm tra.

### 12. Literature Connections and Future Reading

Chọn foundational, original, review hoặc contrasting references có giá trị. Ghi exact title, authors, year và lý do đọc nếu xác minh được. Ghi rõ tình trạng đọc nguồn trực tiếp.

### 13. Systematic Data Extraction

Chèn bảng chung ở Mục 7. Tóm tắt ở cấp paper, thêm bảng theo model hoặc scenario khi các giả định khác nhau có ý nghĩa.

### 14. Personal Research Notes

Áp dụng Mục 11. Nếu chưa có nội dung người dùng cung cấp, ghi `Awaiting personal research notes.`

### Revision History

Ghi ngày ISO và thay đổi thực tế trong lần tạo hoặc cập nhật theo Mục 10.

## 6. Cấu trúc cho Original Research Article

### 01. Research Overview

Tóm tắt câu hỏi, cách tiếp cận, kết quả chính, scientific narrative và phân loại nghiên cứu. Nêu rõ evidence nào tác giả trực tiếp tạo ra.

### 02. Background and Motivation

Đặt bài trong bối cảnh thời điểm công bố. Nêu giới hạn của approaches trước đó, động cơ nghiên cứu và khoảng trống do tác giả chỉ ra.

### 03. Research Problem and Contributions

Nêu research problem, questions, hypotheses, objectives và các đóng góp scientific, theoretical, methodological thực sự có trong bài. Nếu tái cấu trúc câu hỏi nghiên cứu từ nội dung, ghi `AI-derived interpretation` và nêu đoạn nguồn.

### 04. Theoretical Foundations

Giải thích khái niệm, định nghĩa, mathematical formulation, động lực, giả định, phạm vi áp dụng và kiến thức tiền đề. Ưu tiên trực giác rồi trình bày các quan hệ toán có thể sử dụng lại.

### 05. Research Methodology

Ưu tiên mục này với original methodological research. Giữ các tiểu mục có ích và dùng trạng thái thiếu thông tin ở Mục 8 khi một chi tiết quan trọng chưa xác định được.

#### 5.1. Overall Research Workflow

Mô tả từng bước thực tế, theo trình tự từ câu hỏi hoặc dữ liệu đầu vào đến phân tích, kiểm chứng và kết quả.

#### 5.2. Base Model or Dataset

Với modeling, ghi nguồn mô hình, lý do chọn, governing equations, state variables, control parameters, observables, intrinsic dynamics, equilibria, attractors, stability và bifurcation structure. Với empirical research, ghi nguồn dataset, population hoặc hệ thí nghiệm, acquisition, cỡ mẫu, tiêu chí chọn và loại, đặc tính tín hiệu, preprocessing và observables. Xác định đơn vị phân tích như người, đêm hoặc trajectory nếu có.

#### 5.3. Model Assumptions

Nêu giả định, giản lược, điều kiện ban đầu và phạm vi hợp lệ khi áp dụng. Chỉ rõ giả định nào tác giả nêu và giả định nào được suy ra từ cách thiết lập.

#### 5.4. Model Construction and Modification

| Component | Original structure | Modification | Scientific purpose | Source |
|---|---|---|---|---|

Chỉ rõ thành phần kế thừa, thành phần mới và thành phần thay đổi, lý do và câu hỏi được phục vụ. Gọi tên riêng việc sửa governing equations, thay tham số, thiết kế forcing hoặc thay điều kiện thí nghiệm.

#### 5.5. Research and Experimental Design

Ghi initial conditions, tham số và ranges, external forcing và profiles, noise, scenarios, thiết lập mô phỏng, control, baseline và sensitivity analysis theo thông tin được báo cáo. Nêu điều kiện tương ứng với từng so sánh.

#### 5.6. Transition Definition and Criteria

Nêu định nghĩa operational, cơ chế được khảo sát, criterion, tipping threshold, cách nhận diện thời điểm chuyển trạng thái và ground truth hoặc reference event. Dùng nhãn riêng cho ngưỡng lý thuyết, ngưỡng operational, thời điểm từ model fit và thời điểm quan sát.

#### 5.7. Mechanism Investigation

Giải thích tác giả khảo sát cơ chế bằng chứng minh, phân tích ổn định, thí nghiệm đối chứng, mô phỏng hoặc dữ liệu như thế nào. Phân biệt B-tipping, N-tipping, R-tipping, cơ chế tương tác và các cơ chế động lực khác theo evidence. Nếu chỉ có giả thuyết hoặc transition chưa phân loại được, ghi trạng thái đó.

#### 5.8. Mathematical and Computational Methods

| Method | Scientific purpose | Implementation logic | Assumptions | Source |
|---|---|---|---|---|

Với mỗi phép toán quan trọng, nêu đại lượng cần tìm, lý do, cách thực hiện và câu hỏi khoa học mà kết quả giúp trả lời.

#### 5.9. Data Analysis, Detection and Prediction

Ghi signal processing, feature extraction, dynamical representation, thống kê, EWS, detection và prediction khi có. Nêu training, testing, baselines, metrics, false positives và false negatives. Phân biệt ước lượng trạng thái hiện tại, phát hiện sự kiện và dự báo phía trước. Ghi dữ liệu nào có sẵn tại thời điểm mô phỏng dự báo, điều kiện pseudo-real-time hoặc prospective, và mốc tham chiếu của lead time.

#### 5.10. Validation Strategy

Phân biệt mathematical demonstration, analytical verification, numerical verification, controlled experimental validation, empirical evidence và statistical inference. Nêu tiêu chí thành công, điều kiện kiểm định và phạm vi mà kết quả hỗ trợ.

#### 5.11. Reproducibility

Ghi code, dữ liệu, tham số, numerical methods, phần mềm, chi tiết triển khai, thông tin còn thiếu và reproduction status. Chỉ ghi trạng thái đã tái lập khi thực sự chạy và kiểm tra kết quả.

### 06. Results and Scientific Evidence

#### Main Results

Tổ chức kết quả theo research questions. Nêu kèm điều kiện và nguồn cho những finding quan trọng.

#### Original Figure and Table Analysis

Với hình hoặc bảng chính, ghi số, mục đích, điều kiện, biến, tham số, kết quả quan sát, diễn giải động lực, kết luận được hỗ trợ và vị trí nguồn. Đối chiếu bản hiển thị gốc, trục, đơn vị, legend và caption trong PDF. Nếu chỉ cần chỉ dẫn để xem lại, ghi tham chiếu hình hoặc bảng ngay trong hồ sơ.

#### Quantitative Results

| Result | Value | Unit | Conditions | Source |
|---|---|---|---|---|

#### Claim–Evidence Mapping

| Scientific claim | Supporting evidence | Evidence type | Evidence origin | Source location |
|---|---|---|---|---|

#### Scope of Mechanism Verification

Nêu cơ chế đã được chứng minh bằng toán, minh họa bằng mô phỏng, hỗ trợ bằng thí nghiệm hoặc suy ra từ quan sát. Ghi cơ chế thay thế còn khả dĩ và cơ chế nằm ngoài phạm vi paper.

### 07. Discussion and Authors' Limitations

Ghi cách tác giả diễn giải kết quả, limitations họ thừa nhận, phạm vi kết luận và future work họ đề xuất.

### 08. Critical Evaluation

Đánh dấu các nhận định do AI phát triển. Đánh giá điểm mạnh, model assumptions, giới hạn dữ liệu, evidence quality, alternative explanations, robustness, generalizability và reproducibility. Chỉ ra căn cứ và điều kiện cho các nhận định quan trọng.

### 09. Scientific and Methodological Insights

Giải thích kết quả lý thuyết hoặc động lực đáng nhớ và phương pháp nghiên cứu hoặc tính toán có thể tái sử dụng. Chú ý lựa chọn mô hình, kiểm tra cơ chế hoặc cách thiết kế so sánh có giá trị cho bài toán khác.

### 10. Relevance to My Research

Nêu transferable theories, models và methodologies, ứng dụng sinh lý tiềm năng, khoảng trống và câu hỏi ứng viên, khó khăn toán học, tính toán và yêu cầu dữ liệu. Phân biệt evidence của bài với liên hệ do AI đề xuất.

### 11. Literature Connections

Ghi foundational papers, related work, methodological extensions và contrasting evidence đáng đọc. Xác minh title, authors, year khi có thể. Nếu chỉ biết qua references của paper, ghi rõ tình trạng đó.

### 12. Future Investigation

Nêu câu hỏi còn mở, khái niệm cần xem lại, model để tái lập, method để triển khai và tài liệu cần đọc thêm. Ghi rõ phần do tác giả đề xuất và phần do AI gợi ý.

### 13. Systematic Data Extraction

Chèn bảng chung ở Mục 7. Dùng thêm bảng theo model hoặc scenario nếu nhiều kết quả phụ thuộc vào thiết lập khác nhau.

### 14. Personal Research Notes

Áp dụng Mục 11. Nếu chưa có nội dung người dùng cung cấp, ghi `Awaiting personal research notes.`

### Revision History

Ghi ngày ISO và thay đổi thực tế trong lần tạo hoặc cập nhật theo Mục 10.

## 7. Bảng Systematic Data Extraction chung

Dùng đúng các hàng này trong mọi hồ sơ, giữ thứ tự để dễ so sánh về sau. Ghi ngắn gọn và trỏ đến vị trí nguồn. Đối với điều kiện hoặc cơ chế khác nhau, dùng hàng mở rộng hoặc một bảng bổ sung ở cấp model/scenario và giữ nguyên bảng cấp paper. Gắn nguồn gốc evidence theo từng kết quả nếu hồ sơ có cả original và secondary evidence.

| Extraction field | Extracted information | Source location |
|---|---|---|
| Article type | | |
| Study design | | |
| Research problem | | |
| Research objectives | | |
| Application domain | | |
| Investigated phenomenon | | |
| Tipping mechanism | | |
| Mechanism identification status | | |
| Theoretical framework | | |
| Dynamical model | | |
| Model origin | | |
| Model modifications | | |
| State variables | | |
| Observable variables | | |
| Attractor type | | |
| Control parameters | | |
| External forcing | | |
| Stochastic noise | | |
| Transition definition | | |
| Transition criterion | | |
| Analysis methodology | | |
| EWS / Predictors | | |
| Validation strategy | | |
| Evidence type | | |
| Evidence origin | | |
| Main scientific findings | | |
| Main quantitative results | | |
| Authors' limitations | | |
| Alternative explanations | | |
| Author-identified research gaps | | |
| Code availability | | |
| Data availability | | |
| Reproduction status | | |
| Research relevance | | |

Dùng trạng thái ở Mục 8 khi thiếu thông tin. Trỏ đến phần đã kiểm tra nếu ghi `Not reported`. Ghi nguồn trực tiếp hoặc secondary source theo tình trạng truy cập. Dùng personal insights trong phần ghi chú hoặc liên hệ nghiên cứu, tách khỏi evidence khoa học trong bảng.

## 8. Đối chiếu nguồn và cách viết

### Nguồn và khả năng truy xuất

- PDF gốc được giao là primary source cho hồ sơ. Đọc các phần liên quan trong Abstract, Introduction, theory, Methods, Results, Discussion, figure captions, bảng, appendices và references. Ghi rõ phần nào là supplemental material, preprint, bản xuất bản hoặc correction nếu có.
- Gắn vị trí cho claim quan trọng, ví dụ `§2.1`, `published p. 1178`, `PDF p. 6`, `Eq. (2.4)`, `Fig. 3(b)`, `Table 1` hoặc `Appendix A`. Phân biệt số trang in của bài với trang đếm từ đầu PDF. Dùng đúng số và định danh xuất hiện trong nguồn.
- Giữ dấu, số mũ, đơn vị, ký hiệu, variables, parameters và giả định. Dùng LaTeX math trong Markdown. Kiểm tra trang render nếu text extraction làm sai phương trình. Khi có correction hoặc erratum đã biết, ghi phiên bản đang dùng, phạm vi sửa và vị trí đối chiếu. Trình bày điểm mâu thuẫn như một vấn đề cần xác minh.
- Với số liệu, ghi cohort hoặc sample, đơn vị, thời điểm, setting, thống kê báo cáo, mẫu số và điều kiện loại mẫu khi ảnh hưởng cách hiểu. Trình bày kết quả dưới từng điều kiện thay vì gộp các scenario khác nhau.
- Dùng nguồn chính thức hoặc tài liệu thực tế đã cung cấp để xác minh code, data, supplementary materials và publisher metadata. Phản ánh đúng tình trạng truy cập và xác minh trong hồ sơ.

### Phân biệt claim và evidence

Dùng nguồn gốc phù hợp cho từng nội dung. `Paper-reported` là nội dung, phép đo hoặc kết luận của chính bài. `Secondary evidence` là finding bài dẫn từ công trình khác. `AI-generated interpretation` là giải thích hay phê bình được phát triển khi soạn. `User-provided personal insight` là nhận định do người dùng thực sự đưa ra.

Nêu rõ claim là mathematical proof, analytical result, numerical experiment, controlled experiment, observation, statistical association hay hypothesis. Model fit cho biết mức phù hợp trong những điều kiện kiểm tra. Việc xác định cơ chế nhân quả cần bằng chứng thích hợp riêng. Phân biệt khả năng phát hiện hoặc ước lượng trạng thái với năng lực dự báo sự kiện trong tương lai. Nêu giới hạn suy luận đối với các cơ chế thay thế và thống kê tương quan. Ghi candidate research gaps như câu hỏi cần kiểm tra và chỉ gọi một khoảng trống là do tác giả xác định khi có nguồn.

### Trạng thái thiếu thông tin

| Trạng thái | Khi sử dụng |
|---|---|
| `Not reported` | Đã đọc phần thích hợp và nguồn không báo cáo chi tiết đó. |
| `Not applicable` | Trường không áp dụng cho thiết kế hoặc mục tiêu của paper. |
| `Not reviewed` | Nguồn có thể tồn tại nhưng chưa được đọc trong phiên. |
| `Not accessible` | Nguồn hoặc phần cần kiểm tra chưa truy cập được. |
| `To verify` | Có chi tiết thiếu căn cứ hoặc có mâu thuẫn cần xác minh. |
| `To revisit` | Có vấn đề lý thuyết hoặc phương pháp cần đọc lại khi phát triển hướng nghiên cứu. |

### Ngôn ngữ

Viết nội dung bằng tiếng Việt, giữ English scientific terminology và exact English title. Dùng giọng khoa học, trực diện, giải thích trực giác trước chi tiết toán. Giữ độ dài theo độ phức tạp và giá trị khoa học. Đặt nội dung chi tiết tại một mục chính và trỏ chéo khi cần. Diễn giải bằng lời của mình và dùng trích dẫn ngắn có nguồn khi thật sự cần. Giữ nguyên main section headings và bảng extraction chung. Mục tiêu là hồ sơ độc lập, có câu hỏi, cách làm, evidence và giới hạn đủ để xem lại sau này.

## 9. Trọng tâm nghiên cứu

Chọn trọng tâm phù hợp với nội dung thực tế của paper.

- **Critical Transitions và Tipping Theory** — Xem underlying mechanisms, bifurcation structures, attractor dynamics, stability/resilience, stochastic escape, non-autonomous dynamics, B-, N-, R-tipping, interacting mechanisms, critical thresholds, transition timing và mechanism-dependent EWS.
- **Dynamical Modeling** — Xem cách câu hỏi chi phối lựa chọn mô hình, nguồn mô hình nền, thay đổi phương trình hoặc tham số, thiết kế external forcing, controlled numerical experiments, mechanism investigation và model validation.
- **Physiological Research** — Xem physiological justification, latent state variables, observable biomedical signals, observation models, distinction giữa mechanistic và phenomenological modeling, empirical evaluation và transferability.
- **Extreme Events** — Xem định nghĩa sự kiện, statistical characterization, intermittency, attractor crisis, rare-event mechanisms và prediction methodology.

## 10. Đặt tên, tránh trùng và cập nhật

Đặt tên `FirstAuthor_Year_ShortTitle.md`. Ưu tiên tên ngắn, có thể đọc, bỏ ký tự không hợp lệ và độc lập với thứ tự đọc. Dùng short title cụ thể để phân biệt bài cùng tác giả đầu và năm. Có thể thêm một hậu tố dựa trên title nếu đích đã được một paper khác sử dụng. Giữ citation key ổn định qua các lần cập nhật nếu có thể.

Trước khi tạo, quét mọi hồ sơ Markdown trong cả hai thư mục. So sánh DOI đã chuẩn hóa bằng cách bỏ tiền tố `doi:` hoặc URL DOI, bỏ khoảng trắng thừa và bỏ qua khác biệt hoa thường. Sau đó so sánh exact title đã chuẩn hóa khoảng trắng, dấu câu và hoa thường. Đối chiếu authors và publication year để xác nhận cùng một công trình. Với khác biệt do online-first, preprint hoặc bản xuất bản, kiểm tra quan hệ phiên bản từ nguồn trước khi quyết định. Tên file hoặc độ giống title chỉ là dấu hiệu tìm ứng viên. Khi hai DOI đã xác minh khác nhau, cần căn cứ về quan hệ phiên bản trước khi gộp.

- **Paper mới** — Tạo đúng một file trong thư mục đích và ghi lần tạo ở Revision History.
- **Paper đã lưu** — Mở file hiện có, thêm hoặc sửa phần cần thiết, bảo toàn personal notes, manual edits và tham chiếu nguồn chính xác. Chỉ sửa lỗi factual có bằng chứng và ghi thay đổi. Giữ lại các thông tin có giá trị từ phiên bản trước.
- **Phân loại cần đổi** — Ghi lý do, kiểm tra đích và chuyển chính file đang cập nhật sang thư mục phù hợp sau khi kiểm tra khả năng bảo toàn nội dung. Kiểm tra chỉ có một bản ghi cho paper sau khi chuyển.
- **Đã có nhiều bản ghi hoặc nhận diện chưa chắc chắn** — Báo vị trí và loại xung đột. Ưu tiên bảo toàn cả dữ liệu hiện có trong khi làm rõ hồ sơ chính. Tránh ghi thêm hoặc hợp nhất phá hủy dữ liệu khi còn xung đột chưa giải quyết.

Trong `## Revision History`, ghi ngày ISO và thay đổi có thể kiểm tra, chẳng hạn nguồn bổ sung đã đọc, số liệu được sửa, phân loại được đổi hoặc personal notes được tích hợp. Giữ các mục lịch sử trước đó. Chỉ chỉnh sửa hồ sơ của paper đang được yêu cầu.

## 11. Tích hợp ghi chú cá nhân

Tích hợp reading notes, thảo luận, câu hỏi, diễn giải, derivations và critical evaluations khi chúng thực sự được người dùng cung cấp hoặc chỉ định. Giữ ý và chỉnh sửa thủ công của người dùng. Đặt nhãn nguồn cho các insight quan trọng và liên kết với mục khoa học thích hợp khi có ích. Chỉ coi các cuộc trao đổi trước đây là đầu vào khi nội dung hoặc tài liệu đã được cung cấp trong session đang làm việc.

Nếu đầu vào chỉ có PDF, thực hiện scientific extraction, giải thích và critical evaluation có nhãn phù hợp. Để `## 14. Personal Research Notes` với nội dung `Awaiting personal research notes.`

## 12. Kiểm tra trước khi lưu

- [ ] Article type, primary contribution, lý do phân loại và thư mục đích phù hợp với full text.
- [ ] Bibliographic metadata đã được xác minh trong phạm vi tiếp cận. Trường thiếu có giá trị rỗng, phạm vi đọc và các điểm cần xác minh đã được ghi.
- [ ] YAML hợp lệ, đủ trường và đúng controlled vocabulary. File dùng UTF-8, đúng main section headings và có bảng extraction chung đầy đủ.
- [ ] Claim chính có vị trí nguồn. Equations, dấu, số mũ, variables, số liệu, units, điều kiện, hình và bảng đã được đối chiếu.
- [ ] Proof, simulation, experiment, observation, statistical inference và hypothesis được nhận dạng đúng. Model fit, mechanism inference, detection và prediction được diễn giải theo evidence.
- [ ] Original evidence, secondary evidence, nhận định tác giả, AI interpretation và personal notes có nguồn gốc rõ ràng. Research gap và tình trạng đọc hoặc xác nhận cá nhân phản ánh đúng những gì đã biết.
- [ ] Đã kiểm tra trùng trong cả hai thư mục. Đã bảo toàn existing notes và manual edits, lưu một hồ sơ cho paper ở đúng thư mục và ghi Revision History.
- [ ] Đã đọc lại file sau khi lưu. Mọi hạn chế nguồn, mục cần kiểm tra thêm hoặc xung đột còn lại đều được nêu trong hồ sơ và báo cáo.

## 13. Báo cáo sau mỗi lần xử lý

Trả kết quả ngắn gồm exact paper title, article type và lý do, phạm vi đọc nguồn, đường dẫn hồ sơ, trạng thái tạo mới hay cập nhật, các chủ đề khoa học chính, phần cần xác minh, thông tin còn thiếu và trạng thái personal notes. Khi chưa thể lưu, nêu phần đã thực hiện và trở ngại cụ thể. Nếu đã lưu thành công, đưa đường dẫn file để người dùng xem nội dung.
