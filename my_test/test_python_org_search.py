from selenium import webdriver
from selenium.webdriver.common.keys import Keys
wd = webdriver.Firefox()
wd.get("http://www.python.org")
assert "Python" in wd.title
el = wd.find_element_by_name("q")
el.send_keys("pycon")
el.send_keys(Keys.RETURN)
assert "No results found." not in wd.page_source
wd.close()
