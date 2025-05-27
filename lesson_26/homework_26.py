from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.alert import Alert


driver = webdriver.Firefox()

driver.get("http://localhost:8000/dz.html")

WebDriverWait(driver, 5).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1"))
)

input1 = driver.find_element(By.ID, "input1")
input1.send_keys("Frame1_Secret")
button1 = driver.find_element(By.XPATH, '//button[.="Перевірити"]')
button1.click()

alert = driver.switch_to.alert
alert = Alert(driver)
if alert.text == "Верифікація пройшла успішно!":
    print("Alert text is corrrect:", alert.text)
else:
    print("Alert text is incorrect:", alert.text)
alert.accept()
driver.switch_to.default_content()


WebDriverWait(driver, 5).until(
    EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2"))
)
input2 = driver.find_element(By.ID, "input2")
input2.send_keys("Frame2_Secret")
button2 = driver.find_element(By.XPATH, '//button[.="Перевірити"]')
time.sleep(2)
button2.click()
alert = driver.switch_to.alert
alert = Alert(driver)
if alert.text == "Верифікація пройшла успішно!":
    print("Alert text is corrrect:", alert.text)
else:
    print("Alert text is incorrect:", alert.text)
alert.accept()

driver.quit()
