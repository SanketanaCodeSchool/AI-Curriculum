import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-pro')

def get_travel_recommendations(climate, activity):
    # Basic prompt
    prompt = f"""
    Suggest 1 travel destination based on these preferences:
    - Preferred climate: {climate}
    - Desired activity type: {activity}
    
    Provide:
    1. City and Country
    2. Main attractions
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("AI Travel Recommender")
    
    # Basic inputs
    climate = st.selectbox(
        "What's your preferred climate?",
        ["Tropical", "Mediterranean", "Cold/Snow"]
    )
    
    activity = st.selectbox(
        "What type of activities do you enjoy?",
        ["Beach & Relaxation", "Adventure & Sports", "Cultural & Historical"]
    )
    
    if st.button("Get Recommendation"):
        recommendation = get_travel_recommendations(climate, activity)
        st.write(recommendation)

if __name__ == "__main__":
    main() 