import uuid
from time import sleep


def test_registration(home_page, registration_page):
    unique_email = f"test_{uuid.uuid4().hex[:3]}@mail.com"
    password = "P@Ssw)rD223445"

    # 1. Клік на кнопку Sign up
    assert home_page.find_element_(home_page.sign_in_button).is_displayed()
    home_page.click_btn_(home_page.sign_in_button)

    # 2. Перевірка та заповнення полів
    # ----------- Name -------------
    name_el = home_page.find_element_(registration_page.name_input)
    assert name_el.is_displayed()
    assert name_el.is_enabled()
    home_page.clear_field_(registration_page.name_input)
    home_page.send_keys_(registration_page.name_input, "John")
    assert name_el.get_attribute("value") == "John"

    # ----------- Last name -------------
    last_name_el = home_page.find_element_(registration_page.last_name_input)
    assert last_name_el.is_displayed()
    assert last_name_el.is_enabled()
    home_page.clear_field_(registration_page.last_name_input)
    home_page.send_keys_(registration_page.last_name_input, "Doe")
    assert last_name_el.get_attribute("value") == "Doe"

    # ----------- Email -------------
    email_el = home_page.find_element_(registration_page.email_input)
    assert email_el.is_displayed()
    assert email_el.is_enabled()
    home_page.clear_field_(registration_page.email_input)
    home_page.send_keys_(registration_page.email_input, unique_email)
    assert email_el.get_attribute("value") == unique_email

    # ----------- Password -------------
    password_el = home_page.find_element_(registration_page.password_input)
    assert password_el.is_displayed()
    assert password_el.is_enabled()
    home_page.clear_field_(registration_page.password_input)
    home_page.send_keys_(registration_page.password_input, password)
    assert password_el.get_attribute("value") == password

    # ----------- Repeat Password -------------
    re_enter_password_input = home_page.find_element_(registration_page.re_enter_password_input)
    assert re_enter_password_input.is_displayed()
    assert re_enter_password_input.is_enabled()
    home_page.clear_field_(registration_page.re_enter_password_input)
    sleep(1)
    home_page.send_keys_(registration_page.re_enter_password_input, password)
    assert re_enter_password_input.get_attribute("value") == password

    #  Натискаємо "Register"
    register_button = home_page.find_element_(registration_page.register_button)
    assert register_button.is_displayed()
    assert register_button.is_enabled()
    home_page.click_btn_(registration_page.register_button)
    sleep(2)
    user_profile = home_page.find_element_text_(registration_page.title)
    assert user_profile == "Garage"
