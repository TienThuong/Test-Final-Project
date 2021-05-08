import time
import unittest
import chromedriver_autoinstaller
from parameterized import parameterized
from selenium import webdriver
import pytest
from Test.BaseTest import Base
from Pages.Contact import Contact, Letter


chromedriver_autoinstaller.install()


class ContactUs(unittest.TestCase):

    def setUp(self):
        print("Initiating Chrome driver")
        self.driver = webdriver.Chrome()
        print("-----------------------------------------")
        print("Test is started")
        self.driver.implicitly_wait(10)
        self.driver.get("http://automationpractice.com/")
        self.driver.maximize_window()

    @parameterized.expand([
         ["Chrome"],
         ["Firefox"],
     ])
    def test_contact(self):

        email = 'yenoanhhh@gmail.com'
        order = '26'
        url = 'C:/Users/Administrator/Pictures/1.jpg'
        message = 'Happiness is when she love you'
        ct = Contact(self.driver)
        base = Base(self.driver)
        base.click('xpath', Contact.button_contact)
        time.sleep(3)
        ct.set_subject()
        base.send_key('id', ct.email, email)
        base.send_key('id', ct.order, order)
        base.send_key('id', ct.file_upload, url)
        base.send_key('id', ct.message, message)
        base.click('id', ct.button_send_contact)
        time.sleep(5)
        title = ct.check_message_notice()

        self.assertEqual("Your message has been successfully sent to our team.", title, "This notice is about contact")
    @unittest.skip
    def test_letter(self):
        email = 'yyoah@gmail.com'
        lt = Letter(self.driver)
        lt.set_letter(email)
        lt.click_sendletter()
        time.sleep(5)
        title = lt.check_notice_letter()
        self.assertEqual("Newsletter : You have successfully subscribed to this newsletter.", title,
                         'This notice is about letter')

    def tearDown(self):
        self.driver.quit()
        print('Test complete.....')


if __name__ == '__main__':
    unittest.main()
