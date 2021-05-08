from selenium.webdriver.support.select import Select

from Pages.Locator import Contact


class Letter(Contact):

    def __init__(self, driver):
        self.driver = driver

    # New Letter
    def set_letter(self, email):
        self.driver.find_element_by_id(self.letter).clear()
        self.driver.find_element_by_id(self.letter).send_keys(email)

    def click_sendletter(self):
        self.driver.find_element_by_name(self.button_letter).click()

    def check_notice_letter(self):
        return self.driver.find_element_by_xpath(self.message_notice).text


class Contact(Contact):

    def __init__(self, driver):
        self.driver = driver

    # ContactUS
    def click_contact(self):
        self.driver.find_element_by_xpath(self.button_contact).click()

    def set_subject(self):
        elt = self.driver.find_element_by_id(self.subject)
        drp = Select(elt)
        drp.select_by_value('2')

    def check_message_notice(self):
        return self.driver.find_element_by_xpath(self.notice).text
