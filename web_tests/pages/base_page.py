from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    HEADER_TITLE = (By.XPATH, '//span[@class="oxd-topbar-header-breadcrumb"]/h6')

    def __init__(self, browser):
        self.browser = browser

    def get_element(self, locator, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    @property
    def header_title(self):
        return self.get_element(*BasePage.HEADER_TITLE)
