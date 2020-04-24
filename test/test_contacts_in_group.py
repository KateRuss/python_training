# -*- coding: utf-8 -*-

from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_some_group(app, orm, db):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Test_group1", header="blah-blah-blah"))

    group = random.choice(orm.get_group_list())

    if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_not_in_group(group)) == 0:
        app.contact.create_new(Contact(first_name="contact_name", last_name="last_name"))

    contact = random.choice(orm.get_contacts_not_in_group(group))
    app.contact.add_contact_in_group(group.id, contact.id)
    assert contact in orm.get_contacts_in_group(group)


def test_del_contact_from_some_group(app, orm):
    if len(orm.get_group_list()) == 0:
        app.group.create(Group(name="Test1", header="blah-blah-blah"))
    group = random.choice(orm.get_group_list())
    if len(orm.get_contact_list()) == 0 or len(orm.get_contacts_in_group(group)) == 0:
        contact = app.contact.create_new(Contact(first_name="contact_name", last_name="last_name"))
        app.contact.add_contact_in_group(group.id, contact.id)
    contact = random.choice(orm.get_contacts_in_group(group))
    app.contact.del_contact_from_group(group.id, contact.id)
    assert contact in orm.get_contacts_not_in_group(group)