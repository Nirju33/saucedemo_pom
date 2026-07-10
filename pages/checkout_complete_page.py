from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutCompletePage(BasePage):
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def get_confirmation_message(self):
        return self.find_visible(self.COMPLETE_HEADER).text

    def is_cart_badge_displayed(self):
        try:
            return self.find_visible(self.CART_BADGE, timeout=2).is_displayed()
        except:
            return False