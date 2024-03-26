import requests
from bs4 import BeautifulSoup

# so in this website https://webscraper.io/test-sites/e-commerce/allinone/phones/touch
# we are extracting things one by one, like inside one box of product, we are gettin title, prices and all
# what if I want to extract all of these in one go?
# so instead of using soup - which uses entire HTML, we can simply use HTML of the box where all data is available.
url = "https://webscraper.io/test-sites/e-commerce/allinone/phones/touch"

res = requests.get(url=url)
soup = BeautifulSoup(res.text, "lxml")

# now I went to website and look for the tag which covers the entire box
# and this is the tag - <div class="card product-wrapper thumbnail"> which covers this box
boxes = soup.find_all("div", class_="card product-wrapper thumbnail")
# so on this website we have total 9 products, covered in 9 boxes.
# so we can check the length of these which we just fetched
print(len(boxes)) # and we got 9 boxes
print()
# so, each can use index to get for particular box data
print(boxes[0]) # and noticing navigable string, and can see it covers all the details which we fetched earlier.

# now further we can use the find function
print()
print("Price of first product:")
print(soup.find("h4").text)