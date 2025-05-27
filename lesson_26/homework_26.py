from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def verify_frame(driver, frame_id, input_id, secret_text):
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.ID, frame_id)))
    
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, input_id)))
    input_field = driver.find_element(By.ID, input_id)
    input_field.send_keys(secret_text)

    button_xpath = f"//button[@onclick=\"verifyInput('{input_id}')\"]"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
    driver.find_element(By.XPATH, button_xpath).click()

    WebDriverWait(driver, 10).until(EC.alert_is_present())
    alert = Alert(driver)
    alert_text = alert.text
    assert alert_text == "Верифікація пройшла успішно!", f"Unexpected alert text: {alert_text}"
    alert.accept()
    driver.switch_to.default_content()

if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.get("http://localhost:8000/dz.html")

    try:
        verify_frame(driver, "frame1", "input1", "Frame1_Secret")
        verify_frame(driver, "frame2", "input2", "Frame2_Secret")
    finally:
        driver.quit()





