import random

from Pages.Locator import Order


class OrderPage(Order):

    def __init__(self, driver):
        self.driver = driver

    # get sum price_product in checkout
    def total_price(self):
        list_total_product_price = self.driver.find_elements_by_xpath(self.price_product)  # list elt
        list_price = []
        for elt in list_total_product_price:
            total_product_price = elt.text
            list_price.append(float(total_product_price[1:]))
        return sum(list_price)

    # get total product in checkout
    def amount_total_product(self):
        total_all_product = self.driver.find_element_by_xpath(self.total_product).text
        amount_total_product = float(total_all_product[1:])
        return amount_total_product

    def check_notice_success(self):
        return self.driver.find_element_by_xpath(self.notice_order_success).text

    # Change order detail
    def get_random(self, list_deleted):
        num1 = random.randint(0, len(list_deleted))
        if num1 in list_deleted:
            self.get_random(list_deleted)
        else:
            return num1

    def choice_random(self, list_deleted, value):
        lst_product = self.driver.find_elements_by_xpath(self.change_quantity)
        num1 = self.get_random(list_deleted)
        quantity_product = lst_product[num1]
        quantity_product.clear()
        quantity_product.send_keys(value)

    def delete_random(self, list_deleted):
        lst_product = self.driver.find_elements_by_xpath(self.delete_quantity)
        num2 = self.get_random(list_deleted)
        del_product = lst_product[num2]
        del_product.click()

    # get discount 20 pro
    def check_sale_product(self):
        lst_product = self.driver.find_elements_by_xpath(self.list_product_xpath)
        return lst_product

    # add elt to cart in detail
    def add_toCart(self):
        self.driver.find_element_by_xpath(self.button_addtoCart).click()
