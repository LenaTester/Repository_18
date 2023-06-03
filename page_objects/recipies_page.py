from selenium.webdriver.common.by import By
from web_ui.base_page import BasePage

class RecipiesPage(BasePage):
    __search_recipie_field = (By.XPATH, "//input[@placeholder='Search for fish or type']")
    __recipie_title = (By.XPATH, "//div[@class='sc-eNhIyc iklgMr']")
    __chosen_recipie_title = (By.XPATH, "//div[@class = 'sc-cFlMtL goYdCj']")
    __first_recipie_link = (By.XPATH, "//div[text()='Maine Lobster Rolls']")

    def __init__(self, driver):
        super().__init__(driver)

    def send_serch_recipie(self, recipie):
        self.send_keys(self.__search_recipie_field, recipie)
        return self

    def get_recipies_titles(self):
        return self.get_text_multi(self.__recipie_title)

    def get_chosen_recipie_title(self):
        return self.get_text(self.__chosen_recipie_title)

    def click_first_recipie(self):
        self.click(self.__first_recipie_link)
        return self

    def get_first_recipie_title(self):
        return self.get_text(self.__first_recipie_link)
