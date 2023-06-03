from selenium.webdriver.common.by import By

from web_ui.base_page import BasePage
from page_objects.subscription_page import SubscriptionPage
from page_objects.recipies_page import RecipiesPage

class HomePage(BasePage):
    """GET STARTED"""
    __get_started_button = (By.XPATH, "(//button[text() = 'Get Started'])[1]")
    __zip_code_field = (By.XPATH, "//*[contains(@autocomplete, 'zipCode')]")
    __continue_button = (By.XPATH, "//button[contains(@data-test, 'submitLocationFormButton')]")
    __plan_page_header = (By.XPATH, "//h2")
    __form_error = (By.XPATH, "//span[@class='form-error']")
    __state_and_zip_info = (By.XPATH, "//div[@class='sc-eMigcr bxtuQF']")
    """SIGN UP"""
    __sign_up_button = (By.XPATH, "//li[text()='SIGN UP']")
    __form_title = (By.XPATH, "//div[@class='choose-your-plan-intro']/h2")
    __first_name_field = (By.XPATH, "//input[contains(@name, 'firstName')]")
    __last_name_field = (By.XPATH, "//input[contains(@name, 'lastName')]")
    __email_field = (By.XPATH, "//input[contains(@name, 'email')]")
    __phone_field = (By.XPATH, "//input[contains(@type, 'tel')]")
    __password_field = (By.XPATH, "//input[contains(@name, 'password')]")
    __retype_password = (By.XPATH, "//input[contains(@name, 'retypePassword')]")
    __address_one = (By.XPATH, "//input[contains(@name, 'streetAddress1')]")
    __address_two = (By.XPATH, "//input[contains(@name, 'streetAddress2')]")
    __city_field = (By.XPATH, "//input[contains(@name, 'city')]")
    __state_field = (By.XPATH, "//input[contains(@name, 'countryArea')]")
    __postal_code_field = (By.XPATH, "//input[contains(@name, 'postalCode')]")
    __agree_button = (By.XPATH, "//button[@class='button  button--full-width']")
    __email_error_message = (By.XPATH, "//input[@name='email']/following::span[2]")
    __phone_error_message = (By.XPATH, "//input[@type='tel']/following::span")
    __sign_up_for_new_test = (By.XPATH, "//li[@data-test='desktopMenuLoginOverlayLink'][text() = 'SIGN UP']")
    """CONTACT US"""
    __contact_us_button = (By.XPATH, "//a[@href='/contact-us']")
    __contact_us_form_open = (By.XPATH, "//div[@class='sc-kUQWMX hNhVjA']")
    __contact_us_name = (By.XPATH, "//input[@name='name']")
    __contact_us_email = (By.XPATH, "//input[@name='email']")
    __contact_us_subject = (By.XPATH, "//input[@name='subject']")
    __contact_us_message = (By.XPATH, "//textarea[@name='message']")
    __send_message_button = (By.XPATH, "//button[@data-test='ContactFormSubmit']")
    __notification_contact_us = (By.XPATH, "//h2")
    """BECOME A HOST"""
    __become_a_host_button = (By.XPATH, "//a[@href='/become-a-site-host']")
    __become_a_host_name = (By.XPATH, "//input[@name='name']")
    __become_a_host_email = (By.XPATH, "//input[@name='email']")
    __become_a_host_phone = (By.XPATH, "//input[@name='phoneNumber']")
    __become_a_host_site = (By.XPATH, "//input[@name='siteAddress']")
    __become_a_host_message = (By.XPATH, "//textarea[@name='message']")
    __become_a_host_send_button = (By.XPATH, "//button[@data-test='BecomeASiteHostFormSubmit']")
    __become_a_host_notification = (By.XPATH, "//div[@class='sc-eerKOB jeMoNi']")
    __become_a_host_back_button = (By.XPATH, "//a[@href='/become-a-site-host'][text()='Back']")
    __become_a_host_return_message = (By.XPATH, "//h2[@class='sc-bMVAic fEsqsG']")
    """FOOTER"""
    __footer_how_it_works_link = (By.XPATH, "//div[@class='sc-goBNrf dignCQ']/descendant::a")
    __footer_how_it_works_title = (By.XPATH, "//h1[@class='sc-bMVAic fEsqsG']")
    __footer_get_started_button = (By.XPATH, "//button[@class='sc-iAyFgw sc-gPEVay dEYyNE']")
    __footer_get_started_next_page_title = (By.XPATH, "//div[@class='location__header']/h3")
    __footer_instagram_link = (By.XPATH, "//span[text()='instagram']")
    __instagram_cookie_dialog = (By.XPATH, "//div[@role='dialog']")
    __accept_cookie_instagramm = (By.XPATH, "//button[text()='Only allow essential cookies']")
    __login_to_instagramm_close_button = (By.XPATH, "//span[@aria-label='Close']")
    __company_name_in_instagramm = (By.XPATH, "//h2[@class='_aacl _aacs _aact _aacx _aada']")
    """LOG IN"""
    __log_in_button = (By.XPATH, "//li[@data-test='desktopMenuLoginOverlayLink']")
    __log_in_email_field = (By.XPATH, "//input[@name='email']")
    __log_in_password_field = (By.XPATH, "//input[@name='password']")
    __log_in_submit_button = (By.XPATH, "//button[@data-test='submit']")
    __username = (By.XPATH, "//span[contains(@class, 'main-menu__user')]")
    __logout_button = (By.XPATH, "//li[@data-test='desktopMenuLogoutLink']/a")
    __wrong_creds_notification = (By.XPATH, "//span[@class='input__error']")
    __my_account_button = (By.XPATH, "//li[@data-test='desktopMenuMyAccountLink']/a")
    """SHOP"""
    __shop_on_demand_button = (By.XPATH, "//a[@href='/shop/']")
    __shop_by_category_title = (By.XPATH, "//h2[text()='Shop by Category']")
    """RECIPIES"""
    __recipies_link = (By.XPATH, "//a[text()='Recipes']")

    def __init__(self, driver):
        super().__init__(driver)

    """GET STARTED"""
    def click_sign_in(self):
        self.click(self.__get_started_button)
        return self

    def send_zip_code(self, zip_code):
        self.send_keys(self.__zip_code_field, zip_code)
        return self

    def click_continue(self):
        self.click_2(self.__continue_button)
        return self

    def get_page_header(self):
        return self.get_text(self.__plan_page_header)

    def get_wrong_zip_message(self):
        return self.get_text(self.__form_error)

    def get_state_from_right_corner(self):
        return self.get_text(self.__state_and_zip_info)

    """SIGN UP"""
    def click_sign_up(self):
        self.click_2(self.__sign_up_button)
        return self

    def send_first_name(self, first_name):
        self.send_keys(self.__first_name_field, first_name)
        return self

    def send_last_name(self, last_name):
        self.send_keys(self.__last_name_field, last_name)
        return self

    def send_email(self, email):
        self.send_keys(self.__email_field, email)
        return self

    def send_phone(self, phone):
        self.send_keys(self.__phone_field, phone)
        return self

    def send_password(self, password):
        self.send_keys(self.__password_field, password)
        return self

    def send_retype_password(self, retype_password):
        self.send_keys(self.__retype_password, retype_password)
        return self

    def send_address_one(self, address_one):
        self.send_keys(self.__address_one, address_one)
        return self

    def send_address_two(self, address_two):
        self.send_keys(self.__address_two, address_two)
        return self

    def send_city(self, city):
        self.send_keys(self.__city_field, city)
        return self

    def send_state(self, state):
        self.send_keys(self.__state_field, state)
        return self

    def send_zip(self, zip):
        self.send_keys(self.__postal_code_field, zip)
        return self

    def click_agree(self):
        self.click_2(self.__agree_button)
        return self

    def get_chose_plan_header(self):
        return self.get_text(self.__form_title)

    def wrong_email_message(self):
        return self.get_text(self.__email_error_message)

    def wrong_phone_message(self):
        return self.get_text(self.__phone_error_message)


    """CONTACT US"""
    def click_contact_us(self):
        self.click(self.__contact_us_button)
        return self

    def contact_us_successful_click(self):
        return self.get_text(self.__contact_us_form_open)

    def send_contact_us_name(self, name):
        self.send_keys(self.__contact_us_name, name)
        return self

    def send_contact_us_email(self, email):
        self.send_keys(self.__contact_us_email, email)
        return self

    def send_contact_us_subject(self, subject):
        self.send_keys(self.__contact_us_subject, subject)
        return self

    def send_contact_us_message(self, message):
        self.send_keys(self.__contact_us_message, message)
        return self

    def click_send_message(self):
        self.click(self.__send_message_button)
        return self

    def get_notification_text(self):
        return self.get_text(self.__notification_contact_us)

    """BECOME A HOST"""
    def click_become_a_host(self):
        self.click(self.__become_a_host_button)
        return self

    def become_a_host_name(self, name):
        self.send_keys(self.__become_a_host_name, name)
        return self

    def become_a_host_email(self, email):
        self.send_keys(self.__become_a_host_email, email)
        return self

    def become_a_host_phone(self, phone):
        self.send_keys(self.__become_a_host_phone, phone)
        return self

    def become_a_host_site(self, site):
        self.send_keys(self.__become_a_host_site, site)
        return self

    def become_a_host_message(self, message):
        self.send_keys(self.__become_a_host_message, message)
        return self

    def become_a_host_send_button(self):
        self.click_2(self.__become_a_host_send_button)
        return self

    def become_a_host_notification(self):
        return self.get_text(self.__become_a_host_notification)

    def click_become_a_host_back(self):
        self.click(self.__become_a_host_back_button)
        return self

    def become_a_host_get_back_notification(self):
        return self.get_text(self.__become_a_host_return_message)

    """FOOTER"""
    def click_how_it_works(self):
        self.click(self.__footer_how_it_works_link)
        return self

    def get_title_how_it_works(self):
        return self.get_text(self.__footer_how_it_works_title)

    def click_get_started_footer(self):
        self.click(self.__footer_get_started_button)
        return self

    def get_title_get_started(self):
        return self.get_text(self.__footer_get_started_next_page_title)

    def click_footer_twitter(self):
        self.click(self.__footer_instagram_link)
        return self

    def click_accept_cookie(self):
        self.click(self.__accept_cookie_instagramm)
        return self

    def click_close_login_to_instagramm_button(self):
        self.click(self.__login_to_instagramm_close_button)
        return self

    def get_title_company_name(self):
        return self.get_text(self.__company_name_in_instagramm)

    def switch_to_cookie(self):
        return self.switch(self.__instagram_cookie_dialog)

    """LOG IN"""
    def click_log_in(self):
        self.click(self.__log_in_button)
        return self

    def send_log_in_email(self, email):
        self.send_keys(self.__log_in_email_field, email)
        return self

    def send_log_in_password(self, password):
        self.send_keys(self.__log_in_password_field, password)
        return self

    def click_log_in_submit(self):
        self.click(self.__log_in_submit_button)
        return self

    def get_username(self):
        return self.get_text(self.__username)

    def hover_to_username(self):
        return self.hover(self.__username)

    def click_logout(self):
        self.click(self.__logout_button)
        return self

    def click_my_account(self):
        self.click(self.__my_account_button)
        return self

    def get_log_in_button_text(self):
        return self.get_text(self.__log_in_button)

    def get_wrong_creds_notice(self):
        return self.get_text(self.__wrong_creds_notification)

    def move_to_subscription(self, zip_code):
        self.click(self.__get_started_button)
        self.send_keys(self.__zip_code_field, zip_code)
        self.click(self.__continue_button)
        return SubscriptionPage(self.driver)

    """SHOP"""
    def click_shop_on_demand(self):
        self.click(self.__shop_on_demand_button)
        return self

    def get_shop_by_category_title(self):
        return self.get_text(self.__shop_by_category_title)

    def click_cart_button(self):
        self.click(self.__cart_button)
        return self

    def click_continue_shopping_button(self):
        self.click(self.__continue_shopping_button)
        return self

    def move_to_recipies(self):
        self.click(self.__recipies_link)
        return RecipiesPage(self.driver)
