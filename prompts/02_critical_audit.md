# PROMPT 02 — CRITICAL AUDIT (Same Explore Output, v3)

Đọc **cả PDF gốc** `paper/{{PAPER_FILE}}` và `explore_paper/{{PAPER_ID}}_explore.md`. Đóng vai methodological reviewer phản biện độc lập. **Không tạo file audit riêng.** Mọi chỉnh sửa và audit phải nằm trong **cùng file Explore**.

## Audit checklist (ưu tiên methodological novelty)
1. **Task identity:** Phương pháp thực sự nhận input gì và trả output gì? Nó là characterization, retrospective detection, parameter inference hay future prediction? Phải biết model equations, control parameter, state labels, intervention hoặc future observations không?
2. **Novelty decomposition:** Thành phần nào borrowed/adapted/new? So với **các prior methods được paper dẫn**, authors' novelty claim cụ thể là gì? Novel formulation, estimator, objective, feature, architecture, validation protocol, application hay conceptual interpretation? Nếu không đủ bằng chứng để tuyên bố first-of-kind, nói rõ.
3. **Mathematical validity:** Kiểm tra definitions, equations, assumptions, approximations, identifiability, statistical dependence và cách suy luận từ metric đến mechanism.
4. **Evidence strength:** Claim nào dựa vào theorem, simulation, controlled experiment, real-world data hay interpretation? Đánh giá baselines, ablations, sample sizes, ground truth, calibration, sensitivity, uncertainty, statistical tests, out-of-sample/generalization. Phân biệt `not reported` và `failed`.
5. **Claim–evidence mismatch:** Chỉ ra các khẳng định bị diễn giải quá mức (universality, robustness, causality, early warning, prediction lead time, identification of tipping mechanism, outperforming baseline...).
6. **Reproducibility:** Các yếu tố còn thiếu (data access, code, parameter values, thresholds, time windows, seeds, train/test split, solver, fitting objective); independent reproduction có khả thi không?
7. **Biomedical transferability:** Nếu áp dụng ECG/EEG/PPG, những assumptions/input cần thay đổi là gì? Đánh dấu là **hypothesis**, không tự tuyên bố literature gap hay clinical validity.

## Chỉnh sửa file
- Đối chiếu mọi nhận định quan trọng với PDF, dẫn page/section/equation/figure.
- **Sửa trực tiếp** các lỗi trong phần Explore; không giữ lại kết luận sai chỉ vì đã viết trước đó.
- Thay `## Critical Audit (chờ Prompt 02)` bằng `## Critical Audit` gồm 4 tiểu mục ngắn: `Verified strengths`, `Corrections / qualifications`, `Methodological limitations`, `Open questions`.
- Cuối audit thêm **Novelty verdict** (1–3 câu), phân loại `New method / Methodological extension / New application or validation / Conceptual contribution / Unclear` (có thể chọn nhiều loại), với bằng chứng.
- Bảo tồn các user notes nếu có; không tạo `*_audit.md` hay thay đổi output thư mục khác.

## Output
Cập nhật **duy nhất** `explore_paper/{{PAPER_ID}}_explore.md`; báo những corrections quan trọng nhất và đường dẫn file. Viết bằng tiếng Việt, giữ technical terms tiếng Anh.
