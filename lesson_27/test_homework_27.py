from get_browser_chrome import chrome
from np_page_homework_27 import NovaPoshtaTrackingPage
from lesson_27_ex import fill_input, clickable, click_element, exist_element


def test_np_tracking(ttn="20411111111111"):
    driver = chrome(headless=False)
    try:
        page = NovaPoshtaTrackingPage(driver)
        exist_element(driver, page.input_ttn_number[1], time_for_wait=5)

        fill_input(driver, page.input_ttn_number[1], ttn)

        assert clickable(driver, page.search_btn[1], time_for_wait=5)
        click_element(driver, page.search_btn[1])

        status_elem = exist_element(driver, page.status_block[1], time_for_wait=5)
        status_text = status_elem.text.strip()

        print(f"Статус для ТТН {ttn}: {status_text}")
        assert status_text == page.error_message_text
    finally:
        driver.quit()
