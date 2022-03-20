from selenium.webdriver.support.ui import Select
from model.contact import Contact

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        # create new contact
        self.open_add_new_contact_page()
        # fill contact firm
        self.fill_contact_form(contact)
        # submit
        wd.find_element_by_xpath("//input[21]").click()
        self.return_home_page()

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.phone_home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.phone_work)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_value_of_list_box("bday", contact.bday)
        self.change_value_of_list_box("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_value_of_list_box("aday", contact.aday)
        self.change_value_of_list_box("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_value_of_list_box(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.return_home_page()
        # click edit contact
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # edit contact firm
        self.fill_contact_form(contact)
        # update
        wd.find_element_by_name("update").click()
        self.return_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_home_page()
        # click edit contact
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # click delete contact
        wd.find_element_by_xpath("//div[@id='content']/form[2]/input[2]").click()
        self.return_home_page()

    def return_home_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith('/addressbook/'):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.return_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            #text = element.find_element_by_name("selected[]").get_attribute("title")
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(id=id))
        return contacts
