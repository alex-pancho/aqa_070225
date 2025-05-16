import pytest

@pytest.mark.parametrize("sort_by, limit", [
    ("price", 5),
    ("brand", 3),
    ("year", None),
    ("engine_volume", 0),
    ("invalid_field", 5),
])
def test_get_cars(auth_session, logger, sort_by, limit):
    url = "http://127.0.0.1:8080/cars"
    params = {}
    if sort_by:
        params["sort_by"] = sort_by
    if limit is not None:
        params["limit"] = limit

    response = auth_session.get(url, params=params)

    logger.info(f"GET /cars?{params} - Status: {response.status_code}")
    logger.debug(f"Response text: {response.text}")

    assert response.status_code == 200
    cars = response.json()
    assert isinstance(cars, list)

    
    if cars and sort_by and sort_by in cars[0]:
        values = [car.get(sort_by) for car in cars]
        sorted_values = sorted(values)
        assert values == sorted_values, f"Cars are not sorted by {sort_by}"

    
    if limit and limit > 0:
        assert len(cars) <= limit, f"Returned more than {limit} cars"