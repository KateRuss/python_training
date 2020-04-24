# -*- coding: utf-8 -*-

from model.group import Group
from random import randrange
import pytest


@pytest.mark.ui_tests
def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test_group"))
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="new_test_group_name_2")
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    assert len(old_groups) == app.group.count()
    old_groups[index] = group
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)



# def test_modify_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="test_group", header="1", footer="123"))
#     old_groups = app.group.get_group_list()
#     app.group.modify_first_group(Group(header="new_header"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
