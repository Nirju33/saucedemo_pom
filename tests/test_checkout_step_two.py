from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_step_one_page import CheckoutPage
from pages.checkout_step_two_page import CheckoutTwoPage

def setup_checkout_flow(driver, item_count=1):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("standard_user", "secret_sauce")
    login.wait_for_inventory()
    
    inventory = InventoryPage(driver)
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    for i in range(item_count):
        buttons[i].click()
        
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    
    checkout_one = CheckoutPage(driver)
    checkout_one.fill_checkout_form("Nirjala", "k.c.", "4004")
    checkout_one.click_continue()
    return CheckoutTwoPage(driver)


def test_tc_22_verify_product_details_matching(driver):
    checkout_two = setup_checkout_flow(driver, item_count=1)
    name, qty, price = checkout_two.get_product_details()
    
    assert name == "Sauce Labs Backpack"
    assert qty == "1"
    assert price == "$29.99"


def test_tc_23_verify_sum_of_multiple_items(driver):
    checkout_two = setup_checkout_flow(driver, item_count=2)
    subtotal_text = checkout_two.get_item_total_text()
    
    assert "Item total: $39.98" in subtotal_text


def test_tc_24_verify_tax_row_visibility(driver):
    checkout_two = setup_checkout_flow(driver, item_count=1)
    assert checkout_two.is_tax_displayed() is True


def test_tc_25_cancel_button_redirects_to_inventory(driver):
    checkout_two = setup_checkout_flow(driver, item_count=1)
    checkout_two.click_cancel()
    assert "inventory.html" in driver.current_url


def test_tc_26_verify_exact_total_calculations(driver):
    checkout_two = setup_checkout_flow(driver, item_count=1)
    
    subtotal = checkout_two.get_item_total_text()
    total = checkout_two.get_final_total_text()
    
    assert "$29.99" in subtotal
    assert "$32.39" in total


def test_tc_27_verify_direct_url_access_flaw(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("standard_user", "secret_sauce")
    login.wait_for_inventory()
    
    driver.get("https://www.saucedemo.com/checkout-step-two.html")
    
    assert "checkout-step-two.html" in driver.current_url