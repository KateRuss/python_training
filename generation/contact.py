# -*- coding: utf-8 -*-

from model.contact import Contact
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits + " "
    return prefix + "".join((random.choice(symbols) for i in range(random.randrange(maxlen))))


testdata = [Contact(first_name="", last_name="")]+[Contact(first_name=random_string("first_Name:", 20),
                    last_name=random_string("Last_name:", 20), address=random_string("address:", 20),
                    home_phone_number=random_string("H:", 20), mobile_phone_number=random_string("M:", 20),
                    work_phone_number=random_string("W:", 20), email_1=random_string("E1:", 25),
                    email_2=random_string("E2:", 25), email_3=random_string("E3:", 10))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent = 2)
    out.write(jsonpickle.encode(testdata))