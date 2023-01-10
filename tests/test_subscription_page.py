import re
from pythonProject.Repository_18.web_ui.data_generator import random_string, random_phone, random_password, random_zip
from selenium.common.exceptions import TimeoutException
import time

"""PLAN"""
def test_plan_options_presence(get_subscription_page):
    """check, that Home Delivery and Community Pick Up options are present - 1"""
    options = []
    home_delivery = get_subscription_page.home_delivery_check()
    community_pick_up = get_subscription_page.community_pick_up_check()
    options.extend([home_delivery, community_pick_up])
    assert options == ['Home Delivery', 'Community Pick-up'], \
        f'\nOne or both options are missing\nActual: {options}' \
        f'\nExpected: Home Delivery, Community Pick-up'

def test_plan_steps_presence(get_subscription_page):
    """check, that Plan steps are present - 2"""
    steps = []
    plan = get_subscription_page.step_plan_check()
    delivery_options = get_subscription_page.step_delivery_options_check()
    addons = get_subscription_page.step_addon_check()
    checkout = get_subscription_page.step_checkout_check()
    steps.extend([plan, delivery_options, addons, checkout])
    assert steps == ['Plan', 'Delivery Options', 'Addons', 'Checkout'], \
        f'\nOne or several steps are missing\nActual: {steps}' \
        f'\nExpected: Plan, Delivery Options, Addons, Checkout'

def test_plan_price_presence(get_subscription_page):
    """check, that price of plan is shown - 3"""
    price_check = get_subscription_page.check_price()
    listed_price = list(price_check)
    first_element = listed_price[0]
    price = listed_price[1:]
    price_string = ''.join(price).replace('.', '')
    price_string_is_digit = price_string.isdigit()
    assert first_element == '$', \
        f'\nPrice is missing\nActual: {first_element}' \
        f'\nExpected: $'
    assert price_string_is_digit == True, \
        f'\nPrice is missing\nActual: {price_string_is_digit}' \
        f'\nExpected: digit'

def test_plan_quantity_of_servings(get_subscription_page):
    """check, that quantity of sevings is shown - 4"""
    quantity_of_servings_check = get_subscription_page.check_quantity_of_servings()
    quantity_list = re.findall('^\S', quantity_of_servings_check)
    quantity = quantity_list[0]
    check_if_digit = quantity.isdigit()
    assert check_if_digit == True, \
        f'\nQuantity of servings is missing\nActual: {check_if_digit}' \
        f'\nExpected: $'

def test_redirection_after_choosing_plan(get_subscription_page):
    """check, that after choosing plan user is redirected to next page - 5"""
    choose_your_products = get_subscription_page.click_select_this_box().click_proceed_button().check_new_page_title()
    assert choose_your_products == 'Choose your products and\ncustomize your box', \
        f'\nRedirection is not working\nActual: {choose_your_products}' \
        f'\nExpected: Choose your products and\ncustomize your box'

"""DELIVERY OPTIONS"""
def test_user_can_add_fish_to_plan(get_subscription_page):
    """check, that user can add fish to plan - 6"""
    adding_fish = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().get_text_quantity_and_fish()
    quantity_list = re.findall('[0-9]', adding_fish)
    quantity = quantity_list[0]
    quantity_is_digit = quantity.isdigit()
    assert quantity_is_digit == True, \
        f'\nUser can not add fish\nActual: {quantity_is_digit}' \
        f'\nExpected: True'

def test_check_progress_of_subscription(get_subscription_page):
    """check, that user can see, how many items he can add - 7"""
    adding_fish = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().summary_of_progress()
    check_for_pattern = re.findall('[0-9] of [0-9]', adding_fish)
    assert adding_fish == check_for_pattern[0], \
        f'\nUser can not add fish\nActual: {check_for_pattern}' \
        f'\nExpected: True'

def test_check_adding_items_and_continue(get_subscription_page):
    """check, that user can add items and continue - 8"""
    adding_fish = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().click_plus_button().click_plus_button().click_plus_button().click_continue_button(). \
        check_add_ons_page_title()
    assert adding_fish == 'Choose Your Add-ons', \
    f'\nRedirection is not working\nActual: {adding_fish}' \
    f'\nExpected: Choose Your Add-ons'

    """CHECKOUT"""
def test_check_first_delivery_date_presence(get_subscription_page):
    """check, that first delivery date is shown - 9"""
    date_of_delivery = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().click_plus_button().click_plus_button().click_plus_button().click_continue_button(). \
        click_proceed_to_checkout_button().get_date_of_delivery()
    list_delivery_date = date_of_delivery.split()
    assert list_delivery_date[0] in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'], \
    f'\nFirst delivery date is not shown\nActual: {list_delivery_date[0]}' \
    f'\nExpected: Monday'
    assert list_delivery_date[1] in ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], \
    f'\nFirst delivery date is not shown\nActual: {list_delivery_date[1]}' \
    f'\nExpected: December'
    assert list_delivery_date[2].isdigit() == True, \
    f'\nFirst delivery date is not shown\nActual: {list_delivery_date[2]}' \
    f'\nExpected: 01'

