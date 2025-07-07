import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="TripAdvisor Sentiment Dashboard", layout="wide")

data_path = "data/sentiment_results.csv"

st.title("📊 Pittsburgh TripAdvisor Sentiment Dashboard")

if not os.path.exists(data_path):
    st.error("Sentiment data not found. Run sentiment_analysis.py first.")
else:
    df = pd.read_csv(data_path)

    st.metric("Total Reviews", len(df))
    st.metric("Positive", (df["sentiment_label"] == "positive").sum())
    st.metric("Negative", (df["sentiment_label"] == "negative").sum())
    st.metric("Neutral", (df["sentiment_label"] == "neutral").sum())

    st.subheader("Sentiment Distribution")
    st.bar_chart(df["sentiment_label"].value_counts())

    st.subheader("Raw Review Samples")
    st.dataframe(df[["content", "sentiment_score", "sentiment_label"]].head(20))
