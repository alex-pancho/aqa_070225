def test_register_user (main_page, log_in_form, registration_form, garage_page, name, last_name, email, password):
    main_page.open_login_form()
    log_in_form.open_register_form()
    registration_form.fill_in_name_field(name)
    registration_form.fill_in_last_name_field(last_name)
    registration_form.fill_in_email_field(email)
    registration_form.fill_in_password_field(password)
    registration_form.fill_in_reenter_password_field(password)
    register_button = registration_form.item(registration_form.REGISTER_BUTTON[1])
    assert register_button.is_clickable(), "'Register' button is not clickable, check entered data" 
    registration_form.click_register_button()
    confirmation_pop_up = garage_page.item(garage_page.REGISTRATION_CONFIRMATION[1])
    assert confirmation_pop_up.is_visible(), "User is not registered"
    confirmation_pop_up.highlight_and_make_screenshot("registration_confirmation.png")