from selenium.webdriver.common.by import By
import random
import time
from web_ui.base_page import BasePage
from page_objects.shop_page import ShopPage


class SubscriptionPage(BasePage):
    """PLAN"""
    __home_delivery_button = (By.XPATH, "//button[@class='choose-your-plan-button choose-your-plan-button--active']")
    __community_pick_up_button = (By.XPATH, "//button[@class='choose-your-plan-button false']")
    __step_plan = (By.XPATH, "//span[@class='sc-jhLVlY kzRugZ']")
    __step_delivery_options = (By.XPATH, "//span[@class='sc-jhLVlY eJXijH']")
    __step_addon = (By.XPATH, "//span[@class='sc-jhLVlY dakGnJ'][1]")
    __step_checkout = (By.XPATH, "//span[@class='sc-jhLVlY dakGnJ']//following::span")
    __plan_price = (By.XPATH, "//div[@class='plan-price']")
    __quantity_of_servings = (By.XPATH, "//div[@class='plan-price']/following::span")
    __select_this_box_radio = (By.XPATH, "//input[@type = 'radio']")
    __choose_your_products_page_title = (By.XPATH, "//h2[@class = 'sc-eYDgzN bXdttx']")
    __proceed_button = (By.XPATH, "//button[@class='button button--full-width']")
    """DELIVERY OPTIONS"""
    __add_to_cart_button = (By.XPATH, "//button[@class='button  button--full-width']")
    __quantity_of_added_fish = (By.XPATH, "//div[@class='custom-box-summary-quantity']")
    __summary_progress = (By.XPATH, "//div[@class='custom-box-summary-progress-label']")
    __plus_button = (By.XPATH, "//button[@class='sc-dmXgXv grWWxj'][text()='+']")
    __continue_button = (By.XPATH, "//button[@class='button button--full-width']")
    __add_ons_page_title = (By.XPATH, "//h2[@class='sc-hZhUor ggVDmv']")
    """CHECKOUT"""
    __proceed_to_checkout_button = (By.XPATH, "//button[@data-test='ProceedCheckout']")
    __date_field = (By.XPATH, "//div[@class='css-dvua67-singleValue dropdown__single-value']")
    __total_field_title = (By.XPATH, "//div[@class='title'][text()='Total']")
    __total_value = (By.XPATH, "//div[@class='content__info-item-value content__info-item-value--total']")
    __delivery_title = (By.XPATH, "//div[@class='title'][text()='Delivery']")
    __delivery_price = (By.XPATH, "//div[@class='content__info-item-value'][text()='Free']")
    __login_to_checkout_button = (By.XPATH, "//button[@class='button  button--full-width']")
    __input_error_message = (By.XPATH, "//span[@class='input__error']")
    __login_to_checkout_email = (By.XPATH, "//input[@name='email']")
    __login_to_checkout_password = (By.XPATH, "//input[@name='password']")
    __shipping_address_title = (By.XPATH, "//h3[@class='sc-fNHLbd iSiBBU'][text()='Shipping Address']")
    __billing_info_title = (By.XPATH, "//h3[@data-test='checkoutPageSubtitle']")
    __add_new_address_radio = (By.XPATH, "//input[@id='addNewShippingAddressRadio']")
    __shipping_address_name = (By.XPATH, "//input[@name='firstName']")
    __shipping_address_lastname = (By.XPATH, "//input[@name='lastName']")
    __shipping_address_phone = (By.XPATH, "//input[@name='phone']")
    __shipping_address_address_1 = (By.XPATH, "//input[@name='streetAddress1']")
    __shipping_address_address_2 = (By.XPATH, "//input[@name='streetAddress2']")
    __shipping_address_city = (By.XPATH, "//input[@name='city']")
    __shipping_address_postal_code = (By.XPATH, "//input[@name='postalCode']")
    __shipping_address_state = (By.XPATH, "//input[@name='countryArea']")
    __save_shipping_address_button = (By.XPATH, "//button[@data-test='submitButtonAddressForm']")
    __new_address_string = (By.XPATH, "//span[@class='sc-dnqmqq oGfDh']")
    __cart_button = (By.XPATH, "//li[text()='CART']")
    __continue_shopping_button = (By.XPATH, "//button[@name='continueShopping']")

    def __init__(self, driver):
        super().__init__(driver)

    """PLAN"""
    def home_delivery_check(self):
        return self.get_text(self.__home_delivery_button)

    def community_pick_up_check(self):
        return self.get_text(self.__community_pick_up_button)

    def step_plan_check(self):
        return self.get_text(self.__step_plan)

    def step_delivery_options_check(self):
        return self.get_text(self.__step_delivery_options)

    def step_addon_check(self):
        return self.get_text(self.__step_addon)

    def step_checkout_check(self):
        return self.get_text(self.__step_checkout)

    def check_price(self):
        return self.get_text(self.__plan_price)

    def check_quantity_of_servings(self):
        return self.get_text(self.__quantity_of_servings)

    def click_select_this_box(self):
        self.click(self.__select_this_box_radio)
        return self

    def check_new_page_title(self):
        return self.get_text(self.__choose_your_products_page_title)

    def click_proceed_button(self):
        self.click(self.__proceed_button)
        return self

    """DELIVERY OPTIONS"""
    def click_random_fish(self):
        self.click(self.__add_to_cart_button)
        return self

    def get_text_quantity_and_fish(self):
        return self.get_text(self.__quantity_of_added_fish)

    def summary_of_progress(self):
        return self.get_text(self.__summary_progress)

    def click_plus_button(self):
        self.click_2(self.__plus_button)
        return self

    def click_continue_button(self):
        self.click_2(self.__continue_button)
        return self

    def check_add_ons_page_title(self):
        return self.get_text(self.__add_ons_page_title)

    """CHECKOUT"""
    def click_proceed_to_checkout_button(self):
        self.click(self.__proceed_to_checkout_button)
        return self

    def get_date_of_delivery(self):
        return self.get_text(self.__date_field)

    def get_total_field_title(self):
        return self.get_text(self.__total_field_title)

    def get_total_value(self):
        return self.get_text(self.__total_value)

    def get_text_of_delivery_title(self):
        return self.get_text(self.__delivery_title)

    def get_text_of_delivery_cost(self):
        return self.get_text(self.__delivery_price)

    def click_login_to_checkout(self):
        self.click(self.__login_to_checkout_button)
        return self

    def get_text_of_input_error_message(self):
        return self.get_text(self.__input_error_message)

    def send_login_to_checkout_email(self, email):
        self.send_keys(self.__login_to_checkout_email, email)
        return self

    def send_login_to_checkout_password(self, password):
        self.send_keys(self.__login_to_checkout_password, password)
        return self

    def get_text_shipping_address(self):
        return self.get_text(self.__shipping_address_title)

    def get_text_billing_info(self):
        return self.get_text(self.__billing_info_title)

    def click_add_new_address_radio(self):
        self.click(self.__add_new_address_radio)
        return self

    def send_shipping_address_name(self, name):
        self.send_keys(self.__shipping_address_name, name)
        return self

    def send_shipping_address_lastname(self, lastname):
        self.send_keys(self.__shipping_address_lastname, lastname)
        return self

    def send_shipping_address_phone(self, phone):
        self.send_keys(self.__shipping_address_phone, phone)
        return self

    def send_shipping_address_address_1(self, address_1):
        self.send_keys(self.__shipping_address_address_1, address_1)
        return self

    def send_shipping_address_address_2(self, address_2):
        self.send_keys(self.__shipping_address_address_2, address_2)
        return self

    def send_shipping_address_city(self, city):
        self.send_keys(self.__shipping_address_city, city)
        return self

    def send_shipping_address_postal_code(self, postal_code):
        self.send_keys(self.__shipping_address_postal_code, postal_code)
        return self

    def send_shipping_address_state(self, state):
        self.send_keys(self.__shipping_address_state, state)
        return self

    def click_save_shipping_address(self):
        self.click(self.__save_shipping_address_button)
        return self

    def get_text_new_address(self):
        return self.get_text_multi(self.__new_address_string)

    def move_to_shop(self):
        time.sleep(2)
        self.click(self.__cart_button)
        self.click(self.__continue_shopping_button)
        return ShopPage(self.driver)
