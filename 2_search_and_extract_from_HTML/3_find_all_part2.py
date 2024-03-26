import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

res = requests.get(url)

soup = BeautifulSoup(res.text, "lxml")

"""
Earlier I wanted to find_all p tag and h4, so I used find on each, 
but we can even get these tags with one go as well.
we just need to give list
"""
print(soup.find_all(["p", "h4"]))

print()
# we can use Boolean to find something as well
# like there is some tag - <div id="cookieBanner" style="display: none;">
# and I want to get all the tags with id attribute
print(soup.find_all(id = True))

# and in the website there are some products, and there are like 3 product with name Iphone.
# then we can get all the pro
print(soup.find_all(string="Iphone")) # so it basically trying to find in all tags where string is equal to Iphone
# we can even find it with regular expression
import re
print(soup.find_all(string= re.compile("Iph")))

print()
# find_all gives all the result but we can also limit it
# like I want first 3 results
print(soup.find_all("h4", class_ = re.compile("float-end"), limit=3) ) # specifying limtt
