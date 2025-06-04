import time
from selenium.common import exceptions as EXCEPT
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait

class WebElement:
    _locator = ('', '')
    _web_driver = None
    _page = None
    _timeout = 10
    _wait_after_click = False

    def __init__(self, timeout=10, wait_after_click=False, **kwargs):
        self._timeout = timeout
        self._wait_after_click = wait_after_click
        for by, locate in kwargs.items():
            if by == 'driver':
                self._web_driver = locate
            elif by == 'xpath':
                self._locator = (By.XPATH, locate)

    def find(self, timeout=None):
        timeout = timeout or self._timeout
        try:
            return WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_element_located(self._locator)
            )
        except (EXCEPT.WebDriverException, EXCEPT.JavascriptException):
            return None

    def wait_to_be_clickable(self, timeout=None, check_visibility=True):
        timeout = timeout or self._timeout
        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.element_to_be_clickable(self._locator)
            )
            if check_visibility:
                self.wait_until_not_visible(timeout)
            return element
        except:
            return None

    def is_clickable(self):
        return self.wait_to_be_clickable(timeout=0.1) is not None

    def is_presented(self):
        return self.find(timeout=0.1) is not None

    def is_visible(self):
        element = self.find(timeout=1)
        return element.is_displayed() if element else False

    def wait_until_not_visible(self, timeout=None):
        timeout = timeout or self._timeout
        try:
            element = WebDriverWait(self._web_driver, timeout).until(
                EC.visibility_of_element_located(self._locator)
            )
            if element:
                js = (
                    'return (!(arguments[0].offsetParent === null) && '
                    '!(window.getComputedStyle(arguments[0]) === "none") && '
                    'arguments[0].offsetWidth > 0 && arguments[0].offsetHeight > 0);'
                )
                visibility = self._web_driver.execute_script(js, element)
                iteration = 0
                while not visibility and iteration < 10:
                    time.sleep(0.5)
                    iteration += 1
                    visibility = self._web_driver.execute_script(js, element)
            return element
        except:
            return None

    def send_keys(self, keys, wait=0.5):
        keys = keys.replace('\n', '\ue007')
        element = self.find()
        if element:
            element.clear()
            element.send_keys(keys)
            time.sleep(wait)
        else:
            raise AttributeError(f'Element with locator {self._locator} not found')

    def get_text(self):
        element = self.find()
        return str(element.text) if element else ''

    def get_attribute(self, attr_name):
        element = self.find()
        return element.get_attribute(attr_name) if element else None

    def _set_value(self, web_driver, value, clear=True):
        element = self.find()
        if clear and element:
            element.clear()
        if element:
            element.send_keys(value)

    def click(self, hold_seconds=0, x_offset=1, y_offset=1):
        element = self.wait_to_be_clickable()
        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).pause(hold_seconds).click(on_element=element).perform()
            if self._wait_after_click:
                self._page.wait_page_loaded()
        else:
            raise AttributeError(f'Element with locator {self._locator} not found')

    def right_mouse_click(self, x_offset=0, y_offset=0, hold_seconds=0):
        element = self.wait_to_be_clickable()
        if element:
            action = ActionChains(self._web_driver)
            action.move_to_element_with_offset(element, x_offset, y_offset).pause(hold_seconds).context_click(on_element=element).perform()
        else:
            raise AttributeError(f'Element with locator {self._locator} not found')

    def highlight_and_make_screenshot(self, file_name='element.png'):
        element = self.find()
        if element:
            self._web_driver.execute_script("arguments[0].scrollIntoView();", element)
            self._web_driver.execute_script("arguments[0].style.border='3px solid red';", element)
            self._web_driver.save_screenshot(file_name)

    def scroll_to_element(self):
        element = self.find()
        if element:
            self._web_driver.execute_script("arguments[0].scrollIntoView();", element)

    def delete(self):
        element = self.find()
        if element:
            self._web_driver.execute_script("arguments[0].remove();", element)

    def select(self, text: str):
        select_element = self.find()
        if select_element:
            _select = Select(select_element)
            _select.select_by_visible_text(text)


class ManyWebElements(WebElement):
    def __getitem__(self, item):
        elements = self.find()
        return elements[item]

    def find(self, timeout=None):
        timeout = timeout or self._timeout
        try:
            return WebDriverWait(self._web_driver, timeout).until(
                EC.presence_of_all_elements_located(self._locator)
            )
        except:
            return []

    def _set_value(self, web_driver, value):
        raise NotImplementedError('This action is not applicable for the list of elements')

    def click(self, hold_seconds=0, x_offset=0, y_offset=0):
        raise NotImplementedError('This action is not applicable for the list of elements')

    def count(self):
        return len(self.find())

    def get_text(self):
        return [str(el.text) for el in self.find()]

    def get_attribute(self, attr_name):
        return [el.get_attribute(attr_name) for el in self.find()]

    def highlight_and_make_screenshot(self, file_name='element.png'):
        elements = self.find()
        for el in elements:
            self._web_driver.execute_script("arguments[0].scrollIntoView();", el)
            self._web_driver.execute_script("arguments[0].style.border='3px solid red'", el)
        self._web_driver.save_screenshot(file_name)
