def test_admin(get_admin_page):
    """test successful login for admin - 1"""
    result = get_admin_page.get_page_header()
    assert result == 'Dashboard'
    f'\nTitle is not correct\nActual: {result}' \
    f'\nExpected: Dashboard'

def test_successful_host_request(host_request, get_admin_page):
    """test adding new host - 2"""
    new_email = host_request[2]
    email_in_admin = get_admin_page.click_deliveries().click_host_requests().send_new_email(new_email).\
    click_search_button().new_record_email_check()
    assert new_email == email_in_admin
    f'\nEmail is not correct\nActual: {email_in_admin}' \
    f'\nExpected: {new_email}'

def test_correct_host_data(host_request, get_admin_page):
    """test checking host data - 3"""
    new_name = host_request[1]
    new_email = host_request[2]
    new_site = host_request[3]
    new_phone = host_request[4]
    new_message = host_request[5]
    get_new_host_data = get_admin_page.click_deliveries().click_host_requests().send_new_email(new_email).\
    click_search_button().click_link_to_new_host()
    name_in_admin = get_new_host_data.new_host_name_check()
    email_in_admin = get_new_host_data.new_host_email_check()
    site_in_admin = get_new_host_data.new_host_site_check()
    phone_in_admin = get_new_host_data.new_host_phone_check()
    message_in_admin = get_new_host_data.new_host_message_check()
    assert new_name == name_in_admin
    f'\nEmail is not correct\nActual: {name_in_admin}' \
    f'\nExpected: {new_name}'
    assert new_email == email_in_admin
    f'\nEmail is not correct\nActual: {email_in_admin}' \
    f'\nExpected: {new_email}'
    assert new_site == site_in_admin
    f'\nEmail is not correct\nActual: {site_in_admin}' \
    f'\nExpected: {new_site}'
    assert new_phone == phone_in_admin
    f'\nEmail is not correct\nActual: {phone_in_admin}' \
    f'\nExpected: {new_phone}'
    assert new_message == message_in_admin
    f'\nEmail is not correct\nActual: {message_in_admin}' \
    f'\nExpected: {new_message}'

def test_successful_user_registration(user_registration, get_admin_page):
    """test adding new user - 4"""
    new_email = user_registration[1]
    email_in_admin = get_admin_page.click_users_link().send_new_user_email(new_email).click_search_user().new_user_email_check()
    assert new_email == email_in_admin
    f'\nEmail is not correct\nActual: {email_in_admin}' \
    f'\nExpected: {new_email}'

def test_correct_user_data(user_registration, get_admin_page):
    """test checking user data - 5"""
    new_email = user_registration[1]
    new_name = user_registration[2]
    new_lastname = user_registration[3]
    get_new_user_data = get_admin_page.click_users_link().send_new_user_email(new_email).click_search_user().click_user_data_link()
    email_in_admin = get_new_user_data.new_user_email_check()
    name_in_admin = get_new_user_data.new_user_name_check()
    lastname_in_admin = get_new_user_data.new_user_lastname_check()
    assert new_email == email_in_admin
    f'\nEmail is not correct\nActual: {email_in_admin}' \
    f'\nExpected: {new_email}'
    assert new_name == name_in_admin
    f'\nName is not correct\nActual: {name_in_admin}' \
    f'\nExpected: {new_name}'
    assert new_lastname == lastname_in_admin
    f'\nLastname is not correct\nActual: {lastname_in_admin}' \
    f'\nExpected: {new_lastname}'
