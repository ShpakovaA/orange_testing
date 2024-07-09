from web_tests.pages.login_page import LoginPage


def test_user_dropdown_menu(browser, valid_user):
    """
    1.Navigate to base url
    2.Login
    Verify user dropdown menu is displayed in top header
    3.Click on user dropdown menu
    Verify drop down is clickable
    Verify About, Support, Change Password, Logout options are displayed

    """

    login_page = LoginPage(browser)
    login_page.navigate()

    dashboard_page = login_page.perform_successful_login(valid_user)
    user_dropdown = dashboard_page.user_dropdown
    assert user_dropdown.is_displayed(), "User dropdown is not displayed"

    user_dropdown.click()

    assert dashboard_page.user_dropdown_menu.is_displayed(), "User dropdown menu is not displayed"
    assert dashboard_page.about_option.is_displayed(), "About option is not displayed"
    assert dashboard_page.support_option.is_displayed(), "Support option is not displayed"
    assert dashboard_page.change_password_option.is_displayed(), "Change Password option is not displayed"
    assert dashboard_page.logout_option.is_displayed(), "Logout option is not displayed"


def test_logout(browser, valid_user):
    """
    1.Navigate to base url
    2.Login
    3.Click on user dropdown menu on Dashboard page
    4.Click Logout
    Verify that login page is displayed
    """
    login_page = LoginPage(browser)
    login_page.navigate()

    dashboard_page = login_page.perform_successful_login(valid_user)
    dashboard_page.logout()

    assert login_page.is_displayed(), "Logout failed"


def test_search_field_valid_query(browser, valid_user):
    """
    1. Navigate to base url
    2. Login
    3. Enter valid query in Search field in main menu
    Verify that relevant option is auto suggested
    """
    login_page = LoginPage(browser)
    login_page.navigate()
    dashboard_page = login_page.perform_successful_login(valid_user)

    dashboard_page.search("Time")

    assert dashboard_page.time_option.is_displayed(), "Relevant option isn't found"


def test_side_panel_button(browser, valid_user):
    """
    1. Navigate to base url
    2. Login
    Verify side panel is displayed
    3. Click Hide button
    Verify main menu is hidden
    4. Click button again
    Verify main menu is displayed
    """

    login_page = LoginPage(browser)
    login_page.navigate()

    dashboard_page = login_page.perform_successful_login(valid_user)

    assert dashboard_page.side_panel.is_displayed(), "Side panel isn't displayed"

    dashboard_page.hide_side_panel()
    assert dashboard_page.icon_for_hidden_panel.is_displayed(), "Wrong button behaviour, when try to hide side panel"

    dashboard_page.display_side_panel()
    assert dashboard_page.icon_for_displayed_panel.is_displayed(), "Wrong button behaviour, when try to display side panel"

