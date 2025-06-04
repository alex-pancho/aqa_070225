import time
import pytest
import random

def generate_test_email():
    return f"testuser_{random.randint(1000, 9999)}@example.com"


def test_user_registration(open_registration, fill_registration_form, get_success_toast):
    email = generate_test_email()
    fill_registration_form("Тест", "Тестовий", email, "Qwerty123!")
    message = get_success_toast()

    assert "Registration was successful" in message
