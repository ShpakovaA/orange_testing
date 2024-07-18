import pytest


def test_user_dropdown_menu(dashboard_page):
    """
    1.Navigate to base url
    2.Login
    Verify user dropdown menu is displayed in top header
    3.Click on user dropdown menu
    Verify drop down is clickable
    Verify About, Support, Change Password, Logout options are displayed

    """

    user_dropdown = dashboard_page.user_dropdown

    assert dashboard_page.user_dropdown.is_displayed(), "User dropdown is not displayed"

    user_dropdown.click()

    assert dashboard_page.user_dropdown_menu.is_displayed(), "User dropdown menu is not displayed"
    assert dashboard_page.about_option.text == "About", "About option is not displayed"
    assert dashboard_page.support_option.text == "Support", "Support option is not displayed"
    assert dashboard_page.change_password_option.text == "Change Password", "Change Password option is not displayed"
    assert dashboard_page.logout_option.text == "Logout", "Logout option is not displayed"


def test_successful_logout(dashboard_page):
    """
    1.Navigate to base url
    2.Login
    3.Click on user dropdown menu on Dashboard page
    4.Click Logout
    Verify that login page is displayed
    """
    login_page_ = dashboard_page.logout()

    assert login_page_.is_displayed(), "Logout failed"


@pytest.mark.parametrize('query, search_result', [("Time", "Time"), ("P", "PIM"), ("P", "Performance")])
def test_search_field_valid_query(dashboard_page, query, search_result):
    """
    1. Navigate to base url
    2. Login
    3. Enter valid query in Search field in main menu
    Verify that relevant option is auto suggested
    """

    dashboard_page.search(query)
    assert dashboard_page.side_panel_item_is_displayed(search_result)


def test_side_panel_button(dashboard_page):
    """
    1. Navigate to base url
    2. Login
    Verify side panel is displayed
    3. Click Hide button
    Verify main menu is hidden
    4. Click button again
    Verify main menu is displayed
    """

    assert dashboard_page.side_panel.is_displayed(), "Side panel isn't displayed"

    dashboard_page.hide_side_panel()
    assert dashboard_page.hidden_side_panel.is_displayed(), "Side panel isn't hidden"
    assert dashboard_page.icon_for_hidden_panel.is_displayed(), "Wrong icon is displayed when side panel is hidden"
    assert dashboard_page.collapsed_layout_container.is_displayed(), "Wrong page UI for hidden side panel"

    dashboard_page.display_side_panel()
    assert dashboard_page.side_panel.is_displayed(), "Side panel isn't displayed"
    assert dashboard_page.icon_for_displayed_panel, "Wrong icon is displayed when side panel is displayed"
    assert dashboard_page.layout_container.is_displayed(), "Wrong page UI for displayed side panel"
