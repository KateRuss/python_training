from model.contact import Contact
from random import randrange
import pytest
import random


@pytest.mark.ui_tests
def test_delete_some_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_new(Contact(first_name="contact_name", last_name="last_name"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)



# !!! it work but you should run it last!!!
# def test_delete_all_contact(app):
#     app.contact.delete_all_contact()
#     app.session.logout()

