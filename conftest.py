import pytest
from selene import browser


@pytest.fixture(scope='function')
def browser_management():
    browser.config.window_width = 1366
    browser.config.window_height = 768123123

    yield

    browser.quit()
