import streamlit as st

# Initialize Session State for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# UI Design
st.set_page_config(page_title="AI Study Buddy", page_icon="🤖")
st.title("🤖 My AI Study Buddy")
st.caption("Ask me anything about math or science!")

# Display Chat History
for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

# User Input
user_input = st.chat_input("Ask me a question...")
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    st.chat_message("assistant").markdown("I am just a bot, I need some intelligence!")