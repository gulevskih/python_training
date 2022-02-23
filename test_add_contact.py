# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from contact import Contact

class TestAddContact(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

    def test_add_contact(self):
        driver = self.driver
        self.open_home_page(driver)
        self.login(driver, 'admin', 'secret')
        self.open_contacts_page(driver)
        self.create_new_contact(driver, Contact(firstname="qwerty", middlename="zxcvb", lastname="asdfgh",
                                                nickname='ritkgkb', title='vndkti', company='auriga', address='lj346',
                                                home='lkjdsfklj', mobile='945934562', work='ork', fax='ax',
                                                email="@adsf", email2="@qwer", email3="@zxcv", homepage='wwwjklcom',
                                                bday='13', bmonth='September', byear="1984",
                                                aday='4', amonth='May', ayear="1977",
                                                address2='viekdl323', phone2='905234534', notes='theend'))
        self.return_home_page(driver)
        self.logout(driver)

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def return_home_page(self, driver):
        driver.find_element_by_link_text("home").click()

    def create_new_contact(self, driver, Contact):
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(Contact.firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(Contact.middlename)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(Contact.lastname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(Contact.nickname)
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(Contact.title)
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys(Contact.company)
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys(Contact.address)
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys(Contact.home)
        driver.find_element_by_name("mobile").click()
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys(Contact.mobile)
        driver.find_element_by_name("work").click()
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys(Contact.work)
        driver.find_element_by_name("fax").click()
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys(Contact.fax)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(Contact.email)
        driver.find_element_by_name("email2").click()
        driver.find_element_by_name("email2").clear()
        driver.find_element_by_name("email2").send_keys(Contact.email2)
        driver.find_element_by_name("email3").click()
        driver.find_element_by_name("email3").clear()
        driver.find_element_by_name("email3").send_keys(Contact.email3)
        driver.find_element_by_name("homepage").click()
        driver.find_element_by_name("homepage").clear()
        driver.find_element_by_name("homepage").send_keys(Contact.homepage)
        #driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(Contact.bday)
        #driver.find_element_by_xpath("//option[@value='6']").click()
        #driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(Contact.bmonth)
        #driver.find_element_by_xpath("//option[@value='October']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(Contact.byear)
        #driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text(Contact.aday)
        #driver.find_element_by_xpath("//div[@id='content']/form/select[3]/option[17]").click()
        #driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text(Contact.amonth)
        #driver.find_element_by_xpath("//select[4]/option[6]").click()
        driver.find_element_by_name("ayear").click()
        driver.find_element_by_name("ayear").clear()
        driver.find_element_by_name("ayear").send_keys(Contact.ayear)
        # Secondary
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys(Contact.address2)
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys(Contact.phone2)
        driver.find_element_by_name("notes").click()
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys(Contact.notes)
        # submit
        driver.find_element_by_xpath("//input[21]").click()

    def open_contacts_page(self, driver):
        driver.find_element_by_link_text("add new").click()

    def login(self, driver, username, password):
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_id("content").click()
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, driver):
        driver.get("http://localhost/addressbook/edit.php")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
