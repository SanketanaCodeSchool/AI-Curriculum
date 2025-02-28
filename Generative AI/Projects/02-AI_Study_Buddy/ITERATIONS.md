# AI Study Buddy Chatbot Project Iterations

This document outlines a step-by-step progression of your AI chatbot project using Streamlit and Google's Generative AI, starting from a basic version and advancing to a fully-featured chatbot.

---

## **Iteration 1: Basic Chatbot Setup**

### Features:

- Set up basic Streamlit app structure
- Add title and caption
- Create simple text input and display

### Code:

```python
import streamlit as st

st.title("🤖 My AI Study Buddy Chatbot")
st.caption("Your personal AI-powered math & science tutor!")

user_input = st.text_input("Ask me a question...")
if user_input:
    st.write(f"You asked: {user_input}")
```

---

## **Iteration 2: Integrate Google Generative AI**

### Features:

- Add environment variable handling
- Initialize Gemini model
- Generate basic responses

### Code:

```python
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")

st.title("🤖 My AI Study Buddy Chatbot")
st.caption("Your personal AI-powered math & science tutor!")

user_input = st.text_input("Ask me a question...")
if user_input:
    response = model.generate_content(user_input)
    st.write(f"Answer: {response.text}")
```

---

## **Iteration 3: Add Chat Interface**

### Features:

- Switch to chat input
- Add basic chat message display
- Implement try-catch for error handling

### Code:

```python
# ... existing imports and setup ...

st.title("🤖 My AI Study Buddy Chatbot")
st.caption("Your personal AI-powered math & science tutor!")

user_input = st.chat_input("Ask me a question...")

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(user_input)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
```

---

## **Iteration 4: Subject-Specific Responses**

### Features:

- Implement session state for chat history
- Display previous messages

### Code:

```python
# ... existing imports and setup ...

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 My AI Study Buddy Chatbot")
st.caption("Your personal AI-powered math & science tutor!")

for entry in st.session_state.chat_history:
    role, message = entry
    if role == "user":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)

user_input = st.chat_input("Ask me a question...")

if user_input:
    st.session_state.chat_history.append(("user", user_input))
    with st.chat_message("user"):
        st.markdown(user_input)
    
    with st.chat_message("assistant"):
        try:
            response = model.generate_content(user_input)
            reply = response.text.strip()
            st.markdown(reply)
            st.session_state.chat_history.append(("bot", reply))
        except Exception as e:
            error_message = f"Error: {e}"
            st.error(error_message)
            st.session_state.chat_history.append(("bot", error_message))
```

---

## **Iteration 5 (final): Add Subject Selection and Polish**

### Features:

- Add sidebar with subject selection
- Update page configuration
- Add loading spinner
- Enhance prompt with subject context

### Code:

```python
# ... existing imports and setup ...

# Initialize Session State
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# UI Design
st.set_page_config(page_title="AI Study Buddy Chatbot", page_icon="🤖")
st.title("🤖 My AI Study Buddy Chatbot")
st.caption("Your personal AI-powered math & science tutor!")

# Sidebar for Subject Selection
subject = st.sidebar.selectbox("Choose a subject 📚", ["General", "Math", "Science"])

# Display Chat History
for entry in st.session_state.chat_history:
    role, message = entry
    if role == "user":
        st.chat_message("user").markdown(message)
    else:
        st.chat_message("assistant").markdown(message)

# User Input
user_input = st.chat_input("Ask me a question...")

# Generate AI Response
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

---

## **Future Enhancements:**

- Save chat history to a file.
- Add user authentication.
- Support for multimedia responses (images, videos).

