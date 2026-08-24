import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urljoin

# url = "https://quotes.toscrape.com/"


# print(response.status_code)
# print(response.text)





def scrape_page(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.text, 'html.parser')
  response.raise_for_status()
  quotes = soup.find_all("div", class_="quote")
  quotes_data = []

  
  for quote in quotes:
    tags = quote.find_all("a", class_="tag")
    tag_list = []
    for tag in tags:
      tag_list.append(tag.get_text())

    text = quote.find("span", class_="text")
    author = quote.find("small" , class_="author")

    data = {
      "quote": text.get_text(),
      "author": author.get_text(),
      "tags": ", ".join(tag_list)
    }

    quotes_data.append(data)

  nextbutton = soup.find("li", class_="next")
  if nextbutton:
    next_a = nextbutton.find("a")
    next_url = urljoin(url,next_a["href"])
  else:
    next_url = None

  
  return quotes_data,next_url

all_quotes = []
page = 1

url = "https://quotes.toscrape.com/"

while url:
  data, next_url = scrape_page(url)
  all_quotes.extend(data)

  print(f"Scraped: {len(data)} quotes")

  url = next_url

print(len(all_quotes))

print("===== QUOTE SCRAPER =====")
with open("quotes.csv","w", newline="", encoding="utf-8") as file:
  fieldnames = ["quote", "author", "tags"]
  writer = csv.DictWriter(file, fieldnames=fieldnames)

  writer.writeheader()

  writer.writerows(all_quotes)

print()
print(all_quotes)