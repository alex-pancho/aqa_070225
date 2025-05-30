from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class ElementTextContains:
    """
    Спеціальна умова очікування: перевіряє, чи текст елемента містить заданий підрядок.
    """
    def __init__(self, locator_xpath: str, text: str):
        self.locator_xpath = locator_xpath
        self.text = text

    def __call__(self, driver):
        try:
            element = driver.find_element(By.XPATH, self.locator_xpath)
            return self.text in element.text
        except NoSuchElementException:
            return False
        return False

def get_element_with_text_value(driver, xpath: str, text_value: str, max_timeout: int = 10):
    """
    Чекає, доки елемент за XPath не буде містити вказаний текст.
    Повертає True, якщо текст знайдено, інакше генерує TimeoutException.
    """
    wait = WebDriverWait(driver, max_timeout)
    try:
        return wait.until(ElementTextContains(xpath, text_value))
    except TimeoutException:
        raise TimeoutException(f"Тайм-аут: Елемент за XPath '{xpath}' не містив текст '{text_value}' протягом {max_timeout}с.")

def exist_element(driver, xpath: str, time_for_wait: int = 5):
    """Чекає на присутність елемента в DOM за XPath."""
    try:
        element = WebDriverWait(driver, timeout=time_for_wait).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Елемент з XPath '{xpath}' не знайдено на {driver.current_url} протягом {time_for_wait} сек")

def visibility(driver, xpath: str, time_for_wait: int = 5):
    """Чекає на видимість елемента за XPath."""
    try:
        element = WebDriverWait(driver, timeout=time_for_wait).until(
            EC.visibility_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Елемент з XPath '{xpath}' не видимий на {driver.current_url} протягом {time_for_wait} сек")

def clickable(driver, xpath: str, time_for_wait: int = 5):
    """Чекає, доки елемент за XPath не стане клікабельним."""
    try:
        element = WebDriverWait(driver, timeout=time_for_wait).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Елемент з XPath '{xpath}' не клікабельний на {driver.current_url} протягом {time_for_wait} сек")

def click_element(driver, xpath: str, time_for_wait: int = 5):
    """Функція для кліку на елемент, чекає на його клікабельність."""
    element = clickable(driver, xpath, time_for_wait=time_for_wait)
    element.click()

def fill_input(driver, xpath: str, text: str, time_for_wait: int = 5):
    """Функція для заповнення поля вводу текстом, чекає на його існування."""
    element = exist_element(driver, xpath, time_for_wait=time_for_wait)
    element.clear()
    element.send_keys(text)



class NovaPoshtaTracker:
    """
    Клас для відстеження посилок, що використовує допоміжні функції.
    """
    def __init__(self, headless=True):
        chrome_options = webdriver.ChromeOptions()
        if headless:
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
        
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=chrome_options)
        self.base_url = "https://tracking.novaposhta.ua/#/uk"
        self.default_wait_time = 15
        print("Драйвер браузера ініціалізовано.")

    def _handle_cookie_banner(self):
        cookie_agree_button_xpath = "//button[contains(text(), 'Погоджуюсь') and contains(@class, 'cookie-banner__button--type-agree')]"
        try:
            click_element(self.driver, cookie_agree_button_xpath, time_for_wait=5)
            print("Cookie банер: натиснуто 'Погоджуюсь'.")
        except TimeoutException:
            print("Cookie банер не знайдено або не вдалося натиснути.")
        except Exception as e:
            print(f"Інша помилка при обробці cookie банера: {e}")

    def get_package_status(self, tracking_number: str) -> str:
        print(f"Запит статусу для ТТН: {tracking_number}")
        self.driver.get(self.base_url)
        
        self._handle_cookie_banner()

        input_field_xpath = "//input[@id='number']"
        try:
            fill_input(self.driver, input_field_xpath, tracking_number, time_for_wait=self.default_wait_time)
            print(f"Номер ТТН '{tracking_number}' введено в поле.")
        except TimeoutException:
            print(f"Помилка: не вдалося знайти/заповнити поле вводу для ТТН.")
            return "Помилка: поле вводу не знайдено/не заповнено"
        
        error_red_message_xpath = "//div[contains(@class, 'red-error-message')]"
        try:
            red_error_element = visibility(self.driver, error_red_message_xpath, time_for_wait=3)
            message = red_error_element.text.strip()
            print(f"Знайдено первинне повідомлення про помилку: '{message}'")
            return message
        except TimeoutException:
            pass 

        try:
            WebDriverWait(self.driver, self.default_wait_time).until(EC.url_contains(tracking_number))
            print(f"URL успішно змінився і містить '{tracking_number}'.")
        except TimeoutException:
            print(f"URL не змінився і не містить '{tracking_number}' вчасно.")
            try: 
                red_error_element = visibility(self.driver, error_red_message_xpath, time_for_wait=1)
                return red_error_element.text.strip()
            except TimeoutException:
                return "Помилка: URL не змінився, статус не визначено"

        loader_xpath = "//div[contains(@class, 'np-loader')]"
        try:
            WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, loader_xpath)))
            WebDriverWait(self.driver, self.default_wait_time).until(EC.invisibility_of_element_located((By.XPATH, loader_xpath)))
            print("Індикатор завантаження оброблено.")
        except TimeoutException:
            print("Індикатор завантаження не з'явився або не зник вчасно.")
            pass
        
        status_text_xpath = "//div[@class='header__status-text']"
        error_not_found_xpath = "//div[@class='not-found-wrapper__title']"
        
        try:
            status_element = visibility(self.driver, status_text_xpath, time_for_wait=self.default_wait_time)
            status_message = status_element.text.strip()
            print(f"Отримано статус: '{status_message}'")
            return status_message
        except TimeoutException:
            print(f"Текст статусу за XPath '{status_text_xpath}' не знайдено. Спроба знайти повідомлення 'Номер не знайдено'.")
            try:
                error_element = visibility(self.driver, error_not_found_xpath, time_for_wait=self.default_wait_time // 2)
                error_message = error_element.text.strip()
                print(f"Отримано повідомлення 'Номер не знайдено': '{error_message}'")
                return error_message
            except TimeoutException:
                message = f"Не вдалося знайти ані статус, ані повідомлення про помилку для ТТН '{tracking_number}'."
                print(message)
                return "Не вдалося отримати статус (timeout або елементи не знайдено)"
        except Exception as e:
            message = f"Неочікувана помилка при отриманні статусу для ТТН '{tracking_number}': {e}"
            print(message)
            return f"Неочікувана помилка: {e}"

    def close_browser(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            print("Браузер закрито.")