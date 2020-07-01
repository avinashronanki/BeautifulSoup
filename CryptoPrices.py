from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import requests
import random

cmc = requests.get("https://coinmarketcap.com/")
soup = bs(cmc.content, 'html.parser')
print(soup.title) # title of the page

# Parsing the website

print(soup.prettify())

#
data =  soup.find ('script', id = "__NEXT_DATA__")