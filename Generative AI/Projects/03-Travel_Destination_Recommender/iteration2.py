import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Google Gemini API
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-pro')

def get_travel_recommendations(climate, activity, budget, duration):
    # Enhanced prompt with budget and duration
    prompt = f"""
    Suggest 2 travel destinations based on these preferences:
    - Preferred climate: {climate}
    - Desired activity type: {activity}
    - Budget level: {budget}
    - Trip duration: {duration} days
    
    For each destination, provide:
    1. City and Country
    2. Main attractions
    3. Estimated daily budget
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("AI Travel Recommender")
    
    # Added new inputs
    climate = st.selectbox(
        "What's your preferred climate?",
        ["Tropical", "Mediterranean", "Cold/Snow"]
    )
    
    activity = st.selectbox(
        "What type of activities do you enjoy?",
        ["Beach & Relaxation", "Adventure & Sports", "Cultural & Historical"]
    )
    
    # New: Budget and duration inputs
    budget = st.radio(
        "What's your budget level?",
        ["Budget/Backpacker", "Mid-range", "Luxury"]
    )
    
    duration = st.slider("How many days?", 3, 30, 7)
    
    if st.button("Get Recommendations"):
        try:
            recommendations = get_travel_recommendations(
                climate, activity, budget, duration
            )
            st.write(recommendations)
        except Exception as e:
            st.error("Something went wrong. Please try again!")

if __name__ == "__main__":
    main() 