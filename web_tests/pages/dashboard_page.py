from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class DashboardPage(BasePage):

    HEADER_TITLE = (By.XPATH, '//span[@class="oxd-topbar-header-breadcrumb"]/h6[text()="Dashboard"]')
    USER_DROPDOWN = (By.XPATH, '//header//span[@class="oxd-userdropdown-tab"]')
    USER_DROPDOWN_MENU = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]')
    ABOUT_OPTION = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li/a[text()="About"]')
    SUPPORT_OPTION = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li/a[text()="Support"]')
    CHANGE_PASSWORD_OPTION = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li/a[text()="Change Password"]')
    LOGOUT = (By.XPATH, '//ul[@class="oxd-dropdown-menu"]/li/a[text()="Logout"]')
    SEARCH_FIELD =(By.XPATH, '//div/input[@placeholder="Search"]')
    TIME_OPTION_MAIN_MENU = (By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"][text()="Time"]')
    SIDE_PANEL = (By.XPATH, '//nav[@aria-label="Sidepanel"]')
    SIDE_PANEL_BUTTON = (By.XPATH, '//button[@class="oxd-icon-button oxd-main-menu-button"]')
    ICON_FOR_DISPLAYED_PANEL = (By.XPATH, '//button/i[@class="oxd-icon bi-chevron-left"]')
    ICON_FOR_HIDDEN_PANEL = (By.XPATH, '//button/i[@class="oxd-icon bi-chevron-right"]')

    def __init__(self, browser):
        super().__init__(browser)

    @property
    def header_title_dashboard(self):
        return self.get_element(DashboardPage.HEADER_TITLE)

    @property
    def user_dropdown(self):
        return self.get_element(DashboardPage.USER_DROPDOWN)

    @property
    def user_dropdown_menu(self):
        return self.get_element(DashboardPage.USER_DROPDOWN_MENU)

    @property
    def about_option(self):
        return self.get_element(DashboardPage.ABOUT_OPTION)

    @property
    def support_option(self):
        return self.get_element(DashboardPage.SUPPORT_OPTION)

    @property
    def change_password_option(self):
        return self.get_element(DashboardPage.CHANGE_PASSWORD_OPTION)

    @property
    def logout_option(self):
        return self.get_element(DashboardPage.LOGOUT)

    @property
    def search_field(self):
        return self.get_element(DashboardPage.SEARCH_FIELD)

    @property
    def time_option(self):
        return self.get_element(DashboardPage.TIME_OPTION_MAIN_MENU)

    @property
    def side_panel(self):
        return self.get_element(DashboardPage.SIDE_PANEL)

    @property
    def side_panel_button(self):
        return self.get_element(DashboardPage.SIDE_PANEL_BUTTON)

    @property
    def icon_for_displayed_panel(self):
        return self.get_element(DashboardPage.ICON_FOR_DISPLAYED_PANEL)

    @property
    def icon_for_hidden_panel(self):
        return self.get_element(DashboardPage.ICON_FOR_HIDDEN_PANEL)

    def hide_side_panel(self):
        if not self.icon_for_displayed_panel.is_displayed():
            self.side_panel_button.click()
        self.side_panel_button.click()

    def display_side_panel(self):
        if not self.icon_for_hidden_panel.is_displayed():
            self.side_panel_button.click()
        self.side_panel_button.click()

    def search(self, query):
        self.search_field.send_keys(query)

    def is_displayed(self):
        return self.header_title_dashboard.is_displayed()

    def logout(self):
        self.user_dropdown.click()
        self.logout_option.click()

