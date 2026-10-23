# PROMPT 03 — RESEARCH DISCUSSION (Methodology-Centered, v3)

Đọc PDF gốc `paper/{{PAPER_FILE}}` và bản đã kiểm chứng `explore_paper/{{PAPER_ID}}_explore.md`, đặc biệt phần **Critical Audit**. Nếu thiếu audit, ghi rõ điều đó và chỉ tổng hợp các điểm được PDF hỗ trợ, không tự coi file đã verified.

**Nhiệm vụ:** Viết một research note **tiếng Việt**, giữ English technical terms, đủ ngắn để nói chuyện với Prof trong khoảng **3–5 phút**, nhưng chính xác và có storytelling tự nhiên. Lấy câu hỏi **"Existing method thiếu gì → tác giả thay đổi phương pháp như thế nào → evidence chứng minh được điều gì?"** làm mạch xuyên suốt. Không biến output thành danh sách thuật ngữ hoặc một bài review dài.

## Cấu trúc cố định (8 mục)
1. **Problem:** Bài toán cụ thể; target output và observable/input thực tế.
2. **Motivation:** Tại sao prior approaches chưa đủ; chỉ dẫn đúng giới hạn mà paper thực sự nêu.
3. **Methodology:** Existing components vs newly proposed components; pipeline, 1–2 công thức quan trọng nếu thật sự cần, assumptions then chốt.
4. **Results:** 2–4 findings quan trọng nhất; figure/table/quantitative numbers và loại validation.
5. **Discussion:** Ý nghĩa động lực học/thống kê; paper chứng minh gì và không chứng minh gì.
6. **Novelty:** Phân loại novelty chính xác; nhấn mạnh cái mới là algorithm/formulation, methodological extension, interpretation, application hay validation; so với prior work mà paper có căn cứ.
7. **Limitations:** Ưu tiên input assumptions, mechanism assumptions, baseline comparison, reliability, generalization, prospective performance.
8. **Potential Gap / Research Implications:** Những câu hỏi còn mở, hướng liên hệ EEG/ECG/PPG nói chung; **không gọi là established literature gap** nếu chưa review lĩnh vực liên quan.

## Kết thúc
- `### 3 Key Takeaways`: **đúng 3 gạch đầu dòng**, tiếng Việt, súc tích.
- `### Một phút trình bày với Prof`: một đoạn văn tự nhiên 120–180 từ, có đủ problem–method–result–novelty–limit.
- `### Methodological Fingerprint`: bảng 1 hàng hoặc key-value cực gọn với `Input, Known information, Output, Core method, Novel component, Evidence, Main assumption`.
- Gắn citations dạng `(Fig. X; Sec. Y)` khi nêu results/methods cụ thể; không đưa các claim chưa xác nhận thành facts.

## Output
- Chỉ tạo/cập nhật `sumarize_paper/{{PAPER_ID}}_discussion.md` (giữ nguyên chính tả thư mục `sumarize_paper`).
- Không sửa Explore, không tạo slides.
- Không bịa thiếu sót thành research gap; không thêm claims ngoài PDF nếu không được yêu cầu.
- Trả lời đường dẫn kết quả và một câu tóm tắt novelty.
