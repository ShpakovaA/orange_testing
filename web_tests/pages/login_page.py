from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage
import web_tests.pages.dashboard_page as dashboard_page


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
        self.browser.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        return self

    def is_displayed(self):
        return self.login_button.is_displayed()

    def enter_username(self, user):
        self.username_field.send_keys(user.username)

    def enter_password(self, user):
        self.password_field.send_keys(user.password)

    def click_login_button(self):
        self.login_button.click()

    def fill_creds_and_click_login_button(self, user):
        self.enter_username(user)
        self.enter_password(user)
        self.click_login_button()

    def perform_successful_login(self, user):
        self.fill_creds_and_click_login_button(user)
        return dashboard_page.DashboardPage(self.browser)

    def perform_unsuccessful_login(self, user):
        self.fill_creds_and_click_login_button(user)
        return self




