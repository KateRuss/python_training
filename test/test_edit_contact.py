from model.contact import Contact


def test_edit_first_contact(app):
    app.contact.edit_first_contact(Contact(first_name="edit_name_1",last_name="",address="edit_address",
                                         home_phone_number="565656565664333",mobile_phone_number="887878787",
                                         work_phone_number="",fax_number="123",email_1="aaaa@m.r",
                                         email_2="hhhh",email_3=""))
