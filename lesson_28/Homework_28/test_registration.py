import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_registration(driver, go_to_registration, fill_registration_form, submit_form, check_success_alert, check_redirect_to_garage):
    go_to_registration()
    email = fill_registration_form()
    submit_form()

    alert_text = check_success_alert()
    if alert_text:
        assert "registration complete" in alert_text.lower(), "Registration alert not shown or incorrect"
    else:
        assert check_redirect_to_garage(), "No success alert and user was not redirected to garage"
