from model.contact import Contact
from random import randrange

def test_edit_some_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.create_new(Contact(first_name="contact_name", last_name="last_name"))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="бла-бла-бла", last_name="TestLastName",
                      address="jgjvhzjvjzvjv 887878", home_phone_number="765787657888",
                      mobile_phone_number="88599485")
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.contact_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
