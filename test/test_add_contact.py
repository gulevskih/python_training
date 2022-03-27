from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=firstname, lastname=lastname, address=address, email=email)
    for firstname in ['', random_string("firstname", 10)]
    for lastname in ['', random_string("lastname", 10)]
    for address in ['', random_string("address", 20)]
    for email in ['', random_string("email", 20)]
]

@pytest.mark.parametrize('contact', testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    #contact = Contact(firstname="Sten", middlename="Platonovich", lastname="Li",
                      #nickname='ritkgkb', title='vndkti', company='auriga', address='lj346',
                      #homephone='(831)954824', mobilephone='945 934 562', workphone='(911) 000-28', fax='ax',
                      #email="a_b@mail.ru", email2="abc-def@gmai.com", email3="", homepage='www.jkl.com',
                      #bday='13', bmonth='September', byear="1984",
                      #aday='4', amonth='May', ayear="1977",
                      #address2='viekdl323', secondaryphone='+7905234534', notes='theend')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_full_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Sten", middlename="Platonovich", lastname="Li",
                      nickname='ritkgkb', title='vndkti', company='auriga', address='lj346',
                      homephone='(831)954824', mobilephone='945 934 562', workphone='(911) 000-28', fax='ax',
                      email="a_b@mail.ru", email2="abc-def@gmai.com", email3="", homepage='www.jkl.com',
                      bday='13', bmonth='September', byear="1984",
                      aday='4', amonth='May', ayear="1977",
                      address2='viekdl323', secondaryphone='+7905234534', notes='theend')
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)