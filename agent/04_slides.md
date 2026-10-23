# PROMPT 04 — COMPACT RESEARCH SLIDES

**Nguồn:** `paper/{{PAPER_FILE_NAME}}`, `explore_paper/{{PAPER_ID}}_explore.md` (bao gồm mục Critical Audit), `sumarize_paper/{{PAPER_ID}}_discussion.md`.
**Paper ID:** `{{PAPER_ID}}`.
**Thư mục thiết kế:** `template/`.

Hãy tạo **2–3 slides** trình bày paper cho một buổi research meeting. Đọc và sử dụng template trong `template/` nếu có; bảo toàn design system, tỷ lệ và slide master của template. Nếu có nhiều template hoặc không có file phù hợp, chọn mẫu tương thích nhất theo tên/mục đích, hoặc dùng thiết kế khoa học tối giản, nhất quán; ghi lựa chọn trong phần ghi chú kết quả.

Storytelling ưu tiên:
- **Slide 1 — Problem & Motivation:** Bài toán, đối tượng/dữ liệu, tại sao cần phương pháp.
- **Slide 2 — Core Idea & Method:** Pipeline ngắn; 1 công thức hoặc 1 figure quan trọng nhất; nêu rõ assumptions quan trọng.
- **Slide 3 — Results, Novelty & Limitations:** 1–2 main findings, chính xác novelty, một limitation quyết định và một câu hỏi mở cho biomedical signals.

Quy tắc slide:
- **Tiếng Việt**, giữ English technical terms; mỗi slide chỉ có **một thông điệp chính**, ít chữ, ưu tiên diagram/figure đúng nguồn.
- Không được tự chế số liệu, tái vẽ figure gây hiểu sai, hoặc gắn figure của paper khác.
- Nếu dùng hình từ PDF, chú thích `Nguồn: [Author et al., year], Fig. ...`; nếu không thể trích hợp lệ, dùng sơ đồ nguyên lý do bạn dựng và ghi “Minh họa khái niệm”.
- Phân biệt detected/estimated critical point với prospective prediction; không tuyên bố method universal hoặc superior nếu không có benchmark.
- Cỡ chữ đủ đọc khi thuyết trình; không đưa cả đoạn summary lên slides.
- Speaker notes (nếu công cụ hỗ trợ): 2–4 câu nói tự nhiên cho mỗi slide, liên kết thành mạch 2–3 phút.

**Đầu ra:** `slide/{{PAPER_ID}}_slides.pptx` (định dạng trình chiếu chỉnh sửa được). Nếu công cụ không thể xuất PPTX, tạo `slide/{{PAPER_ID}}_slides.md` dạng slide-by-slide và nêu rõ giới hạn; không giả vờ đã tạo PPTX.

**Kiểm tra trước khi hoàn thành:** xem/render từng slide nếu môi trường cho phép để kiểm tra cắt chữ, tương phản, nguồn figure và sự nhất quán với research discussion. Không chỉnh sửa PDF gốc, exploration (bao gồm audit) hay summary trong bước này.
