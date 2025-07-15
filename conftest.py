# conftest.py
import pytest
import allure
from utils.webmanager import WebManager

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to use: chrome or firefox")

@pytest.fixture(scope="session")
def config(pytestconfig):
    return {
        "browser": pytestconfig.getoption("browser"),
        "base_url": "https://automationexercise.com"
    }

@pytest.fixture(scope="function")
def browser(config):
    wm = WebManager(browser=config["browser"])
    driver = wm.start_browser()
    yield driver
    # On test teardown
    try:
        allure.attach(driver.get_screenshot_as_png(), name="screenshot", attachment_type=allure.attachment_type.PNG)
    except Exception:
        pass  # Ignore if driver crashed
    wm.stop_browser()
