import streamlit as st
from components.upload import render_uploader
from components.history_download import render_history_download
from components.chatUI import render_chat
import requests

st.set_page_config(page_title="🤖Project7 Chatbot", layout="wide")
st.title("🤖 Coding Assistant Chatbot")

res = requests.get("http://127.0.0.1:8000/")
# st.write(res.json())


render_uploader()
render_chat()
render_history_download()