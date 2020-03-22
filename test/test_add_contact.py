# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create_new(Contact(first_name="testFirstName", last_name="TestLastName",
                                   address="jgjvhzjvjzvjv 887878", home_phone_number="765787657888",
                                   mobile_phone_number="88599485"))


def test_add_empty_contact(app):
    app.contact.create_new(Contact())

