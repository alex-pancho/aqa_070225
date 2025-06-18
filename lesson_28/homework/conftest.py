import pytest

from aqa_070225.lesson_28.homework.browsers import create_firefox, create_chrome
from aqa_070225.lesson_28.homework.pages.registration_form_page import RegistrationPage
from aqa_070225.lesson_28.homework.pages.home_page import HomePage
URL = "https://guest:welcome2qauto@qauto.forstudy.space"


@pytest.fixture(scope="session")
def firefox_driver():
    driver = create_firefox(debug=True)
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def chrome_driver():
    driver = create_chrome(debug=True)
    driver.get(URL)
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def home_page(chrome_driver):
    return HomePage(chrome_driver)


@pytest.fixture(scope="session")
def registration_page(chrome_driver):
    return RegistrationPage(chrome_driver)
