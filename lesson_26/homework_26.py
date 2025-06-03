from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time


def init_driver():
    """Ініціалізація Selenium WebDriver."""
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    return webdriver.Chrome(options=options)


def verify_frame(driver, frame_id, input_id, secret_text):
    driver.switch_to.frame(frame_id)
    input_elem = driver.find_element(By.ID, input_id)
    input_elem.send_keys(secret_text)

    driver.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)
    alert = Alert(driver)
    alert_text = alert.text

    assert alert_text == "Верифікація пройшла успішно!", f"[{frame_id}] Невірне повідомлення: {alert_text}"
    alert.accept()

    driver.switch_to.default_content()


def test_verify_all_frames():
    driver = init_driver()
    try:
        driver.get("http://localhost:8000/dz.html")

        frames = [
            {"frame_id": "frame1", "input_id": "input1", "secret": "Frame1_Secret"},
            {"frame_id": "frame2", "input_id": "input2", "secret": "Frame2_Secret"}
        ]

        for frame in frames:
            verify_frame(
                driver,
                frame["frame_id"],
                frame["input_id"],
                frame["secret"]
            )
        print("Усі фрейми успішно верифіковані.")
    finally:
        driver.quit()


if __name__ == "__main__":
    test_verify_all_frames()
