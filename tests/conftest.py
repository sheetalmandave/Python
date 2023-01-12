from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"

    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service("/home/sheetal/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        driver.get("https://magento.softwaretestingboard.com/")
        driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()