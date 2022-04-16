from model.contact import Contact
from model.group import Group
import random
from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_contact_to_group(app, db):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name='test'))
    #groups = db.get_group_list()
    #group = random.choice(groups)
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact.id)
