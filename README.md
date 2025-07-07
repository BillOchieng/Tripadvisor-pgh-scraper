# TripAdvisor Review Scraper – Pittsburgh Edition

A data-driven application built with **Python**, **Selenium**, and **BeautifulSoup** to extract hotel and restaurant reviews from **TripAdvisor**, specifically focused on the **Pittsburgh, PA** area. This project automates review scraping, analyzes sentiment using **TextBlob**, and visualizes trends through an interactive **Streamlit dashboard**.

---

## 🔧 Features
- Scrapes review titles, full content, and star ratings
- Targets hotels and restaurants in Pittsburgh, PA
- Stores reviews in structured CSV files
- Performs sentiment analysis (positive, negative, neutral) using TextBlob
- Visualizes insights with an interactive dashboard
- Dockerized and CI-ready for scalable deployments

---

## 📊 Use Cases
- Track sentiment trends among Pittsburgh visitors
- Benchmark hospitality service performance
- Analyze seasonal travel behavior and review tone
- Enable data storytelling for travel/tourism stakeholders

---

## 🚀 Getting Started

### ▶️ Local Development
```bash
# 1. Set up virtual environment and install dependencies
bash setup.sh

# 2. Scrape data
python scraper.py

# 3. Analyze sentiment
python sentiment_analysis.py

# 4. Launch dashboard
streamlit run streamlit_dashboard/app.py
```

### 🐳 Docker Workflow
```bash
# Build the image
docker-compose build

# Launch dashboard
docker-compose up dashboard

# Run sentiment analysis in Docker
docker-compose run --rm --profile worker sentiment_worker
```

---

## 📁 Project Structure
```
Tripadvisor-pgh-scraper/
├── scraper.py
├── sentiment_analysis.py
├── streamlit_dashboard/app.py
├── data/                 # Contains raw_reviews.csv & sentiment_results.csv
├── notebooks/            # Jupyter notebook for EDA
├── web/                  # Optional HTML/JS visualizer
├── Dockerfile
├── docker-compose.yml
├── .env
├── .gitignore
├── .dockerignore
├── setup.sh
├── requirements.txt
└── README.md
```

---

## 💡 Future Enhancements
- Add review date filters
- Use VADER for more granular sentiment classification
- Integrate PostgreSQL or MongoDB for persistent storage
- Deploy on Render or Vercel
- Schedule automatic scraping (via cron or serverless function)

---

## 🌐 Tech Stack & Tools
| Category           | Tools/Languages               |
|-------------------|-------------------------------|
| Scraping          | Python, Selenium, BeautifulSoup |
| Analysis          | pandas, TextBlob              |
| Dashboard         | Streamlit                     |
| DevOps            | Docker, Docker Compose, GitHub Actions |
| Deployment Ready  | Render-compatible, .env config |
| Optional Frontend | HTML, Chart.js (in `web/`)    |

---

## 👥 About
Built by [Bill Ochieng](https://github.com/BillOchieng) to explore real-world sentiment analysis in the travel sector. This project blends automation, NLP, and data storytelling in a deployable, production-style workflow.

---

## 📬 Contact
Feel free to connect via [LinkedIn](https://linkedin.com/in/) or open an [Issue](https://github.com/BillOchieng/Tripadvisor-pgh-scraper/issues) to collaborate or suggest improvements.

---

## 📚 References
- Bright Data. (2024). *How to scrape TripAdvisor*. Retrieved from https://brightdata.com/blog/web-data/how-to-scrape-tripadvisor
- Giuseppegambino. (2020). *Scraping TripAdvisor with Python*. GitHub repository. https://github.com/giuseppegambino/Scraping-TripAdvisor-with-Python-2020
- Oxylabs. (2024). *TripAdvisor scraping tutorial*. Retrieved from https://oxylabs.io/blog/how-to-scrape-tripadvisor
- TextBlob Documentation. (n.d.). *Quickstart Guide*. https://textblob.readthedocs.io/en/dev/quickstart.html
- Vidhya, A. (2021). *Sentiment analysis with TextBlob and VADER*. Analytics Vidhya. https://www.analyticsvidhya.com/blog/2021/10/sentiment-analysis-with-textblob-and-vader/
- YouTube. (2024). *Deploy a Streamlit App Using Docker*. https://www.youtube.com/watch?v=5pPTNzUcIxg
- Streamlit Docs. (2024). *Docker deployment guide*. https://docs.streamlit.io/deploy/tutorials/docker
- Ribeiro, F. N., Araújo, M., Gonçalves, P., André Gonçalves, M., & Benevenuto, F. (2016). *SentiBench - A benchmark comparison of state-of-the-practice sentiment analysis methods*. Information Sciences, 364-365, 1-25. https://doi.org/10.1016/j.ins.2016.05.008

---

## ⭐ Repo Stats (Auto Updated)
![GitHub language count](https://img.shields.io/github/languages/count/BillOchieng/Tripadvisor-pgh-scraper)
![GitHub top language](https://img.shields.io/github/languages/top/BillOchieng/Tripadvisor-pgh-scraper)
![GitHub last commit](https://img.shields.io/github/last-commit/BillOchieng/Tripadvisor-pgh-scraper)

---
