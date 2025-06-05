from selenium.webdriver.common.by import By

class HomePage:

    def __init__(self, driver, url) -> None:
        self.driver = driver
        self.driver.get(url)
    
    input_fld = (By.XPATH, '//*[@id="en"]')
    search_btn = (By.XPATH, '//*[id="np-number-input-desktop-btn-search-en"]')
    status_text = (By.XPATH, '//*[id="np-number-input-desktop-btn-search-en"]')