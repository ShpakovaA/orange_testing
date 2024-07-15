from web_tests.pages.base_page import BasePage
from web_tests.components.header import HeaderSection
from web_tests.components.side_panel import SidePanel


class DashboardPage(SidePanel, HeaderSection, BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def is_displayed(self):
        return self.header_title == "Dashboard"






