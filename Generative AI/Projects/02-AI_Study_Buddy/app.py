import streamlit as st
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import os

# Ensure the offload folder exists
os.makedirs("offload", exist_ok=True)

# Use a lightweight LLM
MODEL_NAME = "deepseek-ai/deepseek-coder-1.3b-base"

# Load tokenizer & model with MPS acceleration (for Mac M1/M2)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME, torch_dtype=torch.float16, device_map="auto", offload_folder="offload"
)

# Debugging information
st.write("Model and tokenizer loaded successfully.")

# Streamlit UI
st.title("📚 My AI Study Buddy 🤖")
st.write("Ask me math or science questions!")

user_input = st.text_input("Your Question:", "")

if st.button("Get Answer"):
    if user_input:
        try:
            inputs = tokenizer(user_input, return_tensors="pt").to("mps")
            st.write("Inputs processed successfully.")
            outputs = model.generate(**inputs, max_length=100)
            st.write("Outputs generated successfully.")
            response = tokenizer.decode(outputs[0], skip_special_tokens=True)

            st.write("### 🤖 AI Response:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question.")