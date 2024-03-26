import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://webscraper.io/test-sites/e-commerce/allinone/phones/touch'

res = requests.get(url=url)
soup = BeautifulSoup(res.text, "lxml")

# find() - syntax - .find('tag_you_want_to_find')
# find is a powerful function, is the main function to search throughout the HTML
# this time we are going to use find function to find the header tag
print(soup.find('header'))

# now, if we have many the same tags then we can pass attribute as well to find the tag
# like earlier we find attribute like this -
print(soup.header.attrs)
print()
# and with find we can specify attribtute like this - but we need to know about the tag name and attribute - <div class="container test-site"> 
# so above is div tag and attribute is container test-site, so we will specify attribute like in a dictionary
print(soup.find('div', {"class":"container test-site"})) # syntax - soup_var_name.find("header_name", {"attribute_name": "value_of_that_attr"})

# there is another way to find the value of this class attribute, but keep in mind that it just works with class attribute
print(soup.find('div', class_ = "container test-site"))

print()
# lets aim to find out price of product
print(soup.find('h4', class_ = "float-end price card-title pull-right")) # from website I got to know about tag name and attribute and value.

# but there is other product which has price $57.99 and on analysing I noticed that is the same tag with same attribute, then how can we fetch the other product price?
# so, for this we can't use find function, and for this we use find_all()