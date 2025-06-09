import pytest
from homework_27 import track_number

@pytest.mark.parametrize("tracking_number,expected_status", [
    # Реальний номер та очікуваний статус
    ("20451163138077", "Отримана"),

])
def test_track_status(tracking_number, expected_status):
    status = track_number(tracking_number)
    assert expected_status.lower() in status.lower(), f"Очікувався статус '{expected_status}', але отримано '{status}'"
