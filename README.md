# TripAdvisor Review Scraper – Pittsburgh Edition

A web scraper built with Python, Selenium, and BeautifulSoup to extract hotel and restaurant reviews from TripAdvisor specific to Pittsburgh, PA. This project focuses on collecting and analyzing summer-season traveler sentiment.

## 🔧 Features
- Scrapes review titles, content, and star ratings
- Targeted to hotels/restaurants in Pittsburgh
- Outputs structured CSV for further analysis
- Designed to integrate with sentiment analysis pipelines (VADER/TextBlob)

## 📊 Use Cases
- Sentiment trends among Pittsburgh visitors
- Hospitality service benchmarking
- Seasonal travel behavior insights

## 🚀 Getting Started
```bash
pip install selenium beautifulsoup4
python scraper.py
```

## 💡 Next Steps
- Add review date filters
- Integrate with sentiment analysis script
- Build dashboard using Streamlit or Dash
- Run scraper.py → populates data/raw_reviews.csv
- Run sentiment_analysis.py → creates data/sentiment_results.csv
- Run streamlit run app.py → launches your dashboard
