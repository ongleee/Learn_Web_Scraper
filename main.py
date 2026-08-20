import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

# print(response.status_code)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all("div", class_="quote")
print(len(quotes))

print("===== QUOTE SCRAPER =====")
for quote in quotes:
  tags = quote.find_all("a", class_="tag")
  tag_list = []
  for tag in tags:
    tag_list.append(tag.get_text())
  text = quote.find("span", class_="text")
  author = quote.find("small" , class_="author")

  print("Quote: " ,end="")
  print(text.get_text())
  print("Author: " ,end="")
  print(author.get_text())
  print("Tags: " ,end="")
  for i in tag_list:
    print(i,end=' ')
  print()
  print()