from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Sten", middlename="Platonovich", lastname="Li",
                      nickname='ritkgkb', title='vndkti', company='auriga', address='lj346',
                      homephone='(831)954824', mobilephone='945 934 562', workphone='(911) 000-28', fax='ax',
                      email="@adsf", email2="@qwer", email3="@zxcv", homepage='wwwjklcom',
                      bday='13', bmonth='September', byear="1984",
                      aday='4', amonth='May', ayear="1977",
                      address2='viekdl323', secondaryphone='905234534', notes='theend')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
