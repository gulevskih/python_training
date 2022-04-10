from model.contact import Contact
from random import randrange
import random

def test_delete_some_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    position = old_contacts.index(contact)
    app.contact.delete_contact_by_id(contact.id)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[position:position+1] = []
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        db_list = map(clean, db.get_contact_list())
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_delete_some_contact_old(app):
#    if app.contact.count() == 0:
#       app.contact.create(Contact(firstname="test"))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    app.contact.delete_contact_by_index(index)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) - 1 == len(new_contacts)
#    old_contacts[index:index+1] = []
#    assert old_contacts == new_contacts