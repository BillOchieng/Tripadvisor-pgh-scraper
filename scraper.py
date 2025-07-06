# 📁 Project: TripAdvisor Review Scraper – Pittsburgh Edition

# ────────────────────────────────
# scraper.py
# ────────────────────────────────
import time
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup Chrome driver options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")

# Start driver
driver = webdriver.Chrome(options=options)

# URL for a sample Pittsburgh hotel (can be looped for multiple hotels)
url = "https://www.tripadvisor.com/Hotel_Review-g53449-d100860-Reviews-Omni_William_Penn_Hotel-Pittsburgh_Pennsylvania.html"
driver.get(url)
time.sleep(5)

# Expand all reviews by clicking "More"
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

reviews = []
review_blocks = soup.find_all('div', class_='YibKl MC R2 Gi z Z BB pBbQr')

for block in review_blocks:
    try:
        title = block.find('a', class_='Qwuub').text.strip()
        body = block.find('q', class_='QewHA H4 _a').text.strip()
        rating_tag = block.find('div', class_='Hlmiy F1')
        rating_class = rating_tag.find('span')['class'][1] if rating_tag else None
        rating = int(rating_class.split('_')[-1])/10 if rating_class else None

        reviews.append([title, body, rating])
    except Exception as e:
        continue

# Save to CSV
with open('pittsburgh_reviews.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Title', 'Review Text', 'Rating'])
    writer.writerows(reviews)

print(f"Scraped {len(reviews)} reviews.")
driver.quit()
