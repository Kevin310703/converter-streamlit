# converter-streamlit

Ứng dụng Streamlit nhiều trang:
- PDF → Word (nhiều file, tải DOCX hoặc ZIP)
- Ảnh → Word (nhúng ảnh vào DOCX)

## Chạy ứng dụng

```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Sử dụng
- Chọn trang ở thanh điều hướng (PDF → Word hoặc Ảnh → Word).
- PDF → Word: tải lên nhiều PDF, xem tiến trình, tải DOCX hoặc ZIP.
- Ảnh → Word: tải ảnh (PNG/JPG), nhận DOCX chứa ảnh.
