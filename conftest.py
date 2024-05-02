import pytest
from selene import browser


@pytest.fixture(autouse=True)
def browser_management():
    browser.config.window_width = 1366
    browser.config.window_height = 768

    yield

    browser.quit()
