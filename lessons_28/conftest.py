import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.registration_page import RegistrationPage

@pytest.fixture(scope="session")
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    yield driver
    driver.quit()

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)
