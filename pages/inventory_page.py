from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage

class InventoryPage(BasePage):
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    
    TWITTER_LINK = (By.LINK_TEXT, "Twitter")
    FACEBOOK_LINK = (By.LINK_TEXT, "Facebook")
    LINKEDIN_LINK = (By.LINK_TEXT, "LinkedIn")
    
    BURGER_MENU = (By.ID, "react-burger-menu-btn")
    RESET_LINK = (By.ID, "reset_sidebar_link")
    CART_BUTTONS = (By.XPATH, "//button[contains(@class, 'btn_inventory')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    
    FIRST_PRODUCT = (By.CLASS_NAME, "inventory_item_name")
    BACK_BUTTON = (By.ID, "back-to-products")

    def sort_by(self, text):
        Select(self.find_visible(self.SORT_DROPDOWN)).select_by_visible_text(text)

    def get_prices(self):
        return [float(el.text.replace("$", "")) for el in self.find_all_visible(self.PRODUCT_PRICES)]

    def get_names(self):
        return [el.text for el in self.find_all_visible(self.PRODUCT_NAMES)]

    def is_cart_empty(self):
        try:
            return not self.find_visible(self.CART_BADGE, timeout=2).is_displayed()
        except:
            return True