
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename='test',
                                   bday='13', bmonth='September', byear="1984",
                                   aday='4', amonth='May', ayear="1977"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="New_firstname", middlename="New_middlename",
                                           bday='2', bmonth='October', byear="998",
                                           aday='8', amonth='January', ayear="1221"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
