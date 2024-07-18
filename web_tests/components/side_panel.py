from selenium.webdriver.common.by import By
from web_tests.pages.base_page import BasePage


class SidePanel(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    SEARCH_FIELD = (By.XPATH, '//div/input[@placeholder="Search"]')
    SIDE_PANEL = (By.XPATH, '//aside[@class="oxd-sidepanel"]')
    HIDDEN_SIDE_PANEL = (By.XPATH, '//aside[@class="oxd-sidepanel toggled"]')
    SIDE_PANEL_BUTTON = (By.XPATH, '//button[@class="oxd-icon-button oxd-main-menu-button"]')
    ICON_FOR_DISPLAYED_PANEL = (By.XPATH, '//button/i[contains(@Class,"bi-chevron-left")]')
    ICON_FOR_HIDDEN_PANEL = (By.XPATH, '//button/i[contains(@Class,"bi-chevron-right")]')
    LAYOUT_CONTAINER = (By.XPATH, '//div[@class="oxd-layout-container"]')
    LAYOUT_CONTAINER_COLLAPSED = (By.XPATH, '//div[@class="oxd-layout-container --collapse"]')
    ITEM = (By.XPATH, '//span[@class="oxd-text oxd-text--span oxd-main-menu-item--name"][text()="{title}"]')

    @property
    def search_field(self):
        return self.get_element(SidePanel.SEARCH_FIELD)

    @property
    def side_panel(self):
        return self.get_element(SidePanel.SIDE_PANEL, timeout=4)

    @property
    def hidden_side_panel(self):
        return self.get_element(SidePanel.HIDDEN_SIDE_PANEL, timeout=4)

    @property
    def side_panel_button(self):
        return self.get_element(SidePanel.SIDE_PANEL_BUTTON)

    @property
    def icon_for_displayed_panel(self):
        return self.get_element(SidePanel.ICON_FOR_DISPLAYED_PANEL)

    @property
    def icon_for_hidden_panel(self):
        return self.get_element(SidePanel.ICON_FOR_HIDDEN_PANEL)

    @property
    def layout_container(self):
        return self.get_element(SidePanel.LAYOUT_CONTAINER)

    @property
    def collapsed_layout_container(self):
        return self.get_element(SidePanel.LAYOUT_CONTAINER_COLLAPSED)

    @property
    def menu_item(self):
        def get_item_title(title):
            return self.get_element(SidePanel.ITEM, title=title)

        return get_item_title

    def side_panel_is_hidden(self):
        return self.collapsed_layout_container.is_displayed() and self.icon_for_hidden_panel.is_displayed()

    def side_panel_is_displayed(self):
        return self.layout_container.is_displayed() and self.icon_for_displayed_panel.is_displayed()

    def hide_side_panel(self):
        if not self.side_panel_is_displayed():
            self.side_panel_button.click()
        self.side_panel_button.click()

    def display_side_panel(self):
        if not self.side_panel_is_hidden():
            self.side_panel_button.click()
        self.side_panel_button.click()

    def search(self, query):
        self.search_field.send_keys(query)

    def side_panel_item_is_displayed(self, title):
        return self.menu_item(title).is_displayed()
