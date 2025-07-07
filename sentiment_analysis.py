# Script to process the scraped data using tools like VADER or TextBlob.


import pandas as pd
from textblob import TextBlob
import os

# Load data
input_path = "data/raw_reviews.csv"
output_path = "data/sentiment_results.csv"

if not os.path.exists(input_path):
    raise FileNotFoundError(f"{input_path} not found. Run scraper.py first.")

df = pd.read_csv(input_path)

# Basic check for expected columns
if 'content' not in df.columns:
    raise ValueError("Expected 'content' column in CSV.")

# Sentiment analysis
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

df['sentiment_score'] = df['content'].astype(str).apply(get_sentiment)
df['sentiment_label'] = df['sentiment_score'].apply(lambda s: 'positive' if s > 0 else 'negative' if s < 0 else 'neutral')

df.to_csv(output_path, index=False)
print(f"Sentiment results saved to {output_path}")
