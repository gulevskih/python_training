
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test",
                                   bday='13', bmonth='September', byear="1984",
                                   aday='4', amonth='May', ayear="1977"))
    old_contacts = app.contact.get_contact_list()
    app.contact.edit_first_contact(Contact(firstname="New_firstname", middlename="New_middlename",
                                           bday='2', bmonth='September', byear="1984",
                                           aday='8', amonth='May', ayear="1977"))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
