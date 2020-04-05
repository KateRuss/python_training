# -*- coding: utf-8 -*-
from model.contact import Contact
import random
import string
import pytest
import re



def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits + " "
    return prefix + "".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


testdata = [Contact(first_name=random_string("first_Name:", 20), last_name=random_string("Last_name:", 20),
                    address=random_string("address:", 20), home_phone_number=random_string("H:", 20),
                    mobile_phone_number=random_string("M:", 20), work_phone_number=random_string("W:", 20),
                    email_1=random_string("E1:", 25), email_2=random_string("E2:", 25), email_3=random_string("E3:", 10))
    for i in range(5)
]


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
