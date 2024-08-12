import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Test_Exceptions:
    @pytest.mark.exceptions
    def test_no_such_element_exception(self, driver):
        # Open page
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")

        # Click Add button
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()

        # explicit wait Explicit waits are loops added to the code that poll the application for a specific condition
        # to evaluate as true before it exits the loop and continues to the next command in the code. If the
        # condition is not met before a designated timeout value, the code will give a timeout error.
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(
            ec.presence_of_element_located((By.XPATH, "(//div //input[@class='input-field'])[2]")))

        # Verify Row 2 input field is displayed
        # row_2_input_locator = driver.find_element(By.XPATH, ("(//div //input[@class='input-field'])[2]"))
        assert row_2_input_element.is_displayed(), "row 2 input should be displayed but its not"

    @pytest.mark.exceptions
    @pytest.mark.element_non_tracable
    def test_element_not_interacatable_exception(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-exceptions/")
        add_button_locator = driver.find_element(By.ID, "add_btn")
        add_button_locator.click()
        wait = WebDriverWait(driver, 10)
        row_2_input_element = wait.until(
            ec.presence_of_element_located((By.XPATH, "(//div //input[@class='input-field'])[2]")))
        row_2_input_element.send_keys("burger")
        time.sleep(10)  # to visibly check input sent
        driver.find_element(By.XPATH, "//div[@id='rows']/div[3]/div[@class='row']/button[@id='save_btn']").click()
        confirmation_message = driver.find_element(By.CSS_SELECTOR, "#confirmation")
        confirmation_message.is_displayed()
        assert confirmation_message.text == "Row 2 was saved"
