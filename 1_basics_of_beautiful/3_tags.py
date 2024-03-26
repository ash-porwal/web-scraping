# tags in HTML represnts like <>, so if a tag starts and it will carry the Data and then tag will get closed.
# now lets try to extract tags

import requests
from bs4 import BeautifulSoup

url = "https://webscraper.io/test-sites/e-commerce/allinone/computers"
response = requests.get(url=url)
soup = BeautifulSoup(response.text, 'lxml')
# print(soup)

# on printing above line, I noticed there are tags written, so I want to get the content of <header> 
# for this I will do - 
# variable_name_of_beautifulsoup.tag_name
print(soup.header)
