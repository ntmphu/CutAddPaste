# Sổ thí nghiệm

Chưa có kết quả chạy của nhóm. Không điền điểm paper vào cột kết quả thực nghiệm.
RPA F1 là metric chính; PA F1 là metric phụ. Dùng đơn vị phần trăm ở bảng tổng hợp.

## Mốc tham chiếu — Table 3, CutAddPaste

| Dataset | Paper RPA F1 (%) | Paper PA F1 (%) |
| --- | --- | --- |
| AIOps | 77.41 ± 0.96 | 84.68 ± 0.67 |
| UCR | 68.22 ± 1.55 | 81.95 ± 1.25 |
| SWaT | 45.86 ± 2.64 | 92.35 ± 1.03 |
| WADI | 26.58 ± 3.47 | 65.20 ± 10.15 |

Paper báo mean/std của 10 lần chạy; đây không phải khoảng sai số chấp nhận cho nhóm.
Nguồn: https://doi.org/10.1145/3637528.3671739

## Kết quả nhóm

| Run ID | Dataset / coverage | Commit | Config / seed | RPA F1 (%) | PA F1 (%) | Artifacts | Đã xác minh bởi |
| --- | --- | --- | --- | --- | --- | --- | --- |

## Mẫu ghi từng lần chạy — sao chép phần dưới

### Run ID: `<dataset>-<seed>-<ngay>-<lan>`

- Người chạy / ngày:
- Trạng thái: pilot / running / completed / failed / partial
- Dataset version, file manifest/hash, số series và cột:
- Split và số windows train/validation/test:
- Commit code đầy đủ (`git rev-parse HEAD`):
- Working tree sạch? Nếu không, lưu patch chính xác cùng artifacts:
- Config: đường dẫn và bản snapshot thực tế; CLI overrides:
- Seed:
- Lệnh chạy / link notebook và version Kaggle:
- Python, PyTorch và dependency versions:
- GPU, thời gian, peak memory (nếu đo được):
- Epoch đã chạy, checkpoint được chọn và tiêu chí chọn:
- Normalization, window labels, score alignment:
- Threshold / UCR selection; split cung cấp nhãn cho lựa chọn:
- Evaluator commit, RPA/PA và cách aggregation:
- Coverage đầy đủ hay subset? Series lỗi/bỏ qua:
- RPA F1 (%) / PA F1 (%):
- Sai lệch với paper và lý do:
- Link log / checkpoint / scores + labels + series IDs / config:
- Người kiểm tra, ngày kiểm tra, kết luận:

Đảm bảo thành viên khác truy cập được artifacts; không công khai dữ liệu hạn chế chia sẻ.
Giữ scores để tính lại metric không cần train lại. Khi tổng hợp nhiều seed,
ghi danh sách run IDs, số seed và quy ước tính standard deviation.
