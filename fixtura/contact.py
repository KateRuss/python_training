from model.contact import Contact
import re

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill contact fields (displayd on home page)
        self.change_contact_field("firstname", contact.first_name)
        self.change_contact_field("lastname", contact.last_name)
        self.change_contact_field("address", contact.address)
        self.change_contact_field("mobile", contact.mobile_phone_number)
        self.change_contact_field("work", contact.work_phone_number)
        self.change_contact_field("fax", contact.fax_number)
        self.change_contact_field("email", contact.email_1)
        self.change_contact_field("emai2", contact.email_2)
        self.change_contact_field("emai3", contact.email_3)
        self.change_contact_field("address2", contact.address2)
        self.change_contact_field("notes", contact.notes)

    def change_contact_field(self, fild_name, value):
        if value is not None:
            wd = self.app.wd
            wd.find_element_by_name(fild_name).click()
            wd.find_element_by_name(fild_name).clear()
            wd.find_element_by_name(fild_name).send_keys(value)

    def create_new(self, contact):
        wd = self.app.wd
        # create new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_contact_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_for_del_by_index(index)
        # delete element
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit element delete
        wd.switch_to.alert.accept()
        wd.implicitly_wait(3)
        self.contact_cache = None

    def select_contact_for_del_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_all_contact(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit contact delete
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.edit_contact_by_index(0, contact)


    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # edit contact
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.return_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.return_to_home_page()
        wd.find_elements_by_xpath("//img[@alt='Details']")[index].click()

    def contact_count(self):
        wd = self.app.wd
        self.app.return_to_home_page()
      #  self.app.return_to_home_page()
        #if wd.find_element_by_xpath("//span[@id='search_count']") == 0:
        return int(wd.find_element_by_xpath("//span[@id='search_count']").text)

    contact_cache = None
    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.return_to_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):
                cells = row.find_elements_by_tag_name("td")
                last_name = cells[1].text
                name = cells[2].text
                id = cells[0].find_element_by_tag_name("input").get_attribute("value")
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(last_name=last_name, first_name=name, address = address, id=id,
                                                  all_emails_from_homepage=all_emails,
                                                  all_phones_from_home_page=all_phones))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(first_name=firstname, last_name=lastname, id=id, home_phone_number=homephone,
                       mobile_phone_number=mobilephone,work_phone_number=workphone, address=address, email_1=email1,
                       email_2=email2, email_3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        return Contact(home_phone_number=homephone, mobile_phone_number=mobilephone, work_phone_number=workphone)


