import streamlit as st
from rag_pipeline import answer_query, retrieve_docs, llm_model

uploaded_file = st.file_uploader("Upload Pdf", type="pdf", accept_multiple_files=False)

# Chat Area
user_query = st.text_area("Enter your prompt:", height=150, placeholder="Ask Anything!")

ask_question = st.button("Ask AI Assistant")

if ask_question:
    if uploaded_file:
        st.chat_message("user").write(user_query)

        # RAG Pipeline
        retrieve_docs= retrieve_docs(user_query)
        response = answer_query(documents=retrieve_docs, model = llm_model, query=user_query)
        st.chat_message("AI Assistant").write(response)
    else:
        st.error("Kindly upload a valid pdf file first")
