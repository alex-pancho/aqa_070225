import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def open_page(self, url: str) -> None:
        return self.driver.get(url)

    def find_element_(self, locator: tuple):
        return self.driver.find_element(*locator)

    def find_elements_(self, locator: tuple):
        return self.driver.find_elements(*locator)

    def find_element_text_(self, locator: tuple):
        return self.find_element_(locator).text

    def get_attribute_(self, locator: tuple, value):
        return self.find_element_(locator).get_attribute(value)


    def send_keys_(self, locator, text: [str, int], hide=False) -> [tuple, str, int]:
        if hide:
            return self.find_element_(locator).send_keys(text)
        else:
            return self.find_element_(locator).send_keys(text)

    def clear_field_(self, locator):
        return self.find_element_(locator).clear()


    def click_btn_(self, locator):
        return self.find_element_(locator).click()

    def click_on_js_(self, locator: tuple):
        return self.driver.execute_script("arguments[0].click();", self.find_element_(locator))


    def wait_presence_of_el_located(self, time_: int, locator: tuple):
        return Wait(self.driver, time_).until(EC.presence_of_element_located(locator))

    def wait_visible_of_el_located(self, time_: int, locator: tuple):
        return Wait(self.driver, time_).until(EC.visibility_of_element_located(locator))

    def actions_chains_move_click(self, move_to: tuple, click_to=None):
        action = ActionChains(self.driver)
        move_element = self.find_element_(move_to)
        action.move_to_element(move_element)
        clickable_element = self.find_element_(click_to)
        action.click(clickable_element)
        action.perform()
