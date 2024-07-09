import pytest
from selenium.webdriver import Chrome
from web_tests.helpers.user import User
from web_tests.pages.login_page import LoginPage


@pytest.fixture()
def browser():
    browser = Chrome()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()


@pytest.fixture(scope="session")
def valid_user():
    return User("Admin", "admin123")


@pytest.fixture(scope="session")
def invalid_user():
    return User("Admin", "mn123")


@pytest.fixture()
def login_page(browser):
    return LoginPage(browser).navigate()


@pytest.fixture()
def dashboard_page(login_page, valid_user):
    return login_page.perform_successful_login(valid_user)


