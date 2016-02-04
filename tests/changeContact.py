from model.contact import Contact


def test_change_contact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.change_contact(Contact(firstname ="changed_firstname",middlename ="changed_middlename",
                                        lastname ="changed_lastname",nickname ="changed_nickname",
                                        title ="title",company ="company",
                                        address ="changed_address",home ="home",
                                        mobile ="000000000",work ="777777",
                                        fax ="fax",email ="changed_email@example.com",
                                        email2 ="email2@example.com",email3 ="email3@example.com",
                                        byear ="1995",homepage ="www.example.com",
                                        address2 ="address2",
                                        phone2 ="0933434555",
                                        notes ="notes"))
    app.session.logout()