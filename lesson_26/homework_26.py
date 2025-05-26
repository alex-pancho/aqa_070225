import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

driver = webdriver.Firefox()
driver.get("http://localhost:8000/dz.html")

def check_alert(input_text, frame_id, expected_alert_text):
    try:
        driver.switch_to.frame(driver.find_element(By.ID, frame_id))
        
        input_field =  driver.find_element(By.XPATH, "//input")
        input_field.clear()
        input_field.send_keys(input_text)
        
        check_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Перев')]")
        check_button.click()
        time.sleep(1)

        alert = Alert(driver)
        alert_text = alert.text

        if alert_text== expected_alert_text:
          print(f'{frame_id}, TEST PASSED Actual: {alert_text}, Expected: {expected_alert_text} ')
        else: 
            print(f'{frame_id}, TEST FAILED Actual: {alert_text}, Expected: {expected_alert_text} ')
        alert.accept()
      
        driver.switch_to.default_content()
    except Exception as e:
        raise ValueError(f"incorrect frame id:, {e}")
    
if __name__ ==  "__main__":
    
    success_alert_text = "Верифікація пройшла успішно!"
    fail_alert_text = "Введено неправильний текст!"
    correct_input_1 = "Frame1_Secret"
    correct_input_2 = "Frame2_Secret"
    incorrect_input = "Frame"
    frame_1 = "frame1"
    frame_2 = "frame2"
    TestData=[[correct_input_1, frame_1, success_alert_text],
              [incorrect_input, frame_1, fail_alert_text],
              [correct_input_2, frame_2, success_alert_text],
              [incorrect_input, frame_2, fail_alert_text],
              [incorrect_input, frame_1, success_alert_text], #fail expected
              [correct_input_2, frame_2, fail_alert_text]] #fail expected

    for data_set in TestData:
        check_alert(*data_set)
    driver.quit()
    