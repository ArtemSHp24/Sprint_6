import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service

GECKO_PATH = r"C:\Users\User\Desktop\Drivers\geckodriver.exe"

@pytest.fixture(scope="function")
def driver():
    options = webdriver.FirefoxOptions()
    options.set_preference("dom.disable_open_during_load", False)

    service = Service(GECKO_PATH)
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

