import streamlit as st
import feedparser

@st.cache_data(ttl=3600)  # Cache data for 1 hour (3600 seconds)
def fetch_news(ticker):
    """
    Fetches news headlines from Google News RSS feed for a given ticker.
    Results are cached to prevent re-fetching on every app interaction.
    """
    if not ticker:
        return []
        
    url = f"https://news.google.com/rss/search?q={ticker}&hl=en-US&gl=US&ceid=US:en"
    feed = feedparser.parse(url)
    return feed.entries
