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

## Folder Structure
Tripadvisor-pgh-scraper/
│
├── scraper.py
├── sentiment_analysis.py
├── app.py  # (or /dashboard if you expand it)
├── data/
│   ├── raw_reviews.csv
│   └── sentiment_results.csv
├── notebooks/
│   └── eda.ipynb
├── README.md
├── requirements.txt
├── pyproject.toml
├── poetry.lock
└── .gitignore

## 💡 Next Steps
- Add review date filters
- Integrate with sentiment analysis script
- Build dashboard using Streamlit or Dash

**Want me to help you scaffold any of these files or kickstart the sentiment analysis or dashboard script?**
