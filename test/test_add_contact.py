# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest
import re



@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_new(contact)
    assert len(old_contacts) + 1 == app.contact.contact_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_add_empty_contact(app):
#     app.contact.create_new(Contact())
