from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def get_element(self, locator, timeout=3, **kwargs):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((locator[0], locator[1].format(**kwargs))))
