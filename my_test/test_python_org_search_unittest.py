import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class python_org_search(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()

    def test_python_org_search(self):
        wd = self.wd
        wd.get("https://www.python.org")
        self.assertIn("Python", wd.title)
        q = wd.find_element_by_name("q")
        q.send_keys("pycon")
        q.send_keys(Keys.RETURN)
        assert "No results found." not in wd.page_source

    def tearDown(self):
        self.wd.close()


if __name__ == "__main__":
    unittest.main()

