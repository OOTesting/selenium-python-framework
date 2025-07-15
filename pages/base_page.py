from typing import Optional, Tuple, List
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from locators import BasePageLocators


class BasePage:
    driver: WebDriver
    locators = BasePageLocators()
    wait_timeout = 5

    def __init__(
        self,
        driver: WebDriver,
        base_url: str,
        url: Optional[str] = None,
        open_on_init: bool = False,
    ):
        self.driver = driver
        self.base_url = base_url
        self.actions = ActionChains(driver)

        self.url = url if url else self.base_url

        if open_on_init:
            self.open()

    def open(self, path: str = ""):
        self.driver.get(self.base_url + path)

    def wait(self, timeout: int = None) -> WebDriverWait:
        if timeout is None:
            timeout = self.wait_timeout
        return WebDriverWait(driver=self.driver, timeout=timeout)

    def find_element(self, locator: Tuple[str, str], timeout: int = None) -> WebElement:
        return self.wait(timeout=timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator: Tuple[str, str], timeout: int = None) -> List[WebElement]:
        return self.wait(timeout=timeout).until(EC.presence_of_all_elements_located(locator))

    def find_alert(self, timeout: int = None):
        return self.wait(timeout=timeout).until(EC.alert_is_present())

    def find_clickable_element(self, locator: Tuple[str, str], timeout: int = None) -> WebElement:
        return self.wait(timeout=timeout).until(EC.element_to_be_clickable(locator))

    def find_visible_element(self, locator: Tuple[str, str], timeout: int = None) -> WebElement:
        return self.wait(timeout=timeout).until(EC.visibility_of_element_located(locator))

    def is_alert_present(self, timeout: int = None):
        try:
            self.find_alert(timeout=timeout)
        except TimeoutException:
            return False
        return True

    def is_element_present(self, locator: Tuple[str, str], timeout: int = None) -> bool:
        try:
            self.find_element(locator=locator, timeout=timeout)
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, locator: Tuple[str, str], timeout: int = None) -> bool:
        try:
            self.find_element(locator=locator, timeout=timeout)
        except TimeoutException:
            return True
        return False

    def get_item_location(self, locator: Tuple[str, str], timeout: int = None) -> dict:
        element = self.find_element(locator=locator, timeout=timeout)
        return element.location
