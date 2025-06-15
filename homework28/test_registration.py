import time
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.registration_page import RegistrationPage as Reg  

# Generate a unique email address
def generate_unique_email():
    return f"testuser_{random.randint(10000, 99999)}@example.com"

def test_user_registration(driver):
    wait = WebDriverWait(driver, 10)

    # Click the "Sign up" button
    wait.until(EC.element_to_be_clickable(Reg.REGISTER_BTN)).click()

    # Fill in the registration form
    wait.until(EC.presence_of_element_located(Reg.FIRST_NAME_INPUT)).send_keys("Test")
    driver.find_element(*Reg.LAST_NAME_INPUT).send_keys("User")
    driver.find_element(*Reg.EMAIL_INPUT).send_keys(generate_unique_email())
    driver.find_element(*Reg.PASSWORD_INPUT).send_keys("Qwerty123$")
    driver.find_element(*Reg.REPEAT_PASSWORD_INPUT).send_keys("Qwerty123$")

    # Submit the registration form
    wait.until(EC.element_to_be_clickable(Reg.SUBMIT_BTN)).click()

    # Check if registration was successful
    alert = wait.until(EC.presence_of_element_located(Reg.SUCCESS_ALERT))
    assert "registration complete" in alert.text.lower()