import logging
import pytest
import requests
from requests.auth import HTTPBasicAuth


def setup_logger():
    """Налаштування логування в консоль та в файл"""
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler("search.log", encoding="utf-8")
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

logger = setup_logger()


@pytest.fixture(scope='class')
def auth_session():
    """Фікстура для авторизації — повертає сесію з токеном"""
    session = requests.Session()
    url = "http://127.0.0.1:8080/auth"
    auth = HTTPBasicAuth('test_user', 'test_pass')

    logger.info("HTTPBasicAuth - аутентифікація користувача")
    response = session.post(url, auth=auth)
    assert response.status_code == 200, f"Аутентифікація не успішна - {response.text}"

    access_token = response.json().get("access_token")
    assert access_token, "Токен відсутній у відповіді"

    session.headers.update({'Authorization': f'Bearer {access_token}'})
    logger.info("Авторизація успішна")
    return session


class TestCarSearchAPI:

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 6),
        ("year", 2),
        ("engine_volume", 3),
        ("brand", 9),
        ("year", 5),
        ("price", 30),
    ])
    def test_get_cars(self, auth_session, sort_by, limit):
        """Тест пошуку авто з параметрами sort_by та limit"""
        url = "http://127.0.0.1:8080/cars"
        params = {}

        if sort_by:
            params["sort_by"] = sort_by
        if limit:
            params["limit"] = limit

        logger.info(f"GET /cars?sort_by={sort_by}&limit={limit}")
        response = auth_session.get(url, params=params)

        logger.info(f"Статус відповіді запиту - {response.status_code}")
        assert response.status_code == 200, f"Запит має статус код - {response.text}"

        data = response.json()
        logger.info(f"Кількість результатів: {len(data)}")

        if limit:
            assert len(data) <= limit, f"Очікувалося {limit} результатів або менше, повернулося {len(data)}"
