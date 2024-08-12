import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

""""
for running test in headed mode, can use below code
my_driver = webdriver.Chrome()

for running test in headless mode, can use below code
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
my_driver = webdriver.Chrome(options=chrome_options)
"""


# @pytest.fixture() # to run test based on browser name I give in config file @pytest.fixture(params=["chrome",
# "firefox"])  # to run all tests in browsers one by one, by giving parameters directly
@pytest.fixture()
def driver(request):
    # browser = request.param  # to run test parallely
    browser = request.config.getoption("--browser")  # to run test based on argument, I give in configuration

    print(f"Creating {browser} driver")

    if browser == "chrome":
        my_driver = webdriver.Chrome()
    # my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox()
    # my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        my_driver = webdriver.Edge()
    else:
        raise TypeError(f"expected 'chrome' or 'firefox or edge', but got {browser}")
    # my_driver.implicitly_wait(10)
    yield my_driver
    print(f"closing {browser} driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browser to execute tests (chrome or firefox or edge)"
    )
