# PROMPT 04 — RESEARCH SLIDES (Methodology-Centered, v3)

Đọc `sumarize_paper/{{PAPER_ID}}_discussion.md`, `explore_paper/{{PAPER_ID}}_explore.md` và PDF `paper/{{PAPER_FILE}}`. Quan sát thư mục `template/` và **dùng presentation template thực có sẵn** nếu phù hợp; giữ layout, fonts/colors và style nhất quán. Nếu không có template hoặc không thể sử dụng, tạo slide tối giản, chuyên nghiệp và nói rõ fallback. **Không tự bịa figures, metrics, hoặc kết quả**.

**Mục tiêu:** Tạo **2–3 slides** cho discussion với Prof, ít chữ, đủ để kể lại **Problem → methodological limitation → proposed change → evidence → novelty/limitations**. Nội dung tiếng Việt, giữ nguyên English technical terms. Ưu tiên correctness hơn hình thức.

## Storyboard khuyến nghị
- **Slide 1 — Problem & Methodological Motivation:** Problem, input–output và vì sao existing approach chưa đủ. Một visual/pipeline giản lược nếu hữu ích.
- **Slide 2 — Proposed Method & Evidence:** Nêu rõ cái gì borrowed/cái gì new; workflow hoặc equation trọng tâm; 1 figure/bảng kết quả then chốt từ paper với nguồn `Fig./Table/Section` rõ ràng.
- **Slide 3 — Novelty, Limitations & Research Implications:** 2–3 contributions có bằng chứng; 2 key limitations; 1 câu hỏi mở liên quan biomedical signals **được đánh dấu giả thuyết**.

Có thể chỉ dùng **2 slides** nếu paper thiên về reference/validation và không có đủ methodological novelty; không kéo giãn nội dung để đủ slide.

## Yêu cầu kỹ thuật/chất lượng
- Mỗi slide có 1 headline dạng kết luận, tối đa ~3–4 short bullets, tránh paragraph dài, ưu tiên typography dễ đọc.
- Figures trích từ paper phải chính xác, không vẽ lại làm thay đổi ý nghĩa; nếu không thể trích, tự tạo schematic được ghi rõ `Sơ đồ minh họa` và không giả lập dữ liệu.
- Cần phân biệt retrospective detection, critical-point identification và prospective prediction.
- Dùng journal/title/author/year ở footnote, và ghi nguồn figure ngay tại slide tương ứng.
- Kiểm tra overflow, legibility, missing symbols/font, citations, slide order. Tạo file `.pptx` editable; nếu template không edit được, dùng alternative phù hợp.
- Không chỉnh sửa Explore hoặc Research Discussion trong bước này; nếu phát hiện lỗi khoa học, báo riêng thay vì âm thầm chuyển lên slide.

## Output
- Lưu **duy nhất** `slide/{{PAPER_ID}}_slides.pptx` (ngoại trừ file tạm cần thiết, xóa sau khi hoàn thành).
- Nếu hệ thống hỗ trợ, render từng slide để kiểm tra visual quality trước khi bàn giao.
- Trả lời đường dẫn PPTX, số slides và một câu mô tả mạch trình bày.
