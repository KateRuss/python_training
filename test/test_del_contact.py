from model.contact import Contact
from random import randrange

def test_delete_some_contact(app):
    if app.contact.contact_count() == 0:
        app.contact.create_new(Contact(first_name="contact_name", last_name="last_name"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.contact_count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] =[]
    assert old_contacts == new_contacts

# !!! it work but you should run it last!!!
# def test_delete_all_contact(app):
#     app.contact.delete_all_contact()
#     app.session.logout()

