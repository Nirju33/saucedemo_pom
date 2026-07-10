from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutPage
from pages.checkout_step_two_page import CheckoutTwoPage
from pages.checkout_complete_page import CheckoutCompletePage

class end_to_endPage:
    def __init__(self, driver):
        self.driver = driver
        
     
        self.login_page = LoginPage(self.driver)
        self.inventory_page = InventoryPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.checkout_one = CheckoutPage(self.driver)
        self.checkout_two = CheckoutTwoPage(self.driver)
        self.checkout_complete = CheckoutCompletePage(self.driver)
    
    def valid_credential_login(self, username, password):
        self._wait_for_page_ready()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    def fill_checkout_form(self, first_name, last_name, zip_code):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.ZIP_CODE_INPUT, zip_code)
        
    def get_product_details(self):
        name = self.find(self.ITEM_NAME).text
        qty = self.find(self.ITEM_QUANTITY).text
        price = self.find(self.ITEM_PRICE).text
        return name, qty, price
    
    def get_confirmation_message(self):
        return self.find_visible(self.COMPLETE_HEADER).text