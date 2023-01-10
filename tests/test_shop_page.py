import time
import re

def test_low_high_price_sorting(get_shop_page):
    """check, that low-high price sorting is working - 1"""
    sorting_result = get_shop_page.click_fresh_local_fish().click_sort_by().click_low_high_price_option().get_fish_sorted_prices()
    values_list = []
    for element in sorting_result:
        values_list.append(re.findall('[0-9]+.[0-9][0-9]', element))
        new_values_list = values_list
        values_with_discounts = []
        for item in new_values_list:
            values_with_discounts.append(float(item[-1]))
    assert values_with_discounts == sorted(values_with_discounts), \
        f'\nLow-hiht sorting is not working\nActual: {values_with_discounts}' \
        f'\nExpected: {sorted(values_with_discounts)}'

def test_add_fish_to_cart(get_shop_page):
    """check, that fish can be added to cart - 2"""
    get_local_fish = get_shop_page.click_fresh_local_fish()
    fish_name = get_local_fish.get_fish_name()
    selected_fish_name = get_local_fish.click_buy_fish().get_selected_fish_name()
    assert selected_fish_name == fish_name, \
        f'\nFish names do not match\nActual: {selected_fish_name}' \
        f'\nExpected: {fish_name}'

def test_choose_random_fish(get_shop_page):
    """check, that random fish can be added to cart - 3"""
    select_fish = get_shop_page.click_fresh_local_fish().choose_random_fish().get_selected_fish_name()
    assert select_fish in ['Tuna', 'Salmon'], \
        f'\nFish name differs from available fishes\nActual: {select_fish}' \
        f'\nExpected: Product Name, Salmon, Sardin, Tuna'

def test_one_10_lb_fish_total(get_shop_page):
    """check, that cost of 1 fish is calculated correctly - 4"""
    buying_one_fish = get_shop_page.click_fresh_local_fish().click_buy_fish().click_pack_size().\
        click_pack_size_10_lb().click_add_to_cart()
    one_fish_price = buying_one_fish.get_one_fish_price()
    total_fish_price = buying_one_fish.get_total_fish_price()
    assert total_fish_price == one_fish_price, \
        f'\nCalculation for 1 fish is not correct\nActual: {total_fish_price}' \
        f'\nExpected: {one_fish_price}'

def test_two_10_lb_fish_total(get_shop_page):
    """check, that cost of 2 fishes is calculated correctly - 5"""
    buying_two_fish = get_shop_page.click_fresh_local_fish().click_buy_fish().click_pack_size().\
        click_pack_size_10_lb().clear_fish_quantity().send_fish_quantity('2').click_add_to_cart()
    one_fish_price = buying_two_fish.get_one_fish_price()
    total_fish_price = buying_two_fish.get_total_fish_price()
    one_fish_price_number_value = re.findall('[0-9]+.[0-9][0-9]', one_fish_price)
    total_fish_price_number_value = re.findall('[0-9]+.[0-9][0-9]', total_fish_price)
    time.sleep(10)
    assert total_fish_price_number_value == one_fish_price_number_value * 2, \
        f'\nCalculation for 2 fishes is not correct\nActual: {total_fish_price_number_value}' \
        f'\nExpected: {one_fish_price_number_value * 2}'

def test_total_fish_quantity_in_cart(get_shop_page):
    """check, that quantity of fish is shown in cart - 6"""
    buying_two_fish = get_shop_page.click_fresh_local_fish().click_buy_fish().click_pack_size(). \
        click_pack_size_10_lb().clear_fish_quantity().send_fish_quantity('2').click_add_to_cart().get_total_fish_quantity()
    assert buying_two_fish == '2', \
        f'\nTotal fish quantity is not shown in cart\nActual: {buying_two_fish}' \
        f'\nExpected: 2'

def test_removing_fish_from_cart(get_shop_page):
    """check, that fish can be removed from cart - 7"""
    removing_fish = get_shop_page.click_fresh_local_fish().click_buy_fish().click_pack_size(). \
        click_pack_size_10_lb().clear_fish_quantity().send_fish_quantity('2').click_add_to_cart().click_remove(). \
        get_removed_fish_message()
    assert removing_fish == 'Your cart is empty', \
        f'\nTotal fish quantity is not shown in cart\nActual: {removing_fish}' \
        f'\nExpected: Your cart is empty'