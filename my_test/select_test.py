import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select


class select_test(unittest.TestCase):

    def setUp(self):
        self.wd = webdriver.Firefox()

    def test_select(self):
        wd = self.wd
        wd.get("http://localhost:8081/addressbook/")
        wd.find_element_by_name("user").send_keys("admin")
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_name("pass").submit()
        select = Select(wd.find_element_by_name("to_group"))
        select.select_by_index(1)

    def tearDown(self):
        self.wd.close()

if __name__ == "__main__":
    unittest.main()