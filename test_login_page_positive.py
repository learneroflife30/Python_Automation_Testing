import time
from selenium.webdriver.common.by import By
import pytest


class TestPositiveScenarios:
    @pytest.mark.alltests
    @pytest.mark.login
    @pytest.mark.positive
    def test_positive_login(self, driver):
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.delete_all_cookies()
        driver.maximize_window()
        current_url = driver.current_url
        print(current_url)
        current_title = driver.title
        print(current_title)

        testLogin_locator = driver.find_element(By.CSS_SELECTOR, "#login h2")
        test_Login = testLogin_locator.text  # get some content from page
        print(test_Login)

        assert current_url == "https://practicetestautomation.com/practice-test-login/"
        assert current_title == "Test Login | Practice Test Automation"
        assert test_Login == "Test login"

        # enter the username in username field
        username_locator = driver.find_element(By.XPATH, "/html//input[@id='username']")
        username_locator.send_keys("incorrect password", )
        time.sleep(1)
        username_locator.clear()
        username_locator.send_keys("student")
        time.sleep(2)

        # enter the password in password field
        password_locator = driver.find_element(By.XPATH, "/html//input[@id='password']")
        password_locator.send_keys("incorrect password")
        time.sleep(2)
        password_locator.clear()
        time.sleep(1)
        password_locator.send_keys("Password123")
        time.sleep(2)

        # click on the submit button
        submit_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_locator.click()
        time.sleep(2)

        # verify the new page is desired page
        # 1. get url and assert it
        # assertEqual(a, b), assert driver.title == "Example Domain", Asserts that `a` is equal to `b`.
        actual_url = driver.current_url
        assert actual_url == "https://practicetestautomation.com/logged-in-successfully/"

        # 2. get logged in successfully message text
        logged_in_successfully = driver.find_element(By.CSS_SELECTOR, ".post-header")
        actual_text = logged_in_successfully.text
        assert actual_text == "Logged In Successfully"

        # 3. successful message
        congratulationsMessage_locator = driver.find_element(By.CSS_SELECTOR, ".has-text-align-center")
        congratulationsMessage = congratulationsMessage_locator.text
        print(congratulationsMessage)

        # 4. get log out button
        logout_selector = driver.find_element(By.LINK_TEXT, "Log out")
        assert logout_selector.is_displayed()

        time.sleep(1)

        driver.quit()
