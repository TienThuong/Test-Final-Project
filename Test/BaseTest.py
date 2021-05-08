import random
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Pages.OrderPage import OrderPage


class Base:

    def __init__(self, driver):
        self.driver = driver
        self.checkout = OrderPage(self.driver)

    # login common

    def login(self):
        email = 'nam99@gmail.com'
        pw = '@@q7vLZDt2PdmuG'
        self.driver.find_element(By.XPATH, self.checkout.email_checkout_xpath).send_keys(email)
        self.driver.find_element(By.XPATH, self.checkout.pass_checkout_xpath).send_keys(pw)

    # click common
    def click(self, elt, locator):
        if elt == 'xpath':
            self.driver.find_element(By.XPATH, locator).click()
        elif elt == 'id':
            self.driver.find_element(By.ID, locator).click()

    # send key common
    def send_key(self, elt, locator, text):
        if elt == 'xpath':
            self.driver.find_element(By.XPATH, locator).send_keys(text)
        elif elt == 'id':
            self.driver.find_element(By.ID, locator).send_keys(text)

    # check element present
    def check_exist_elt(self, locator):
        try:
            elt = self.driver.find_element_by_xpath(locator)
            elt_text = elt.text
            if elt_text == "You must agree to the terms of service before continuing.":
                return True
        except NoSuchElementException:
            return False

    # Proceed to checkout
    def check_out(self):
        self.click('xpath', self.checkout.proceed_checkout_xpath)
        self.login()
        self.click('xpath', self.checkout.button_signin_xpath)
        self.click('xpath', self.checkout.proceed_checkout2_xpath)
        self.click('xpath', self.checkout.proceed_checkout3_xpath)
        if self.check_exist_elt(self.checkout.alert_term_xpath):
            self.click('xpath', self.checkout.close_alert_term)
        self.click('xpath', self.checkout.click_term_xpath)
        self.click('xpath', self.checkout.proceed_checkout3_xpath)
        self.click('xpath', self.checkout.payment_method)
        self.click('xpath', self.checkout.confirm_order_xpath)

    # get random product in homepage
    def get_product(self, start, end):
        lsts_pro = self.driver.find_elements_by_xpath(self.checkout.lst_pro)

        for i in range(start, end):
            rand = random.randint(1, len(lsts_pro))
            print(rand)
            imga = self.driver.find_element_by_xpath(self.checkout.img.format(rand))
            pro = self.driver.find_element_by_xpath(self.checkout.list_pro.format(rand))
            actions = ActionChains(self.driver)
            time.sleep(1)
            actions.move_to_element(imga).move_to_element(pro).click().perform()
            time.sleep(1)
            self.driver.find_element_by_xpath(self.checkout.continue_shopping_xpath).click()

    # get size's image
    def get_size(self, locator):
        size = self.driver.find_element_by_xpath(locator).size
        return size

    # get location's image
    def get_location(self, locator):
        elt = self.driver.find_element_by_xpath(locator)
        return elt.location

    # clear text common

    def clear_text(self, clr):
        elt = self.driver.find_element_by_xpath(clr)
        return elt.clear()

    # compare image and location
    def compareer(self, x, y):
        if x > y:
            return False
        elif x == y:
            return False
        else:
            return True
