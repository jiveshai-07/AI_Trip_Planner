import streamlit as st
from components.auth import check_login, logout
from components.ui import load_ui, footer
from components.navbar import navbar
import os

check_login()
load_ui()
navbar()

st.title("⚙️ Settings")

st.markdown("## 🔑 API Status")

api_key = (
    os.getenv("OPENROUTER_API_KEY")
    or st.secrets.get("OPENROUTER_API_KEY", None)
)

if api_key:
    st.success("✅ OpenRouter API Key is configured.")
else:
    st.error("❌ OpenRouter API Key is missing.")

st.markdown("## 👤 Account")
st.write(f"**Logged in as:** {st.session_state.username}")

if st.button("🚪 Logout"):
    logout()

st.markdown("## 🗑️ Data")

if st.button("🗑️ Clear Chat History"):
    st.session_state.chat_history = []
    st.success("Chat history cleared.")

footer()