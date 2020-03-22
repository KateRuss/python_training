#author - E.Rusetskaya

class Contact:

    def __init__(self, first_name = None, last_name = None, address= None, home_phone_number= None,
                 mobile_phone_number= None, work_phone_number= None, fax_number= None, email_1= None, email_2= None,
                 email_3= None, address2 = None, notes = None):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.home_phone_number = home_phone_number
        self.mobile_phone_number = mobile_phone_number
        self.work_phone_number = work_phone_number
        self.fax_number = fax_number
        self.email_1 = email_1
        self.email_2 = email_2
        self.email_3 = email_3
        self.address2 = address2
        self.notes = notes