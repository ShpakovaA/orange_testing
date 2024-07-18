import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from web_tests.helpers.user import User
import web_tests.pages.login_page as LP


@pytest.fixture()
def browser():
    browser = Chrome(service=ChromeService(ChromeDriverManager().install()))
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
    return LP.LoginPage(browser).navigate()


@pytest.fixture()
def dashboard_page(login_page, valid_user):
    return login_page.perform_successful_login(valid_user)


