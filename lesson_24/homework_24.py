import pytest
import requests
from requests.auth import HTTPBasicAuth
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('test_search.log', mode='w')
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

BASE_URL = "http://127.0.0.1:8080"


@pytest.fixture(scope='class')
def auth_session():
    session = requests.Session()
    url = f'{BASE_URL}/auth'
    auth = HTTPBasicAuth('test_user', 'test_pass')

    response = session.post(url, auth=auth)
    assert response.status_code == 200, f"Auth failed: {response.text}"

    token = response.json().get('access_token')
    session.headers.update({'Authorization': f'Bearer {token}'})

    return session


# Параметри для тесту: sort_by і limit
test_data = [
    ("price", 3),
    ("year", 5),
    ("engine_volume", 2),
    ("brand", 4),
    ("price", 10),
    ("year", 1),
    ("brand", 6),
]


def get_cars(auth_session, sort_by=None, limit=None):
    params = {}
    if sort_by is not None:
        params["sort_by"] = sort_by
    if limit is not None:
        params["limit"] = limit

    url = f'{BASE_URL}/cars'
    logger.info(f"GET {url} | params={params}")
    response = auth_session.get(url, params=params)
    data = response.json()
    logger.info(f"Status Code: {response.status_code}")
    logger.info(f"Response: {data}")

    assert response.status_code == 200, f"Status code not 200: {response.status_code}"
    assert isinstance(data, list), "Response is not a list"
    return data


@pytest.mark.usefixtures("auth_session")
class TestCarSearch:

    def test_get_all_cars(self, auth_session):
        data = get_cars(auth_session)
        assert len(data) > 0

    @pytest.mark.parametrize("sort_by, limit", test_data)
    def test_sorting(self, auth_session, sort_by, limit):
        data = get_cars(auth_session, sort_by=sort_by)
        for i in range(len(data) - 1):
            assert data[i][sort_by] <= data[i + 1][sort_by], \
                f"{data[i][sort_by]} > {data[i + 1][sort_by]} at index {i}"

    @pytest.mark.parametrize("sort_by, limit", test_data)
    def test_limit(self, auth_session, sort_by, limit):
        data = get_cars(auth_session, limit=limit)
        assert len(data) <= limit, f"Got {len(data)} items, expected max {limit}"

    @pytest.mark.parametrize("sort_by, limit", test_data)
    def test_sort_and_limit(self, auth_session, sort_by, limit):
        data = get_cars(auth_session, sort_by=sort_by, limit=limit)
        for i in range(len(data) - 1):
            assert data[i][sort_by] <= data[i + 1][sort_by], \
                f"{data[i][sort_by]} > {data[i + 1][sort_by]} at index {i}"
        assert len(data) <= limit

    def test_negative_limit(self, auth_session):
        data = get_cars(auth_session, limit=-1)
        assert len(data) >= 0

    def test_invalid_sort_by(self, auth_session):
        data = get_cars(auth_session, sort_by="non_existing_field")
        assert len(data) >= 0
