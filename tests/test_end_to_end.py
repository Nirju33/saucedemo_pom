import time
from pages.login_page import LoginPage
from tests.test_cart import go_to_cart
from tests.test_checkout_complete import complete_checkout_flow, setup_login
from tests.test_checkout_step_one import navigate_to_checkout_page
from tests.test_checkout_step_two import setup_checkout_flow
from tests.test_inventory import login_and_get_inventory


def test_Valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("standard_user", "secret_sauce")
    login_page.wait_for_inventory()
    assert "inventory" in driver.current_url
    
def test_price_sorting(driver):
    inventory = login_and_get_inventory(driver)
    
    inventory.sort_by("Price (low to high)")
    assert inventory.get_prices() == sorted(inventory.get_prices())

    inventory.sort_by("Price (high to low)")
    assert inventory.get_prices() == sorted(inventory.get_prices(), reverse=True)

def test_tc_15_remove_item_from_cart(driver):
    inventory = login_and_get_inventory(driver)
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    buttons[0].click()  
    
    cart = go_to_cart(inventory)
    assert cart.get_items_count() == 1
    
    cart.click_remove_item()
    assert cart.get_items_count() == 0
    assert inventory.is_cart_empty()

def test_tc_19_valid_checkout_form_submission(driver):
    checkout = navigate_to_checkout_page(driver)
    
    checkout.fill_checkout_form("Nirjala", "k.c.", "4004")
    checkout.click_continue()
    time.sleep(3)
    
    assert "checkout-step-two.html" in driver.current_url
    
def test_tc_22_verify_product_details_matching(driver):
    checkout_two = setup_checkout_flow(driver, item_count=1)
    name, qty, price = checkout_two.get_product_details()
    
    assert name == "Sauce Labs Backpack"
    assert qty == "1"
    assert price == "$29.99"
    
    
def test_tc_28_checkout_complete_confirmation_message(driver):
    inventory = setup_login(driver)
    complete_page = complete_checkout_flow(driver, inventory)
    assert complete_page.get_confirmation_message() == "Thank you for your order!"



