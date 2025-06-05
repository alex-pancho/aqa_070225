from get_browser import chrome
from np_tracking_page import NPTrackingPage
from lesson_27_ex import fill_input, clickable, click_element, exist_element


def test_np_tracking():
    driver = chrome(headless=False)
    try:
        page = NPTrackingPage(driver)
        exist_element(driver, page.input_ttn[1], time_for_wait=10)

        ttn = "20400000000000"
        fill_input(driver, page.input_ttn[1], ttn)

        assert clickable(driver, page.search_btn[1], time_for_wait=10)
        click_element(driver, page.search_btn[1])

        status_elem = exist_element(driver, page.status_block[1], time_for_wait=10)
        status_text = status_elem.text.strip()

        print(f"Статус для ТТН {ttn}: {status_text}")
        assert status_text != ""
        assert status_text == page.error_message_text
    finally:
        driver.quit()
