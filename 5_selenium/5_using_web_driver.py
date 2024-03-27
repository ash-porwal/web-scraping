"""
find_element vs. find_elements

- find_element: 
    This method is used when you expect only a single element to be returned. 
    It returns the first element matching the specified locator. 
    If no elements are found, a NoSuchElementException will be raised.

- find_elements: 
    This method is used when you expect multiple elements to be returned. 
    It returns a list of all elements matching the specified locator. 
    If no elements are found, an empty list is returned.


"""

from selenium import webdriver # provides all the WebDriver implementations.
from selenium.webdriver.common.keys import Keys # The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.by import By # The By class is used to locate elements within a document.

driver = webdriver.Chrome()
driver.get("http://quotes.toscrape.com/js/")

# Now I want to get data from a tag
# There are various strategies to locate elements in a page.
# like in beautiful soup we have find and find_all
# in Selenium we have find_element and find_elements
# WebDriver offers a number of ways to find elements using the find_element method.
elem = driver.find_elements(By.CLASS_NAME, "text") # getting data of tag - <span class="text">
for each_quote in elem:
    print(each_quote.text)
driver.close()
