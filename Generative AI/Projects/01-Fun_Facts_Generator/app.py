import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("GEMINI_API_KEY not found in .env file!")
    st.stop()

genai.configure(api_key=api_key)

# Function to generate a fun fact
def generate_fun_fact(topic):
    try:
        model = genai.GenerativeModel("gemini-pro")
        response = model.generate_content(f"Tell me a fun fact about {topic}.")
        return response.text.strip()
    except Exception as e:
        return f"Error generating fun fact: {str(e)}"

# Streamlit UI
st.title("🎉 AI-Powered Fun Facts Generator (Free)")
st.write("Enter a topic, and the AI will generate a fun fact for you!")

topic = st.text_input("Enter a topic (e.g., Space, Animals, History)")

if st.button("Generate Fun Fact"):
    if topic:
        with st.spinner("Generating fun fact..."):
            fact = generate_fun_fact(topic)
            st.success(fact)
    else:
        st.warning("Please enter a topic.")