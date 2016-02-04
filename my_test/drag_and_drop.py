import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains

class drag_and_drop(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Firefox()

    def test_drag_and_drop(self):
        wd = self.wd
        wd.get("http://localhost:8083/pageForTest/drag.html")
        el = wd.find_element_by_id("el")
        target = wd.find_element_by_id("target")
        drag = ActionChains(wd)
        drag.drag_and_drop(el, target).perform()

    def tearDown(self):
        self.wd.close()

if __name__ == "__main__":
    unittest.main()