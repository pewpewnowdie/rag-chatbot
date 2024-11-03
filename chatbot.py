import streamlit as st
from langchain_chroma import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM as Ollama
from get_embedding_function import get_embedding_function
from query_data import query_rag

CHROMA_PATH = "chroma"

PROMPT_TEMPLATE = """
You are a helpful assistant used by a customer for ISP JioFiber. Answer the following question based only on the provided context:

{context}

---

Question: {question}
Answer this question without mentioning about the context that you have read.
"""

st.title('Chatbot')

if 'messages' not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    st.chat_message(message['role']).markdown(message['content'])

prompt = st.chat_input('Type here...')

if prompt:
    st.chat_message('user').markdown(prompt)
    st.session_state.messages.append({'role': 'user', 'content': prompt})
    
    response = query_rag(prompt)
    st.chat_message('assistant').markdown(response)
    
    st.session_state.messages.append({'role': 'assistant', 'content': response})
