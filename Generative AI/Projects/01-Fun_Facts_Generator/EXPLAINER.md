# 🎉 AI-Powered Fun Facts Generator – Code Explanation

This Python app uses **Streamlit** and **Google Generative AI (Gemini API)** to generate fun facts based on the topic entered by the user.

---

## 📦 **Imports and Setup**

```python
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
```

- `streamlit`: For creating the web-based user interface.
- `google.generativeai`: To generate AI-based responses using Google's Gemini API.
- `os`: To access environment variables.
- `dotenv`: To securely load environment variables from a `.env` file.

---

## 🔑 **Loading and Configuring the API Key**

```python
load_dotenv()
genai.configure(api_key="your_api_key_here")
```

- Loads environment variables securely using `dotenv`.
- Configures the **Gemini API** using an API key for authentication.

> 🔒 **Note**: It's better to store API keys in a `.env` file for security.

---

## 🧠 **Function to Generate Fun Facts**

```python
def generate_fun_fact(topic):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(f"Tell me a fun fact about {topic}.")
    return response.text.strip()
```

- Initializes the **Gemini Pro** model.
- Takes a `topic` as input and requests a fun fact from the AI model.
- Returns the AI's response after removing extra spaces.

---

## 🎨 **User Interface (Streamlit UI)**

```python
st.title("🎉 AI-Powered Fun Facts Generator")
st.write("Enter a topic, and the AI will generate a fun fact for you!")
```

- Displays the app's title and a short description.

---

## ✏️ **User Input Field**

```python
topic = st.text_input("Enter a topic (e.g., Space, Animals, History)")
```

- Allows the user to input a topic for which they want a fun fact.

---

## 🚀 **Generating and Displaying Fun Facts**

```python
if st.button("Generate Fun Fact"):
    if topic:
        fact = generate_fun_fact(topic)
        st.success(fact)
    else:
        st.warning("Please enter a topic.")
```

- When the "Generate Fun Fact" button is clicked:
  - If a valid topic is entered, it displays the fun fact.
  - If no topic is entered, it prompts the user to enter one.

---

## ✅ **Key Features**

- Uses AI to generate fun facts on any given topic.
- Provides instant, interactive responses using Streamlit.
- Handles empty input with a friendly warning message.

---

## 🚀 **How to Run the App**

1. Install the required packages:
   ```bash
   pip install streamlit google-generativeai python-dotenv
   ```
2. Add your **Gemini API key** to a `.env` file (recommended):
   ```
   GEMINI_API_KEY=your_api_key_here
   ```
3. Run the app using Streamlit:
   ```bash
   streamlit run your_script_name.py
   ```

---

Have fun generating cool facts! 🎊
