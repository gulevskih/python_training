
from model.contact import Contact

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test",
                                   bday='13', bmonth='September', byear="1984",
                                   aday='4', amonth='May', ayear="1977"))
    app.contact.delete_first_contact()
