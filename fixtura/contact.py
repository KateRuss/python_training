from model.contact import Contact

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

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # delete element
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit element delete
        wd.switch_to.alert.accept()

    def delete_all_contact(self):
        wd = self.app.wd
        wd.find_element_by_id("MassCB").click()
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit contact delete
        wd.switch_to.alert.accept()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        # select first contact for edit
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # edit contact
        self.fill_contact_form(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.return_to_home_page()

    def contact_count(self):
        wd = self.app.wd
        self.app.return_to_home_page()
      #  self.app.return_to_home_page()
        if wd.find_element_by_xpath("//span[@id='search_count']") == 0:
            return True

    def get_contact_list(self):
        wd = self.app.wd
        self.app.return_to_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            row = element.find_elements_by_tag_name("td")
            last_name = row[1].text
            name = row[2].text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(last_name=last_name, first_name=name, id=id))
        return contacts

