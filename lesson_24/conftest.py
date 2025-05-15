import pytest
import requests
from requests.auth import HTTPBasicAuth

@pytest.fixture(scope="session") 
def auth_session():
    session = requests.Session()
    url = "http://127.0.0.1:8080/auth"
    auth = HTTPBasicAuth('test_user', 'test_pass')
    response = session.post(url, auth=auth)
    assert response.status_code == 200
    token = response.json()["access_token"]
    session.headers.update({"Authorization": f"Bearer {token}"})
    return session

# Визначення фікстури з допомогою декоратора @pytest.fixture
@pytest.fixture
def my_fix():
    # Ця частина коду буде виконана перед кожним тестом,
    # який використовує цю фікстуру
    data = {"key": "value"}
    yield data

@pytest.fixture(scope="function", autouse=True)
def my_printable_fixture(request):
    print(f"Test {request.node.name}")
    yield # test itself run
    print("Test end message")

@pytest.fixture(params=[1, 2, 3])
def my_fixture(request):
    param_value = request.param
    print(f"Setup with param value: {param_value}")
    return param_value * 2

# Параметризована фікстура
@pytest.fixture(params=[requests.get, requests.post])
def http_method(request):
    return request.param

@pytest.fixture(scope='class') # module
def prepare_database(): 
    print("Підготовка бази даних...")
    yield
    print("Очищення бази даних...")


@pytest.fixture(scope='module', autouse=True)
def prepare_config():
    print("Підготовка конфігурації...")
    yield
    print("Очищення конфігурації...")

@pytest.fixture(params=[(1, 2), (5, 5), (10, -5)])
def input_data(request):
    return request.param

@pytest.fixture
def prepare_data(request):
    data = request.param * 2
    return data