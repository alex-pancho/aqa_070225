from selenium.webdriver.common.by import By

class RegistrationPageLocators:
    SIGN_UP_BUTTON = (By.XPATH, "//button[contains(text(),'Sign up')]")
    NAME_INPUT = (By.ID, "signupName")
    LASTNAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    REPASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    REGISTER_BUTTON = (By.XPATH, "//button[@type='submit' and contains(text(), 'Register')]")
    SUCCESS_TOAST = (By.CLASS_NAME, "success")
