from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Locators:
    INPUT_FIELD = "//input[@id='number']"
    COOKIE_AGREE_BUTTON = "//button[contains(text(), 'Погоджуюсь') and contains(@class, 'cookie-banner__button--type-agree')]"
    ERROR_MESSAGE_RED = "//div[contains(@class, 'red-error-message')]"
    LOADER = "//div[contains(@class, 'np-loader')]"
    STATUS_TEXT = "//div[@class='header__status-text']"
    NOT_FOUND_TEXT = "//div[@class='not-found-wrapper__title']"


def wait_for(driver, xpath: str, wait_type, timeout: int = 5):
    """Універсальна обгортка для очікувань з WebDriverWait."""
    try:
        return WebDriverWait(driver, timeout).until(wait_type((By.XPATH, xpath)))
    except TimeoutException:
        raise TimeoutException(f"[{wait_type.__name__}] Тайм-аут {timeout}с: '{xpath}' на {driver.current_url}")


def click_element(driver, xpath: str, timeout: int = 5):
    element = wait_for(driver, xpath, EC.element_to_be_clickable, timeout)
    element.click()


def fill_input(driver, xpath: str, text: str, timeout: int = 5):
    element = wait_for(driver, xpath, EC.presence_of_element_located, timeout)
    element.clear()
    element.send_keys(text)


class ElementTextContains:
    """Очікування, поки елемент містить заданий текст."""
    def __init__(self, xpath: str, text: str):
        self.xpath = xpath
        self.text = text

    def __call__(self, driver):
        try:
            element = driver.find_element(By.XPATH, self.xpath)
            return self.text in element.text
        except NoSuchElementException:
            return False


def wait_for_text(driver, xpath: str, expected_text: str, timeout: int = 10):
    try:
        return WebDriverWait(driver, timeout).until(ElementTextContains(xpath, expected_text))
    except TimeoutException:
        raise TimeoutException(f"Тайм-аут {timeout}с: елемент '{xpath}' не містив текст '{expected_text}'.")


class NovaPoshtaTracker:
    def __init__(self, headless=True):
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")

        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.base_url = "https://tracking.novaposhta.ua/#/uk"
        self.default_wait = 15
        print("Драйвер браузера ініціалізовано.")

    def _handle_cookie_banner(self):
        try:
            click_element(self.driver, Locators.COOKIE_AGREE_BUTTON, timeout=5)
            print("Cookie банер прийнято.")
        except TimeoutException:
            print("Cookie банер не зʼявився.")
        except Exception as e:
            print(f"Помилка при cookie банері: {e}")

    def get_package_status(self, tracking_number: str) -> str:
        print(f"Запит ТТН: {tracking_number}")
        self.driver.get(self.base_url)
        self._handle_cookie_banner()

        try:
            fill_input(self.driver, Locators.INPUT_FIELD, tracking_number, timeout=self.default_wait)
            print(f"Введено ТТН: {tracking_number}")
        except TimeoutException:
            return "Помилка: поле ТТН не знайдено або не вдалося заповнити"

        # Первинне повідомлення про помилку
        try:
            error = wait_for(self.driver, Locators.ERROR_MESSAGE_RED, EC.visibility_of_element_located, timeout=3)
            return error.text.strip()
        except TimeoutException:
            pass

        # Очікування редіректу за URL
        try:
            WebDriverWait(self.driver, self.default_wait).until(EC.url_contains(tracking_number))
        except TimeoutException:
            try:
                error = wait_for(self.driver, Locators.ERROR_MESSAGE_RED, EC.visibility_of_element_located, timeout=1)
                return error.text.strip()
            except TimeoutException:
                return "Помилка: URL не змінився, статус невідомий"

        # Очікування завершення завантаження
        try:
            wait_for(self.driver, Locators.LOADER, EC.presence_of_element_located, timeout=3)
            wait_for(self.driver, Locators.LOADER, EC.invisibility_of_element_located, timeout=self.default_wait)
        except TimeoutException:
            print("Лоадер не зник вчасно.")

        # Спроба отримати статус
        try:
            status_element = wait_for(self.driver, Locators.STATUS_TEXT, EC.visibility_of_element_located, timeout=self.default_wait)
            return status_element.text.strip()
        except TimeoutException:
            try:
                error_element = wait_for(self.driver, Locators.NOT_FOUND_TEXT, EC.visibility_of_element_located, timeout=self.default_wait // 2)
                return error_element.text.strip()
            except TimeoutException:
                return f"Не вдалося отримати статус ТТН '{tracking_number}'"

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            print("Браузер закрито.")
            self.driver = None
