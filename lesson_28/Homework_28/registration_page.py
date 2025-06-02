from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def item(self, locator):
        return self.driver.find_element(*locator)

    SIGNIN_BUTTON = (By.CLASS_NAME, "header_signin")
    REGISTRATION_BUTTON = (By.XPATH, "//button[text()='Registration']")

    NAME_INPUT = (By.ID, "signupName")
    LASTNAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    REPASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Register']")
    SUCCESS_ALERT = (By.CLASS_NAME, "alert")
