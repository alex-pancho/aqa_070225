import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lesson_28.HW_28.pages.registration_page import RegistrationPageLocators as Loc




@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless") 
    options.add_argument("--window-size=1920,1080")

    url = "https://guest:welcome2qauto@qauto2.forstudy.space/"
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture
def open_registration(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(Loc.SIGN_UP_BUTTON)
    ).click()


@pytest.fixture
def fill_registration_form(driver):
    def _fill(name, last, email, password):
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(Loc.NAME_INPUT)).send_keys(name)
        driver.find_element(*Loc.LASTNAME_INPUT).send_keys(last)
        driver.find_element(*Loc.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Loc.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.REPASSWORD_INPUT).send_keys(password)
        driver.find_element(*Loc.REGISTER_BUTTON).click()
    return _fill


@pytest.fixture
def get_success_toast(driver):
    def _get_text(timeout=10):
        toast = WebDriverWait(driver, timeout).until(EC.visibility_of_element_located(Loc.SUCCESS_TOAST))
        return toast.text.strip()
    return _get_text
