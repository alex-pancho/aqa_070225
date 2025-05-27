from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


def frame1(driver):
    """Обробка першого фрейму: введення секрету й підтвердження через alert."""
    driver.switch_to.frame(driver.find_element(By.ID, "frame1"))

    input_1 = driver.find_element(By.ID, "input1")
    input_1.click()
    input_1.send_keys("Frame1_Secret")

    button_1 = driver.find_element(By.XPATH, "//button[text()='Перевірити'][1]")
    button_1.click()

    alert = Alert(driver)
    print("[frame1] Alert text:", alert.text)
    alert.accept()

    time.sleep(2)
    driver.switch_to.default_content()


def frame2(driver):
    """Обробка другого фрейму"""
    driver.switch_to.frame(driver.find_element(By.ID, "frame2"))

    input_2 = driver.find_element(By.ID, "input2")
    input_2.click()
    input_2.send_keys("Frame2_Secret")

    button_2 = driver.find_element(By.XPATH, "//button[text()='Перевірити'][1]")
    button_2.click()

    alert = Alert(driver)
    print("[frame2] Alert text:", alert.text)
    alert.accept()

    time.sleep(2)
    driver.switch_to.default_content()


def main():
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/dz.html")

    try:
        frame1(driver)
        frame2(driver)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()