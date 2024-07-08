from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class DashboardPage(BasePage):

    HEADER_TITLE = (By.XPATH, '//span[@class="oxd-topbar-header-breadcrumb"]/h6[text()="Dashboard"]')

    def __init__(self, browser):
        super().__init__(browser)

    @property
    def header_title_dashboard(self):
        return self.get_element(DashboardPage.HEADER_TITLE)

    def is_displayed(self):
        return self.header_title_dashboard.is_displayed()
