from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class ElementActions:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def find_element(self, xpath):
        try:
            return self.wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            raise NoSuchElementException(f"Element with xpath '{xpath}' not found")

    def find_visible_element(self, xpath):
        try:
            return self.wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            raise NoSuchElementException(f"Element with xpath '{xpath}' not visible")

    def fill_input(self, xpath, text):
        field = self.find_element(xpath)
        field.clear()
        field.send_keys(text)

    def get_text(self, xpath):
        return self.find_visible_element(xpath).text
