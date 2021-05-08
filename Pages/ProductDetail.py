import random
import time

from Pages.Locator import Product


class ProductDetail(Product):

    def __init__(self, driver):
        self.driver = driver

    # check viewlarg when clicking image
    def click_proInto_list(self):
        lst_pro = self.driver.find_elements_by_xpath(self.lst_product)
        random.choice(lst_pro).click()

    # check viewlarge when clicking button view large

    def check_alert(self):
        alert_quantityrezo = self.driver.find_element_by_xpath(self.alert_quantity).text
        return alert_quantityrezo

    # add to cart with quantity >0
    def close_button_alert(self):
        self.driver.find_element_by_xpath(self.close_alert_xpath).click()

    def get_alert_success(self):
        return self.driver.find_element_by_xpath(self.alert_success_xpath).text

    def close_popup(self):
        self.driver.find_element_by_xpath(self.button_close_popup).click()

    def click_button_cart(self):
        self.driver.find_element_by_xpath(self.button_cart_xpath).click()

    def get_name_detail(self):
        return self.driver.find_element_by_xpath(self.get_name_detail_xpath).text

    def get_quantity_detail(self):
        quantity_detail = self.driver.find_element_by_xpath(self.get_quantity_detail_xpath).get_attribute('value')
        return quantity_detail

    def get_name_cart(self):
        get_name = self.driver.find_element_by_xpath(self.get_name_cart_xpath).text
        return get_name

    def get_quantity_cart(self):
        return self.driver.find_element_by_xpath(self.get_quantity_cart_xpath).get_attribute('value')

    # test share to twitter
    def click_button_twitter(self):
        self.driver.find_element_by_xpath(self.twitter).click()

    # test write comment
    def click_signIn(self):
        self.driver.find_element_by_xpath(self.click_sign).click()

    def input_account(self, username, pw):
        self.driver.find_element_by_xpath(self.user_xpath).send_keys(username)
        time.sleep(2)
        self.driver.find_element_by_xpath(self.pw_xpath).send_keys(pw)

    def click_button_sign(self):
        self.driver.find_element_by_xpath(self.button_signIn).click()

    def click_backHome(self):
        self.driver.find_element_by_xpath(self.button_backHome).click()

    def click_writecmt(self):
        self.driver.find_element_by_xpath(self.click_write_cmt).click()

    def write_cmt(self, title, content):
        self.driver.find_element_by_xpath(self.input_title).send_keys(title)
        time.sleep(1)
        self.driver.find_element_by_xpath(self.input_comment).send_keys(content)

    def click_sendcmt(self):
        self.driver.find_element_by_xpath(self.button_send_cmt).click()

    def get_title_success(self):
        return self.driver.find_element_by_xpath(self.check_title).text

    def close_notice_success(self):
        self.driver.find_element_by_xpath(self.close_notice).click()

    # test send friend
    def click_send(self):
        self.driver.find_element_by_xpath(self.send_to_friend).click()

    def input_content(self, name, email):
        self.driver.find_element_by_xpath(self.name_xpath).send_keys(name)
        self.driver.find_element_by_xpath(self.email_xpath).send_keys(email)

    def click_send_email(self):
        self.driver.find_element_by_xpath(self.button_send_mail).click()

    def get_send_email(self):
        return self.driver.find_element_by_xpath(self.notice_send_mail).text

    def click_close_send_email(self):
        self.driver.find_element_by_xpath(self.close_send_email).click()
