
# 🤖 AI Study Buddy Chatbot – Code Explanation

This Python app uses **Streamlit** and Google's **Generative AI (Gemini API)** to create an interactive chatbot that serves as a math and science tutor.

---

## 📦 **Imports and Setup**

```python
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
```
- `streamlit`: For creating the web app interface.
- `google.generativeai`: To interact with Google's Gemini API for generating responses.
- `dotenv`: Loads environment variables from a `.env` file securely.
- `os`: Accesses environment variables like API keys.

---

## 🔑 **Loading and Configuring the API Key**

```python
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
```
- Loads the API key securely from the environment.
- Configures the **Gemini API** with the provided key.

---

## 🧠 **Model Initialization**

```python
model = genai.GenerativeModel("gemini-pro")
```
- Initializes the **Gemini Pro** model, which handles generating responses based on the input prompt.

---

## 💾 **Session State Management**

```python
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
```
- Initializes `chat_history` to track user and bot conversations across multiple interactions in the same session.

---

## 🎨 **User Interface Setup**

```python
st.set_page_config(page_title="AI Study Buddy Chatbot", page_icon="🤖")
st.title("🤖 My AI Study Buddy Chatbot")
st.caption("Your personal AI-powered math & science tutor!")
```
- Configures the page's title, icon, and header for a user-friendly experience.

---

## 📚 **Subject Selection Sidebar**

```python
subject = st.sidebar.selectbox("Choose a subject 📚", ["General", "Math", "Science"])
```
- Lets the user choose a subject from the sidebar to tailor responses accordingly.

---

## 💬 **Chat History Display**

```python
for entry in st.session_state.chat_history:
    role, message = entry
    if role == "user":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)
```
- Displays past messages, differentiating between user input and AI responses.

---

## 📝 **Handling User Input**

```python
user_input = st.chat_input("Ask me a question...")
```
- A text input field where users can type their questions.

---

## ⚡ **Generating AI Responses**

```python
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤖"):
            try:
                prompt = f"Answer this {subject.lower()} question: {user_input}"
                response = model.generate_content(prompt)
                reply = response.text.strip()
                st.markdown(reply)
                st.session_state.chat_history.append(("bot", reply))
            except Exception as e:
                error_message = f"Error: {e}"
                st.error(error_message)
                st.session_state.chat_history.append(("bot", error_message))
```
- Appends user input to the chat history.
- Sends a subject-specific prompt to the AI model.
- Displays the AI’s response in the chat.
- Handles errors gracefully and informs the user if something goes wrong.

---

## ✅ **Key Features**
- Supports **Math**, **Science**, and **General** queries.
- Maintains **chat history** using Streamlit’s session state.
- Provides instant AI-generated responses.
- Handles errors in API responses.

---

## 🚀 **How to Run the App**
1. Install the required packages:
   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```
2. Add your **Gemini API key** to a `.env` file:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
3. Run the app:
   ```bash
   streamlit run your_script_name.py
   ```

---

Happy coding! 🎉
