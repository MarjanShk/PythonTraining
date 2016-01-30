class GroupHelper:

    def __init__(self, app):
            self.app = app

    def open_group_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("Групи").click()

    def create(self, Group):
            wd = self.app.wd
            wd.find_element_by_name("new").click()
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(Group.name)
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(Group.header)
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(Group.footer)
            wd.find_element_by_name("submit").click()

    def return_to_groups_page(self):
            wd = self.app.wd
            wd.find_element_by_link_text("Групи").click()

