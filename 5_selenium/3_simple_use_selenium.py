from selenium import webdriver # provides all the WebDriver implementations.
from selenium.webdriver.common.keys import Keys # The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.by import By # The By class is used to locate elements within a document.

# creating instance of web browser
driver = webdriver.Chrome()

# The driver.get method will navigate to a page given by the URL. 
driver.get("http://quotes.toscrape.com/js/")
