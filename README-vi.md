# MoneyPrinterTurbo – Phiên bản tiếng Việt

Công cụ tạo video ngắn bằng AI: từ chủ đề đến kịch bản, lời đọc, tư liệu, phụ đề, nhạc nền và video đầu ra. Có giao diện web, dòng lệnh và API.

Bản Việt hóa dành cho tài khoản GitHub **goldquocbao-cmd**. Phát triển từ [MoneyPrinterTurbo của harry0703](https://github.com/harry0703/MoneyPrinterTurbo), theo giấy phép MIT. Giữ nguyên thông tin tác giả và giấy phép gốc.

## Phạm vi Việt hóa

- Đủ **582/582 mục** trong danh mục dịch tiếng Anh tại phiên bản nguồn được ghim.
- Bổ sung 159 mục còn thiếu; Việt hóa hướng dẫn cấu hình mô hình, thông báo chi phí và mẫu âm thanh.
- Hiển thị hướng dẫn nhà cung cấp bằng tiếng Việt thay vì tự chuyển sang tiếng Anh.
- Mặc định giao diện `vi`, kịch bản `vi-VN`, giọng `vi-VN-HoaiMyNeural-Female`, phông `BeVietnamPro-Bold.ttf` có sẵn trong dự án.
- Giữ tên thương hiệu, mã mô hình, URL, tên khóa cấu hình và tham số API để ứng dụng hoạt động đúng.
- Tài liệu kỹ thuật, bình luận trong mã, thông báo thư viện bên ngoài và tài liệu gốc khác vẫn có thể chứa tiếng Anh hoặc tiếng Trung. 582 mục là mức bao phủ danh mục dịch, không phải cam kết mọi chuỗi chữ trong toàn bộ dự án đã được dịch.

## Cài đặt trên máy

Cần Git, Python 3.11 trở lên và FFmpeg trong PATH. Python 3.11 là lựa chọn khuyến nghị theo tài liệu nguồn.

Lấy bản Việt hóa rồi chuyển vào thư mục dự án:

```bash
git clone https://github.com/goldquocbao-cmd/MoneyPrinterTurbo-Vietnamese.git
cd MoneyPrinterTurbo-Vietnamese
```

```bash
python -m venv .venv
```

Kích hoạt môi trường:

```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# Linux hoặc macOS
source .venv/bin/activate
```

Cài thư viện và chạy giao diện:

```bash
python -m pip install -r requirements.txt
python -m streamlit run webui/Main.py --server.address=127.0.0.1 --server.port=8501
```

Mở **http://127.0.0.1:8501**. Nếu dùng `uv`, có thể thay bước cài thư viện bằng `uv sync --frozen`, rồi chạy `uv run streamlit run webui/Main.py --server.address=127.0.0.1`.

Ứng dụng tự tạo `config.toml` từ `config.example.toml` khi chạy lần đầu. Nếu đã có cấu hình cũ, đổi ngôn ngữ trong Cài đặt hoặc cập nhật các dòng thuộc `[ui]` trong `config.toml`; không thêm bảng `[ui]` trùng lặp:

```toml
[ui]
language = "vi"
video_language = "vi-VN"
voice_name = "vi-VN-HoaiMyNeural-Female"
font_name = "BeVietnamPro-Bold.ttf"
```

## Chạy bằng Docker

Cần Docker và Docker Compose:

```bash
docker compose up --build -d
```

Giao diện: **http://127.0.0.1:8501**. API: **http://127.0.0.1:8080/docs**. Cấu hình mẫu chỉ mở các cổng này trên máy cục bộ.

## Tạo video tiếng Việt đầu tiên

1. Trong **Cài đặt**, chọn nhà cung cấp mô hình ngôn ngữ và nhập khóa API, địa chỉ gốc, tên mô hình hợp lệ. Có thể dùng Ollama trên máy nếu đã cài mô hình phù hợp.
2. Chọn nguồn tư liệu: video cục bộ, Pexels hoặc Pixabay. Các nguồn trực tuyến cần khóa tương ứng. Từ khóa tìm tư liệu có thể dùng tiếng Anh để tăng khả năng tìm kiếm; lời đọc vẫn là tiếng Việt.
3. Nhập chủ đề rõ ràng, ví dụ: “Ba cách kiểm soát chi tiêu cho người mới khởi nghiệp”. Chọn ngôn ngữ kịch bản `vi-VN` và kiểm tra kịch bản trước khi tạo.
4. Chọn giọng Việt Hoài My; có thể chuyển sang Nam Minh nếu giọng này có trong danh sách tải được. Nghe thử và kiểm tra số, tên riêng, dấu câu.
5. Bật phụ đề, chọn Be Vietnam Pro, chọn khung dọc 9:16 nếu làm video ngắn.
6. Tạo một video để kiểm tra lời đọc, chữ có dấu, độ khớp tư liệu và nhạc trước khi tạo hàng loạt.

## Chi phí và nội dung

Mã nguồn có giấy phép MIT; dịch vụ mô hình AI, tạo tư liệu, giọng đọc hoặc nhạc có thể tính phí riêng. Giá và hạn mức do nhà cung cấp quyết định. Bản Việt hóa không cam kết chi phí bằng không. Các thông báo xác nhận tác vụ có phí được giữ lại.

Chỉ sử dụng tư liệu, nhạc và giọng nói được phép sử dụng. Kiểm tra điều kiện của từng nguồn trước khi xuất bản. Ứng dụng không bảo đảm video sẽ lan truyền hoặc mang lại doanh thu.

Bản Việt hóa không bật lịch đăng Facebook tự động. Cài đặt và tạo video không đồng nghĩa với tự đăng lên mạng xã hội.

Không tải `config.toml`, `.env`, khóa API hoặc token lên GitHub. Các tệp bí mật này đã có trong quy tắc bỏ qua Git của dự án.

## Xử lý lỗi thường gặp

| Hiện tượng | Cách xử lý |
|---|---|
| Giao diện vẫn dùng ngôn ngữ cũ | Chọn Tiếng Việt trong Cài đặt; cấu hình đã lưu có ưu tiên hơn cấu hình mẫu. |
| Không đọc được tiếng Việt | Chọn giọng `vi-VN`, nghe thử, kiểm tra kết nối dịch vụ giọng đọc. |
| Phụ đề mất dấu hoặc hiện ô vuông | Chọn BeVietnamPro-Bold.ttf và kiểm tra phông có trong resource/fonts. |
| Không tìm thấy tư liệu | Kiểm tra khóa nguồn tư liệu; thử từ khóa cụ thể hoặc dùng video cục bộ. |
| Báo lỗi FFmpeg | Cài FFmpeg và kiểm tra `ffmpeg -version`; mở lại cửa sổ lệnh. |
| Lỗi xác thực mô hình | Kiểm tra khóa, địa chỉ gốc và mô hình thuộc cùng tài khoản/nền tảng. |
| Docker không gọi được Ollama | Dùng địa chỉ máy chủ phù hợp thay vì localhost bên trong vùng chứa; Linux có thể cần cấu hình host-gateway. |

## Nguồn và kiểm tra

Nguồn ghim: `68eb5a68b93cfe338198b3dfb151f6d5ec2fe4e5` của harry0703/MoneyPrinterTurbo; phiên bản khai báo trong pyproject.toml: `1.3.8`.

```bash
python -m unittest discover -s test/services -p test_vietnamese_localization.py -v
```

Kiểm tra danh mục dịch, biến định dạng, cấu hình TOML, cú pháp Python, đường đi chọn ngôn ngữ và phông. Chưa kiểm thử tạo video đầu cuối hoặc gọi dịch vụ trả phí trong môi trường thực hiện bản vá này. Xem [báo cáo kiểm tra](docs/KIEM_TRA_VIET_HOA.md) và tài liệu [tiếng Anh gốc](README-en.md) để biết thêm tính năng kỹ thuật.
