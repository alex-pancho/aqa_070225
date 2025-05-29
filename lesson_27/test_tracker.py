import sys
from pathlib import Path
import pytest

sys.path.append(str(Path(__file__).resolve().parent.parent))

from lesson_27.tracker_page import TrackerPage
from lesson_27.get_browser_2 import get_chrome

@pytest.fixture
def driver():
    """
    Pytest fixture that sets up and tears down the Chrome WebDriver.

    If `debug=True`, the browser will run in visible mode (not headless).
    After the test is completed, the driver is quit to close the browser.
    """
    driver = get_chrome(debug=True)  
    yield driver
    driver.quit()

def test_invalid_invoice_number_shows_error(driver):
    """
    Negative test case for tracking Nova Poshta parcel with an invalid invoice number.

    Steps:
    - Open the Nova Poshta tracking website
    - Enter a fake TTN number
    - Submit the form
    - Capture the displayed error message
    - Assert that the error message contains the expected phrase

    This test is useful when no real tracking number is available. It confirms
    that the site correctly handles invalid inputs.
    """
    tracker = TrackerPage(driver)
    tracker.open()

    fake_invoice = "12345678901234"  # Fake TTN number
    expected_phrase = "не знайшли посилку"  # Expected error text

    tracker.enter_invoice_number_and_submit(fake_invoice)
    message = tracker.get_status_text()

    print(f"Received message: {message}")
    assert expected_phrase in message.lower()
