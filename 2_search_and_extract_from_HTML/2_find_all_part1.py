import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

res = requests.get(url=url)

soup = BeautifulSoup(res.text, "lxml")

# lets aim to get all the prices of all product directly from above web page.
print(soup.find_all("h4", class_ = "float-end price card-title pull-right")) # now this returned a list of all product within a tag

print()
# lets try to extract the name of the prodcuts 
print(soup.find_all("a", class_ = "title"))

# now extracting the 
# for each_tag in soup.find_all("h4", class_ = "float-end price card-title pull-right"):
#     print(soup.h4)