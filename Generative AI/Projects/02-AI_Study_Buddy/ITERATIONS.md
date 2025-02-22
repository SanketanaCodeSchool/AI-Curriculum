# AI Study Buddy Chatbot Project Iterations

This document outlines a step-by-step progression of your AI chatbot project using Streamlit and Google's Generative AI, starting from a basic version and advancing to a fully-featured chatbot.

---

## **Iteration 1: Basic Chatbot Setup**

### Features:

- Initialize a simple chatbot interface.
- Accept user input and return a static response.

### Code:

```python
import streamlit as st

st.title("🤖 Basic AI Chatbot")
user_input = st.text_input("Ask a question:")
if user_input:
    st.write("This is a placeholder response.")
```

---

## **Iteration 2: Integrate Google Generative AI**

### Features:

- Load and configure the Gemini AI API.
- Generate AI responses dynamically.

### Code:

```python
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-pro")

st.title("🤖 AI-Powered Chatbot")
user_input = st.text_input("Ask me anything:")
if user_input:
    response = model.generate_content(user_input)
    st.write(response.text.strip())
```

---

## **Iteration 3: Adding Chat History**

### Features:

- Maintain chat history using session state.
- Display user and bot messages separately.

### Code:

```python
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 AI Chatbot with History")

for role, message in st.session_state.chat_history:
    if role == "user":
        st.write(f"You: {message}")
    else:
        st.write(f"Bot: {message}")

user_input = st.text_input("Ask me anything:")
if user_input:
    st.session_state.chat_history.append(("user", user_input))
    response = model.generate_content(user_input)
    reply = response.text.strip()
    st.session_state.chat_history.append(("bot", reply))
    st.write(f"Bot: {reply}")
```

---

## **Iteration 4: Subject-Specific Responses**

### Features:

- Add a subject selection sidebar.
- Tailor responses based on the selected subject.

### Code:

```python
subject = st.sidebar.selectbox("Choose a subject", ["General", "Math", "Science"])

user_input = st.text_input("Ask me a question:")
if user_input:
    prompt = f"Answer this {subject.lower()} question: {user_input}"
    response = model.generate_content(prompt)
    reply = response.text.strip()
    st.write(f"Bot: {reply}")
```

---

## **Iteration 5: Error Handling and Polished UI**

### Features:

- Handle API errors gracefully.
- Improve the user interface.

### Code:

```python
st.set_page_config(page_title="AI Study Buddy Chatbot", page_icon="🤖")

try:
    prompt = f"Answer this {subject.lower()} question: {user_input}"
    response = model.generate_content(prompt)
    reply = response.text.strip()
    st.write(f"Bot: {reply}")
except Exception as e:
    st.error(f"Error: {e}")
```

---

## **Future Enhancements:**

- Save chat history to a file.
- Add user authentication.
- Support for multimedia responses (images, videos).

