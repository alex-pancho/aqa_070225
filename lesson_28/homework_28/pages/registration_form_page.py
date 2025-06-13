from selenium.webdriver.common.by import By
from lesson_28.homework_28.pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    name_input = (By.XPATH, '//*[@id="signupName"]')
    last_name_input = (By.XPATH, '//*[@id="signupLastName"]')
    email_input = (By.XPATH, '//*[@id="signupEmail"]')
    password_input = (By.XPATH, '//*[@id="signupPassword"]')
    re_enter_password_input = (By.XPATH, '//*[@id="signupRepeatPassword"]')
    register_button = (By.XPATH, '/html/body/ngb-modal-window/div/div/app-signup-modal/div[3]/button')
    title = (By.XPATH, "//h1[text()='Garage']")