from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.contact_count:
        app.contact.create_new(Contact(first_name="contact_name", last_name="last_name"))

    old_contacts = app.contact.get_contact_list()
    contact = Contact(first_name="testFirstName", last_name="TestLastName",
                      address="jgjvhzjvjzvjv 887878", home_phone_number="765787657888",
                      mobile_phone_number="88599485")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
