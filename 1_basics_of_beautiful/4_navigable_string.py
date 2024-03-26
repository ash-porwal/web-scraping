"""
Navigable string is just a string corresponding to a text within a text

For example - on webpage below is one tag which is carrying string
    <p>Web Scraper</p>

How can we get this string from inside a tag?
"""

# To get the string, noticed where is this <p> tag,
# this <p> tag is under <header> tag, which actually containing the whole info about page on the current website.

import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

# Getting Navigable string
print(soup.header) # look for <p> tag in the print output

# if we have p tag in above print, so we can just get it
print()
print("-"*8)
print(soup.header.p)
print(soup.header.p.string) # to extract just string within the tag
print("-"*8)
print()

