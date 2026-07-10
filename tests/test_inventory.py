from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
import time
def login_and_get_inventory(driver):
    login = LoginPage(driver)
    login.load()
    login.valid_credential_login("standard_user", "secret_sauce")
    login.wait_for_inventory()
    return InventoryPage(driver)

def test_price_sorting(driver):
    inventory = login_and_get_inventory(driver)
    
    inventory.sort_by("Price (low to high)")
    assert inventory.get_prices() == sorted(inventory.get_prices())

    inventory.sort_by("Price (high to low)")
    assert inventory.get_prices() == sorted(inventory.get_prices(), reverse=True)

def test_footer_social_links(driver):
    inventory = login_and_get_inventory(driver)
    
    inventory.click(inventory.TWITTER_LINK)
    inventory.click(inventory.FACEBOOK_LINK)
    inventory.click(inventory.LINKEDIN_LINK)
    
    time.sleep(5)
    
    assert len(driver.window_handles) == 4

def test_name_sorting(driver):
    inventory = login_and_get_inventory(driver)
    
    inventory.sort_by("Name (A to Z)")
    assert inventory.get_names() == sorted(inventory.get_names())

    inventory.sort_by("Name (Z to A)")
    assert inventory.get_names() == sorted(inventory.get_names(), reverse=True)

def test_reset_app_state(driver):
    inventory = login_and_get_inventory(driver)
    
    buttons = inventory.find_all_visible(inventory.CART_BUTTONS)
    buttons[0].click()
    buttons[1].click()
    
    inventory.click(inventory.BURGER_MENU)
    inventory.click(inventory.RESET_LINK)
    
    assert inventory.is_cart_empty() == True

def test_back_to_products_navigation(driver):
    inventory = login_and_get_inventory(driver)
    
    inventory.click(inventory.FIRST_PRODUCT)
    inventory.wait_for_url_contains("inventory-item.html")
    
    inventory.click(inventory.BACK_BUTTON)
    inventory.wait_for_url_contains("inventory.html")
    
    assert "inventory.html" in driver.current_url