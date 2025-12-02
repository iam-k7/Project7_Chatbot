import streamlit as st
from utils.api import upload_pdfs_api

def render_uploader():
    st.sidebar.header("Upload Coding documents (.PDFs)")
    upload_files=st.sidebar.file_uploader("Upload multiple PDFs",type="pdf",accept_multiple_files=True)
    if st.sidebar.button("Upload DB") and upload_files:
        response=upload_pdfs_api(upload_files)
        if response.status_code==200:
            st.sidebar.success("Uploaded successfully")
        else:
            st.sidebar.error(f"Error: {response.text}")