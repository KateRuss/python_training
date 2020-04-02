# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="testFirstName", last_name="TestLastName",
                                   address="jgjvhzjvjzvjv 887878", home_phone_number="765787657888",
                                   mobile_phone_number="88599485")
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.contact_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_empty_contact(app):
    app.contact.create_new(Contact())

