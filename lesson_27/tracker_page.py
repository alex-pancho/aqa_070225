from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TrackerPage:
    def __init__(self, driver):
        """
        Initialize the TrackerPage with a Selenium WebDriver.

        :param driver: Selenium WebDriver instance (e.g. Chrome, Firefox).
        """
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"

    def open(self):
        """
        Open the Nova Poshta tracking webpage and wait for the input field to load.
        """
        self.driver.get(self.url)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Номер посилки']"))
        )

    def enter_invoice_number_and_submit(self, number):
        """
        Enter the provided invoice number into the tracking field and press Enter.

        :param number: String, the TTN (invoice number) to track.
        """
        input_field = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Номер посилки']"))
        )
        input_field.clear()
        input_field.send_keys(number)
        input_field.send_keys(Keys.ENTER)

    def get_status_text(self):
        """
        Retrieve the error/status message if the parcel is not found.

        :return: String with the error or status message.
        """
        try:
            error_element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(
                    (By.ID, "np-number-input-desktop-message-error-message")
                )
            )
            return error_element.text.strip()
        except:
            return "Стан не знайдено"

