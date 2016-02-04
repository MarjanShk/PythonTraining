def test_delete_firstGroup(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.group.open_group_page()
    app.group.delete()
    app.group.return_to_groups_page()
    app.session.logout()
