"""
This file contains automated tests for the /cars endpoint of the Flask app.
It includes:
- Valid requests with different parameters
- Negative tests for invalid 'limit' values
Logging is enabled to test_search.log and to console.
Tests can be run directly using: `python test_cars_hw24.py` or `pytest`.
"""

import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth
import sys  # Needed for sys.exit in __main__

# ─────────────────────────────────────────────
# Setup Logging Function
# ─────────────────────────────────────────────
def setup_logger():
    """
    Configures logging to both console and a UTF-8 encoded file.
    """
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

    file_handler = logging.FileHandler('test_search.log', mode='w', encoding='utf-8')
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)

    return logger

# Initialize logger
logger = setup_logger()

# Base URL for the Flask app
BASE_URL = "http://127.0.0.1:8080"

# ─────────────────────────────────────────────
# Fixture: Authenticated session
# ─────────────────────────────────────────────
@pytest.fixture(scope="class")
def authenticated_session():
    """
    Creates and returns a session authenticated via /auth endpoint.
    Adds the bearer token to the session headers for all following requests.
    """
    session = requests.Session()
    auth_url = f"{BASE_URL}/auth"
    credentials = HTTPBasicAuth('test_user', 'test_pass')

    logger.info("Sending authentication request using HTTPBasicAuth")
    response = session.post(auth_url, auth=credentials)
    logger.info(f"Auth response status: {response.status_code}")

    assert response.status_code == 200, "Authentication failed"

    token = response.json().get("access_token")
    assert token, "Access token was not returned"
    logger.info("Authentication successful and token received")

    session.headers.update({'Authorization': f'Bearer {token}'})
    return session

# ─────────────────────────────────────────────
# Parametrized test class for /cars endpoint
# ─────────────────────────────────────────────
@pytest.mark.parametrize("sort_by, limit", [
    ("price", 3),
    ("year", 5),
    ("brand", 2),
    ("engine_volume", 4),
    ("price", 10),
    ("year", 1),
    ("brand", 6),
])
class TestCarSearch:
    """
    Tests the /cars endpoint with various sort_by and limit parameters.
    Validates response status, format, and item count.
    """

    def test_search_cars(self, authenticated_session, sort_by, limit):
        """
        Sends a GET request to /cars with given parameters.
        Checks that response is successful, a list is returned, and
        that the number of items does not exceed the limit.
        """
        url = f"{BASE_URL}/cars"
        params = {"sort_by": sort_by, "limit": limit}

        logger.info(f"Testing /cars?sort_by={sort_by}&limit={limit}")
        response = authenticated_session.get(url, params=params)
        logger.info(f"Response status: {response.status_code}")

        assert response.status_code == 200, f"Request failed: {params}"

        data = response.json()
        logger.info(f"Cars returned: {len(data)}")

        # Check response format and count
        assert isinstance(data, list)
        assert len(data) <= limit

# ─────────────────────────────────────────────
# Extra: Testing invalid limit values
# Negative test: checks how API handles bad 'limit' values.
# In most cases, we expect 400 (Bad Request) or 200 (graceful handling).
# But if we get 500, it means the backend doesn't handle input validation well.
# The test fails correctly when we see a 500 status – it's a real issue on the server.
# ─────────────────────────────────────────────

@pytest.mark.parametrize("bad_limit", [-1, 0, "ten", None])
def test_invalid_limit(authenticated_session, bad_limit):
    """
    My negative test: I wanted to check how the API reacts to bad 'limit' values.
    These could be negative numbers, zero, strings or even None.
    I expect the server to either return 400 (Bad Request) or ignore it and respond 200.
    """
    url = f"{BASE_URL}/cars"
    params = {"sort_by": "price", "limit": bad_limit}

    logger.info(f"Negative test with invalid limit={bad_limit}")
    response = authenticated_session.get(url, params=params)
    logger.info(f"Response status: {response.status_code}")

    # Server should return either 200 (graceful handling) or 400 (input validation error)
    assert response.status_code in (200, 400)

# ─────────────────────────────────────────────
# Manual execution support
# ─────────────────────────────────────────────
if __name__ == "__main__":
    """
    Allows the test to be run directly with `python test_cars_hw24.py`.
    This executes pytest programmatically with verbosity level 2.
    """
    sys.exit(pytest.main(["--verbosity=2", __file__]))

