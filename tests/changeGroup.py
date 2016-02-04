from model.group import Group


def test_change_group(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.change((Group(name="changedGroup", header="changedHeader", footer="changedFooter")))
    app.group.return_to_groups_page()
    app.session.logout()
