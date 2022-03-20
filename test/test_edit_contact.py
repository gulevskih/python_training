from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test", middlename='test',
                                   bday='13', bmonth='September', byear="1984",
                                   aday='4', amonth='May', ayear="1977"))
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="New_firstname", middlename="New_middlename")
    contact.id = old_contacts[0].id
    app.contact.edit_first_contact(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)

