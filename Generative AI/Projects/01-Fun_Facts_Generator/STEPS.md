# Steps

1. Ensure Python is install
2. Install streamlit and gemini

```
pip install google-generativeai streamlit python-dotenv
```

3. Create Google Gemini accound and Generate Google API Key
   https://aistudio.google.com/

4. Create Project folder
5. Create .env file
6. Put the following code in the .env file

```
GEMINI_API_KEY="your_api_key_here"
```

7. Check if streamlit is properly installed by running the following command

```
streamlit hello
```

8. Create an app.py and write the code for Fun Fact Generator application

9. Run the project

```
streamlit run app.py
```

## Further Readings

- Streamlit UI element - Try out other UI element of Streamlit
- google.generativeai SDK - Try out other AI capabilities of Google Gemini
- Google AI Studio - Experiement with different Google AI models in Google AI Studio
- Gemini API Cookbook - https://github.com/google-gemini/gemini-api-cookbook/
- Compare different Gemini Models - https://ai.google.dev/gemini-api/docs/models/gemini
- Other AI backend eg: OpenAI, Hugging face transformers

## Concepts

- Steamlit
- Google AI Studio
- Streamlit community deployment
