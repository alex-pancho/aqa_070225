from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class TrackingPage:

    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.driver.get(url)
    
    parcel_number_input_field = (By.XPATH, "//input[@id='en']")
    button_search = (By.XPATH, "//input[@id='np-number-input-desktop-btn-search-en']")
    button_helper = (By.XPATH, "//button//*[contains(text(), 'Зрозуміло') or contains(text(), 'Добре')]") 
    result_status = (By.XPATH, "//div[@class='header__status-text']")
    error = (By.XPATH, "//div [@class='track__form-message track__form-error']")
    
    def search_parcel_by_number (self, number):
        input_parcel_number = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.parcel_number_input_field))
        input_parcel_number.send_keys(number)
        search_button = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.button_search))
        search_button.click()
        return
    
    def parcel_status(self):
        """try:
            helper = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.button_helper ))
            helper.click()
        except TimeoutException:
            pass """
        try:
            status = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.result_status) )
            return  status.text.strip()
        except TimeoutException:
            try:
                error_message = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.error) )
                return  error_message.text.strip()
            except TimeoutException:   
                raise TimeoutError ("Expected element not found")
    

        