from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class GaragePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    REGISTRATION_CONFIRMATION = (By.XPATH, '//p[text()="Registration complete"]')