
from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit_first_contact(Contact(firstname="", middlename="", lastname="",
                               nickname='', title='', company='', address='',
                               phone_home='', mobile='', phone_work='', fax='',
                               email="", email2="", email3="", homepage='',
                               bday='13', bmonth='September', byear="1984",
                               aday='4', amonth='May', ayear="1977",
                               address2='', phone2='', notes=''))
