from pages.base_page import BasePage


class GaragePage(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
    
    add_car = '//button[@class="btn btn-primary"]'
    brand = '//*[@id="addCarBrand"]'
    model = '',  # TODO: add the xpath here
    mileage = '//*[@id="addCarMileage"]'
    add = '//button[. = "Add"]'
    new_car = '//li[@class="car-item"]'
    guest_btn = '//button[. = "Guest log in"]'
    profile = '//a[contains(text(), "Profile")]/ancestor::div[@class="sidebar_btn-group"]'
    settings = '//div[@class ="sidebar_btn-group"]//a[contains(text(), "Settings")]'
    remove_account = '//button[contains(text(), "Remove my account")]'
    remove_confirm = '//button[text() = "Remove"]'