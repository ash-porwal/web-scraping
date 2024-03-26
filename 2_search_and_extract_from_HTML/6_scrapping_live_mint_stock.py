import requests
from bs4 import BeautifulSoup
url = "https://www.livemint.com/market/market-stats/"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, "lxml")

gainer_box = soup.find("div", {"id": "market-box-4"})
print(gainer_box)

stock_prices = gainer_box.find_all("div", class_="price")
all_price = []
for each_price in stock_prices:
    price = each_price.text
    all_price.append(price.strip())


stock_names = gainer_box.find_all("div", class_="sName")

all_name = []
for each_name in stock_names:
    name= each_name.text
    all_name.append((name.strip()))

# df
temp_dict = {
    "Stock name": all_name,
    "Stock price": all_price
}
import pandas as pd
print(pd.DataFrame(temp_dict))