from web_tests.helpers.resources import Resources


def test_valid_credentials_login(login_page, valid_user):
    """
    1. Navigate to base url
    2. Enter valid username
    3. Enter  valid password
    4. Click Login button.
    Verify that Dashboard page is displayed
    """

    dashboard_page_ = login_page.perform_successful_login(valid_user)
    assert dashboard_page_.is_displayed(), "Dashboard page isn't displayed"


def test_invalid_password_login(login_page, invalid_user):
    """
    1. Navigate to base url
    2. Enter valid username
    3. Enter  invalid password
    4. Click Login button.
    Verify that login page is still displayed
    Verify that "Invalid credentials" error message is displayed
    """

    login_page.perform_unsuccessful_login(invalid_user)

    assert login_page.is_displayed(), "Login page isn't displayed"
    assert login_page.error_message.is_displayed(), "Error isn't displayed"
    assert login_page.error_message.text == Resources.LoginPage.INVALID_CREDENTIALS_ERROR, "Error isn't displayed"
