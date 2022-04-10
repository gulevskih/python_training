from model.group import Group


def test_add_group(app, db, data_groups, check_ui):
    group = data_groups
    old_groups = db.get_group_list()
    app.group.create(group)
    #assert len(old_groups) + 1 == app.group.count()
    new_groups = db.get_group_list()
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        def clean(group):
            return Group(id=group.id, name=group.name.strip())
        db_list = map(clean, db.get_group_list())
        assert sorted(db_list, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
