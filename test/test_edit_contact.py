
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test",
                                   bday='13', bmonth='September', byear="1984",
                                   aday='4', amonth='May', ayear="1977"))
    app.contact.edit_first_contact(Contact(middlename="New_middlename",
                                           bday='2', bmonth='September', byear="1984",
                                           aday='8', amonth='May', ayear="1977"))
