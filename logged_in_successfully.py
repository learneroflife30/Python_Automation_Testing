from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class LoggedInSuccessfully:
    __url = "https://practicetestautomation.com/logged-in-successfully/"
    __successfully_message_locator = (By.CSS_SELECTOR, ".post-header")
    __logout_locator = (By.LINK_TEXT, "Log out")

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def expected_url(self) -> str:
        return self._url

    def get_header(self) -> str:
        self._driver.find_element(self.__successfully_message_locator).text

    def is_logout_button_dislpayed(self) -> bool:
        self._driver.find_element(self.__logout_locator).is_displayed()
