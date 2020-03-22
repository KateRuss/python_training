from model.contact import Contact


def test_delete_first_contact(app):
    if app.contact.contact_count:
        app.contact.create_new(Contact(first_name="contact_name", last_name="last_name"))
    app.contact.delete_first_contact()

# !!! it work but you should run it last!!!
# def test_delete_all_contact(app):
#     app.contact.delete_all_contact()
#     app.session.logout()

