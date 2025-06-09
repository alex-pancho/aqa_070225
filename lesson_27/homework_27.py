from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class NovaPoshtaTrackerFirefox:
    """Трекер статусу посилки через Firefox у Linux (Ubuntu)."""

    URL = "https://tracking.novaposhta.ua/#/uk"

    def __init__(self, headless: bool = True):
        geckodriver_path = "/snap/bin/geckodriver"
        driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)
        self.driver = webdriver.Firefox(service=driver_service)
        self.wait = WebDriverWait(self.driver, 10)

    def get_status(self, tracking_number: str) -> str:
        self.driver.get(self.URL)
        try:
            input_box = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
            input_box.clear()
            input_box.send_keys(tracking_number, Keys.ENTER)
            search_button=self.driver.find_element(By.XPATH,"//input[@id='np-number-input-desktop-btn-search-en']")
            search_button.click()

            status_elem = self.wait.until(EC.visibility_of_element_located(
                (By.XPATH, '//div[@class="header__status-text"]')
            ))
            return status_elem.text.strip()
        except TimeoutException:
            return "Не вдалося отримати статус. Можливо, номер некоректний або сайт не відповідає."
        finally:
            self.driver.quit()

def track_number(tracking_number: str) -> str:
    tracker = NovaPoshtaTrackerFirefox()
    return tracker.get_status(tracking_number)

if __name__ == "__main__":
    num = "20451163138077"
    status = track_number(num)
    print("Статус:", status)
