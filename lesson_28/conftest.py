import pytest
import uuid
from get_browser import firefox, chrome
from pages.home_page import HomePage
from pages.garage_page import GaragePage
from pages.registration_modal import RegisterModal
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

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

@pytest.fixture
def test_data():
    return {
        "name": "first",
        "last_name": "last",
        "email": f"{uuid.uuid4()}@test.com",
        "password": "Qwerty123"
    }

@pytest.fixture
def register_delete_user(driver, garage_page):
    #передаємо в тест модалку реєстрації
    yield RegisterModal(driver)
    #робимо спробу видалити створений акаунт
    try:
       
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH, garage_page.settings))).click()

        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       
        wait.until(EC.element_to_be_clickable((By.XPATH, garage_page.remove_account))).click()
        wait.until(EC.element_to_be_clickable((By.XPATH, garage_page.remove_confirm))).click()
    #показуємо помилку якщо видалення не пройшло
    except Exception as e:
        raise TimeoutError(f"Account was not removed: {e}")