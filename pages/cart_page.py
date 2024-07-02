from base_page import BasePage

class CartPage(BasePage):
    def take_screenshot(self):
        self.driver.save_screenshot("screenshot.png")
