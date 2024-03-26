import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

res = requests.get(url=url)

soup = BeautifulSoup(res.text, "lxml")

# Getting all product title tags
product_title_tag = soup.find_all("a", class_ = "title")
print(product_title_tag)

print()
# Getting all prodcut prices
product_prices_tag = soup.find_all("h4", class_="float-end price card-title pull-right")
print(product_prices_tag)

# Now extracting the strings
final_title_list = []
for each_title  in product_title_tag:
    print(each_title.text) # getting navigable string with .text
    final_title_list.append(each_title.text)
print()

final_price_list = []
for each_prices in product_prices_tag:
    print(each_prices.text)
    final_price_list.append(each_prices.text)


final_desc = []
for each_desc in soup.find_all("p", class_ = "description card-text"):
    final_desc.append(each_desc.text)

# Making Pandas df out of these lists we got
import pandas as pd

#we will make dict out of these values
temp_dict = {
    "Product": final_title_list,
    "Price": final_price_list,
    "Description": final_desc
}
final_df = pd.DataFrame(temp_dict)
print(final_df)

