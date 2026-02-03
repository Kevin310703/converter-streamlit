import streamlit as st
from PIL import Image
try:
    img = Image.open("assets/static/img/Logo.png")
except:
    img = "📄"

st.set_page_config(
    page_title="Bean Converter - Chuyển đổi tài liệu",
    page_icon=img,
    layout="centered",
    initial_sidebar_state="collapsed",
    menu_items={
        'Get Help': 'https://www.your-support-link.com',
        'Report a bug': "https://www.your-issue-link.com",
        'About': """
        # 📄 Bean PDF Converter
        
        **Bean Converter** là công cụ hỗ trợ xử lý tài liệu thông minh, giúp bạn tiết kiệm thời gian chuyển đổi định dạng mà vẫn giữ tối đa định dạng gốc.

        ### ✨ Tính năng nổi bật:
        - **Tốc độ cao**: Xử lý nhiều file cùng lúc (Batch processing).
        - **Chất lượng**: Giữ nguyên layout, hình ảnh và bảng biểu từ PDF sang Word.
        - **Bảo mật**: File được xử lý trực tiếp và không lưu trữ trên máy chủ lâu hơn mức cần thiết.
        - **Tiện lợi**: Hỗ trợ nén ZIP tự động khi chuyển đổi số lượng lớn.

        ---
        💡 *Mẹo: Nếu file PDF có mật khẩu hoặc là dạng ảnh quét (scan), hãy đảm bảo bạn đã mở khóa hoặc sử dụng tính năng OCR trước khi tải lên.*
        """
    }
)

pdf_page = st.Page(
    "assets/static/templates/pdf_pages/pdf_to_word.py",
    title="PDF → Word",
    icon=":material/description:",
)

image_page = st.Page(
    "assets/static/templates/image_pages/image_to_word.py",
    title="Ảnh → Word",
    icon=":material/image:",
)

conversion_pages = [pdf_page, image_page]
about_page = [
    st.Page(
        "assets/static/templates/about_pages/about.py",
        title="Tác giả và Bản quyền",
        icon=":material/info:",
    )
]

st.logo("assets/static/img/Logo.png")
pg = st.navigation(
    {
        "Công cụ": conversion_pages,
        "Thông tin": about_page,
    }
)
pg.run()
