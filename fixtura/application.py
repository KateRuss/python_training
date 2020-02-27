# Ekaterina Rusetskaya
# 24.02.20


from selenium import webdriver
from fixtura.session import SessionHelper
from fixtura.group import GroupHelper
from fixtura.contact import ContactHelper

class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home page").click()


    def destroy(self):
        self.wd.quit()
