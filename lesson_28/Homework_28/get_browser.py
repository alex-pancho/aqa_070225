from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

def chrome(debug=False):
    """
    Initializes and returns a Chrome WebDriver instance.

    Args:
        debug (bool): If True, launches the browser in visible mode.
                      If False, runs Chrome in headless mode.

    Returns:
        WebDriver: Configured instance of Chrome WebDriver.
    """
    options = ChromeOptions()

    if not debug:
        options.add_argument("--headless=new")  

    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)

    if debug:
        driver.maximize_window()
    return driver
