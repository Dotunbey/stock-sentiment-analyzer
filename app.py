import streamlit as st
import pandas as pd

# Import your custom modules
from model_loader import load_sentiment_model
from news_fetcher import fetch_news
from sentiment_analyzer import analyze_sentiment

# Set the page configuration
st.set_page_config(page_title="Stock News Sentiment Analyzer", page_icon="📈")

# --- Main App UI ---
st.title("📈 Stock News Sentiment Analyzer")
st.write("Enter a stock ticker to get the latest news and its market sentiment.")

# Load the model and show a spinner
with st.spinner("Loading financial sentiment model... This may take a moment."):
    sentiment_pipeline = load_sentiment_model()

if sentiment_pipeline is None:
    st.error("Error: Could not load sentiment model. Please check the logs.")
else:
    st.success("Model loaded successfully!")

    # User input
    ticker = st.text_input("Enter Stock Ticker (e.g., AAPL, TSLA, GOOG)", value="AAPL")

    if st.button("Analyze News"):
        if not ticker:
            st.warning("Please enter a ticker symbol.")
        else:
            # 1. Fetch News
            with st.spinner(f"Fetching latest news for ${ticker}..."):
                articles = fetch_news(ticker)
            
            if not articles:
                st.error(f"No news found for ${ticker}. Try a different symbol.")
            else:
                # 2. Analyze Sentiment
                with st.spinner(f"Analyzing sentiment for ${ticker} news..."):
                    analysis_results = analyze_sentiment(articles, sentiment_pipeline)
                
                if not analysis_results:
                    st.error("Could not analyze any articles.")
                else:
                    st.success(f"Analysis complete! Found {len(analysis_results)} articles.")
                    
                    # 3. Display Overall "Market Mood"
                    df = pd.DataFrame(analysis_results)
                    average_score = df['score'].mean()
                    
                    if average_score > 0.1:
                        mood = "Positive 🟢"
                    elif average_score < -0.1:
                        mood = "Negative 🔴"
                    else:
                        mood = "Neutral ⚪️"
                    
                    st.subheader(f"Overall Market Mood for ${ticker}: {mood}")
                    st.metric(label="Average Sentiment Score", value=f"{average_score:.3f}")
                    st.write("Score ranges from -1.0 (very negative) to 1.0 (very positive).")

                    # 4. Display Individual Articles
                    st.subheader("Latest Headlines")
                    for result in analysis_results:
                        if result['label'] == 'positive':
                            emoji = "🟢"
                        elif result['label'] == 'negative':
                            emoji = "🔴"
                        else:
                            emoji = "⚪️"
                        
                        st.markdown(f"**{result['title']}**")
                        st.write(f"{emoji} Sentiment: **{result['label']}** (Confidence: {result['confidence']:.2f})")
                        st.markdown(f"[Read full article]({result['link']})", unsafe_allow_html=True)
                        st.markdown("---")
