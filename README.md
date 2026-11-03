# RSA-Simulator

Website mô phỏng thuật toán RSA bằng Python.

## 1. Công nghệ sử dụng

- Python
- Flask
- HTML
- CSS
- JavaScript

## 2. Cấu trúc project

```text
RSA-Simulator/
├── app.py
├── rsa.py
├── templates/
│   └── index.html
├── static/
│   ├── style.css
│   └── script.js
└── README.md
```

## 3. Cài đặt

Mở Terminal tại thư mục project và cài Flask:

```bash
python -m pip install flask
```

## 4. Chạy chương trình

Chạy lệnh:

```bash
python app.py
```

Sau đó mở trình duyệt và truy cập:

```text
http://127.0.0.1:5000
```

## 5. Cách sử dụng

1. Nhấn **Tạo khóa RSA** để tạo Public Key và Private Key.
2. Nhập thông điệp vào ô thông điệp.
3. Nhấn **Mã hóa** để tạo bản mã.
4. Nhấn **Giải mã** để khôi phục thông điệp ban đầu.

## 6. Lưu ý

Đây là project phục vụ mục đích học tập. Các hàm RSA được tự cài đặt trong file `rsa.py`. Chương trình sử dụng cách mã hóa đơn giản để minh họa thuật toán, không phù hợp để bảo vệ dữ liệu thực tế.
