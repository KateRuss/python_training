
from model.group import Group

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group", header="1", footer="123"))
    app.group.modify_first_group(Group(name="new_test_group_name"))

def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_group", header="1", footer="123"))
    app.group.modify_first_group(Group(header="new_header"))
