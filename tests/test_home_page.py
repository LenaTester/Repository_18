import pytest
import time
from web_ui.data_generator import random_string, random_phone, random_password, random_zip

"""GET STARTED"""

@pytest.mark.parametrize('correct_zip', (80001, '00501', '02801'))
def test_get_started_correct_zip(correct_zip, get_home_page):
    """test zip code - positive test - correct zip codes - 1"""
    home_page = get_home_page
    chose_your_plan_page = home_page.click_sign_in().send_zip_code(correct_zip).click_continue().get_page_header()
    assert chose_your_plan_page == 'Choose your plan', \
        f'\nTitle is not as expected\nActual: {chose_your_plan_page}\nExpected: "Choose your plan"'

@pytest.mark.parametrize('correct_zip', (80001, '00501', '02801'))
def test_get_started_zip_in_right_corner(correct_zip, get_home_page):
    """test zip code - positive test - correct state in right corner - 2"""
    home_page = get_home_page
    chose_your_plan_page = home_page.click_sign_in().send_zip_code(correct_zip).click_continue().get_state_from_right_corner()
    assert chose_your_plan_page == 'Western U.S.', \
        f'\nTitle is not as expected\nActual: {chose_your_plan_page}\nExpected: "Western U.S."'

@pytest.mark.parametrize('wrong_zip', (123456, 1234, 'False'))
def test_get_started_wrong_zip(wrong_zip, get_home_page):
    """test zip code - negative test - non-existing zip codes - 3"""
    home_page = get_home_page
    chose_your_plan_page = home_page.click_sign_in().send_zip_code(wrong_zip).click_continue().get_wrong_zip_message()
    assert chose_your_plan_page == f'Sorry, the Zip Code: {wrong_zip}, isn\'t covered by our services yet', \
        f'\nTitle is not as expected\nActual: {chose_your_plan_page}' \
        f'\nExpected: "Sorry, the Zip Code: 111111, isn\'t covered by our services yet"'

"""SIGN UP"""

def test_positive_register(get_home_page):
    """test zip code - positive test - user registration is finished - 4"""
    user_email = random_string() + '@com'
    tmp_password = random_password()
    home_page = get_home_page
    successful_registration = home_page.click_sign_in().send_zip_code('00501').click_continue()
    time.sleep(5)
    successful_registration.click_sign_up(). \
        send_first_name(random_string()).send_last_name(random_string()). \
        send_email(user_email).send_phone('2015550124').send_password(tmp_password). \
        send_retype_password(tmp_password).send_address_one(random_string()).send_address_two(random_string()). \
        send_city(random_string()).send_state(random_string()).send_zip('50001').click_agree().get_chose_plan_header()
    assert successful_registration == 'Choose your plan', \
        f'\nRegistration is not successful\nActual: {successful_registration}\nExpected: "Choose your plan"'

def test_negative_register_wrong_email(get_home_page):
    """negative test - user registration with not-correct email - 5"""
    home_page = get_home_page
    user_email = random_string()
    registration_wrong_email = home_page.click_sign_up().send_first_name(random_string()).send_last_name(random_string()). \
        send_email(user_email).wrong_email_message()
    assert registration_wrong_email == f'Please include an \'@\' in the email address. \'{user_email}\' is missing an \'@\'.', \
        f'\nEmail is not correct\nActual: {registration_wrong_email}' \
        f'\nExpected: Please include an \'@\' in the email address. \'{user_email}\' is missing an \'@\'.'

def test_positive_register_wrong_phone(get_home_page):
    """negative test - user registration with not-correct phone - 6"""
    home_page = get_home_page
    user_email = random_string() + '@com'
    user_phone = 'abc'
    tmp_password = random_password()
    registration_wrong_phone = home_page.click_sign_in().send_zip_code('00501').click_continue()
    time.sleep(5)
    registration_wrong_phone.click_sign_up(). \
        send_first_name(random_string()).send_last_name(random_string()). \
        send_email(user_email).send_phone(user_phone).send_password(tmp_password). \
        send_retype_password(tmp_password).send_address_one(random_string()).send_address_two(random_string()). \
        send_city(random_string()).send_state(random_string()).send_zip('50001').click_agree()
    registration_wrong_phone.wrong_phone_message()
    assert registration_wrong_phone == f'+1abc is not a valid phone number.', \
        f'\nPhone is not correct\nActual: {registration_wrong_phone}' \
        f'\nExpected: +1abc is not a valid phone number.'

    """CONTACT US"""
def test_contact_us_button_is_working(get_home_page):
    """after clicking Contact Us user is redirected to new page - 7"""
    home_page = get_home_page
    successful_contact_us_click = home_page.click_contact_us().contact_us_successful_click()
    assert successful_contact_us_click == 'Contact Us', \
        f'\nContact Us button is working\nActual: {successful_contact_us_click}' \
        f'\nExpected: Contact Us'

def test_positive_contact_us(get_home_page):
    """positive test - user can send a message - 8"""
    home_page = get_home_page
    user_email = random_string() + '@com'
    successful_message = home_page.click_contact_us().send_contact_us_name(random_string()).\
        send_contact_us_email(user_email).send_contact_us_subject(random_string()).\
        send_contact_us_message(random_string()).click_send_message().get_notification_text()
    assert successful_message == 'Feel free to get in touch', \
        f'\nMessage is not send\nActual: {successful_message}' \
        f'\nExpected: Feel free to get in touch'

    """HOST SITE"""
