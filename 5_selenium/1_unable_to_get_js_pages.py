# http://quotes.toscrape.com/js/
# we cant webscrape javascripte driven web page

import requests
from bs4 import BeautifulSoup
url = "http://quotes.toscrape.com/js/"

res = requests.get(url=url)
# print(res.text)

soup = BeautifulSoup(res.text, "lxml")
print(soup)

# now I want to get this tag data
# <div class= "quote">
print()
print(soup.find_all("div", class_ = "quote")) # it is empty

"""
article - https://blog.teclado.com/why-scraping-fail-requests-beautifulsoup-python/#:~:text=When%20we%20make%20a%20request,%2C%20well%2C%20running%20the%20JavaScript.

How does actually requets work?

When you load up a website you want to scrape using your browser, 
the browser will make a request to the page's server to retrieve the page content. 
That's usually some HTML code, some CSS, and some JavaScript.

When we are doing web scraping, all we're interested in is the HTML. 
That's because the HTML usually contains all the information in the page. 
CSS is used to perform styling, and our scraping programs don't care what the page looks like.

So we load the HTML using the requests mode, and parse it using BeautifulSoup... 
and voilà! We have the information we need and we can feed it to our programs.

A key difference between loading the page using your browser and getting the page contents using requests is that your browser executes any JavaScript code that the page comes with. Sometimes you will see the initial page content (before the JavaScript runs) for a few moments, and then the JavaScript kicks in.
When we make a request for page content using requests, the JavaScript does not run. Therefore, you would only see the initial page.

Now, we can overcome this with library - Selenium
"""