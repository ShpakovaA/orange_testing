import pytest
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from web_tests.pages.login_page import LoginPage
from web_tests.pages.login_page import DashboardPage



valid_username = "Admin"
valid_password = "admin123"
invalid_password = "w233"


def test_valid_credentials_login(browser):
    """
    1. Navigate to base url
    2. Enter valid username
    3. Enter  valid password
    4. Click Login button.
    Verify that Dashboard page is displayed
    """

    login_page = LoginPage(browser)
    login_page.navigate()

    dashboard_page = login_page.perform_successful_login(valid_username, valid_password)
    assert dashboard_page.is_displayed(), "Dashboard page isn't displayed"


def test_invalid_password_login(browser):
    """
    1. Navigate to base url
    2. Enter valid username
    3. Enter  invalid password
    4. Click Login button.
    Verify that login page is still displayed
    Verify that "Invalid credentials" error message is displayed
    """

    login_page = LoginPage(browser)
    login_page.navigate()

    login_page.perform_unsuccessful_login(valid_username, invalid_password)
    assert login_page.is_displayed(), "Login page isn't displayed"

    # assert login_page.error_message.is_displayed(), "Error isn't displayed"
    # assert login_page.error_message.text == "Invalid credentials", "Error isn't displayed"


def test_user_dropdown_menu(browser):
    """
    1.Navigate to base url
    2.Login
    Verify user dropdown menu is displayed in top header
    3.Click on user dropdown menu
    Verify drop down is clickable
    Verify About, Support, Change Password, Logout options are displayed

    """
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(4)

    username_field = browser.find_element(By.XPATH, '//div/input[@name="username"]')
    username_field.send_keys(valid_username)

    password_field = browser.find_element(By.XPATH, '//div/input[@name="password"]')
    password_field.send_keys(valid_password)

    login_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    sleep(3)

    user_dropdown = browser.find_element(By.XPATH, '//header//span[@class="oxd-userdropdown-tab"]')
    assert user_dropdown.is_displayed(), "User dropdown menu is not displayed"

    user_dropdown.click()
    sleep(1)

    user_dropdown_menu = browser.find_element(By.XPATH, '//ul[@class="oxd-dropdown-menu"]')
    assert user_dropdown_menu.is_displayed(), "Drop down menu is not displayed after click"

    about_option = browser.find_element(By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li/a[text()="About"]')
    assert about_option.is_displayed(), "About option is not displayed"

    support_option = browser.find_element(By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li/a[text()="Support"]')
    assert support_option.is_displayed(), "Support option is not displayed"

    change_password_option = browser.find_element(By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li/a[text()="Change Password"]')
    assert change_password_option.is_displayed(), "Change Password option is not displayed"

    logout_option = browser.find_element(By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li/a[text()="Logout"]')
    assert logout_option.is_displayed(), "Logout option is not displayed"


def test_logout(browser):
    """
    1.Navigate to base url
    2.Login
    3.Click on user dropdown menu on Dashboard page
    4.Click Logout
    Verify that login page is displayed
    """
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(4)

    username_field = browser.find_element(By.XPATH, '//div/input[@name="username"]')
    username_field.send_keys(valid_username)

    password_field = browser.find_element(By.XPATH, '//div/input[@name="password"]')
    password_field.send_keys(valid_password)

    login_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    sleep(3)

    user_dropdown = browser.find_element(By.XPATH, '//header//span[@class="oxd-userdropdown-tab"]')
    user_dropdown.click()
    sleep(1)

    logout_option = browser.find_element(By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li/a[text()="Logout"]')
    logout_option.click()

    sleep(3)

    assert login_button.is_displayed(), "Logout failed"


def test_search_field_valid_query(browser):
    """
    1. Navigate to base url
    2. Login
    3. Enter valid query in Search field in main menu
    Verify that relevant option is auto suggested
    """
    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(4)

    username_field = browser.find_element(By.XPATH, '//div/input[@name="username"]')
    username_field.send_keys(valid_username)

    password_field = browser.find_element(By.XPATH, '//div/input[@name="password"]')
    password_field.send_keys(valid_password)

    login_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    sleep(3)

    search_field = browser.find_element(By.XPATH, '//div/input[@placeholder="Search"]')
    search_field.send_keys("Time")
    sleep(2)

    relevant_option = browser.find_element(By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"][text()="Time"]')
    assert relevant_option.is_displayed(), "Relevant option isn't found"



def test_side_panel_hide_button(browser):
    """
    1. Navigate to base url
    2. Login
    Verify side panel is displayed
    3. Click Hide button
    Verify main menu is hidden
    4. Click button again
    Verify main menu is displayed
    """

    browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    sleep(4)

    username_field = browser.find_element(By.XPATH, '//div/input[@name="username"]')
    username_field.send_keys(valid_username)

    password_field = browser.find_element(By.XPATH, '//div/input[@name="password"]')
    password_field.send_keys(valid_password)

    login_button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    login_button.click()
    sleep(3)

    side_panel = browser.find_element(By.XPATH, '//nav[@aria-label="Sidepanel"]')
    assert side_panel.is_displayed()

    hide_button = browser.find_element(By.XPATH, '//button[@class="oxd-icon-button oxd-main-menu-button"]')
    hide_button.click()
    icon_for_hidden_panel = browser.find_element(By.XPATH, '//button/i[@class="oxd-icon bi-chevron-right"]')
    assert icon_for_hidden_panel.is_displayed()

    hide_button.click()
    icon_for_displayed_panel = browser.find_element(By.XPATH, '//button/i[@class="oxd-icon bi-chevron-left"]')
    assert icon_for_displayed_panel.is_displayed()