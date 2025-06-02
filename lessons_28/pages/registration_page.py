from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    REG_BUTTON = (By.CSS_SELECTOR, "button.hero-descriptor_btn")  # "Sign Up" button on main page
    NAME_INPUT = (By.NAME, "name")
    LASTNAME_INPUT = (By.NAME, "lastName")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    REPASS_INPUT = (By.NAME, "repeatPassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Register')]")

    def get_elements(self):
        return {
            "reg_btn": self.wait_for_element(self.REG_BUTTON),
            "name": self.wait_for_element(self.NAME_INPUT),
            "lastname": self.wait_for_element(self.LASTNAME_INPUT),
            "email": self.wait_for_element(self.EMAIL_INPUT),
            "password": self.wait_for_element(self.PASSWORD_INPUT),
            "repass": self.wait_for_element(self.REPASS_INPUT),
            "submit": self.wait_for_element(self.SUBMIT_BUTTON),
        }
