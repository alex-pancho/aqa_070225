from selenium.webdriver.common.by import By

class RegistrationPage:
    REGISTER_BTN = (By.XPATH, "//button[contains(text(), 'Sign up')]")
    
    # Fields
    FIRST_NAME_INPUT = (By.ID, "signupName")
    LAST_NAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    REPEAT_PASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    
    
    SUBMIT_BTN = (By.XPATH, "//button[contains(text(), 'Register')]")
    SUCCESS_ALERT = (By.CSS_SELECTOR, "div.alert.alert-success p")