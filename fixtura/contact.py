
class ContactHelper:
    def __init__(self, app):
        self.app = app

    def contact_information(self, contact):
        wd = self.app.wd
        # fill contact fields (displayd on home page)
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.first_name)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.last_name)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone_number)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone_number)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone_number)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_number)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email_2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email_3)

    def create_new(self, contact):
        wd = self.app.wd
        # create new contact
        wd.find_element_by_link_text("add new").click()
        self.contact_information(contact)
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
        self.contact_information(contact)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.app.return_to_home_page()