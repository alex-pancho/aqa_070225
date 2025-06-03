import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    """
    Pytest fixture that initializes and tears down the Selenium WebDriver.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def track_link():
    return "https://tracking.novaposhta.ua/#/uk"

@pytest.fixture
def parcel_number():
    return 59001368623363