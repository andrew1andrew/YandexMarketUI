import time
import sys
import pytest
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'pages')))

from pages.market_page import MarketPage
from pages.cart_page import CartPage


def test_market(driver):
    # 1. Проверка и удаление существующего скриншота
    screenshot_path = "screenshot.png"
    if os.path.exists(screenshot_path):
        os.remove(screenshot_path)
        print(f"Скриншот {screenshot_path} удален.")
    else:
        print(f"Скриншот {screenshot_path} не найден, продолжение выполнения теста.")
    driver.maximize_window()
    market_page = MarketPage(driver)
    cart_page = CartPage(driver)
    # 2. Открываем страницу: https://market.yandex.ru/
    market_page.open("https://market.yandex.ru/")
    # time.sleep(10)
    # 3. Вводим в поиске 'ноутбуки HP'
    market_page.search_product("ноутбуки HP")
    # 4. Отсортировываем 'подешевле'
    market_page.sort_by_price()
    # 5. Ставим фильтр 'Оперативная память' - 8ГБ в чекбоксе
    market_page.select_memory_filter(driver)
    # 6. Отправляем товар в корзину
    market_page.add_product_to_cart()
    # 7. Открываем корзину
    cart_page.open("https://market.yandex.ru/cart")
    # 8. Делаем скриншот
    cart_page.take_screenshot()
