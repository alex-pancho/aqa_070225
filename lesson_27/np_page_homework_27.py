from selenium.webdriver.common.by import By


class NovaPoshtaTrackingPage:
    def __init__(self, driver, url="https://tracking.novaposhta.ua/#/uk"):
        self.driver = driver
        self.driver.get(url)

    input_ttn_number = (By.XPATH, '//*[@id="en"]')
    search_btn = (By.XPATH, '//*[@id="np-number-input-desktop-btn-search-en"]')
    status_block = (By.XPATH, '//*[@id="np-number-input-desktop-message-error-message"]/span')
    error_message_text = "Ми не знайшли посилку за таким номером. Якщо ви шукаєте інформацію про посилку, якій більше 3 місяців, будь ласка, зверніться у контакт-центр: 0 800 500 609"
