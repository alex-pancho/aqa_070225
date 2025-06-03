from selenium.webdriver.common.by import By

class TrackParcel:
    def __init__(self, driver):
        self.driver = driver
        self.number_input = (By.XPATH, '//input[@class="track__form-group-input"]')
        self.search_button = (By.XPATH, '//input[@id="np-number-input-desktop-btn-search-en"]')
        self.parcel_status = (By.XPATH, '//div[@class="header__status-text"]')

    def enter_parcel_number(self, parcel_number):
        """
        Enters the parcel number into the input field.
        """
        self.driver.find_element(*self.number_input).send_keys(parcel_number)

    def click_search_button(self):
        """
        Clicks the search button to track the parcel.
        """
        self.driver.find_element(*self.search_button).click()

    def get_parcel_status(self):
        """
        Returns the current status text of the tracked parcel.
        """
        return self.driver.find_element(*self.parcel_status).text.strip()


  