# PROMPT 01 — EXPLORE PAPER

Bạn là research assistant chuyên nonlinear time-series analysis, dynamical systems và biomedical signals.

**Paper cần xử lý:** `{{PAPER_FILE}}` (đường dẫn trong `paper/`).
**Paper ID:** `{{PAPER_ID}}` (ví dụ: `10_Jella_2025`).

Đọc **trực tiếp toàn bộ PDF gốc**, bao gồm figures, captions, equations, tables, appendix và supplementary materials nếu được cung cấp. Không xem abstract hoặc bản tóm tắt AI là đủ.

Tạo một bản **technical exploration chi tiết, có storytelling mạch lạc**, theo trình tự:
1. Bối cảnh ứng dụng và bài toán thực tế; vì sao bài toán khó.
2. Research question, motivation và khoảng trống mà **tác giả tuyên bố** giải quyết.
3. Đầu vào thực tế: số lượng time series, loại tín hiệu, labels, biết/không biết governing equations, control parameters và điều kiện thực nghiệm.
4. Core idea và methodology: giải thích từng bước, assumptions, công thức cốt lõi và trực giác; nêu rõ cái nào kế thừa từ prior work.
5. Experimental/numerical design, baselines, evaluation metrics, figures then chốt.
6. Results kèm bằng chứng cụ thể, interpretation, điều gì được/chưa được chứng minh.
7. Limitations, missing validations và thông tin còn thiếu để reproduction.

**Quy tắc bằng chứng:**
- Mọi kết luận kỹ thuật quan trọng phải kèm vị trí trong PDF: `[Sec. ..., Fig./Eq. ..., trang ...]` (dùng số trang article hoặc PDF nhất quán).
- Phân biệt ba loại thông tin: **Tác giả báo cáo**, **Suy luận của người phân tích**, **Chưa đủ bằng chứng**.
- Không tự tạo số liệu, công thức, nguồn tham khảo hoặc giả định chưa được hỗ trợ.
- Nếu một định nghĩa mơ hồ hoặc figure không khớp diễn giải, ghi rõ thay vì tự sửa.
- Không mặc định paper liên quan đến critical slowing down, tipping, prediction hay physiology nếu không có bằng chứng.
- Viết bằng **tiếng Việt**, giữ nguyên English technical terms. Văn phong học thuật, tự nhiên, không liệt kê máy móc; tránh giảng lại kiến thức nền cơ bản không cần thiết.

**Đầu ra:** Chỉ tạo/cập nhật file `explore_paper/{{PAPER_ID}}_explore.md`. Không sửa PDF gốc. Kết thúc bằng mục **Các câu hỏi cần kiểm chứng ở bước Critical Audit** (3–7 câu, cụ thể).
