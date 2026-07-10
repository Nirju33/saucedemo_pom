from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(@class, 'cart_button')]")
    CART_ITEMS = (By.CLASS_NAME, "cart_item")
    CART_ITEM_NAMES = (By.CLASS_NAME, "inventory_item_name")

    def click_checkout(self):
        self.find_visible(self.CHECKOUT_BUTTON).click()

    def click_continue_shopping(self):
        self.find_visible(self.CONTINUE_SHOPPING_BUTTON).click()

    def get_items_count(self):
        try:
            items = self.find_all_visible(self.CART_ITEMS, timeout=2)
            return len(items)
        except:
            return 0

    def click_remove_item(self):
        buttons = self.find_all_visible(self.REMOVE_BUTTONS)
        if buttons:
            buttons[0].click()
