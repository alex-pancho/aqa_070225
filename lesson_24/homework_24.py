import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

PORT = 8080
BASE_URL = f"http://127.0.0.1:{PORT}"

def setup_logger(name: str, log_file: str = 'test_search.log') -> logging.Logger:
    """Configures and returns a logger with both console and file handlers"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:  # Щоб уникнути дублювання хендлерів
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(log_file, encoding="utf8")

        console_handler.setLevel(logging.DEBUG)
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

# Створення логера через функцію
logger = setup_logger(__name__)

@pytest.fixture(scope="class")
def auth_session():
    """Fixture to create an authenticated session."""
    session = requests.Session()
    response = session.post(
        f"{BASE_URL}/auth",
        auth=HTTPBasicAuth("test_user", "test_pass")
    )
    assert response.status_code == 200, "Authorization failed"
    token = response.json()["access_token"]
    session.headers.update({"Authorization": f"Bearer {token}"})  # Додаємо токен у заголовки сесії
    return session # Повертаємо авторизовану сесію

@pytest.fixture(scope="class")
def params_fixture():
    """Fixture that returns parameters for GET requests"""
    return [
        ("price", 2),
        ("year", 3),
        ("engine_volume", 4),
        ("brand", 5),
        ("year", 6)
    ]

def test_get_cars(auth_session, params_fixture):
    """Test to get a list of cars using a GET request."""
    for sort_by, limit in params_fixture:
        logger.info(f"Test parameters: sort_by={sort_by}, limit={limit}")
        params = {"sort_by": sort_by, "limit": limit}

        response = auth_session.get(f"{BASE_URL}/cars", params=params)
        logger.info(f"Request URL: {response.url}")
        logger.info(f"Response status code: {response.status_code}")
        logger.info(f"Response text: {response.text}")

        assert response.status_code == 200, f"Failed to get response, received status code {response.status_code}"

        cars = response.json()

        if len(cars) > 1 and sort_by in cars[0]:
            values = [car.get(sort_by) for car in cars]
            sorted_values = sorted(values)
            assert values == sorted_values, f"Results are sorted by: {sort_by}"