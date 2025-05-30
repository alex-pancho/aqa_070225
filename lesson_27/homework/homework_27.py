from browser import chrome
from np_tracking_page import TrackingPage
import pytest

@pytest.mark.parametrize("parcel_number, expected_result", [
    ("20710165506036", "Отримана"),
    ("20400448590006", "Видалено"),
    ("20400333590005", "Ми не знайшли посилку за таким номером"),
    ])
def test_np_tracking_received(parcel_number, expected_result):
    driver = chrome()
    url = "https://tracking.novaposhta.ua/#/uk"
    tracking_page = TrackingPage(driver, url )
    tracking_page.search_parcel_by_number(parcel_number)
    result = tracking_page.parcel_status()
    assert expected_result in result 
    driver.close()