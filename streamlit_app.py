import streamlit as st
import requests
import os

API_URL = "http://localhost:8000"

st.set_page_config(page_title="📄 Doc QA Chatbot", layout="centered")
st.title("📄 Document QA Chatbot")

# Upload section
st.header("📤 Upload Document")

uploaded_file = st.file_uploader("Choose a document (.pdf, .txt, .md, .docx)", type=["pdf", "txt", "md", "docx"])
if uploaded_file is not None:
    if st.button("Upload"):
        with st.spinner("Uploading and indexing..."):
            files = {"file": uploaded_file.getvalue()}
            filename = uploaded_file.name
            res = requests.post(f"{API_URL}/upload/", files={"file": (filename, uploaded_file)})
            if res.status_code == 200:
                st.success(f"Uploaded and indexed: {res.json()['chunks']} chunks")
            else:
                st.error("Failed to upload.")

# Question Answering
st.header("🤖 Ask a Question")

query = st.text_input("Your question", placeholder="e.g., What is this document about?")
if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Thinking..."):
            res = requests.get(f"{API_URL}/ask/", params={"query": query})
            if res.status_code == 200:
                data = res.json()
                st.markdown("### 📥 Answer")
                st.success(data["answer"])
                st.markdown("### 📚 Sources")
                for src in data["sources"]:
                    st.markdown(f"- {src}")
            else:
                st.error("Failed to get response.")
