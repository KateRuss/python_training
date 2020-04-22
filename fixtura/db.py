import pymysql.cursors
from model.group import Group
from model.contact import Contact

class Dbfixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list=[]
        cursor=self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, home, mobile, work, email, email2, email3 from addressbook")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, email2, email3) = row
                list.append(Contact(id=str(id), first_name=firstname, last_name=lastname, address=address,
                                    home_phone_number=home, mobile_phone_number=mobile, work_phone_number=work,
                                    email_1=email, email_2=email2, email_3=email3))
        finally:
            cursor.close()
        return list


    def destroy(self):
        self.connection.close()