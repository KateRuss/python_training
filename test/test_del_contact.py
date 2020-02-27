def test_delete_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete_first_contact()
    app.session.logout()

# !!! it work but you should run it last!!!
# def test_delete_all_contact(app):
#     app.session.login(username="admin", password="secret")
#     app.contact.delete_all_contact()
#     app.session.logout()

