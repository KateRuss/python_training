# Ekaterina Rusetskaya
# 24.02.20


from selenium import webdriver
from fixtura.session import SessionHelper
from fixtura.group import GroupHelper
from fixtura.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == 'Firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'Chrome':
            self.wd = webdriver.Chrome()
        elif browser == 'ie':
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(2)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        if wd.current_url is not self.base_url:
            wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        if wd.current_url is not "http://localhost/addressbook/":
            wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()