def test_check_total_value_presence(get_subscription_page):
    """check, that total value is present - 10"""
    total_value = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().click_plus_button().click_plus_button().click_plus_button().click_continue_button(). \
        click_proceed_to_checkout_button()
    total_value_title = total_value.get_total_field_title()
    total_value_price = total_value.get_total_value()
    listed_value = list(total_value_price)
    first_element = listed_value[0]
    value = listed_value[1:]
    value_string = ''.join(value).replace('.', '')
    value_string_is_digit = value_string.isdigit()
    assert total_value_title == 'Total', \
        f'\nTotal title is missing\nActual: {total_value_title}' \
        f'\nExpected: Total'
    assert first_element == '$', \
        f'\nPrice is missing\nActual: {first_element}' \
        f'\nExpected: $'
    assert value_string_is_digit == True, \
        f'\nPrice is missing\nActual: {value_string_is_digit}' \
        f'\nExpected: digit'

def test_check_cost_of_delivery(get_subscription_page):
    """check, that delivery is free - 11"""
    cost_of_delivery = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().click_plus_button().click_plus_button().click_plus_button().click_continue_button(). \
        click_proceed_to_checkout_button()
    delivery_title = cost_of_delivery.get_text_of_delivery_title()
    cost_of_delivery_value = cost_of_delivery.get_text_of_delivery_cost()
    assert delivery_title == 'Delivery', \
        f'\nDelivery is missing or not free\nActual: {delivery_title}' \
        f'\nExpected: Delivery'
    assert cost_of_delivery_value == 'Free', \
        f'\nDelivery is missing or not free\nActual: {cost_of_delivery_value}' \
        f'\nExpected: Free'

def test_checkout_login_without_subscription(get_subscription_page):
    """check, that login without subscription is not possible - 12"""
    no_subscription_message = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().click_plus_button().click_plus_button().click_plus_button().click_continue_button(). \
        click_proceed_to_checkout_button().click_login_to_checkout().get_text_of_input_error_message()
    assert no_subscription_message == 'Please fill out this field.', \
        f'\nNo warning for Login without subscription\nActual: {no_subscription_message}' \
        f'\nExpected: Please fill out this field.'

def test_checkout_login_wrong_email(get_subscription_page):
    """check, that login with wrong email is not possible - 13"""
    no_subscription_message = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().click_plus_button().click_plus_button().click_plus_button().click_continue_button(). \
        click_proceed_to_checkout_button().send_login_to_checkout_email('wrong_user@test.commm'). \
        send_login_to_checkout_password('goodgpass1').click_login_to_checkout().get_text_of_input_error_message()
    assert no_subscription_message == 'Please, enter valid credentials', \
        f'\nNo warning for Login without subscription\nActual: {no_subscription_message}' \
        f'\nExpected: Please, enter valid credentials'

def test_checkout_login_wrong_password(get_subscription_page):
    """check, that login with wrong password is not possible - 14"""
    no_subscription_message = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().click_plus_button().click_plus_button().click_plus_button().click_continue_button(). \
        click_proceed_to_checkout_button().send_login_to_checkout_email('test@test.commm'). \
        send_login_to_checkout_password('wronggpass1').click_login_to_checkout().get_text_of_input_error_message()
    assert no_subscription_message == 'Please, enter valid credentials', \
        f'\nNo warning for Login without subscription\nActual: {no_subscription_message}' \
        f'\nExpected: Please, enter valid credentials'

def test_checkout_login_correct_creds(get_subscription_page):
    """check, that checkout with correct creds is possible - 15"""
    successful_checkout = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().click_plus_button().click_plus_button().click_plus_button().click_continue_button(). \
        click_proceed_to_checkout_button().send_login_to_checkout_email('test@test.commm'). \
        send_login_to_checkout_password('goodpass1').click_login_to_checkout()
    shipping_address = successful_checkout.get_text_shipping_address()
    billing_info = successful_checkout.get_text_billing_info()
    assert shipping_address == 'Shipping Address', \
        f'\nNot successful checkout\nActual: {shipping_address}' \
        f'\nExpected: Shipping Address'
    assert billing_info == 'Billing Info', \
        f'\nNot successful checkout\nActual: {billing_info}' \
        f'\nExpected: Billing Info'

def test_changing_shipping_address(get_subscription_page):
    """check, that checkout shipping address can be changed - 16"""
    new_shipping_address_name = random_string()
    new_shipping_address_lastname = random_string()
    new_shipping_address_address_1 = random_string()
    new_shipping_address_address_2 = random_string()
    new_shipping_address_city = random_string().upper()
    new_full_address = new_shipping_address_name + ' ' + new_shipping_address_lastname + ', ' + new_shipping_address_address_1 \
    + new_shipping_address_address_2 + ', ' + new_shipping_address_city + ', ' \
    + 'TX 73301,United States of America\n+12015551358'
    shipping_address_change = get_subscription_page.click_select_this_box().click_proceed_button(). \
        click_random_fish().click_plus_button().click_plus_button().click_plus_button().click_continue_button(). \
        click_proceed_to_checkout_button().send_login_to_checkout_email('test@test.commm'). \
        send_login_to_checkout_password('goodpass1').click_login_to_checkout().click_add_new_address_radio(). \
        send_shipping_address_name(new_shipping_address_name). \
        send_shipping_address_lastname(new_shipping_address_lastname).send_shipping_address_phone('12015551358'). \
        send_shipping_address_address_1(new_shipping_address_address_1). \
        send_shipping_address_address_2(new_shipping_address_address_2). \
        send_shipping_address_city(new_shipping_address_city).send_shipping_address_postal_code('73301'). \
        send_shipping_address_state('Texas').click_save_shipping_address().get_text_new_address()
    assert new_full_address in shipping_address_change, \
        f'\nAddress is not added\nActual: addresses list: {shipping_address_change}' \
        f'\nExpected: new address is in the addresses list'
