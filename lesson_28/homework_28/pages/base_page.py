import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait as Wait


class BasePage:

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    # ************************************* ACTION WITH OPEN PAGE *****************************************************

    def open_page(self, url: str) -> None:
        """
            Opens a webpage by a specified URL.

            This method opens the browser and navigates to the given URL.

            Args:
              url (str): The URL of the page to open.
        """
        with allure.step(f'\nOpen the browser and get by URL: {url}'):
            return self.driver.get(url)

    # **************************************** ACTIONS WITH FINED *****************************************************

    def find_element_(self, locator: tuple):
        """
            Finds a web element using the specified locator.

            Args:
              locator (tuple): The locator tuple to find the element.

            Returns:
              WebElement: The first web element that matches the locator.
        """
        return self.driver.find_element(*locator)

    def find_elements_(self, locator: tuple):
        """
              Finds multiple web elements using the specified locator.

              Args:
                locator (tuple): The locator tuple to find the elements.

              Returns:
                list: A list of web elements matching the locator.
        """

        return self.driver.find_elements(*locator)

    def find_element_text_(self, locator: tuple):
        """
            Retrieves the text of a web element.

            This method finds a web element by its locator and extracts its text.

            Args:
            locator (tuple): The locator tuple of the element.

            Returns:
            str: The text content of the element.
        """

        return self.find_element_(locator).text

    def get_attribute_(self, locator: tuple, value):
        """
            Retrieves a specific attribute from a web element.

            This method finds a web element and returns the value of the specified attribute.

            Args:
            locator (tuple): The locator tuple of the element.
            value (str): The attribute name to retrieve.

            Returns:
            str: The value of the specified attribute.
        """

        return self.find_element_(locator).get_attribute(value)

    # ************************************* ACTIONS WITH ELEMENTS *****************************************************

    def send_keys_(self, locator, text: [str, int], hide=False) -> [tuple, str, int]:
        """
            Sends text input to a web element.

            This method finds an element and sends the provided text. If `hide` is True, the text input
            is logged as '*****' for security purposes.

            Args:
            locator (tuple): The locator of the element.
            text ([str, int]): The text or number to input.
            hide (bool): Whether to hide the input in the logs (default: False).

            Returns:
            None
        """
        if hide:

            return self.find_element_(locator).send_keys(text)
        else:

            return self.find_element_(locator).send_keys(text)

    def clear_field_(self, locator):
        """
            Clears the input field of a web element.

            This method clears any text or input present in the located element.

            Args:
            locator (tuple): The locator of the element.

            Returns:
            None
        """

        return self.find_element_(locator).clear()

    # ***************************************** ACTIONS WITH CLICKED **************************************************

    def click_btn_(self, locator):
        """
            Clicks on a web element.

            This method finds the element using the provided locator and performs a click action.

            Args:
            locator (tuple): The locator of the element.

            Returns:
            None
        """
        return self.find_element_(locator).click()

    def click_on_js_(self, locator: tuple):
        """
            Clicks on a web element using JavaScript.

            This method executes a JavaScript click action on the located web element.

            Args:
            locator (tuple): The locator of the element.

            Returns:
            None
        """

        return self.driver.execute_script("arguments[0].click();", self.find_element_(locator))

    # ***************************************** WAIT ELEMENTS *********************************************************

    def wait_presence_of_el_located(self, time_: int, locator: tuple):
        """
            Waits for an element to be present in the DOM.

            This method waits until the specified element is present within the DOM for the given time.

            Args:
            time_ (int): The maximum time to wait in seconds.
            locator (tuple): The locator of the element.

            Returns:
            WebElement: The element once it is present.
        """

        return Wait(self.driver, time_).until(EC.presence_of_element_located(locator))

    def wait_visible_of_el_located(self, time_: int, locator: tuple):
        """
            Waits for an element to be visible on the page.

            This method waits until the specified element is visible within the given time.

            Args:
            time_ (int): The maximum time to wait in seconds.
            locator (tuple): The locator of the element.

            Returns:
            WebElement: The element once it is visible.
        """

        return Wait(self.driver, time_).until(EC.visibility_of_element_located(locator))

    def actions_chains_move_click(self, move_to: tuple, click_to=None):
        """
            Moves the mouse to one element and clicks on another.

            This method uses action chains to move the mouse to the `move_to` element and optionally clicks the `click_to` element.

            Args:
            move_to (tuple): The locator of the element to move to.
            click_to (tuple, optional): The locator of the element to click on.

            Returns:
            None
        """
        action = ActionChains(self.driver)
        move_element = self.find_element_(move_to)
        action.move_to_element(move_element)
        clickable_element = self.find_element_(click_to)
        action.click(clickable_element)
        action.perform()


