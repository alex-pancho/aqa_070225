import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage as Reg
import random

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def wait(driver):
    return WebDriverWait(driver, 10)

@pytest.fixture
def open_registration_form(driver, wait):
    wait.until(EC.element_to_be_clickable(HomePage.registration_button)).click()

@pytest.fixture
def register_user(driver, wait, open_registration_form):
    email = f"testuser_{random.randint(10000,99999)}@example.com"
    wait.until(EC.presence_of_element_located(Reg.FIRST_NAME_INPUT)).send_keys("Test")
    driver.find_element(*Reg.LAST_NAME_INPUT).send_keys("User")
    driver.find_element(*Reg.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Reg.PASSWORD_INPUT).send_keys("Qwerty123$")
    driver.find_element(*Reg.REPEAT_PASSWORD_INPUT).send_keys("Qwerty123$")
    wait.until(EC.element_to_be_clickable(Reg.SUBMIT_BTN)).click()
    return email

@pytest.fixture
def registration_success_alert(driver, wait, register_user):
    return wait.until(EC.presence_of_element_located(Reg.SUCCESS_ALERT))