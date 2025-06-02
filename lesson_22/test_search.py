import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logger = logging.getLogger("car_search_logger")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("test_search.log", mode='w', encoding='utf-8')
console_handler = logging.StreamHandler()

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def auth_session():
    session = requests.Session()
    auth_data = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(f"{BASE_URL}/auth", auth=auth_data)

    assert response.status_code == 200, "Помилка автентифікації"
    token = response.json().get("access_token")
    assert token, "Не отримано токен"

    session.headers.update({"Authorization": f"Bearer {token}"})
    return session


@pytest.mark.parametrize("sort_by,limit", [
    ("price", 5),
    ("year", 3),
    ("engine_volume", 10),
    ("brand", 7),
    ("price", 15),
    ("year", None),
    (None, 8),
])
def test_car_search(auth_session, sort_by, limit):
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit is not None:
        params["limit"] = limit

    response = auth_session.get(f"{BASE_URL}/cars", params=params)
    logger.info(f"GET /cars params={params} => Status {response.status_code}")

    assert response.status_code == 200
    cars = response.json()
    logger.info(f"Received {len(cars)} cars")
    assert isinstance(cars, list)
    if limit is not None:
        assert len(cars) <= limit
