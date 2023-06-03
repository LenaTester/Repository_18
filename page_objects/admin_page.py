from selenium.webdriver.common.by import By

from web_ui.base_page import BasePage


class AdminPage(BasePage):
    """LOG IN - for admin"""
    __email_field = (By.XPATH, "//input[@placeholder='Email']")
    __password_field = (By.XPATH, "//input[@placeholder='Password']")
    __login_button = (By.XPATH, "//input[@class='btn btn-primary']")
    __admin_page_title = (By.XPATH, "//span[@class='breadcrumb-icon']/following::span")
    """HOST SITE"""
    __deliveries_button = (By.XPATH, "//a[@href='#deliveries']")
    __host_requests_button = (By.XPATH, "//a[@href='/admin/rgf_delivery/hostrequest/']")
    __search_field = (By.XPATH, "//input[@type='text']")
    __search_button = (By.XPATH, "//button[@type='submit']")
    __new_record_email = (By.XPATH, "//td[@class='field-email']")
    __link_to_host_data = (By.XPATH, "//th[@class='field-name']/a")
    __new_host_name_field = (By.XPATH, "//input[@name='name']")
    __new_host_email_field = (By.XPATH, "//input[@name='email']")
    __new_host_phone_field = (By.XPATH, "//input[@name='phone_number']")
    __new_host_site_field = (By.XPATH, "//input[@name='site_address']")
    __new_host_message_field = (By.XPATH, "//textarea[@name='message']")
    """SIGN UP"""
    __users_link = (By.XPATH, "//a[@href='/admin/account/user/'][text()='Users']")
    __search_users_field = (By.XPATH, "//input[@placeholder='Search \"Users\"']")
    __search_user_button = (By.XPATH, "//button[@class='btn btn-outline-secondary']")
    __new_user_email = (By.XPATH, "//td[@class='field-email']")
    __link_to_user_data = (By.XPATH, "//th[@class='field-id']/a")
    __new_user_email_field = (By.XPATH, "//input[@type='email']")
    __new_user_first_name_field = (By.XPATH, "//input[@name='first_name']")
    __new_user_lastname_field = (By.XPATH, "//input[@name='last_name']")

    def __init__(self, driver):
        super().__init__(driver)

    """LOG IN"""
    def send_admin_email(self, admin_email):
        self.send_keys(self.__email_field, admin_email)
        return self

    def send_admin_password(self, admin_password):
        self.send_keys(self.__password_field, admin_password)
        return self

    def click_login_button(self):
        self.click(self.__login_button)
        return self

    def get_page_header(self):
        return self.get_text(self.__admin_page_title)

    """HOST SITE"""
    def click_deliveries(self):
        self.click(self.__deliveries_button)
        return self

    def click_host_requests(self):
        self.click_2(self.__host_requests_button)
        return self

    def send_new_email(self, host_email):
        self.send_keys(self.__search_field, host_email)
        return self

    def click_search_button(self):
        self.click(self.__search_button)
        return self

    def new_record_email_check(self):
        return self.get_text(self.__new_record_email)

    def click_link_to_new_host(self):
        self.click(self.__link_to_host_data)
        return self

    def new_host_name_check(self):
        return self.get_attribute_value(self.__new_host_name_field)

    def new_host_email_check(self):
        return self.get_attribute_value(self.__new_host_email_field)

    def new_host_phone_check(self):
        return self.get_attribute_value(self.__new_host_phone_field)

    def new_host_site_check(self):
        return self.get_attribute_value(self.__new_host_site_field)

    def new_host_message_check(self):
        return self.get_text(self.__new_host_message_field)

    """SIGN UP"""

    def click_users_link(self):
        self.click(self.__users_link)
        return self

    def send_new_user_email(self, user_email):
        self.send_keys(self.__search_users_field, user_email)
        return self

    def click_search_user(self):
        self.click(self.__search_user_button)
        return self

    def new_user_email_check(self):
        return self.get_text(self.__new_user_email)

    def click_user_data_link(self):
        self.click(self.__link_to_user_data)
        return self

    def new_user_email_check(self):
        return self.get_attribute_value(self.__new_user_email_field)

    def new_user_name_check(self):
        return self.get_attribute_value(self.__new_user_first_name_field)

    def new_user_lastname_check(self):
        return self.get_attribute_value(self.__new_user_lastname_field)
