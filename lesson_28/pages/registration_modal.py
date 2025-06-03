from pages.base_page import BasePage

class RegisterModal(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        
    name =  "//input[@id = 'signupName']"
    last_name = "//input[@id = 'signupLastName']"
    email = "//input[@id = 'signupEmail']"
    password = "//input[@id = 'signupPassword']"
    re_enter_password = "//input[@id = 'signupRepeatPassword']"
    register_button = "//button[@class = 'btn btn-primary']"