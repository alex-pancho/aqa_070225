import pytest
from nova_poshta_tracker import NovaPoshtaTracker 

@pytest.fixture(scope="module")
def tracker():
    tracker_instance = NovaPoshtaTracker(headless=True) 
    yield tracker_instance
    tracker_instance.close_browser()

test_data = [
    ("12345678901230", "Номер не знайдено"),
    ("00000000000000", "Номер не знайдено"), 
]

@pytest.mark.parametrize("tracking_number, expected_status", test_data)
def test_package_status_with_helpers(tracker: NovaPoshtaTracker, tracking_number: str, expected_status: str):
    if "123124124124214Р" in tracking_number:
        pytest.skip("Будь ласка, замініть шаблонні дані на реальний номер накладної та очікуваний статус у 'test_data'.")

    print(f"\nТестування ТТН: {tracking_number}")
    actual_status = tracker.get_package_status(tracking_number)
    
    print(f"Очікуваний статус: '{expected_status}'")
    print(f"Отриманий статус:   '{actual_status}'")

    assert actual_status == expected_status, \
        f"Для ТТН '{tracking_number}' очікувався статус '{expected_status}', але отримано '{actual_status}'"
    