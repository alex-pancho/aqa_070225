from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    registration_button = (By.XPATH, "//button[text()='Sign up']")