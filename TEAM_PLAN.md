# Kế hoạch tái lập CutAddPaste — 10 ngày

## Phạm vi đã thống nhất

Tái lập phương pháp CutAddPaste chính trên AIOps, UCR, SWaT và WADI;
so sánh RPA F1 và PA F1 với hàng CutAddPaste, Table 3 của paper.
Chạy đủ một seed mỗi dataset trước. Thêm seed nếu còn quota/thời gian.
Ablation, baseline khác và sensitivity sweep chưa nằm trong cam kết.
Tài nguyên: Kaggle T4 miễn phí; dự toán theo quota thực tế và thời gian pilot.

## Phân công — điền tên/GitHub trong buổi họp

| Vai trò | Người phụ trách | Branch | Bàn giao |
| --- | --- | --- | --- |
| AIOps | Chưa chốt | `dataset/aiops` | Đủ 29 series, config, log, checkpoint, scores và metric |
| UCR | Chưa chốt | `dataset/ucr` | Đủ 250 series; ghi rõ lựa chọn epoch và cách đánh giá |
| SWaT | Chưa chốt | `dataset/swat` | Preprocessing, config và kết quả đầy đủ |
| WADI | Chưa chốt | `dataset/wadi` | Xác minh cột đầu vào, preprocessing và kết quả đầy đủ |
| Evaluation / trưởng nhóm | @ntmphu | `evaluation` | Xác minh metric/protocol, tổng hợp, báo cáo và slide |
| Code model/training chung | Chọn một người trong 4 dataset owners | `shared/<ten-viec>` | Pipeline dùng chung, pilot và hướng dẫn chạy |

Trưởng nhóm không mặc định phải làm thay mọi dataset. Chốt người hỗ trợ/tiếp quản khi có
milestone bị trễ. Mỗi dataset owner nộp thêm mô tả cách làm và kết quả cho báo cáo.

## Mốc tiến độ

Ngày 1 là ngày nhóm thống nhất bắt đầu; chưa gán ngày lịch cho tới buổi họp.

| Hạn | Bằng chứng bắt buộc |
| --- | --- |
| Ngày 1 | Chốt tên, người giữ code chung, nguồn dữ liệu và yêu cầu tự reimplement của môn |
| Ngày 2 | Load được dữ liệu; thống kê split, cột, nhãn và số window; chốt protocol |
| Ngày 3 | Pilot end-to-end, scores lưu được, metric được kiểm tra, đo runtime/quota |
| Ngày 5 | Full run xong hoặc có tiến độ, checkpoint/resume và dự kiến hoàn tất |
| Ngày 7 | Đủ kết quả một seed cho cả 4 dataset và artifacts để trưởng nhóm kiểm tra |
| Ngày 8 | Sửa lỗi thiết yếu, khóa thí nghiệm; thêm seed chỉ khi đủ thời gian |
| Ngày 9–10 | Hoàn thiện báo cáo, slide, kiểm tra tái chạy và tập thuyết trình |

Mỗi ngày cập nhật: **Đã xong + link / Đang làm + dự kiến / Vướng gì**.
Trễ mốc phải báo ngay và bàn giao trạng thái đang có; không đợi đến hạn cuối.

## Protocol phải xác minh trước full run

- [ ] Chốt dùng lại source hay tự viết theo yêu cầu môn; ghi rõ phần đóng góp.
- [ ] Ghi version và danh sách file dataset; xác minh đủ series/cột.
- [ ] Chốt split, normalization fit trên phần nào, missing/constant values và window labels.
- [ ] So sánh cấu hình với Appendix B; mọi khác biệt paper/code phải ghi lại.
- [ ] AIOps giữ đúng cách sử dụng nhãn anomaly trong training.
- [ ] Xác minh UCR chọn epoch/early stopping và sample có score lớn nhất theo code tham chiếu.
- [ ] Xác minh nguồn nhãn để chọn threshold/checkpoint; công khai nếu dùng test labels.
- [ ] Kiểm tra RPA/PA bằng ví dụ nhỏ; thống nhất score/window alignment và aggregation.
- [ ] Chọn seed đầu chung (đề xuất `2`, chưa xem là đã chốt).
- [ ] Xác minh artifact/checkpoint và resume hoạt động; không giả định code gốc đã hỗ trợ đủ.

## Định nghĩa hoàn thành

Code đã review, config chính xác, commit và seed, counts/splits, log, checkpoint,
scores + labels + series IDs, link artifacts, RPA/PA qua evaluator chung, và danh sách sai lệch.
Không dùng screenshot điểm làm bằng chứng duy nhất. Một seed báo điểm đơn;
chỉ báo mean/std khi thực sự chạy nhiều seed và ghi số lần chạy.
