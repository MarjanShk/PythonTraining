def test_delete_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.delete_contact()
    app.session.logout()