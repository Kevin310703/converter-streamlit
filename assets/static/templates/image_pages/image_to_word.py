import streamlit as st

from datetime import datetime
from app.utils import images_to_docx_bytes

st.image("assets/static/img/photo.png", width=78)
st.title("Chuyển đổi Ảnh → Word")
st.caption("Tải ảnh lên, tải xuống file DOCX")

with st.expander("ℹ️ Hướng dẫn sử dụng", expanded=False):
    st.markdown("""
        🔹 **Bước 1:** Tải lên một hoặc nhiều ảnh (PNG/JPG/JPEG) bằng trình chọn bên dưới.  
        🔹 **Bước 2:** Nhấn **"Chuyển ảnh"** để chuyển ảnh thành tài liệu Word.  
        🔹 **Bước 3:** Tải xuống file DOCX sau khi hoàn tất.  

        ⚠️ **Lưu ý:**  
        - Ảnh nên rõ nét, không quá nặng để thời gian xử lý nhanh hơn.  
        - Giữ kết nối ổn định trong khi tải lên và chuyển đổi.  
        - Nội dung sẽ được chèn vào một file DOCX duy nhất.  
    """)
    
uploaded_images = st.file_uploader(
    "Chọn ảnh", type=["png", "jpg", "jpeg"], accept_multiple_files=True
)

if st.button("Chuyển ảnh", type="primary", icon=":material/sync:"):
    if not uploaded_images:
        st.warning("Vui lòng chọn ít nhất một ảnh.")
        st.stop()

    docx_bytes, docx_name = images_to_docx_bytes(uploaded_images, "images_to_word.docx")
    st.success(f"Đã tạo {docx_name}")
    st.download_button(
        "Tải DOCX", data=docx_bytes, file_name=docx_name,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        type="primary", icon=":material/file_download:",
    )

st.markdown("---")
st.markdown(f"🚀 **© {datetime.now().year} VIETKIEN**")
