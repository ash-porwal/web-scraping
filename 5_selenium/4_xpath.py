"""
So, what is this xpath?
If I want the xpath of some quote from this website - http://quotes.toscrape.com/js/
Then to get this, we need to Open inspect and with arrow, look for the element you want
then right click, the tag which contains data: right click on tag and copy the xpath

like this tag: <span class="text"> has xpath -> /html/body/div/div[2]/span[1]

And xpath is path expression to navigate through HTML/XML
"""

# once we get xpath, then we can get that element

from selenium.webdriver.common.by import By

"""
The attributes available for the By class are used to locate elements on a page. 
These are the attributes available for By class:

ID = "id"
NAME = "name"
XPATH = "xpath"
LINK_TEXT = "link text"
PARTIAL_LINK_TEXT = "partial link text"
TAG_NAME = "tag name"
CLASS_NAME = "class name"
CSS_SELECTOR = "css selector"

The 'By' class is used to specify which attribute is used to locate elements on a page. 
These are the various ways the attributes are used to locate elements on a page:

find_element(By.ID, "id")
find_element(By.NAME, "name")
find_element(By.XPATH, "xpath")
find_element(By.LINK_TEXT, "link text")
find_element(By.PARTIAL_LINK_TEXT, "partial link text")
find_element(By.TAG_NAME, "tag name")
find_element(By.CLASS_NAME, "class name")
find_element(By.CSS_SELECTOR, "css selector")

If you want to locate several elements with the same attribute replace find_element with find_elements.
"""

"""
For instance, consider this page source:

<html>
 <body>
  <form id="loginForm">
   <input name="username" type="text" />
   <input name="password" type="password" />
   <input name="continue" type="submit" value="Login" />
  </form>
 </body>
</html>

The form element can be located like this:

login_form = driver.find_element(By.ID, 'loginForm')
"""