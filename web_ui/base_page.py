from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)

    def wait_for_element_located(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_for_elements_located(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        element = self.wait_for_element_located(locator)
        element.click()

    def wait_for_element_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def click_2(self, locator):
        element = self.wait_for_element_clickable(locator)
        element.click()

    def get_text(self, locator):
        element = self.wait_for_element_located(locator)
        return element.text

    def get_text_multi(self, locator):
        list_of_texts = []
        time.sleep(2)
        elements = self.wait_for_elements_located(locator)
        for element in elements:
            element_text = element.text
            list_of_texts.append(element_text)
        return list_of_texts

    def get_attribute_value(self, locator):
        element = self.wait_for_element_located(locator)
        return element.get_attribute('value')

    def send_keys(self, locator, value, is_clear=False):
        element = self.wait_for_element_located(locator)
        if is_clear:
            element.clear()
        element.send_keys(value)

    def switch(self, alert):
        element = self.wait.until(EC.alert_is_present(alert))
        return element.switch_to_alert(alert)

    def hover(self, locator):
        element = self.wait_for_element_located(locator)
        action = ActionChains(driver=self.driver)
        return action.move_to_element(element).click().perform()

    def clear(self, locator):
        element = self.wait_for_element_located(locator)
        element.clear()

    @property
    def title(self):
        return self.driver.title
