from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

dbORM = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))

    groups = db.get_group_list()

    #deleting all contacts from a group
    for group in groups:
        app.contact.select_view_group_by_id(group.id)
        app.contact.del_all_contacts_in_group()
        app.open_home_page()

    group = random.choice(groups)
    contacts = db.get_contact_list()
    contact = random.choice(contacts)

    old_list_group = dbORM.get_contacts_in_group(Group(id="%s" % group.id))

    app.contact.add_contact_to_group(contact.id, group.id)

    new_list_group = dbORM.get_contacts_in_group(Group(id="%s" % group.id))

    assert len(old_list_group) + 1 == len(new_list_group)

    old_list_group.append(contact)
    assert old_list_group == new_list_group
