"""
Till now we were fetching data from the current page,
If we want to go to the next page and get the next page data then?
"""
# So, from this page - https://ww5.pogolinks.yachts/movies/
# First i want the data of all hotels and prices from page 1
# and then later going to the next page

import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://ww5.pogolinks.yachts/movies/"
res = requests.get(url=url)
print(res.status_code)
soup = BeautifulSoup(res.text, "lxml")

# now, to go on next page from UI, either we need to clikc on arrow button or click on numbers
# but in Beautifulsoup clicking on the button is not possible - for this we need Selenium
# so, for now - how do we go on next page by clicking on Page number?
# so, if we inspect this then there will be a link to go on the next page
# like this < a href="https://ww5.pogolinks.yachts/movies/page/2/" class="inactive">
# so now we need to extract the URL
next_page_tag = soup.find("a", class_ = "inactive")
print(next_page_tag)

# extract href link - 
print(next_page_tag.get('href')) # notice: sometimes next page href doesn't contains domain name, so we can make it from our own side

# now again we can set url to next_page url and get the response of it.