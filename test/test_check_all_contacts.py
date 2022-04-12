from model.contact import Contact
import re

def test_contact_on_home_page(app, db):
    contacts_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    for i in range(len(contacts_from_db)):
        assert contacts_from_home_page[i].id == contacts_from_db[i].id
        assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname.strip()
        assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname.strip()
        assert contacts_from_home_page[i].address == contacts_from_db[i].address.strip()
        assert contacts_from_home_page[i].all_emails_from_home_page == merge_emails_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))