# -*- coding: utf-8 -*-
from model.contact import Contact


def test_addNewContact(app):
    app.open_home_page()
    app.session.login(username="admin", password="secret")
    app.contact.open_add_contact_page()
    app.contact.create_contact(Contact(firstname ="firstname",middlename ="middlename",
                                        lastname ="lastname",nickname ="nickname",
                                        title ="title",company ="company",
                                        address ="address",home ="home",
                                        mobile ="0964545777",work ="777777",
                                        fax ="fax",email ="email@example.com",
                                        email2 ="email2@example.com",email3 ="email3@example.com",
                                        byear ="1995",homepage ="www.example.com",
                                        address2 ="address2",
                                        phone2 ="0933434555",
                                        notes ="notes"))
    app.session.logout()


