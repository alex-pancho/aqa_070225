from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


def verify_frames(url):
    """
    Open the specified URL, switch into each iframe, enter a secret text,
    click the "Verify" button, and check whether the resulting alert matches
    the expected success or failure message.

    Parameters:
        url (str): The URL of the main page containing two iframes.

    Test cases:
        - Frame1: correct secret → success alert
        - Frame2: incorrect secret → failure alert
    """
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        # Load the test page
        driver.get(url)

        # Define test cases with frame info, input IDs, test text, and expected alerts
        frames = [
            {
                "frame_id": "frame1",
                "input_id": "input1",
                "secret": "Frame1_Secret",
                "expected": "Верифікація пройшла успішно!"
            },
            {
                "frame_id": "frame2",
                "input_id": "input2",
                "secret": "Wrong_Secret",
                "expected": "Введено неправильний текст!"
            }
        ]

        for frame in frames:
            driver.switch_to.default_content()
            print(f"Trying to switch to frame: {frame['frame_id']}")
            wait.until(EC.presence_of_element_located((By.ID, frame["frame_id"])))
            driver.switch_to.frame(driver.find_element(By.ID, frame["frame_id"]))

            input_box = wait.until(EC.presence_of_element_located((By.ID, frame["input_id"])))
            input_box.clear()
            input_box.send_keys(frame["secret"])

            print(f"Clicking 'Перевірити' in {frame['frame_id']}")
            driver.find_element(By.TAG_NAME, "button").click()

            try:
                WebDriverWait(driver, 5).until(EC.alert_is_present())
                alert = Alert(driver)
                alert_text = alert.text
                alert.accept()

                if alert_text == frame["expected"]:
                    print(f"Test passed in {frame['frame_id']}")
                else:
                    print(f"Test failed in {frame['frame_id']} — Expected: '{frame['expected']}', Got: '{alert_text}'")

            except TimeoutException:
                print(f"Alert did not appear in {frame['frame_id']}")

            time.sleep(1)

    finally:
        driver.quit()


if __name__ == "__main__":
    verify_frames("http://localhost:8000/dz.html")
