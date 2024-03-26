"""
Atributes come after tab name, so you might see like this - 
<div class> </div> - so here class is an attribute,
and we might see multiple <div class> tags in the page, but there is where attribute comes in,
it makes that particular tag unique with its own defintion
"""

import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')

# Getting Attribute
tag = soup.header.a
print(tag)
print(tag.attrs) # here in output we are gonna get the Attrubute names as keys in the dict

# now as above is dict, so we can get the value of it as well
print(tag.attrs["data-bs-toggle"])

# as above is dict, so we can perform dict methods, so we can add a new attribute as well
tag.attrs["Test-attr"] = "Custom test tag"
# Checking attribute dict again after adding a new key value in it.
print(tag.attrs)

"""
In HTML if we want to get the comments, then comments look like this -
<!-- This is a comment -->
"""