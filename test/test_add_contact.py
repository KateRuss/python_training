# -*- coding: utf-8 -*-

from model.contact import Contact
from fixtura.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new(Contact(first_name="testFirstName", last_name="TestLastName",
                                   address="jgjvhzjvjzvjv 887878", home_phone_number="765787657888",
                                   mobile_phone_number="88599485", work_phone_number="886945694565476",
                                   fax_number="84584758", email_1="dgkjgjgkdgk", email_2="kjhfkdhkhf",
                                   email_3="kjxkjxlhj"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new(Contact(first_name="", last_name="",
                                   address="", home_phone_number="",
                                   mobile_phone_number="", work_phone_number="",
                                   fax_number="", email_1="", email_2="",
                                   email_3=""))
    app.session.logout()

if __name__ == "__main__":
    unittest.main()
