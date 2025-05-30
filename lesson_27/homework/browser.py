from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chromeOption

def chrome(debug=False):
    """Ініціалізує та повертає екземпляр Firefox WebDriver.

    Args:
        debug (bool): Якщо True, запускає браузер з вікном. Якщо False — у headless режимі.

    Returns:
        WebDriver: Ініціалізований екземпляр Firefox WebDriver.
    """
    options = chromeOption()
    if not debug:
        options.add_argument("--headless")  # Запуск у безголовному режимі (без UI)

    driver = webdriver.Chrome(options=options)
    
    if debug:
        driver.maximize_window()  # Максимізація вікна лише якщо debug увімкнено

    return driver

