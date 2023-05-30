import os
import pytest

from chromedriver import ChromeDriver

@pytest.fixture(scope="class")
def chrome_driver(foreground):
    browser = ChromeDriver(foreground)
    yield browser.driver
    del browser