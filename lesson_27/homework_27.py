from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from homework27_po import HomePage

class ElementTextContains:
    def __init__(self, locator, text):
        self.locator = locator
        self.text = text

    def __call__(self, driver):
        try:
            element = driver.find_element(By.XPATH, self.locator)
            return self.text in element.text
        except:
            return False
        
def exist_element(driver, xpath, time_for_wait:int = 5):
    try:
        element = WebDriverWait(driver, timeout=time_for_wait).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Element with {xpath} not found on {driver.current_url} during {time_for_wait} sec")
        
def fill_input(driver, xpath, text):
    """Функція для заповнення поля вводу текстом"""
    element = exist_element(driver, xpath)
    element.clear()
    element.send_keys(text)
    
def clickable(driver, xpath, time_for_wait:int = 5):
    try:
        element = WebDriverWait(driver, timeout=time_for_wait).until(
            EC.element_to_be_clickable((By.XPATH, xpath))
        )
        return element
    except TimeoutException:
        raise TimeoutException(f"Element with {xpath} not click on {driver.current_url} during {time_for_wait} sec")

def click_element(driver, xpath):
    """Функція для кліку на елемент"""
    element = clickable(driver, xpath)
    element.click()

def test_search():
    url = "https://tracking.novaposhta.ua/#/uk"
    driver = webdriver.Firefox()
    driver.get(url)
    home_page = HomePage(driver, url)
    input_field = exist_element(driver, home_page.input_fld)
    input_field.click()
    text = "59001302358739"
    fill_input(driver, home_page.input_fld, text)
    clickable(driver, home_page.search_btn, 0.1)
    click_element(driver, home_page.search_btn)
    assert WebDriverWait(driver, timeout=5).until(ElementTextContains(home_page.status_text, " Отримана "))
    driver.close()