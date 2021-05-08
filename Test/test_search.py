import time
import unittest

import chromedriver_autoinstaller
from selenium import webdriver

from Pages.SearchPage import ProductDetailPage
from Test.BaseTest import Base

chromedriver_autoinstaller.install()


class Search(unittest.TestCase):

    def setUp(self):
        print('Test start')
        print('-------------------------')

    # check search box when send key and clear
    def test_search(self):
        text = 'Dress'
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        search = ProductDetailPage(self.driver)
        base = Base(self.driver)
        base.click('xpath', search.search_box)
        base.send_key('xpath',search.search_box,text)
        time.sleep(3)
        base.clear_text(search.search_box)
        checkbox = search.check_search()
        self.assertEqual('Search', checkbox, 'This text is not matching')
    #
    # @parameterized.expand([
    #     ["Chrome"],
    #     ["Firefox"],
    # ])
    # Check List suggest
    def test_listsuggest(self):
        # if browser == 'Chrome':
        #     self.driver = webdriver.Chrome()
        #     time.sleep(3)
        # elif browser == 'Firefox':
        #     self.driver = webdriver.Firefox(executable_path='D:/Trainer/Selenium/Test_FinalProject/geckodriver.exe')
        #     time.sleep(3)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        text = 'Dress'
        search = ProductDetailPage(self.driver)
        search.click_search_box()
        search.text_search_box(text)
        time.sleep(5)
        list = search.get_list_suggest_keywords()
        for suggest_keyword in list:
            try:
                self.assertIn('Dress', suggest_keyword, 'This word is not in list')
                print('The suggest keyword is matching')
            except:
                print('The suggest keyword is not matching')

    # Check list suggest with name's product
    # @parameterized.expand([
    #     ["Chrome"],
    #     ["Firefox"],
    # ])
    def test_namesuggest(self):
        # if browser == 'Chrome':
        #     self.driver = webdriver.Chrome()
        #     time.sleep(3)
        # elif browser == 'Firefox':
        #     self.driver = webdriver.Firefox(executable_path='D:/Trainer/Selenium/Test_FinalProject/geckodriver.exe')
        #     time.sleep(3)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        text = 'Dress'
        check_name = ProductDetailPage(self.driver)
        check_name.click_search_box()
        check_name.text_search_box(text)
        time.sleep(3)
        lst_suggest_elt = check_name.check_value_suggest()
        total = len(lst_suggest_elt)
        first_suggest = lst_suggest_elt[0].text
        lst_suggest_elt[0].click()
        title = check_name.get_title()
        if title in first_suggest:
            print('This name is matching')
        for index in range(1, total):
            check_name.text_search_box(text)
            time.sleep(3)
            lst_pro = check_name.get_lst_product()
            elt = lst_pro[index]
            elt_txt = elt.text
            self.driver.implicitly_wait(5)
            elt.click()
            title = check_name.get_title()
            if title in elt_txt:
                print('This name is matching')
            else:
                print('This name is does not matching')

    # check search quantity
    # @parameterized.expand([
    #     ["Chrome"],
    #     ["Firefox"],
    # ])
    def test_search_quantity(self):
        # if browser == 'Chrome':
        #     self.driver = webdriver.Chrome()
        #     time.sleep(3)
        # elif browser == 'Firefox':
        #     self.driver = webdriver.Firefox(executable_path='D:/Trainer/Selenium/Test_FinalProject/geckodriver.exe')
        #     time.sleep(3)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        text = 'Dress'
        search_quantity = ProductDetailPage(self.driver)
        search_quantity.click_search_box()
        search_quantity.text_search_box(text)
        search_quantity.click_button_search()
        lst_quantity = search_quantity.check_quantity_list()
        title_quantity = search_quantity.check_title_search()
        if lst_quantity == title_quantity:
            print('Quantity information displayed is correct for the number of products displayed')
        else:
            print('This does not matching')

    # # check price's product when searching
    # @parameterized.expand([
    #     ["Chrome"],
    #     ["Firefox"],
    # ])
    def test_check_price(self):
        # if browser == 'Chrome':
        #     self.driver = webdriver.Chrome()
        #     time.sleep(3)
        # elif browser == 'Firefox':
        #     self.driver = webdriver.Firefox(executable_path='D:/Trainer/Selenium/Test_FinalProject/geckodriver.exe')
        #     time.sleep(3)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        text = 'Dress'
        product_detail_page = ProductDetailPage(self.driver)
        product_detail_page.text_search_box(text)
        time.sleep(3)
        # list suggest in HomePage
        list_suggest_product_elt = product_detail_page.get_list_suggest_product_elt()
        total = len(list_suggest_product_elt)
        list_suggest_product_elt[0].click()
        price_text = product_detail_page.get_price_text()
        self.assertIsNotNone(price_text, 'This price product is not displayed')
        for index in range(1, total):
            product_detail_page.text_search_box(text)
            time.sleep(5)
            # list suggest in ProductPage
            lst_product = product_detail_page.get_lst_product()
            elt = lst_product[index]
            elt.click()
            self.assertIsNotNone(price_text, 'This price product is not displayed')

    # Kiểm tra kết quả tìm kiếm sau khi nhập sai tên sản phẩm

    # check wrong keyword when searching
    def test_wrong_keyword(self):
        # if browser == 'Chrome':
        #     self.driver = webdriver.Chrome()
        #     time.sleep(3)
        # elif browser == 'Firefox':
        #     self.driver = webdriver.Firefox(executable_path='D:/Trainer/Selenium/Test_FinalProject/geckodriver.exe')
        #     time.sleep(3)
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get('http://automationpractice.com/index.php')
        self.driver.maximize_window()
        text = 'dresSSss'
        check_wrong_keyword = ProductDetailPage(self.driver)
        check_wrong_keyword.click_search_box()
        check_wrong_keyword.text_search_box(text)
        check_wrong_keyword.click_button_search()
        wrong_title = check_wrong_keyword.get_wrong_title()

        self.assertEqual(f'No results were found for your search "{text}"', wrong_title,
                         'This notice does not matching')

    def tearDown(self):
        self.driver.quit()
        print('-------------------------')
        print('Test complete')


if __name__ == '__main__':
    unittest.main()
