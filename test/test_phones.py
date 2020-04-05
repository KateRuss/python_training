import re


def test_phones_on_homepage(app):
    contact_from_homepage = app.contact.get_contact_list()[0]
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_homepage.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_editpage)


def test_phones_on_contact_view_page(app):
    contact_from_view = app.contact.get_contact_from_view_page(0)
    contact_from_editpage = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view.home_phone_number == contact_from_editpage.home_phone_number
    assert contact_from_view.mobile_phone_number == contact_from_editpage.mobile_phone_number
    assert contact_from_view.work_phone_number == contact_from_editpage.work_phone_number


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x), filter(lambda x: x is not None,
                                                                              [contact.home_phone_number,
                                                                               contact.mobile_phone_number,
                                                                               contact.work_phone_number]))))















