# PROMPT 02 — CRITICAL AUDIT / NOVELTY CHECK

**Paper:** `paper/{{PAPER_FILE_NAME}}`
**Exploration:** `explore_paper/{{PAPER_ID}}_explore.md`
**Paper ID:** `{{PAPER_ID}}`

Đối chiếu bản exploration với **PDF gốc**, tập trung kiểm chứng các claims then chốt và xác định ranh giới thật sự của đóng góp khoa học. Không chỉ sửa văn phong; hãy phản biện như một reviewer cẩn trọng.

Trả lời rõ các vấn đề:
1. **Problem formulation / input contract:** Phương pháp thực sự nhận gì làm đầu vào? Một 1D time series hay nhiều recordings? Có cần known control parameter, labels, external interventions, governing model, assumptions về stationarity/bifurcation/transition type không?
2. **Novelty decomposition:** Phần nào là existing methods, application to new system, new phenomenon/interpretation, new representation, new algorithm, new evaluation, hoặc new empirical evidence? Chỉ ra tiền lệ mà **chính paper dẫn**; không gọi một điều là “đầu tiên” nếu không có căn cứ.
3. **Evidence-to-claim audit:** Mỗi main claim được hỗ trợ bởi figure/table/equation/experiment nào? Phân biệt observation, mechanism identification, retrospective detection, critical-point estimation, early warning và prospective prediction.
4. **Reliability:** Có baselines, negative controls, ablation, surrogate/null testing, sensitivity, noise robustness, uncertainty, temporal/out-of-sample validation, false alarms, missed events hay không? Mục nào không có thì ghi “không báo cáo”.
5. **Reproduction feasibility:** Cần dữ liệu, code, parameter values, thresholds, solvers, seeds, preprocessing và evaluation protocol gì? Thiếu gì?
6. **Transferability:** Nếu chuyển sang EEG/ECG/PPG hoặc biomedical time series nói chung, assumptions nào có thể không còn đúng? Chỉ coi đây là *potential implication*, không tuyên bố research gap đã được chứng minh.

**Đầu ra:** `explore_paper/{{PAPER_ID}}_audit.md`, gồm:
- **Executive verdict** (5–8 câu).
- **Claim–Evidence–Caveat table**: claim | bằng chứng chính xác trong PDF | giới hạn.
- **Novelty classification** và những phần đã tồn tại từ trước.
- **Assumptions & input contract**.
- **Unresolved questions / missing evidence**.
- **Decision:** Reference only / Deep read / Reproduction candidate, kèm lý do.

Quy tắc: Viết **tiếng Việt**, giữ English technical terms; đối chiếu PDF trực tiếp và gắn `[Sec./Fig./Eq./trang]` cho các claims quan trọng. Không sửa exploration một cách im lặng; nếu phát hiện lỗi, ghi rõ **“Cần sửa trong exploration”** cùng trích dẫn và cách sửa đề xuất. Không dùng web nếu không được yêu cầu; literature gap chỉ được ghi là giả thuyết cần systematic review.
