import time
import unittest

import chromedriver_autoinstaller
from selenium import webdriver

from Test.BaseTest import Base
from Pages.OrderPage import OrderPage

chromedriver_autoinstaller.install()


class Order(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()

        print('Test start')
        print('-------------------------')

    def test_orderPro(self):
        email = 'nam99@gmail.com'
        pw = '@@q7vLZDt2PdmuG'
        check_order = OrderPage(self.driver)
        modify = Base(self.driver)
        modify.get_product(0, 3)
        modify.click('xpath', OrderPage.checkout_out_xpath)
        time.sleep(3)
        total_product = check_order.total_price()
        all_total_product = check_order.amount_total_product()
        if total_product == all_total_product:
            print('Amount total is True')
        else:
            print('Amount total is False')
        modify.check_out()
        title = check_order.check_notice_success()
        self.assertEqual('Your order on My Store is complete.', title, 'This notice is matching')
        time.sleep(10)

    def test_changeOrderDetail(self):
        value = 3
        email = 'nam99@gmail.com'
        pw = '@@q7vLZDt2PdmuG'
        change_order = OrderPage(self.driver)
        modify = Base(self.driver)
        modify.get_product(0, 5)
        modify.click('xpath', change_order.checkout_out_xpath)
        time.sleep(3)
        list_deleted = []
        change_order.choice_random(list_deleted, value)
        time.sleep(2)
        change_order.delete_random(list_deleted)
        modify.check_out()
        title = change_order.check_notice_success()
        self.assertEqual('Your order on My Store is complete.', title, 'This notice is matching')
        time.sleep(10)

    # Check sale order
    def test_sale_product(self):
        email = 'nam99@gmail.com'
        pw = '@@q7vLZDt2PdmuG'
        get_sale_product = OrderPage(self.driver)
        modify = Base(self.driver)
        lst_product = get_sale_product.check_sale_product()
        sale_product = '-20%'
        for i in lst_product:
            if sale_product in i.text:
                i.click()
                time.sleep(4)
                get_sale_product.add_toCart()
                modify.click('xpath', get_sale_product.checkout_out_xpath)
                modify.check_out()
                title = get_sale_product.check_notice_success()
                self.assertEqual('Your order on My Store is complete.', title, 'This notice is matching')
                time.sleep(10)
        time.sleep(10)

    def tearDown(self):
        self.driver.quit()
        print('-------------------------')
        print('Test complete')


if __name__ == '__main__':
    unittest.main()
