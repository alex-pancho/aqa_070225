from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        
    NAME_FIELD = (By.XPATH, '//input[@id="signupName"]')
    LAST_NAME_FIELD = (By.XPATH, '//input[@id="signupLastName"]')
    EMAIL_FIELD = (By.XPATH, '//input[@id="signupEmail"]')
    PASSWORD_FIELD = (By.XPATH, '//input[@id="signupPassword"]')
    REENTER_PASSWORD_FIELD = (By.XPATH, '//input[@id="signupRepeatPassword"]')
    REGISTER_BUTTON = (By.XPATH, '//button[@class="btn btn-primary" and text()="Register"]')

    def fill_in_name_field(self, name):
        self.driver.find_element(*self.NAME_FIELD).send_keys(name)

    def fill_in_last_name_field(self, last_name):
        self.driver.find_element(*self.LAST_NAME_FIELD).send_keys(last_name)

    def fill_in_email_field(self, email):
        self.driver.find_element(*self.EMAIL_FIELD).send_keys(email)

    def fill_in_password_field(self, password):
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)

    def fill_in_reenter_password_field(self, password):
        self.driver.find_element(*self.REENTER_PASSWORD_FIELD).send_keys(password)

    def click_register_button(self):
        self.driver.find_element(*self.REGISTER_BUTTON).click()