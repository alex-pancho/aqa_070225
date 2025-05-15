import pytest
import logging

logger = logging.getLogger(name)
logger.setLevel(logging.INFO)
handler = logging.FileHandler("test_search.log")
handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))
logger.addHandler(handler)



@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("brand", 3),
    ("year", None),
    ("engine_volume", 0),
    ("invalid_field", 5),
])
def test_get_cars(auth_session, sort_by, limit):
    url = "http://127.0.0.1:8080/cars"
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit is not None:
        params["limit"] = limit

    response = auth_session.get(url, params=params)
    logger.info(f"GET /cars?{params} - {response.status_code} - {response.text}")
    
    assert response.status_code == 200
    assert isinstance(response.json(), list)