from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest


class NovaPoshtaTracker:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open(self):
        self.driver.get(self.url)

    def get_error_message(self, ttn_number):
        self.open()
        self.driver.maximize_window()

        input_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Номер посилки']"))
        )

        input_field.clear()
        input_field.send_keys(ttn_number)
        input_field.send_keys(Keys.ENTER)

        error_text_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located(
                (By.ID, "np-number-input-desktop-message-error-message")
            )
        )

        return error_text_element.text.strip()





class NovaPoshtaTrackingTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.tracker = NovaPoshtaTracker(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_invalid_ttn_shows_error(self):
        ttn = "12345678901234"  
        expected_phrase = "не знайшли посилку"

        error_message = self.tracker.get_error_message(ttn)
        print(f"Отримано повідомлення: {error_message}")
        self.assertIn(expected_phrase, error_message.lower())



if __name__ == "__main__":
    unittest.main()
