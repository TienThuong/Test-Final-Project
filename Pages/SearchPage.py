from Pages.Locator import SearchPage


class ProductDetailPage(SearchPage):

    def __init__(self, driver):
        self.driver = driver

    # Check searchbox after cleared text
    def check_search(self):
        return self.driver.find_element_by_xpath(self.search_box).get_attribute('placeholder')

    def click_search_box(self):
        self.driver.find_element_by_xpath(self.search_box).click()

    def text_search_box(self, text):
        elt = self.driver.find_element_by_xpath(self.search_box)
        elt.clear()
        elt.send_keys(text)

    def click_button_search(self):
        self.driver.find_element_by_xpath(self.button_search_xpath).click()

    # check list suggest
    def get_list_suggest_keywords(self):
        lst_suggest_keywords = self.driver.find_elements_by_xpath(self.list_suggest_xpath)
        lst_text = []
        for suggest_keyword in lst_suggest_keywords:
            suggest_keyword_text = suggest_keyword.text
            lst_text.append(suggest_keyword_text)
        return lst_text

    # check list suggest with name's product
    def check_value_suggest(self):
        lst_suggest = self.driver.find_elements_by_xpath(self.list_suggest_xpath)
        return lst_suggest

    # get list suggest in ProductPage
    def get_lst_product(self):
        elts = self.driver.find_elements_by_xpath(self.list_product_xpath)
        return elts

    # get name's product
    def get_title(self):
        return self.driver.find_element_by_xpath(self.title_xpath).text

    # check search quantity
    def check_quantity_list(self):
        lst_search = self.driver.find_elements_by_xpath(self.list_search_xpath)
        # new_lst = []
        # for lst in lst_search:
        #     lst_text = lst.text
        #     new_lst.append(lst_text)
        # return len(new_lst)
        return len(lst_search)

    # get notice when search
    def check_title_search(self):
        title = self.driver.find_element_by_class_name(self.title_result_class_name).text
        lst_title = title.split()
        new_lst = []
        for i in lst_title:
            new_lst.append(i)
        return int(new_lst[0])

    # check price's product when searching
    def get_list_suggest_product_elt(self):
        lst = self.driver.find_elements_by_xpath(self.list_suggest_xpath)
        # new_lst = []
        # for i in lst:
        #     new_lst.append(i)
        # return new_lst
        return lst

    # get price text when searching
    def get_price_text(self):
        return self.driver.find_element_by_id(self.price_txt).text

    # Kiểm tra khi nhập sai keyword

    def get_wrong_title(self):
        return self.driver.find_element_by_xpath(self.tittle_wrong_xpath).text
