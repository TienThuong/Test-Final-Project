from selenium.webdriver.support.select import Select

from Pages.Locator import Login


class LoginPage(Login):

    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_id(self.email_input_id).clear()
        self.driver.find_element_by_id(self.email_input_id).send_keys(email)

    # check account fail
    def check_message(self):
        return self.driver.find_element_by_xpath(self.error_message).text

    # check account success
    def set_state(self):
        elt = self.driver.find_element_by_id(self.state)
        drp = Select(elt)
        drp.select_by_value('3')

    def set_country(self):
        elt1 = self.driver.find_element_by_id(self.country)
        drp1 = Select(elt1)
        drp1.select_by_visible_text('United States')

    def set_alias(self, alias):
        self.driver.find_element_by_id(self.alias).clear()
        self.driver.find_element_by_id(self.alias).send_keys(alias)

