import time
from selenium.webdriver.common.by import By
import pytest


# for running test in headless mode, can use below code
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--disable-gpu")
# driver = webdriver.Chrome(options=chrome_options)


class TestNegativeScenarios:

    @pytest.mark.alltests
    @pytest.mark.login
    @pytest.mark.negativescenario
    @pytest.mark.parametrize("username, password, expected_error_message",
                             [("student", "incorrectPassword", "Your password is invalid!"),
                              ("wrong_username", "Password123", "Your username is invalid!")])
    def test_negative_login(self, driver, username, password, expected_error_message):
        driver.get("https://practicetestautomation.com/practice-test-login/")
        current_url = driver.current_url
        print("The current url is " + current_url)
        current_title = driver.title
        print("The current title is " + current_title)

        testLogin_locator = driver.find_element(By.CSS_SELECTOR, "#login h2")
        test_Login = testLogin_locator.text
        print(test_Login)

        assert current_url == "https://practicetestautomation.com/practice-test-login/"
        assert current_title == "Test Login | Practice Test Automation"
        assert test_Login == "Test login"

        # enter the username
        username_locator = driver.find_element(By.XPATH, "/html//input[@id='username']")
        username_locator.send_keys(username)
        time.sleep(2)

        # enter the password
        password_locator = driver.find_element(By.XPATH, "/html//input[@id='password']")
        password_locator.send_keys(password)
        time.sleep(2)

        # click on the submit button
        submit_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_locator.click()
        time.sleep(2)

        # validate the error message
        error_Message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        error_message = error_Message_locator.text
        assert error_message == expected_error_message
        time.sleep(2)

    print("----------PARAMETERIZED TEST ABOVE, SEPARATE THE SEGMENT------------")

    # @pytest.mark.alltests
    # @pytest.mark.login
    # @pytest.mark.negativescenario
    # @pytest.mark.negativepassword
    def test_negative_password(self, driver):  # case 1, correct username, incorrect password
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        current_url = driver.current_url
        print("The current url is " + current_url)
        current_title = driver.title
        print("The current title is " + current_title)

        testLogin_locator = driver.find_element(By.CSS_SELECTOR, "#login h2")
        test_Login = testLogin_locator.text  # get some content from page
        print(test_Login)

        assert current_url == "https://practicetestautomation.com/practice-test-login/"
        assert current_title == "Test Login | Practice Test Automation"
        assert test_Login == "Test login"

        # enter the correct username in username field
        username_locator = driver.find_element(By.XPATH, "/html//input[@id='username']")
        username_locator.send_keys("wrong_username")
        time.sleep(1)
        username_locator.clear()
        username_locator.send_keys("student")
        time.sleep(2)

        # enter the incorrect password in password field
        password_locator = driver.find_element(By.XPATH, "/html//input[@id='password']")
        password_locator.send_keys("Password123")
        time.sleep(2)
        password_locator.clear()
        time.sleep(1)
        password_locator.send_keys("incorrectPassword")
        time.sleep(2)

        # click on the submit button
        submit_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_locator.click()

        # validate the error message
        error_Message_locator = driver.find_element(By.XPATH, "//div[@id='error']")
        error_message = error_Message_locator.text
        assert error_message == "Your password is invalid!"
        time.sleep(2)

    # @pytest.mark.alltests
    # @pytest.mark.login
    # @pytest.mark.negativescenario
    # @pytest.mark.negativeusername
    def test_negative_username(self, driver):  # case 2, incorrect username, correct password
        driver.get("https://practicetestautomation.com/practice-test-login/")
        driver.maximize_window()
        current_url = driver.current_url
        print("The current url is " + current_url)
        current_title = driver.title
        print("The current title is " + current_title)

        testLogin_locator = driver.find_element(By.CSS_SELECTOR, "#login h2")
        test_Login = testLogin_locator.text  # get some content from page
        print(test_Login)

        assert current_url == "https://practicetestautomation.com/practice-test-login/"
        assert current_title == "Test Login | Practice Test Automation"
        assert test_Login == "Test login"

        # enter the correct incorrect username in username field
        username_locator = driver.find_element(By.XPATH, "/html//input[@id='username']")
        username_locator.send_keys("student")
        time.sleep(1)
        username_locator.clear()
        username_locator.send_keys("wrong_username")
        time.sleep(2)

        # enter the correct password in password field
        password_locator = driver.find_element(By.XPATH, "/html//input[@id='password']")
        password_locator.send_keys("wrong_password")
        time.sleep(2)
        password_locator.clear()
        time.sleep(1)
        password_locator.send_keys("Password123")
        time.sleep(2)

        # click on the submit button
        submit_locator = driver.find_element(By.XPATH, "/html//button[@id='submit']")
        submit_locator.click()

        # assert the error message
        assert driver.find_element(By.XPATH, "//div[@id='error']").is_displayed()
