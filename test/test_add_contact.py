from model.contact import Contact


def test_add_contact(app, db, data_contacts, check_ui):
    contact = data_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        def clean(contact):
            return Contact(id=contact.id, firstname=contact.firstname.strip(), lastname=contact.lastname.strip())
        db_list = map(clean, db.get_contact_list())
        assert sorted(db_list, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
