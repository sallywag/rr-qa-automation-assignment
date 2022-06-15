from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException


class ElementHandler:
    """Utility class for getting and interacting with page elements."""

    def __init__(self, driver: WebDriver, timeout: int = 5):
        self._wait = WebDriverWait(driver, timeout)

    def get_element(self, css_selector: str) -> WebElement:
        return self._wait.until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, css_selector)
            )
        )

    def send_keys_to_element(self, css_selector: str, keys: str) -> None:
        element = self.get_element(css_selector)
        element.clear()
        element.send_keys(keys)

    def click_element(self, css_selector: str) -> None:
        element = self._wait.until(
            expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()

    def get_text_from_element(self, css_selector: str) -> str:
        element = self.get_element(css_selector)
        return element.text

    def select_value_from_element(self, css_selector: str, value: str) -> None:
        Select(self.get_element(css_selector)).select_by_value(value)

    def get_value_from_element(self, css_selector: str) -> None:
        return self.get_element(css_selector).get_attribute("value")

    def wait_for_timeout(self) -> None:
        try:
            self.get_element("#i-do-not-exist")
        except TimeoutException:
            pass
