from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def chrome(headless=False):
    options = Options()
    if headless:
        options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)