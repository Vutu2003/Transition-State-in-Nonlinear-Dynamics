# PROMPT 03 — RESEARCH DISCUSSION SUMMARY

**Nguồn:** `paper/{{PAPER_FILE_NAME}}`, `explore_paper/{{PAPER_ID}}_explore.md` (bao gồm mục Critical Audit).
**Paper ID:** `{{PAPER_ID}}`.

Từ các nguồn trên, viết một **Research Discussion** ngắn gọn, tự nhiên, có thể dùng để giải thích paper cho giáo sư trong khoảng **3–5 phút**. Ưu tiên PDF gốc nếu các nguồn mâu thuẫn; không biến suy luận của AI thành kết luận tác giả.

Giữ đúng cấu trúc sau và tạo chuyển ý rõ ràng:

1. **Problem:** Bài toán thực tế/khoa học là gì?
2. **Motivation:** Tại sao existing approaches hoặc hiểu biết trước đây chưa đủ? Chỉ nhận định trong phạm vi bằng chứng paper.
3. **Methodology:** Input thật sự; core idea; pipeline và assumptions quan trọng nhất. Giải thích 1–2 công thức nếu cần.
4. **Results:** 2–4 kết quả định lượng/định tính có nguồn, không phóng đại.
5. **Discussion:** Các kết quả có nghĩa gì và không có nghĩa gì?
6. **Novelty:** Phân loại cụ thể: new concept / method extension / new algorithm / application / validation; đối chiếu với công cụ có sẵn.
7. **Limitations:** Giới hạn phương pháp, experimental design, inference và evaluation.
8. **Potential Gap for Biomedical Signals:** Một câu hỏi nghiên cứu khả thi cho EEG, ECG, PPG nói chung, gắn với limitation thật; ghi rõ **candidate research question, chưa phải established gap**.

Cuối file thêm:
- **Key takeaways:** đúng 3 gạch đầu dòng ngắn bằng tiếng Việt.
- **One-minute pitch:** một đoạn văn ngắn, nói tự nhiên, không đọc như bullet list.
- **Reading decision:** Reference only / Deep read / Reproduction candidate.

**Đầu ra:** `sumarize_paper/{{PAPER_ID}}_discussion.md` (giữ nguyên tên thư mục `sumarize_paper` như cấu trúc project, không tự đổi thành `summarize_paper`).

Yêu cầu: Tổng dung lượng phần Research Discussion khoảng **600–900 từ tiếng Việt**, không bắt buộc kéo dài paper ít novelty. Không giải thích toán cơ bản đã biết; giữ English technical terms; citation ngắn `[Fig./Sec./trang]` tại các kết quả quan trọng. Diễn đạt như một câu chuyện từ vấn đề đến đóng góp và giới hạn, không viết một danh sách facts rời rạc.
