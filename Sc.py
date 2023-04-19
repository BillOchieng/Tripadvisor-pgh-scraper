import requests
from bs4 import BeautifulSoup

# URL of the website to scrape reviews from
url = "https://www.example.com/reviews"

# Send a GET request to the website and store the response
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the review elements on the page
reviews = soup.find_all('div', {'class': 'review'})

# Iterate over the review elements and extract the necessary information
for review in reviews:
    # Extract the rating of the review
    rating = review.find('span', {'class': 'rating'}).text.strip()

    # Extract the title of the review
    title = review.find('h3', {'class': 'title'}).text.strip()

    # Extract the text of the review
    text = review.find('div', {'class': 'text'}).text.strip()

    # Extract the author of the review
    author = review.find('span', {'class': 'author'}).text.strip()

    # Extract the date of the review
    date = review.find('span', {'class': 'date'}).text.strip()

    # Print the extracted information
    print('Rating:', rating)
    print('Title:', title)
    print('Text:', text)
    print('Author:', author)
    print('Date:', date)
    print('--------------')
