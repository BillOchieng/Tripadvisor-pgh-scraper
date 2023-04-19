import requests
from bs4 import BeautifulSoup

# make a request to the website and get its HTML content
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)
html_content = response.content

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# find and print the title of the webpage
title = soup.title.string
print("Title: ", title)

# find and print the introduction paragraph of the Wikipedia page
introduction = soup.find("div", {"class": "mw-parser-output"}).p.text
print("Introduction: ", introduction)

# find and print all the links on the webpage
links = soup.find_all("a")
for link in links:
    print(link.get("href"))
