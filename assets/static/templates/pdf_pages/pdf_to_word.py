import io
import zipfile
import streamlit as st

from app.utils import pdf_to_docx_bytes

st.image("assets/static/img/pdf.png", width=78)
st.title("Chuyển đổi PDF → Word")
st.caption("Tải nhiều PDF, nhận DOCX hoặc ZIP")

with st.expander("ℹ️ Hướng dẫn sử dụng", expanded=False):
    st.markdown("""
        🔹 **Bước 1:** Tải lên một hoặc nhiều file PDF bằng trình chọn bên dưới.  
        🔹 **Bước 2:** Nhấn **"Chuyển đổi"** để bắt đầu.  
        🔹 **Bước 3:** Tải xuống DOCX (hoặc ZIP nếu nhiều file) sau khi hoàn tất.  

        ⚠️ **Lưu ý:**  
        - PDF không được đặt mật khẩu và nên có dung lượng vừa phải.  
        - Giữ kết nối ổn định trong khi tải lên và chuyển đổi.  
        - Tên file DOCX sẽ giữ nguyên theo tên PDF gốc.  
    """)

uploaded_files = st.file_uploader(
    "Chọn file PDF", type=["pdf"], accept_multiple_files=True
)

if st.button("Chuyển đổi", type="primary", icon=":material/sync:"):
    if not uploaded_files:
        st.warning("Vui lòng chọn ít nhất một file PDF.")
        st.stop()

    progress = st.progress(0.0, text="Bắt đầu chuyển đổi…")
    status = st.empty()

    results = []
    for idx, uploaded in enumerate(uploaded_files):
        status.write(f"Đang xử lý {uploaded.name}…")
        error = None
        docx_bytes = None
        docx_name = None
        try:
            docx_bytes, docx_name = pdf_to_docx_bytes(uploaded.getbuffer(), uploaded.name)
        except Exception as exc:  # pragma: no cover - user feedback only
            error = str(exc)
        results.append({
            "pdf": uploaded.name,
            "docx": docx_name,
            "docx_bytes": docx_bytes,
            "error": error,
        })
        progress.progress((idx + 1) / len(uploaded_files), text=f"Hoàn thành {idx + 1}/{len(uploaded_files)}")

    ok = [r for r in results if r["error"] is None]
    st.success(f"Thành công {len(ok)}/{len(results)} file.")

    for item in results:
        if item["error"]:
            st.error(f"{item['pdf']}: lỗi - {item['error']}")
        else:
            st.write(f"✅ {item['pdf']} → {item['docx']}")

    if ok:
        if len(ok) == 1:
            st.download_button(
                "Tải xuống DOCX",
                data=ok[0]["docx_bytes"],
                file_name=ok[0]["docx"],
                mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                icon=":material/file_download:",
                type="primary",
            )
        else:
            zip_buf = io.BytesIO()
            with zipfile.ZipFile(zip_buf, "w", zipfile.ZIP_DEFLATED) as zipf:
                for item in ok:
                    zipf.writestr(item["docx"], item["docx_bytes"])
            zip_buf.seek(0)
            st.download_button(
                "Tải ZIP",
                data=zip_buf,
                file_name="pdf_to_word.zip",
                mime="application/zip",
            )
