def analyze_sentiment(articles, sentiment_pipeline):
    """
    Analyzes the sentiment of a list of article titles using the loaded model.
    """
    if not articles or sentiment_pipeline is None:
        return []

    results = []
    
    for article in articles:
        title = article.title
        link = article.link
        
        try:
            # Run the sentiment analysis
            sentiment_result = sentiment_pipeline(title)[0]
            label = sentiment_result['label']
            score = sentiment_result['score']
            
            # Convert label to a numerical score for averaging
            if label == 'positive':
                num_score = score
            elif label == 'negative':
                num_score = -score
            else:
                num_score = 0
                
            results.append({
                "title": title,
                "link": link,
                "label": label,
                "confidence": score,
                "score": num_score  # The normalized score for averaging
            })
        except Exception as e:
            # Log error to console, but don't crash the app
            print(f"Error analyzing title: {title} (Error: {e})")
            
    return results
