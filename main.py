import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)
response.raise_for_status()
# print(response.status_code)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all("div", class_="quote")
print(len(quotes))

quotes_data = []

print("===== QUOTE SCRAPER =====")
for quote in quotes:
  tags = quote.find_all("a", class_="tag")
  tag_list = []
  for tag in tags:
    tag_list.append(tag.get_text())
  text = quote.find("span", class_="text")
  author = quote.find("small" , class_="author")


  data = {
    "qoute": text.get_text(),
    "author": author.get_text(),
    "tags": ", ".join(tag_list)
  }

  quotes_data.append(data)

print()
print(quotes_data)