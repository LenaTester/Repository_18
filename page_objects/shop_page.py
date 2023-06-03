from selenium.webdriver.common.by import By
import random
from web_ui.base_page import BasePage


class ShopPage(BasePage):
    __fresh_local_fish_title = (By.XPATH, "//h2[text()='Fresh, Local Fish']")
    __fish_price = (By.XPATH, "//p[@data-test='productPrice']")
    __sort_by_dropdown = (By.XPATH, "//div[@class='sc-dqBHgY eqxcwJ']")
    __low_high_price_sorting = (By.XPATH, "//div[@class='css-f0q9c7-option select-undefined__option'][text()='Price Low-High']")
    __buy_button = (By.XPATH, "//div[@class='sc-dcOKER bWCiRC']")
    __fish_full_element = (By.XPATH, "//div[@class='product-waves-wrapper sc-lXiCt iJcDxe']")
    __fish_name = (By.XPATH, "//h4[@data-test='productTile']")
    __buy_fish_button = (By.XPATH, "//div[text()='BUY']")
    __selected_fish_name = (By.XPATH, "//h3[@data-test='productName']")
    __pack_size_field = (By.XPATH, "//input[@data-test='variantPicker']")
    __pack_size_10_lb = (By.XPATH, "//div[@data-test-id='10 lb']")
    __quantity_field = (By.XPATH, "//input[@name='quantity']")
    __add_to_cart_button = (By.XPATH, "//button[@data-test='addProductToCartButton']")
    __one_fish_price = (By.XPATH, "//p[@data-test='unitPrice']/span")
    __total_price_calculation = (By.XPATH, "//p[@data-test='totalPrice']/span")
    __ordered_fish_quantity = (By.XPATH, "//input[@name='quantity']")
    __remove_button = (By.XPATH, "//div[@data-test='removeButton']")
    __empty_cart_message = (By.XPATH, "//h3[@class='sc-fHlXLc VcUjv']")

    def __init__(self, driver):
        super().__init__(driver)

    def click_fresh_local_fish(self):
        self.click(self.__fresh_local_fish_title)
        return self

    def click_sort_by(self):
        self.click(self.__sort_by_dropdown)
        return self

    def click_low_high_price_option(self):
        self.click_2(self.__low_high_price_sorting)
        return self

    def get_fish_sorted_prices(self):
        return self.get_text_multi(self.__fish_price)

    def choose_random_fish(self):
        fishes = self.wait_for_elements_located(self.__fish_full_element)
        random_product = random.choice(fishes)
        return self.click(random_product)

    def get_fish_name(self):
        return self.get_text(self.__fish_name)

    def click_buy_fish(self):
        self.click(self.__buy_fish_button)
        return self

    def get_selected_fish_name(self):
        return self.get_text(self.__selected_fish_name)

    def click_pack_size(self):
        self.click(self.__pack_size_field)
        return self

    def click_pack_size_10_lb(self):
        self.click(self.__pack_size_10_lb)
        return self

    def click_add_to_cart(self):
        self.click(self.__add_to_cart_button)
        return self

    def get_one_fish_price(self):
        return self.get_text(self.__one_fish_price)

    def get_total_fish_price(self):
        return self.get_text(self.__total_price_calculation)

    def clear_fish_quantity(self):
        self.clear(self.__quantity_field)
        return self

    def send_fish_quantity(self, quantity):
        self.send_keys(self.__quantity_field, quantity)
        return self

    def get_total_fish_quantity(self):
        return self.get_attribute_value(self.__ordered_fish_quantity)

    def click_remove(self):
        self.click(self.__remove_button)
        return self

    def get_removed_fish_message(self):
        return self.get_text(self.__empty_cart_message)





