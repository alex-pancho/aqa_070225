from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions


def create_firefox(debug=False):
    options = FirefoxOptions()
    if not debug:
        options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    if debug:
        driver.maximize_window()
    return driver


def create_chrome(debug=False):
    options = ChromeOptions()
    if not debug:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")  # Chrome автоматично відкриє на весь екран
    driver = webdriver.Chrome(options=options)
    return driver
