import pytest 
import requests
import logging
from requests.auth import HTTPBasicAuth

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler('test_search.log')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)


logger.addHandler(file_handler)
logger.addHandler(file_handler)

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope='class')

def auth_session(request):
    session = requests.Session()

    auth_url = f"{BASE_URL}/auth"
    auth = HTTPBasicAuth('test_user', 'test_pass')

    response = session.post(auth_url, auth=auth)

    assert response.status_code == 200, "Authentication failed"

    token = response.json().get("access_token")
    assert token is not None, "Token not found in response"
    session.headers.update({'Authorization' : f'Bearer {token}'})

    request.cls.session = session

@pytest.mark.usefixtures("auth_session")
class TestCarSearch:
    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 3),
        ("year", 5),
        ("engine_volume", 2),
        ("brand", 4),
        ("price", 10),
        ("year", 1),
        ("engine_volume", 7)                    
    ])
    
    def test_car_search(self, sort_by, limit):
        url = f"{BASE_URL}/cars"
        params = {"sort_by": sort_by, "limit": limit}

        try:
            response = self.session.get(url, params=params)
        except requests.RequestException as e:
            logger.error(f"Error while making request to {url}: {e}")
            pytest.fail(f"RequestException: {e}")

        logger.info(f"GET /cars?sort_by={sort_by}&limit={limit}")
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response: {response.text}")

        if response.status_code != 200:
            logger.warning(f"Failed request with status code: {response.status_code}")
            pytest.fail(f"Expected status 200 but got {response.status_code}")

        data = response.json()
        assert isinstance(data, list), "Expected a list in response"
        assert len(data) <= limit, f"Received more records than limit={limit}"



if __name__ == "__main__":
    import sys
    import pytest
    sys.exit(pytest.main([__file__]))
    