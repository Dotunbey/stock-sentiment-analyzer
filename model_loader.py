import streamlit as st
from transformers import pipeline

@st.cache_resource
def load_sentiment_model():
    """
    Loads and caches the pre-trained financial sentiment model.
    This function is decorated with @st.cache_resource, so it only
    runs once when the app first starts.
    """
    model_name = "ProsusAI/finbert"
    
    # We can't use st.write here, as it's just a loader
    # The app.py will handle loading messages
    print(f"Loading sentiment model ({model_name})...")
    try:
        sentiment_pipeline = pipeline("sentiment-analysis", model=model_name)
        print("Model loaded successfully!")
        return sentiment_pipeline
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
