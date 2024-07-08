import pytest
from selenium.webdriver import Chrome


@pytest.fixture()
def browser():
    browser = Chrome()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()
