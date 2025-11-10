# 📈 Stock News Sentiment Analyzer

A web application built with Streamlit and Hugging Face Transformers that fetches the latest news for a given stock ticker and analyzes its market sentiment.



## ✨ Features

* **Real-time News:** Fetches the latest headlines from Google News.
* **Financial AI:** Uses `ProsusAI/finbert`, a sentiment analysis model specifically trained on financial text.
* **"Market Mood":** Calculates an average sentiment score to give a quick overview of market feeling.
* **Interactive UI:** Built with Streamlit for a clean, responsive user interface.
* **Modular Code:** The project is broken into logical modules (UI, model, news) for clean, maintainable code.

## 🛠️ How to Run This Project

### 1. Prerequisites

* Python 3.8+
* Git

### 2. Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR-USERNAME/stock-sentiment-analyzer.git](https://github.com/YOUR-USERNAME/stock-sentiment-analyzer.git)
    cd stock-sentiment-analyzer
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```

### 3. Running the App

Once the dependencies are installed, run the Streamlit app:

```bash
streamlit run app.py
```

Your browser should automatically open to the app!

## Project Structure

```
stock-sentiment-analyzer/
├── .gitignore           # Tells Git which files to ignore
├── app.py               # The main Streamlit UI application
├── model_loader.py      # Module to load and cache the AI model
├── news_fetcher.py      # Module to fetch news data
├── README.md            # You are reading this!
├── requirements.txt     # List of all Python dependencies
├── sentiment_analyzer.py  # Module for the sentiment analysis logic
```
