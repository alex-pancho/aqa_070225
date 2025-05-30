from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

def verify_frame(driver, frame_id, input_id, secret_text):
    # Switch to the frame by ID
    driver.switch_to.frame(driver.find_element(By.ID, frame_id))

    # Find the input field and enter the secret text
    input_field = driver.find_element(By.ID, input_id)
    input_field.clear()
    input_field.send_keys(secret_text)

    # Click the "Verify" button
    driver.find_element(By.TAG_NAME, "button").click()

    # Wait for the alert to appear
    time.sleep(1)
    alert = driver.switch_to.alert

    # Read the alert text
    alert_text = alert.text
    print(f"[{frame_id}] Alert text: {alert_text}")

    # Check if verification was successful
    if "успішно" in alert_text:
        print(f"[{frame_id}] ✅ Verification successful")
    else:
        print(f"[{frame_id}] ❌ Verification failed")

    # Close the alert
    alert.accept()

    # Switch back to the main page
    driver.switch_to.default_content()

def main():
    # Start the browser
    driver = webdriver.Chrome()

    # Open the main HTML page with frames
    driver.get("http://localhost:8000/dz.html")

    # Frame IDs, input field IDs, and secret values
    frames_data = [
        ("frame1", "input1", "Frame1_Secret"),
        ("frame2", "input2", "Frame2_Secret")
    ]

    # Loop through each frame and verify
    for frame_id, input_id, secret in frames_data:
        verify_frame(driver, frame_id, input_id, secret)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    main()