import pytest
from nova_poshta_tracker import NovaPoshtaTracker

@pytest.fixture(scope="module")
def tracker():
    """Фікстура для ініціалізації трекера з автоматичним закриттям браузера."""
    instance = NovaPoshtaTracker(headless=True)
    yield instance
    instance.close_browser()


# Тестові дані: (номер накладної, очікуваний статус)
test_data = [
    ("12345678901230", "Номер не знайдено"),
    ("00000000000000", "Номер не знайдено"),
]


@pytest.mark.parametrize("tracking_number, expected_status", test_data)
def test_get_package_status(tracker: NovaPoshtaTracker, tracking_number: str, expected_status: str):
    print(f"\n🔍 Перевірка ТТН: {tracking_number}")
    actual_status = tracker.get_package_status(tracking_number)

    print(f"✅ Очікуваний статус: '{expected_status}'")
    print(f"📦 Отриманий статус:  '{actual_status}'")

    assert actual_status == expected_status, (
        f"❌ Помилка: для ТТН '{tracking_number}' очікувався статус '{expected_status}', але отримано '{actual_status}'"
    )
