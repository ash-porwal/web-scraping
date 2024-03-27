"""
doc - https://selenium-python.readthedocs.io/installation.html

Selenium - 
- It is a browser automation tool
- with selenium we can evalute JS and get the content.
- so, selenium is going to open up its own controlled browser (like - Google Chrome)
- Selenium is a web scraping library just like Beautifulsoup

With Selenium we can -
- Click on a button
- Send text to an input box
- create wait time for the page to load
- we can take Screenshot
- self scrolling

"""
"""
Installing selenium 

- pip install selenium --break-system-packages

and with above installion we need drives as well
Drivers - 
Selenium requires a driver to interface with the chosen browser. 
Firefox, for example, requires geckodriver, which needs to be installed before the below examples can be run. 
Make sure it's in your PATH, e. g., place it in /usr/bin or /usr/local/bin.

Chrome:
# download based on chrome version we are using
https://chromedriver.chromium.org/downloads

Edge:

# download based on edge version we are using
https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/

Firefox:

# download based on firefox version we are using
https://github.com/mozilla/geckodriver/releases

Safari:

# download based on safari version we are using
https://webkit.org/blog/6900/webdriver-support-in-safari-10/


once download above file, we need to put it into a file path
"""

"""
No stable Selenium Chrome Webdriver for the latest Google Chrome version according to the availability matrix


If you are using Chrome version 115 or newer you have to check the Chrome for Testing availability dashboard
which provides convenient JSON endpoints for specific ChromeDriver version downloading.

Selenium Manager ->
With the availability of Selenium v4.6 and above you don't need to explicitly download ChromeDriver, 
GeckoDriver or any browser drivers as such. 
You just need to ensure that the desired browser client i.e. google-chrome, firefox or microsoft-edge is installed.

Selenium Manager is the new tool integrated with selenium4 that would help to get a working webdriver 
version to run Selenium out of the box. 
Beta 1 of Selenium Manager will configure the browser drivers for Chrome, Firefox, and Edge if they are not present on the PATH.
"""
# I just installed selenium with pip - pip install selenium
# and didnt specifically installed any web browser or selenium manager
# now testing webdriver

from selenium import webdriver

driver = webdriver.Chrome() # this opens up web browser - we specified chrome so will open chrome
driver.get("https://github.com/ash-porwal") # and want to open some link
