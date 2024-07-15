from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class HeaderSection(BasePage):
    HEADER_TITLE = (By.XPATH, '//span[@class="oxd-topbar-header-breadcrumb"]/h6')
    USER_DROPDOWN = (By.XPATH, '//header//span[@class="oxd-userdropdown-tab"]')
    USER_DROPDOWN_MENU = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]')
    ABOUT_OPTION = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li[1]')
    SUPPORT_OPTION = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li[2]')
    CHANGE_PASSWORD_OPTION = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li[3]')
    LOGOUT_OPTION = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li[4]')

    def __init__(self, browser):
        super().__init__(browser)

    @property
    def header(self):
        return self.get_element(HeaderSection.HEADER_TITLE)

    @property
    def header_title(self):
        return self.header.text

    @property
    def user_dropdown(self):
        return self.get_element(HeaderSection.USER_DROPDOWN)

    @property
    def user_dropdown_menu(self):
        return self.get_element(HeaderSection.USER_DROPDOWN_MENU)

    @property
    def about_option(self):
        return self.get_element(HeaderSection.ABOUT_OPTION)

    @property
    def support_option(self):
        return self.get_element(HeaderSection.SUPPORT_OPTION)

    @property
    def change_password_option(self):
        return self.get_element(HeaderSection.CHANGE_PASSWORD_OPTION)

    @property
    def logout_option(self):
        return self.get_element(HeaderSection.LOGOUT_OPTION)

    def about_option_is_displayed(self):
        return self.about_option.text == "About"

    def support_option_is_displayed(self):
        return self.support_option.text == "Support"

    def change_password_option_is_displayed(self):
        return self.change_password_option.text == "Change Password"

    def logout_option_is_displayed(self):
        return self.logout_option.text == "Logout"

    def logout(self):
        self.user_dropdown.click()
        self.logout_option.click()


