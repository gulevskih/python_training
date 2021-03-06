from model.group import Group
from random import randrange
import random

def test_edit_group_name(app, db, check_ui):
    if app.group.count() == 0:
        app.group.create(Group(name='test'))
    old_groups = db.get_group_list()
    group_edit = random.choice(old_groups)
    group = Group(name="New group")
    position = old_groups.index(group_edit)
    app.group.edit_group_by_id(group_edit.id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[position] = group
    assert old_groups == new_groups
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list = map(clean, db.get_group_list())
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


#def test_edit_group_name_old(app):
    #if app.group.count() == 0:
        #app.group.create(Group(name='test'))
    #old_groups = app.group.get_group_list()
    #index = randrange(len(old_groups))
    #group = Group(name="New group")
    #group.id = old_groups[index].id
    #app.group.edit_group_by_index(index, group)
    #new_groups = app.group.get_group_list()
    #assert len(old_groups) == len(new_groups)
    #old_groups[index] = group
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name='test'))
#    app.group.edit_first_group(Group(header="New header"))


#def test_edit_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name='test'))
#    app.group.edit_first_group(Group(footer="New footer"))

