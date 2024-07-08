from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage
from web_tests.pages.dashboard_page import DashboardPage


class LoginPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    USERNAME_FIELD = (By.XPATH, '//div/input[@name="username"]')
    PASSWORD_FIELD = (By.XPATH, '//div/input[@name="password"]')
    LOGIN_BUTTON = (By.XPATH, '//button[@type="submit"]')
    ERROR_MESSAGE = (By.XPATH, '//div[@role="alert"]/div/p')

    @property
    def username_field(self):
        return self.get_element(LoginPage.USERNAME_FIELD)

    @property
    def password_field(self):
        return self.get_element(LoginPage.PASSWORD_FIELD)

    @property
    def login_button(self):
        return self.get_element(LoginPage.LOGIN_BUTTON)

    @property
    def error_message(self):
        return self.get_element(LoginPage.ERROR_MESSAGE)

    def navigate(self):
        self._browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def is_displayed(self):
        self.login_button.is_displayed()

    def enter_username(self, username):
        self.username_field.send_keys(username)

    def enter_password(self, password):
        self.password_field.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def fill_creds_and_click_login_button(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def perform_successful_login(self, username, password):
        self.fill_creds_and_click_login_button(username,password)
        return DashboardPage(self._browser)

    def perform_unsuccessful_login(self, username, password):
        self.fill_creds_and_click_login_button(username, password)
        return self




