# We will try to scrap some web scraping test sites
# https://webscraper.io/test-sites (or just google - Web Scraping test sites)

# So, I will try to get HTML content from this site -https://webscraper.io/test-sites/e-commerce/allinone/computers
# for this we will need requests to fetch HTML content and beautifulsoup4 library

import requests
from bs4 import BeautifulSoup

# now, to get the HTML content, we need that web page URL.
# which we already have - https://webscraper.io/test-sites/e-commerce/allinone/computers
url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"

response = requests.get(url=url)
print(response.text) # here we can get the HTML content if status code is 200

# now we want to parse above HTML content, so for this we need Beautifulsoup
soup = BeautifulSoup(response.text, 'lxml') # passing lxml parser - so what happens actually is, response.text gives us String format of HTML content, and lxml makes that String into back to HTML format
print()
print("-----Format-----")
print()
print(soup)