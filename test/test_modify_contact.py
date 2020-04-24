# -*- coding: utf-8 -*-

from model.contact import Contact
from random import randrange
import pytest

@pytest.mark.ui_tests
def test_edit_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contact(first_name="contact_name", last_name="last_name"))
    old_contacts = db.get_contact_list()
    contact = Contact(first_name="бла-бла-бла_new", last_name="TestLastName", mobile_phone_number="88599485")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.contact_count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)