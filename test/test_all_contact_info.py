import re
from model.contact import Contact

def test_all_contact_info_from_homepage(app, db):
    contacts_from_homepage = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)

    for contact_from_homepage in contacts_from_homepage:
        for contact_from_db in contacts_from_db:
            if contact_from_homepage.id == contact_from_db.id:
                assert contact_from_homepage.first_name ==contact_from_db.first_name
                assert contact_from_homepage.last_name == contact_from_db.last_name
                assert contact_from_homepage.address == contact_from_db.address
                assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(
                    contact_from_db)
                assert contact_from_homepage.all_emails_from_homepage == merge_emails_like_on_home_page(
                    contact_from_db)

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