from pages.login_page import LoginPage

# TEST VAILD
def test_Valid_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.valid_credential_login("standard_user", "secret_sauce")
    login_page.wait_for_inventory()
    assert "inventory" in driver.current_url

# TEST INVAID
def test_invaild_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.invalid_credential_login("Nirju_user", "hello@12")
    error_msg = login_page.get_error_message()
    assert "do not match" in error_msg

# Empty
def test_Empty_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.Empty_credential_login("","")
    error_msg = login_page.get_error_message()
    assert "required" in error_msg.lower()
# Uppercase
def test_Uppercase_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.Uppercasee_credential_login("STANDARD_USER", "SECRET_SAUCE")
    error_msg = login_page.get_error_message()
    assert "do not match" in error_msg
#User_empty
def test_User_empty_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.User_empty_credential_login("","secret_sauce")
    error_msg = login_page.get_error_message()
    assert "username is required" in error_msg.lower()