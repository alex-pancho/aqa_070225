import pytest
from get_browser import firefox, chrome
from pages.log_in_form import LogInForm
from pages.registration_form import RegistrationForm
from pages.main_page import MainPage
from pages.garage_page import GaragePage


URL = "https://guest:welcome2qauto@qauto.forstudy.space"

@pytest.fixture(scope="module")
def driver():
    _driver = chrome(True)
    _driver.get(URL)
    yield _driver
    _driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def log_in_form(driver):
    return LogInForm(driver)

@pytest.fixture
def registration_form(driver):
    return RegistrationForm(driver)

@pytest.fixture
def garage_page(driver):
    return GaragePage(driver)

@pytest.fixture
def name():
    return 'Iuliia'

@pytest.fixture
def last_name():
    return 'Lazurkevych'

@pytest.fixture
def email():
    return 'lazurkevych@test8.com'

@pytest.fixture
def password():
    return 'Qwerty123!'