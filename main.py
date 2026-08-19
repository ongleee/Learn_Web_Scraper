import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"

response = requests.get(url)

print(response.status_code)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')

quote = soup.find("div", class_="quote")
text = quote.find("span", class_="text")

print(text.text)

author = quote.find("small", class_="author")
print(author.text)