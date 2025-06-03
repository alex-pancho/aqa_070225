from pages.base_page import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    sign_in_button = '//button[.="Sign In"]'
    sign_up_button ='//button[.="Sign Up"]'
    registration_button = '//button[.="Registration"]'
    name_input = '//input[@id="signupName"]'
    last_name_input ='//input[@id="signupLastName"]'
    email_input = '//input[@id="signupEmail"]'
    password_input = '//input[@id="signupPassword"]'
    repeat_password ='//input[@id="signupRepeatPassword"]'
    register_btn='//button[.="Register"]'
    