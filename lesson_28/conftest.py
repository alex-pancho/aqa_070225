import pytest
from get_browser import firefox, chrome
from pages.home_page import HomePage
from pages.garage_page import GaragePage
from pages.registration_module import RegistrationModule

URL = "https://guest:welcome2qauto@qauto.forstudy.space"


@pytest.fixture(scope="module")
def driver():
    _driver = firefox()
    _driver.get(URL)
    yield _driver
    _driver.quit()


@pytest.fixture
def home_page(driver):
    return HomePage(driver)


@pytest.fixture
def garage_page(driver):
    return GaragePage(driver)


@pytest.fixture
def registration_module(driver):
    return RegistrationModule(driver)


@pytest.fixture
def registration_data():
    return {
        "name": "Vadym",
        "last_name": "Hello",
        "email": "example32@gmail.com",
        "password": "String123"
    }


@pytest.fixture
def registration_flow(home_page, registration_data, registration_module, garage_page):
    sign_up_button = home_page.item(home_page.sign_up_button)
    assert sign_up_button.is_clickable()
    sign_up_button.click()

    registration_module.item(registration_module.sign_up_name).send_keys(registration_data["name"])
    registration_module.item(registration_module.sign_up_last_name).send_keys(registration_data["last_name"])
    registration_module.item(registration_module.sign_up_email).send_keys(registration_data["email"])
    registration_module.item(registration_module.sign_up_password).send_keys(registration_data["password"])
    registration_module.item(registration_module.sign_up_repeat_password).send_keys(registration_data["password"])
    registration_module.item(registration_module.register_button).click()
    assert garage_page.item(garage_page.profile).is_visible()


@pytest.fixture
def delete_account(garage_page):
    yield
    print("Teardown: очищення ресурсу після тесту")
    garage_page.item(garage_page.settings).click()
    garage_page.item(garage_page.remove_account).scroll_to_element()
    garage_page.item(garage_page.remove_account).click()

    # garage_page.item(garage_page.remove_account).click()
    garage_page.item(garage_page.remove_confirm).click()
