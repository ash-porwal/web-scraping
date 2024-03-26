"""
Applications - 

    - Web scraping is great for getting financial data fast 
      it is used all around the world to get numbers in stocks, balance sheet etc.
      if we see a website where stock prices are up to date then they might be using web scraping from like stock exchange to update those prices on website.

    - Scraping prices for reviews at a restaurant or hotel - to get the best deal and compare the prices of different hotels
      same goes with skyscrapper website which compares flight prices

    - If some product is in demand maybe because of resell price, and we wait for the product to get drop in their store, so we can web scrape it
      and whenever there is a new product available in their store then it buys right away.

    - Web scraping is useful for getting data from machine learning.

    - We can scrape social medie accounts as well - like snapchat, insta, FB
"""

"""
What is Web Scraping?

    - It refers to extraction of data from a website.
    - While web scraping can be done manually we will use code to create an automated process (Known as web crawer or bot) to obtain data.

    - Two parts to web scraping:
        1. Fetching - downloading of a page (which a browser does when a user views a page)
        2. Extraction - when content of a page if parsed, searched, or reformatted to obtain peiecs of data

- We can web scrape almost like 99% of websites online, but there are some sites which may have protective measures 
  to ensure that the bot is not accessing their site or extracting data from it.
  Example - Email websites(bell, gmail, outlook).

-  Also whenever we see checbox with "I am not a robot" is to ensure that web screapers like us cant access the site and scrape the data.
- If website sees suspicious activity they will suspend us from the site, example - Instagram
"""

# Packages we need

"""
1. Beautifulsoup - used to pulling data out of HTML or XML
   pip install beautifulsoup4 --break-system-packages

2. After beautifulsoup we need Parser
   pip install lxml --break-system-packages.

3. Then we need requests library
   pip install requests --break-system-packages.
"""
