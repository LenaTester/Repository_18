import pytest
from Repository_18.web_ui.data_generator import random_string, random_phone, random_password
import time

from Repository_18.page_objects.home_page import HomePage
from Repository_18.page_objects.admin_page import AdminPage
from Repository_18.web_ui.driver_factory import DriverFactory


@pytest.fixture()
def create_driver():
    driver = DriverFactory.create_driver(driver_id=1)
    driver.get('https://staging-rgf-frontstore.vercel.app/')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def get_home_page(create_driver):
    return HomePage(create_driver)

@pytest.fixture()
def create_driver_for_admin():
    driver = DriverFactory.create_driver(driver_id=1)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def get_admin_page(create_driver_for_admin):
    driver = create_driver_for_admin
    driver.get('https://staging.rgf.dengun.net/admin/login/?next=/admin/')
    admin_page = AdminPage(driver)
    admin_page.send_admin_email('xxxxxxxxxxxx').send_admin_password('xxxxxxxxx').click_login_button()
    return admin_page

@pytest.fixture()
def host_request(get_home_page):
    home_page = get_home_page
    user_name = random_string()
    user_email = random_string() + '@com'
    user_phone = random_phone()
    user_site = random_string()
    user_message = random_string()
    home_page.click_become_a_host().become_a_host_name(user_name). \
        become_a_host_email(user_email).become_a_host_phone(user_phone).become_a_host_site(user_site). \
        become_a_host_message(user_message).become_a_host_send_button()
    return home_page, user_name, user_email, user_site, user_phone, user_message

@pytest.fixture()
def user_registration(get_home_page):
    user_email = random_string() + '@com'
    user_name = random_string()
    user_lastname = random_string()
    tmp_password = random_password()
    home_page = get_home_page
    successful_registration = home_page.click_sign_in().send_zip_code('50001').click_continue()
    time.sleep(3)
    successful_registration.click_sign_up(). \
        send_first_name(user_name).send_last_name(user_lastname). \
        send_email(user_email).send_phone('2015550124').send_password(tmp_password). \
        send_retype_password(tmp_password).send_address_one(random_string()).send_address_two(random_string()). \
        send_city(random_string()).send_state(random_string()).send_zip('50001').click_agree()
    return successful_registration, user_email, user_name, user_lastname

@pytest.fixture()
def get_subscription_page(get_home_page):
    return get_home_page.move_to_subscription('00501')

@pytest.fixture()
def get_shop_page(get_subscription_page):
    return get_subscription_page.move_to_shop()

@pytest.fixture()
def get_recipies_page(get_home_page):
    return get_home_page.move_to_recipies()
