from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def get_chrome(debug=False):
    options = ChromeOptions()
    
    if not debug:
        options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    
    if debug:
        driver.maximize_window()
    return driver
