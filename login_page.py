from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from Tests.conftest import driver
from page_objects.base_page import BasePage


class login_page(BasePage):
    __url = "https://practicetestautomation.com/practice-test-login/"
    __username_field = (By.XPATH, "/html//input[@id='username']")
    __password_field = (By.XPATH, "/html//input[@id='password']")
    __submit_field = (By.XPATH, "/html//button[@id='submit']")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)


    def open(self):
        super().open_url(self.__url)

    def execute_login(self, username: str, password: str):

        super()._type(self.__username_field, username)
        super()._type(self.__password_field, password)
        super()._click(self.__submit_field)



