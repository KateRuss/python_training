# -*- coding: utf-8 -*-

from fixtura.orm import ORMfixture
from model.group import Group

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
   l = db.get_contacts_not_in_group('147')
   for item in l:
        print(item)
   print(len(l))
finally:
    pass #db.destroy()