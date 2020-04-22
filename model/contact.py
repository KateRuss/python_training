#author - E.Rusetskaya
from sys import maxsize
class Contact:

    def __init__(self, first_name = None, last_name = None, address= None, home_phone_number= None,
                 mobile_phone_number= None, work_phone_number= None, fax_number= None, all_phones_from_home_page=None,
                 all_emails_from_homepage = None, email_1= None, email_2= None, email_3= None, address2 = None,
                 notes = None, id = None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.home_phone_number = home_phone_number
        self.mobile_phone_number = mobile_phone_number
        self.work_phone_number = work_phone_number
        self.fax_number = fax_number
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_homepage = all_emails_from_homepage
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.address2 = address2
        self.notes = notes
        self.id = id


    def __repr__(self):
        return "%s:%s:%s:%s:%s:" % (self.id, self.first_name, self.last_name, self.address, self.home_phone_number)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize