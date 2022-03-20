from model.contact import Contact
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename='test',
                                   bday='13', bmonth='September', byear="1984",
                                   aday='4', amonth='May', ayear="1977"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="New_firstname", middlename="New_middlename")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

