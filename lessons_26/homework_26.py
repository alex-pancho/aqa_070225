from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def verify_frames(url):
    driver = webdriver.Chrome()

    try:
        driver.get(url)

        frames_info = [
            {"frame_id": "frame1", "input_id": "input1", "secret": "Frame1_Secret"},
            {"frame_id": "frame2", "input_id": "input2", "secret": "Frame2_Secret"},
        ]

        for frame in frames_info:
            driver.switch_to.default_content()
            driver.switch_to.frame(driver.find_element(By.ID, frame["frame_id"]))

            input_element = driver.find_element(By.ID, frame["input_id"])
            input_element.clear()
            input_element.send_keys(frame["secret"])

            driver.find_element(By.TAG_NAME, "button").click()

            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())
                alert = Alert(driver)
                alert_text = alert.text
                print(f"[{frame['frame_id']}] Alert: {alert_text}")

                expected_text = "Верифікація пройшла успішно!"
                assert alert_text == expected_text, f"❌ Невірний alert у {frame['frame_id']}"

                alert.accept()

            except TimeoutException:
                print(f"Alert не з’явився у {frame['frame_id']}")

        print("Усі фрейми пройдено успішно.")

    finally:
        driver.quit()


if __name__ == "__main__":
    verify_frames("http://localhost:8000/dz.html")
