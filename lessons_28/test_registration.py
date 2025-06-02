import uuid
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_user_registration(driver, registration_page):
    # Клік по кнопці "Sign Up"
    reg_btn = registration_page.wait_for_element(registration_page.REG_BUTTON)
    reg_btn.click()

    # Чекаємо поки з’являться поля
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )

    elements = registration_page.get_elements()

    # Використовуємо унікальний емейл
    unique_email = f"user_{uuid.uuid4().hex[:6]}@example.com"

    elements["name"].send_keys("Test")
    elements["lastname"].send_keys("User")
    elements["email"].send_keys(unique_email)
    elements["password"].send_keys("Test1234$")
    elements["repass"].send_keys("Test1234$")
    elements["submit"].click()

    # Очікуємо на підтвердження входу (Garage)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Garage')]"))
    )

    assert "Garage" in driver.page_source
