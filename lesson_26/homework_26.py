from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert

# Ініціалізація веб-драйвера
def init_driver():
    geckodriver_path = "/snap/bin/geckodriver"
    driver_service = webdriver.FirefoxService(executable_path=geckodriver_path)
    driver = webdriver.Firefox(service=driver_service)
    return driver

# Робота з веб-елементами і виконання дій на сторінці
def open_frame_and_input_pass(driver, frame: str, input_xpath:str, key: str, btn_xpath:str):
    driver.switch_to.frame(driver.find_element(By.ID, frame))
    input = driver.find_element(By.ID, input_xpath)
    input.send_keys(key)
    input_btn= driver.find_element(By.XPATH, btn_xpath)
    input_btn.click()
    alert = Alert(driver)
    if alert.text== "Верифікація пройшла успішно!":
        print("Було введено коректне секретне слово")
    else:
        print("Було введено неправильне секретне слово")
    alert.accept()
    driver.switch_to.default_content()

if __name__ == "__main__":
    driver=init_driver()
    driver.get("http://localhost:8000/dz.html")
    open_frame_and_input_pass(driver=driver, frame="frame1", input_xpath="input1", key="Frame1_Secret",
                                btn_xpath='//button[@onclick="verifyInput(\'input1\')"]')
    open_frame_and_input_pass(driver=driver, frame="frame2", input_xpath="input2", key="Frame2_Secret",
                                btn_xpath='//button[@onclick="verifyInput(\'input2\')"]')
    driver.quit()