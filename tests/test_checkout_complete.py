import pytest
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_complete_page import CheckoutCompletePage

def setup_login(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("standard_user", "secret_sauce")
    login.wait_for_inventory()
    return InventoryPage(driver)

def complete_checkout_flow(driver, inventory):
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    buttons[0].click()
    
    inventory.click(inventory.CART_BADGE)
    cart = CartPage(driver)
    cart.click_checkout()
    
    driver.find_element(By.ID, "first-name").send_keys("Nirjala")
    driver.find_element(By.ID, "last-name").send_keys("K.C.")
    driver.find_element(By.ID, "postal-code").send_keys("44600")
    driver.find_element(By.ID, "continue").click()
    driver.find_element(By.ID, "finish").click()
    return CheckoutCompletePage(driver)

def test_tc_28_checkout_complete_confirmation_message(driver):
    inventory = setup_login(driver)
    complete_page = complete_checkout_flow(driver, inventory)
    assert complete_page.get_confirmation_message() == "Thank you for your order!"

def test_tc_29_cart_badge_resets_to_zero_after_order(driver):
    inventory = setup_login(driver)
    complete_page = complete_checkout_flow(driver, inventory)
    assert not complete_page.is_cart_badge_displayed()

def test_tc_30_direct_access_checkout_complete_without_order(driver):
    setup_login(driver)
    driver.get("https://www.saucedemo.com/checkout-complete.html")
    complete_page = CheckoutCompletePage(driver)
    
    assert "Thank you for your order!" in complete_page.get_confirmation_message()

def test_tc_31_verify_cart_badge_quantity(driver):
    inventory = setup_login(driver)
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    buttons[0].click()
    buttons[1].click()
    
    try:
        badge_text = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        assert badge_text == "2"
    except:
        pytest.fail("Cart badge failed to display item count.")