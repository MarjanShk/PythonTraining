# -*- coding: utf-8 -*-
from model.group import Group


def test_addGroup(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.create(Group(name="myGroup", header="myGroupHeader", footer="myGroupFooter"))
    app.group.return_to_groups_page()
    app.session.logout()
