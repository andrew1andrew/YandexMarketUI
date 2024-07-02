from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from locators.market_locators import MarketLocators
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC


class MarketPage(BasePage):
    def search_product(self, query):
        search_input = self.element_is_visible(MarketLocators.SEARCH_INPUT)
        search_input.send_keys(query)
        search_input.submit()

    def sort_by_price(self):
        sort_button = self.element_is_visible(MarketLocators.SORT_BUTTON)
        sort_button.click()

    def select_memory_filter(self, driver):
        actions = ActionChains(driver)
        filter_checkbox = self.elements_are_visible(MarketLocators.FILTER_CHECKBOX)
        # Перемещение курсора к элементу
        actions.move_to_element(filter_checkbox[1]).perform()
        # Нажатие на чекбокс
        filter_checkbox[1].click()

    def add_product_to_cart(self):
        max_attempts = 3
        attempts = 0
        while attempts < max_attempts:
            try:
                add_to_cart_button = Wait(self.driver, 10).until(EC.element_to_be_clickable(
                    MarketLocators.ADD_TO_CART_BUTTON))
                add_to_cart_button.click()
                break
            except StaleElementReferenceException:
                attempts += 1
                if attempts == max_attempts:
                    raise  # Если превышено количество попыток, выбрасываем исключение
                else:
                    self.driver.refresh()
                    Wait(self.driver, 10).until(EC.presence_of_element_located(
                        MarketLocators.ADD_TO_CART_BUTTON))
