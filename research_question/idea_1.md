
# Research Idea: Sliding-Window Analysis of Dynamical State Transitions

**Status:** Candidate Research Question — Exploratory
**Research Type:** Foundational Methodological Study
**Future Application:** EEG / ECG / PPG

## 1. Research Motivation

Các nghiên cứu gần đây sử dụng nonlinear time-series measures để characterize dynamical transitions:

- **Jella et al. (2025):** Recurrence-based critical-point estimation.
- **Das et al. (2024):** Statistical complexity of extreme-event regimes.
- **Seralan et al. (2026):** Variance-based characterization of extreme-event transitions.

Các nghiên cứu chủ yếu sử dụng mathematical models với known control parameters. Metrics thường được tính trên dữ liệu ở từng parameter condition.

**Research Direction:** Khảo sát thông tin về dynamical state transitions có thể thu được khi một observation window trượt qua vùng chuyển tiếp.

## 2. Research Questions

**Main RQ:**

> How do sliding-window nonlinear time-series measures characterize dynamical state transitions, and how reliably can they detect the emergence of a new dynamical regime?

**Sub-RQs:**

- **RQ1 — Characterization:** NTSA metrics thay đổi như thế nào khi observation window đi qua transition?
- **RQ2 — Detectability:** Cần bao nhiêu thông tin từ state mới để phân biệt đáng tin cậy với state trước?
- **RQ3 — Generalizability:** Metric responses có nhất quán giữa các transition mechanisms không?
- **RQ4 — Robustness:** Window size, noise, sampling và transition speed ảnh hưởng như thế nào?

## 3. Core Methodological Idea

Với một known transition boundary giữa State A và State B:

- Sliding window có độ dài cố định W.
- k là số samples của State B nằm trong window.
- p_B = k/W là tỷ lệ dữ liệu thuộc State B.
- Q(p_B) biểu diễn response của một NTSA metric.

**Objective:** Khảo sát metric sensitivity, detection reliability và minimum detectable post-transition proportion.

Lưu ý: p_B là window-composition variable, **không phải physical control parameter hoặc critical point**.

## 4. Proposed Experimental Design

### Experiment A — Controlled Parameter Sweep

- Mô phỏng nonlinear dynamical systems tại các control parameter values khác nhau.
- Xác định regimes và transition mechanisms.
- Sử dụng kết quả làm baseline cho NTSA metrics.

### Experiment B — Dynamical Transition Trajectory

- Cho control parameter thay đổi theo thời gian: μ(t).
- Tạo continuous trajectories đi qua transition regions.
- Áp dụng sliding-window NTSA.
- Đánh giá metric evolution, detection delay và false alarms.

**Important:** Ghép hai stationary trajectories A/B không tương đương với một physical dynamical transition.

## 5. Candidate Systems and Measures

**Dynamical Models:**

- Brusselator — Period-doubling / interior crisis.
- Ikeda map hoặc forced Liénard — Interior crisis.
- Coupled Hindmarsh–Rose — Pomeau–Manneville intermittency.
- SQUID trimer — Quasiperiodic intermittency.

**Candidate Metrics:**

- Recurrence Quantification Analysis (RQA).
- Shannon entropy / statistical complexity.
- Mean Recurrence Time (MRT).
- Variance-based complexity measures.

## 6. Scientific Challenges

- Phân biệt intrinsic dynamical changes và window-mixing effects.
- Xác định operational ground truth cho transitions.
- Đánh giá sensitivity, specificity và detection delay.
- Kiểm tra window-size dependence và finite-sample bias.
- Không đồng nhất statistical change detection với critical-transition identification.
- Kiểm tra novelty so với sliding-window RQA, change-point detection và online dynamical monitoring.

## 7. Expected Contribution (Hypothesis)

Xây dựng bằng chứng định lượng về:

1. Thông tin dynamical transitions được phản ánh trong sliding-window NTSA metrics.
2. Giới hạn detectability theo window size và lượng dữ liệu hậu chuyển tiếp.
3. Sự khác biệt trong metric responses giữa các transition mechanisms.

**Current Position:** Research hypothesis, chưa phải validated method hoặc confirmed research gap.

## 8. Long-Term Direction

Foundational numerical validation → Methodological assessment → Potential applications to physiological state changes (EEG, ECG, PPG).

---

**Key Insight:**

> The research novelty may lie not in sliding-window analysis itself, but in systematically quantifying what dynamical transition information becomes detectable, when it becomes detectable, and under which conditions.
