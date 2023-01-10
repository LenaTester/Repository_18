def test_search_for_recipie(get_recipies_page):
    """check, that search by fish name returns correct recipies - 1"""
    searching_recipie = get_recipies_page.send_serch_recipie('Lobster').get_recipies_titles()
    searching_recipie_lists = []
    for element in searching_recipie:
        listed_element = element.split()
        searching_recipie_lists.append(listed_element)
    for element in searching_recipie_lists:
        assert 'Lobster' in element, \
        f'\nRecipies search is not working\nActual: {searching_recipie_lists}' \
        f'\nExpected: List of recipies titles'

def test_read_recipie(get_recipies_page):
    """check, that search by fish name returns correct recipies - 2"""
    chosing_recipie = get_recipies_page.send_serch_recipie('Lobster')
    first_recipie_title = chosing_recipie.get_first_recipie_title()
    chosen_recipie_title = chosing_recipie.click_first_recipie().get_chosen_recipie_title()
    assert chosen_recipie_title == first_recipie_title, \
        f'\nWrong recipie is opened\nActual: {chosen_recipie_title}' \
        f'\nExpected: Chosen recipie title should be shown'