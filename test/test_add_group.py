# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="test_group", header="fhfh", footer="hfhhgjkj"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))

if __name__ == "__main__":
    unittest.main()
