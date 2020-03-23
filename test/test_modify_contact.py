from model.contact import Contact


def test_edit_first_contact(app):
    if app.contact.contact_count():
        app.contact.create_new(Contact(first_name="contact_name", last_name="last_name"))
    app.contact.edit_first_contact(Contact(first_name="edit_name_my_name",last_name="vjvh",
                                           mobile_phone_number="222222222222",))
