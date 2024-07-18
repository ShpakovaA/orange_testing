from web_tests.pages.base_page import BasePage
import web_tests.components.header as header
from web_tests.components.side_panel import SidePanel


class DashboardPage(SidePanel, header.HeaderSection, BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def is_displayed(self):
        return self.header_title == "Dashboard"






