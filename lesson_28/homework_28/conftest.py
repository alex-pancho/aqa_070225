import pytest
from get_browser import firefox, chrome
from homework_28.pages_home.home_page import HomePage
from homework_28.pages_home.garage_page import GaragePage

URL = "https://guest:welcome2qauto@qauto.forstudy.space"


@pytest.fixture(scope="module")
def driver():
    _driver = firefox(True)
    _driver.get(URL)
    yield _driver
    _driver.quit()

@pytest.fixture
def home_page(driver):
    return HomePage(driver)

@pytest.fixture
def garage_page(driver):
    return GaragePage(driver)