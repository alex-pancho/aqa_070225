from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class MainPage(BasePage):
    
    SIGN_IN_BUTTON = (By.XPATH, '//button[@class="btn btn-outline-white header_signin"]')

    def __init__(self, driver):
        super().__init__(driver)
        
    def open_login_form(self):
        self.driver.find_element(*self.SIGN_IN_BUTTON).click()