def test_host_site_positive_attempt(get_home_page):
    """positive test - user can send request to become a host - 9"""
    home_page = get_home_page
    user_email = random_string() + '@com'
    successful_attempt = home_page.click_become_a_host().become_a_host_name(random_string()).\
        become_a_host_email(user_email).become_a_host_phone(random_phone()).become_a_host_site(random_string()). \
        become_a_host_message(random_string()).become_a_host_send_button().become_a_host_notification()
    assert successful_attempt == 'Your message has been submitted, we will reply as soon as possible.', \
        f'\nRequest is not sent\nActual: {successful_attempt}' \
        f'\nExpected: Your message has been submitted, we will reply as soon as possible.'

def test_host_registration_return(host_request):
    """when new host is registered, Back button is working - 10"""
    home_page = host_request[0]
    successful_attempt = home_page.click_become_a_host_back().become_a_host_get_back_notification()
    assert successful_attempt == 'Become A Site Host', \
        f'\nRequest is not sent\nActual: {successful_attempt}' \
        f'\nExpected: Become A Site Host'

    """FOOTER"""
def test_how_it_works_link_is_working(get_home_page):
    """after clicking How it Works user is redirected to new page - 11"""
    home_page = get_home_page
    successful_how_it_work_redirect = home_page.click_how_it_works().get_title_how_it_works()
    assert successful_how_it_work_redirect == 'How it works', \
        f'\nHow it Works button is not working\nActual: {successful_how_it_work_redirect}' \
        f'\nExpected: How it works'

def test_get_started_link_is_working(get_home_page):
    """after clicking Get Started user is redirected to new page - 12"""
    home_page = get_home_page
    successful_get_started_redirect = home_page.click_get_started_footer().get_title_get_started()
    assert successful_get_started_redirect == 'What’s your location?', \
        f'\nGet Started button is not working\nActual: {successful_get_started_redirect}' \
        f'\nExpected: What’s your location?'

def test_instagramm_link_is_working(get_home_page):
    """after clicking Instagram icon is redirected to Instagram - 13"""
    home_page = get_home_page
    successful_instagramm_redirect = home_page.click_footer_twitter().\
        click_accept_cookie().\
        click_close_login_to_instagramm_button().get_title_company_name()
    assert successful_instagramm_redirect == 'realgoodfish', \
        f'\nInstagramm redirect is not working\nActual: {successful_instagramm_redirect}' \
        f'\nExpected: realgoodfish'

"""LOG IN"""
def test_successful_login(get_home_page):
    """positive case - after clicking Log In user successfuly logs in - 14"""
    home_page = get_home_page
    successful_login = home_page.click_log_in().send_log_in_email('test@test.commm').send_log_in_password('goodpass1'). \
        click_log_in_submit().get_username()
    assert successful_login == 'TEST', \
        f'\nLog in successful\nActual: {successful_login}' \
        f'\nExpected: TEST'

def test_login_wrong_password(get_home_page):
    """negative case - attempt to log in with wrong password - 15"""
    home_page = get_home_page
    login_with_wrong_creds = home_page.click_log_in().send_log_in_email('test@test.commm').send_log_in_password('wrongpass1'). \
        click_log_in_submit()
    time.sleep(5)
    login_with_wrong_creds.get_wrong_creds_notice()
    assert login_with_wrong_creds == 'Please, enter valid credentials', \
        f'\nLog in failed\nActual: {login_with_wrong_creds}' \
        f'\nExpected: Please, enter valid credentials'

def test_login_wrong_email(get_home_page):
    """negative case - attempt to log in with wrong email - 16"""
    home_page = get_home_page
    login_with_wrong_creds = home_page.click_log_in().send_log_in_email('wrong_user@test.commm').send_log_in_password('goodgpass1'). \
        click_log_in_submit()
    time.sleep(2)
    login_with_wrong_creds.get_wrong_creds_notice()
    assert login_with_wrong_creds == 'Please, enter valid credentials', \
        f'\nLog in failed\nActual: {login_with_wrong_creds}' \
        f'\nExpected: Please, enter valid credentials'

def test_successful_log_out(get_home_page):
    """after loggin in user can log out - 17"""
    home_page = get_home_page
    successful_logout = home_page.click_log_in().send_log_in_email('test@test.commm').send_log_in_password('goodpass1'). \
        click_log_in_submit().hover_to_username().click_logout()
    time.sleep(2)
    assert successful_logout == 'LOG IN', \
        f'\nSuccessful log out\nActual: {successful_logout}' \
        f'\nExpected: LOG IN'

    """SHOP"""
def test_redirection_to_shopping_page(get_home_page):
    """after clicking Shop on Demand shopping page is opened - 18"""
    home_page = get_home_page
    redirection_to_shopping_page = home_page.click_shop_on_demand().get_shop_by_category_title()
    assert redirection_to_shopping_page == 'Shop by Category', \
        f'\nSuccessful log out\nActual: {redirection_to_shopping_page}' \
        f'\nExpected: Shop by Category'



