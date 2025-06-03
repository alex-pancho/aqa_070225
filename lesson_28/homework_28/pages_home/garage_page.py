from pages.base_page import BasePage


class GaragePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    add_car = '//button[@class="btn btn-primary"]'