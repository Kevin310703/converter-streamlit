import streamlit as st

from app.utils import images_to_docx_bytes

st.subheader("Chuyển Ảnh → Word")
st.caption("Chèn các ảnh vào file DOCX để tải xuống")

uploaded_images = st.file_uploader(
    "Chọn ảnh", type=["png", "jpg", "jpeg"], accept_multiple_files=True
)

if st.button("Chuyển ảnh"):
    if not uploaded_images:
        st.warning("Vui lòng chọn ít nhất một ảnh.")
        st.stop()

    docx_bytes, docx_name = images_to_docx_bytes(uploaded_images, "images_to_word.docx")
    st.success(f"Đã tạo {docx_name}")
    st.download_button(
        "Tải DOCX", data=docx_bytes, file_name=docx_name,
        mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
