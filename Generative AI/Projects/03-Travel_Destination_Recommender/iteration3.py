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
    # Enhanced prompt with more details
    prompt = f"""
    Suggest 3 travel destinations based on these preferences:
    - Preferred climate: {climate}
    - Desired activity type: {activity}
    - Budget level: {budget}
    - Trip duration: {duration} days
    
    For each destination, provide:
    1. City and Country
    2. Main attractions
    3. Estimated daily budget
    4. Best time to visit
    """
    
    response = model.generate_content(prompt)
    return response.text

def main():
    st.title("🌎 AI Travel Destination Recommender")
    st.write("Let's help you find your perfect travel destination!")
    
    # Enhanced UI with sections
    st.subheader("Your Travel Preferences")
    
    # More options added
    climate = st.selectbox(
        "What's your preferred climate?",
        ["Tropical", "Mediterranean", "Cold/Snow", "Desert", "Temperate"]
    )
    
    activity = st.selectbox(
        "What type of activities do you enjoy?",
        ["Beach & Relaxation", "Adventure & Sports", "Cultural & Historical",
         "Nature & Wildlife", "Food & Shopping"]
    )
    
    budget = st.radio(
        "What's your budget level?",
        ["Budget/Backpacker", "Mid-range", "Luxury"]
    )
    
    duration = st.slider("How many days do you plan to travel?", 3, 30, 7)
    
    if st.button("Get Recommendations! 🎯"):
        with st.spinner("Finding perfect destinations..."):
            try:
                recommendations = get_travel_recommendations(
                    climate, activity, budget, duration
                )
                st.subheader("🌟 Your Personalized Travel Recommendations")
                st.write(recommendations)
                st.balloons()
            except Exception as e:
                st.error(f"Oops! Something went wrong: {str(e)}")

if __name__ == "__main__":
    main() 