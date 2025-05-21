import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

logger = logging.getLogger("car_search_test")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("test_search.log", mode="w")
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(console_handler)

@pytest.fixture(scope="class")
def authorized_session():
    session = requests.Session()     
    auth_url = "http://127.0.0.1:8080/auth"
    credentials = HTTPBasicAuth("test_user", "test_pass")
    
    logger.info("Sending authentication request...")    
    response = session.post(auth_url, auth=credentials)
        
    assert response.status_code == 200, "Auth failed"
    access_token = response.json()["access_token"]
        
    session.headers.update({'Authorization': f'Bearer {access_token}'})
    logger.info("Auth successful. Token added to headers.")

    yield session
    
    
class TestCarsSearch:

    @pytest.mark.parametrize("sort_by, limit", [
        ("price", 5),
        ("year", 3),
        ("engine_volume", 10),
    ])
    def test_search(self, authorized_session, sort_by, limit):
        url = f"http://127.0.0.1:8080/cars?sort_by={sort_by}&limit={limit}"
        logger.info(f"Sending GET request to: {url}")

        response = authorized_session.get(url)
        
        logger.info(f"Status code: {response.status_code}")
        logger.info(f"Response: {response.json()}")
        
        assert response.status_code == 200