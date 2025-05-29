from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from homework_27_po import TrackParcel 

def test_receive_parcel_status(driver, track_link, parcel_number):
    """
    Verify the parcel tracking page correctly shows the status "Отримана" for a given parcel number.
    """
    driver.get(track_link)
    track_parcel_page = TrackParcel(driver)
    track_parcel_page.enter_parcel_number(parcel_number)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(track_parcel_page.search_button))
    track_parcel_page.click_search_button()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(track_parcel_page.parcel_status))
    actual_parcel_status = track_parcel_page.get_parcel_status()
    assert actual_parcel_status == "Отримана", f"Unexpected status received: {actual_parcel_status}"