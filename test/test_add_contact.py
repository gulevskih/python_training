
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(Contact(firstname="qwerty", middlename="zxcvb", lastname="asdfgh",
                               nickname='ritkgkb', title='vndkti', company='auriga', address='lj346',
                               phone_home='831954824', mobile='945934562', phone_work='911', fax='ax',
                               email="@adsf", email2="@qwer", email3="@zxcv", homepage='wwwjklcom',
                               bday='13', bmonth='September', byear="1984",
                               aday='4', amonth='May', ayear="1977",
                               address2='viekdl323', phone2='905234534', notes='theend'))
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
