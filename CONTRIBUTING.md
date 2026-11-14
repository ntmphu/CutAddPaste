# Quy tắc làm việc nhóm

## Branch và review

- `main`: phiên bản dùng chung, chỉ gộp thay đổi qua Pull Request (PR).
- Branch dataset: `dataset/aiops`, `dataset/ucr`, `dataset/swat`, `dataset/wadi`.
- Trưởng nhóm dùng `evaluation`; thay đổi hạ tầng chung dùng `shared/<ten-viec>`.
- Mở PR vào `main`; trưởng nhóm review trước khi merge. Không tự merge PR của mình.
- Trước khi chạy thí nghiệm, đồng bộ code đã được duyệt và ghi commit chạy thực tế.
- Không force-push `main`, không commit trực tiếp vào `main` sau bước setup ban đầu.
- Thay đổi model, augmentation, trainer, loader hoặc metric dùng chung phải báo nhóm trong PR.
  Nêu dataset nào bị ảnh hưởng; không tự chỉnh để cải thiện riêng điểm dataset của mình.

Các quy tắc trên là thỏa thuận của nhóm. Muốn GitHub bắt buộc review thì trưởng nhóm
phải bật branch protection/ruleset; việc thêm tài liệu không tự bật bảo vệ trên server.

## Bắt đầu và gửi bài

Ví dụ cho AIOps (đổi branch theo phân công):

```bash
git fetch origin
git switch dataset/aiops
git merge origin/main
# Chỉnh sửa, kiểm tra, rồi thêm đúng các file cần thiết
git add conf/cut_add_paste/IOpsCompetition_Configs.py
git commit -m "fix: correct AIOps configuration"
git push -u origin dataset/aiops
```

Mở PR trên GitHub, điền mẫu có sẵn. Khi có conflict ở code chung, trao đổi với người
phụ trách trước khi giải quyết; không chọn toàn bộ một phía để bỏ qua conflict.

## Commit

Dùng `feat:`, `fix:`, `docs:`, `chore:` hoặc `experiment:` với mô tả rõ việc.
Ví dụ: `fix: correct UCR window labels`, `docs: record SWaT pilot results`.
Mỗi commit là một thay đổi có ý nghĩa. Không cần cài hook hay công cụ ép định dạng.

## File và artifacts

- Giữ cấu trúc gốc: `conf/cut_add_paste/`, `dataloader/`, `models/`, `utils/`.
- Dataset owners chủ yếu chỉnh config của mình; loader dùng chung cần review.
- Không đưa dữ liệu mới, checkpoint, dự đoán dung lượng lớn, token hay Kaggle API key lên Git.
- Lưu artifacts trên Kaggle/Drive phù hợp quyền truy cập; ghi link trong `EXPERIMENTS.md`.
- Hai ZIP dữ liệu đã được upstream track vẫn nằm trong lịch sử; `.gitignore` không xóa chúng.
  Không commit bản ZIP cập nhật. Không sửa lịch sử để xóa file trong đợt setup này.
- Giữ citation tác giả. Ghi rõ code tái sử dụng và phần nhóm tự viết trong báo cáo.

## Kiểm tra trước PR

Kiểm tra diff, chạy kiểm tra phù hợp với thay đổi và ghi bằng chứng trong PR.
Thay đổi tài liệu chỉ cần kiểm tra nội dung/link; thay đổi model, dữ liệu hoặc metric cần
kiểm tra nhỏ tương ứng. Không ghi “đã chạy GPU” nếu mới kiểm tra cú pháp hoặc CPU.
Không chạy full GPU khi split, metric hoặc pilot còn chưa được xác minh.
