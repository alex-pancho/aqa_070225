from pages.base_page import BasePage


class RegistrationModule(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    sign_up_name = '//input[@id="signupName"]'
    sign_up_last_name = '//input[@id="signupLastName"]'
    sign_up_email = '//input[@id="signupEmail"]'
    sign_up_password = '//input[@id="signupPassword"]'
    sign_up_repeat_password = '//input[@id="signupRepeatPassword"]'
    register_button = '//button[.="Register"]'