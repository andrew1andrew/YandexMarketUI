from selenium.webdriver.common.by import By


class MarketLocators:
    SEARCH_INPUT = (By.CSS_SELECTOR, "[placeholder='Искать на Яндекс Маркете']")
    SORT_BUTTON = (By.CSS_SELECTOR, "[data-autotest-id='aprice']")
    FILTER_CHECKBOX = (By.CSS_SELECTOR, 'div[data-zone-name="FilterValue"]:first-of-type label[role="checkbox"]')
    ADD_TO_CART_BUTTON = (By.XPATH, '(//div[@data-zone-name="cartButton"])[9]//button[@data-auto="cartButton"]')