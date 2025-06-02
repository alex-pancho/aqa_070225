import os
import sys
import pytest
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from lesson_28.get_browser import chrome
from lesson_28.Homework_28.registration_page import RegistrationPage

@pytest.fixture(scope="module")
def driver():
    driver = chrome(debug=True)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)

@pytest.fixture
def go_to_registration(registration_page):
    def _go():
        wait = WebDriverWait(registration_page.driver, 10)
        wait.until(EC.element_to_be_clickable(RegistrationPage.SIGNIN_BUTTON))
        registration_page.item(RegistrationPage.SIGNIN_BUTTON).click()

        wait.until(EC.element_to_be_clickable(RegistrationPage.REGISTRATION_BUTTON))
        registration_page.item(RegistrationPage.REGISTRATION_BUTTON).click()
    return _go

@pytest.fixture
def fill_registration_form(registration_page):
    def _fill():
        registration_page.item(RegistrationPage.NAME_INPUT).send_keys("Test")
        registration_page.item(RegistrationPage.LASTNAME_INPUT).send_keys("User")
        email = f"test{random.randint(1000,9999)}@mail.com"
        registration_page.item(RegistrationPage.EMAIL_INPUT).send_keys(email)
        registration_page.item(RegistrationPage.PASSWORD_INPUT).send_keys("Qwerty123$")
        registration_page.item(RegistrationPage.REPASSWORD_INPUT).send_keys("Qwerty123$")
        return email
    return _fill

@pytest.fixture
def submit_form(registration_page):
    def _submit():
        WebDriverWait(registration_page.driver, 10).until(
            EC.element_to_be_clickable(RegistrationPage.SUBMIT_BUTTON)
        )
        registration_page.item(RegistrationPage.SUBMIT_BUTTON).click()
    return _submit

@pytest.fixture
def check_success_alert(driver, registration_page):
    def _check():
        try:
            WebDriverWait(driver, 10).until(
                lambda d: registration_page.item(registration_page.SUCCESS_ALERT).is_displayed()
            )
            return registration_page.item(registration_page.SUCCESS_ALERT).text
        except Exception:
            return ""
    return _check

@pytest.fixture
def check_redirect_to_garage(driver):
    def _check():
        try:
            WebDriverWait(driver, 10).until(lambda d: "/panel/garage" in d.current_url)
            return True
        except Exception:
            return False
    return _check
