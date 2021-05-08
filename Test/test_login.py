import time
import unittest

import chromedriver_autoinstaller
from selenium import webdriver

from Pages.LoginPage import LoginPage
from Test.BaseTest import Base

chromedriver_autoinstaller.install()


class Login(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()

    def test_login_error(self):
        email = 'abc123'
        login = LoginPage(self.driver)
        base = Base(self.driver)
        base.click('xpath', login.sign_in)
        login.set_email(email)
        base.click('id', login.button_login_id)
        time.sleep(3)
        message = login.check_message()
        self.assertEqual('Invalid email address.', message, 'Email is True')

    def test_login_success(self):
        email = "tienthuong8@gmail.com"
        firstname = 'oanh'
        lastname = 'ngoc yen'
        password = 'oanh123'
        address = 'Hai Duong'
        city = 'Ha Noi'
        zipcode = 10000
        phone = '0388826899'
        alias = 'Nothing'
        login = LoginPage(self.driver)
        base = Base(self.driver)
        base.click('xpath', login.sign_in)
        login.set_email(email)
        base.click('id', login.button_login_id)
        time.sleep(3)
        base.send_key('xpath', login.first_name, firstname)
        base.send_key('xpath', login.last_name, lastname)
        base.send_key('id', login.pass_word, password)
        base.send_key('id', login.address, address)
        base.send_key('id', login.city, city)
        login.set_state()
        base.send_key('id', login.zip, zipcode)
        login.set_country()
        base.send_key('id', login.phone, phone)
        login.set_alias(alias)
        base.click('id', login.button_register)
        time.sleep(2)
        title = self.driver.title
        self.assertEqual('My account - My Store', title, 'This title is matching')
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()
        print('Test complete.....')


if __name__ == '__main__':
    unittest.main()
