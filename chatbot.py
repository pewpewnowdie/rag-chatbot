import streamlit as st
from query_data import query_rag

st.title('Chatbot')
st.chat_message('assistant').markdown("Hello! I'm a chatbot designed to assist you. How can I help you?")

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
