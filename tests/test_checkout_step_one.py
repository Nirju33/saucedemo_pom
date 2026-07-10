from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.checkout_step_one_page import CheckoutPage
import time

def navigate_to_checkout_page(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("standard_user", "secret_sauce")
    login.wait_for_inventory()
    
    inventory = InventoryPage(driver)
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    buttons[0].click()
    
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    driver.find_element(By.ID, "checkout").click()
    return CheckoutPage(driver)


def test_tc_19_valid_checkout_form_submission(driver):
    checkout = navigate_to_checkout_page(driver)
    
    checkout.fill_checkout_form("Nirjala", "k.c.", "4004")
    checkout.click_continue()
    time.sleep(3)
    
    assert "checkout-step-two.html" in driver.current_url


def test_tc_20_invalid_zip_code_validation(driver):
    checkout = navigate_to_checkout_page(driver)
    
    checkout.fill_checkout_form("Nirjala", "k.c.", "abcde")
    checkout.click_continue()
    time.sleep(5)
    

    assert "checkout-step-two.html" in driver.current_url


def test_tc_21_cancel_checkout_navigation(driver):
    checkout = navigate_to_checkout_page(driver)
    
    checkout.click_cancel()
    time.sleep(5)
    
    assert "cart.html" in driver.current_url