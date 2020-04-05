import re
from random import randrange

def test_all_contact_from_homepage(app):
    contacts = app.contact.get_contact_list()
    index = randrange(len(contacts))
    contact_from_homepage = app.contact.get_contact_list()[index]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_homepage.first_name == contact_from_editpage.first_name
    assert contact_from_homepage.last_name == contact_from_editpage.last_name
    assert contact_from_homepage.address == contact_from_editpage.address
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_editpage)
    assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_home_page(contact_from_editpage)



def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.home_phone_number,
                                                                               contact.mobile_phone_number,
                                                                               contact.work_phone_number]))))
def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x!="", filter(lambda x: x is not None, [contact.email_1, contact.email_2,
                                                    contact.email_3])))