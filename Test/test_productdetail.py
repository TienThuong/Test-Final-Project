import time
import unittest

import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.ProductDetail import ProductDetail
from Test.BaseTest import Base

chromedriver_autoinstaller.install()


class Test_Product(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(5)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        print('Test start')
        print('-----------------------')

    # check viewlarge when clicking image
    def test_viewlarge(self):
        check_viewlarge = ProductDetail(self.driver)
        base = Base(self.driver)
        check_viewlarge.click_proInto_list()
        base.click('xpath', check_viewlarge.normal_image)
        time.sleep(3)
        normal_image = base.get_size(check_viewlarge.normal_image)
        big_image = base.get_size(check_viewlarge.big_image)
        size_normal_image = normal_image.get('height')
        siz_big_image = big_image.get('height')
        base.compareer(size_normal_image, siz_big_image)
        location_image = base.get_location(check_viewlarge.big_image)
        get_location_image = location_image.get('y')
        location_name = base.get_location(check_viewlarge.title_xpath)
        get_location_name = location_name.get('y')
        base.compareer(get_location_name, get_location_image)

    # check viewlarge when clicking button view large
    def test_close_Viewlarge(self):
        check_click_button = ProductDetail(self.driver)
        base = Base(self.driver)
        check_click_button.click_proInto_list()
        base.click('xpath', check_click_button.normal_image)
        base.click('xpath', check_click_button.button_close)
        base.click('xpath', check_click_button.button_viewlarge)
        time.sleep(3)
        normal_image = base.get_size(check_click_button.normal_image)
        big_image = base.get_size(check_click_button.big_image)
        size_normal_image = normal_image.get('height')
        siz_big_image = big_image.get('height')
        base.compareer(size_normal_image, siz_big_image)
        location_image = base.get_location(check_click_button.normal_image)
        get_location_image = location_image.get('y')
        location_name = base.get_location(check_click_button.big_image)
        get_location_name = location_name.get('y')
        base.compareer(get_location_name, get_location_image)

    # add to cart with quantity = 0
    def test_quantityzero(self):
        quantity = 0
        check_quantityzero = ProductDetail(self.driver)
        base = Base(self.driver)
        check_quantityzero.click_proInto_list()
        base.click('xpath', check_quantityzero.normal_image)
        base.click('xpath', check_quantityzero.button_close)
        base.clear_text(check_quantityzero.quantity_xpath)
        base.send_key('xpath', check_quantityzero.quantity_xpath, quantity)
        time.sleep(3)
        base.click('xpath', check_quantityzero.buton_addtocart)
        title = check_quantityzero.check_alert()
        self.assertEqual('Null quantity.', title, 'This alert is not matching')

    # add to cart with quantity >0
    def test_quantity(self):
        quantity1 = 0
        quantity2 = 1
        check_quantity = ProductDetail(self.driver)
        base = Base(self.driver)
        check_quantity.click_proInto_list()
        base.click('xpath', check_quantity.normal_image)
        time.sleep(3)
        base.click('xpath', check_quantity.button_close)
        base.clear_text(check_quantity.quantity_xpath)
        base.send_key('xpath', check_quantity.quantity_xpath, quantity1)
        base.click('xpath', check_quantity.buton_addtocart)
        check_quantity.close_button_alert()
        base.clear_text(check_quantity.quantity_xpath)
        base.send_key('xpath', check_quantity.quantity_xpath, quantity2)
        base.click('xpath', check_quantity.buton_addtocart)
        time.sleep(5)
        title = check_quantity.get_alert_success()
        self.assertEqual('Product successfully added to your shopping cart', title, "This notice is does not matching")
        check_quantity.close_popup()
        get_name_detail = check_quantity.get_name_detail()
        get_quantity_detail = check_quantity.get_quantity_detail()
        base.click('xpath', check_quantity.button_cart_xpath)
        get_name_cart = check_quantity.get_name_cart()
        get_quantity_cart = check_quantity.get_quantity_cart()
        if get_name_detail == get_name_cart:
            if get_quantity_detail == get_quantity_cart:
                print('This product is successfully added to the cart')
    # test share to twitter
    def test_sharetwitter(self):
        share_twitter = ProductDetail(self.driver)
        share_twitter.click_proInto_list()
        time.sleep(3)
        share_twitter.click_button_twitter()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//input[@name='session[username_or_email]']").send_keys("Vải thiều")
        self.driver.find_element(By.XPATH, "//input[@name='session[password]']").send_keys('linderella')
        time.sleep(5)

    # test write comment
    def test_write_comment(self):
        user = 'nam99@gmail.com'
        pw = '@@q7vLZDt2PdmuG'
        title = 'How nice this product'
        content = 'This product is so nice and I love it so much'
        write_comment = ProductDetail(self.driver)
        write_comment.click_signIn()
        write_comment.input_account(user, pw)
        write_comment.click_button_sign()
        write_comment.click_backHome()
        write_comment.click_proInto_list()
        write_comment.click_writecmt()
        write_comment.write_cmt(title, content)
        time.sleep(3)
        write_comment.click_sendcmt()
        title = write_comment.get_title_success()
        self.assertEqual('Your comment has been added and will be available once approved by a moderator',
                         title, 'This notice is not matching')
        write_comment.close_notice_success()

    # test send to friend
    def test_send_toFriend(self):
        user = 'Nguyen Van Nam'
        email = 'Nguyenvannam@gmail.com'
        send_email = ProductDetail(self.driver)
        send_email.click_proInto_list()
        send_email.click_send()
        send_email.input_content(user, email)
        send_email.click_send_email()
        time.sleep(3)
        title = send_email.get_send_email()
        self.assertEqual('Your e-mail has been sent successfully',
                         title, 'This notice is not matching')
        send_email.click_close_send_email()

    def tearDown(self):
        self.driver.quit()
        print('-----------------------')
        print('Test complete')


if __name__ == '__main__':
    unittest.main()
