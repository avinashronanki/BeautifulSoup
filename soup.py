from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random

# #
# page = requests.get("http://quotes.toscrape.com/")
#
# soup = bs(page.content, 'html.parser')
# # inspect the class name on webiste
# txt = soup.find_all(class_='text')
# #print(txt)
#
# # exclude the unnecessary code
# quotes = [i.text for i in soup.find_all(class_='text')]
# print(quotes)
#
# #Authors
# authors = [i.text for i in soup.find_all(class_='author')]
# print(authors)
#
#
# # Multiple pages
# urls=[f"http://quotes.toscrape.com/page/{i}/" for i in range(1,11)]
# print(urls )
#
# # Avoiding Web Scraping Detection
# rate = [i/10 for i in range(10)]
# time.sleep(random.choice(rate))

# List of Authors and Quotes
authors = []

quotes = []

# List of URLs
urls = [f"http://quotes.toscrape.com/page/{i}/" for i in range(1, 11)]

# List for Randomizing our request rate
rate = [i / 10 for i in range(10)]

# Iterating through the URLS
for url in urls:

    # Accessing the Webpage
    page = requests.get(url)

    # Getting the webpage's content in pure html
    soup = bs(page.content,features="lxml")

    # Adding the authors and quotes to their lists
    authors.extend([i.text for i in soup.find_all(class_='author')])

    quotes.extend([i.text for i in soup.find_all(class_='text')])

    # Checking to see if we hit our required number of quotes then breaking the loop
    if len(quotes) >= 52:
        break

    # Randomizing our request rate
    time.sleep(random.choice(rate))

print(authors)