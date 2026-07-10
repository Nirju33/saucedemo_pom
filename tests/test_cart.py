from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def login_and_get_inventory(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("standard_user", "secret_sauce")
    login.wait_for_inventory()
    return InventoryPage(driver)

def go_to_cart(inventory):
    inventory.click(inventory.CART_BADGE)
    return CartPage(inventory.driver)

def test_tc_14_checkout_empty_cart(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("standard_user", "secret_sauce")
    login.wait_for_inventory()
    
    driver.get("https://www.saucedemo.com/cart.html")
    cart = CartPage(driver)
    cart.click_checkout()
    
    assert "checkout-step-one.html" in driver.current_url

def test_tc_15_remove_item_from_cart(driver):
    inventory = login_and_get_inventory(driver)
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    buttons[0].click()  
    
    cart = go_to_cart(inventory)
    assert cart.get_items_count() == 1
    
    cart.click_remove_item()
    assert cart.get_items_count() == 0
    assert inventory.is_cart_empty()

def test_tc_16_verify_product_details_in_cart(driver):
    inventory = login_and_get_inventory(driver)
    expected_name = inventory.get_names()[0]
    
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    buttons[0].click()
    
    cart = go_to_cart(inventory)
    actual_name = cart.find_visible((By.CLASS_NAME, "inventory_item_name")).text
    assert actual_name == expected_name

def test_tc_17_continue_shopping_navigation(driver):
    inventory = login_and_get_inventory(driver)
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    buttons[0].click()
    
    cart = go_to_cart(inventory)
    cart.click_continue_shopping()
    assert "inventory.html" in driver.current_url

def test_tc_18_checkout_button_navigation(driver):
    inventory = login_and_get_inventory(driver)
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    buttons[0].click()
    
    cart = go_to_cart(inventory)
    cart.click_checkout()
    assert "checkout-step-one.html" in driver.current_url