def test_delete_first_contact(app):
    app.contact.delete_first_contact()

# !!! it work but you should run it last!!!
# def test_delete_all_contact(app):
#     app.contact.delete_all_contact()
#     app.session.logout()

