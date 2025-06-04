from pages.elements import WebElement


class BasePage:
    locators = {}

    def __init__(self, driver):
        self.driver = driver

    def item(self, xpath: str) -> WebElement:
        #xpath =  self.__getattribute__(element_name)# self.locators.get(name)
        msg = f"{self.__class__.__name__} has no xpath for element: , " + \
              f"may be typo? Exsist names is: {self.locators.keys()}"
        if xpath is None:
            raise AttributeError(msg)
        return WebElement(driver=self.driver, xpath=xpath)