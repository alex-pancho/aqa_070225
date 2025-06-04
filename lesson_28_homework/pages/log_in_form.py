from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LogInForm(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    
    REGISTRATION_BUTTON = (By.XPATH, '//button[@class="btn btn-link" and text()="Registration"]')

    def open_register_form(self):
        self.driver.find_element(*self.REGISTRATION_BUTTON).click()