import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

@pytest.fixture(scope="session")
def auth_session():
    session = requests.Session()
    url = "http://127.0.0.1:8080/auth"
    auth = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(url, auth=auth)
    assert response.status_code == 200, "Authorization failed"
    token = response.json()["access_token"]
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

@pytest.fixture(scope="session")
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.DEBUG)

    if not logger.handlers:
        
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)
        
        file_handler = logging.FileHandler("test_search.log", mode='w', encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger
