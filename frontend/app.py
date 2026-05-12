import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(
    page_title="DriveMind AI",
    page_icon="🔎",
    layout="centered"
)

st.markdown("""
<style>

html, body, [class*="css"]  {
    color: black !important;
}

.stApp {
    background-color: #f5f7fb;
}

.block-container {
    max-width: 900px;
    padding-top: 30px;
    padding-bottom: 80px;
}

h1, h2, h3, h4, h5, h6, p, span, label, div {
    color: #111827 !important;
}

.main-box {
    background: white;
    padding: 28px;
    border-radius: 16px;
    border: 1px solid #d1d5db;
    margin-bottom: 24px;
}

.main-title {
    font-size: 40px;
    font-weight: 800;
    margin-bottom: 8px;
    color: #111827 !important;
}

.main-subtitle {
    font-size: 17px;
    color: #4b5563 !important;
}

.file-card {
    background: white;
    border: 1px solid #d1d5db;
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 14px;
}

.file-name {
    font-size: 20px;
    font-weight: 700;
    color: #111827 !important;
    margin-bottom: 10px;
}

.file-info {
    font-size: 15px;
    color: #374151 !important;
    margin-bottom: 6px;
}

.open-btn {
    display: inline-block;
    margin-top: 10px;
    background: #2563eb;
    color: white !important;
    padding: 8px 14px;
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
}

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: white !important;
}

.stChatMessage {
    background: white;
    border-radius: 12px;
    padding: 10px;
    border: 1px solid #d1d5db;
}

</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.header("Example Searches")
    st.write("find pdf files")
    st.write("find daily reports")
    st.write("find qr codes")
    st.write("find invoices")
    st.write("find images")
    st.write("show folders")

st.markdown("""
<div class="main-box">
    <div class="main-title">🔎 DriveMind AI</div>
    <div class="main-subtitle">
        Search Google Drive files using natural language.
    </div>
</div>
""", unsafe_allow_html=True)

st.subheader("💬 Chat")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Example: find daily reports")

if user_input:

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):

        with st.spinner("Searching Drive..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"message": user_input}
                )

                data = response.json()

                bot_reply = data.get("reply", "No response received.")
                files = data.get("files", [])

                st.success(bot_reply)

                if files:

                    st.markdown("### Matching Files")

                    for file in files:

                        st.markdown(f"""
<div class="file-card">

<div class="file-name">
📄 {file.get("name")}
</div>

<div class="file-info">
<b>Type:</b> {file.get("mimeType")}
</div>

<div class="file-info">
<b>Modified:</b> {file.get("modifiedTime")}
</div>

<a class="open-btn"
href="{file.get("webViewLink")}"
target="_blank">
Open File
</a>

</div>
""", unsafe_allow_html=True)

                else:
                    st.warning("No matching files found.")

                st.session_state.messages.append({
                    "role": "assistant",
                    "content": bot_reply
                })

            except Exception as e:
                st.error("Backend error.")
                st.write(e)