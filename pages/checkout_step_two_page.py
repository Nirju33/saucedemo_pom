from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutTwoPage(BasePage):
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_QUANTITY = (By.CLASS_NAME, "cart_quantity")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    
    SUBTOTAL_LABEL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX_LABEL = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_LABEL = (By.CLASS_NAME, "summary_total_label")
    
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")

    def get_product_details(self):
        name = self.find(self.ITEM_NAME).text
        qty = self.find(self.ITEM_QUANTITY).text
        price = self.find(self.ITEM_PRICE).text
        return name, qty, price

    def get_item_total_text(self):
        return self.find(self.SUBTOTAL_LABEL).text

    def is_tax_displayed(self):
        return self.find(self.TAX_LABEL).is_displayed()

    def get_final_total_text(self):
        return self.find(self.TOTAL_LABEL).text

    def click_cancel(self):
        self.click(self.CANCEL_BUTTON)