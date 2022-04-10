from model.contact import Contact
from random import randrange
import random

def test_edit_contact(app, db, check_ui):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", mobilephone="+7(905)4444867"))
    old_contacts = db.get_contact_list()
    contact_edit = random.choice(old_contacts)
    position = old_contacts.index(contact_edit)
    contact = Contact(firstname="New_firstname  ", lastname="  New_lastname")
    app.contact.edit_contact_by_id(contact_edit.id, contact)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[position] = contact
    assert old_contacts == new_contacts
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        db_list = map(clean, db.get_contact_list())
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)


#def test_edit_contact_old(app):
#    if app.contact.count() == 0:
#        app.contact.create(Contact(firstname="test", mobilephone="+7(905)4444867"))
#    old_contacts = app.contact.get_contact_list()
#    index = randrange(len(old_contacts))
#    contact = Contact(firstname="New_firstname", lastname="New_lastname")
#    contact.id = old_contacts[index].id
#    app.contact.edit_contact_by_index(index, contact)
#    new_contacts = app.contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[index] = contact
#    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

