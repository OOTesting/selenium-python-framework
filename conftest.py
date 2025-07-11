# conftest.py
import pytest
from utils.driver_factory import get_driver

@pytest.fixture
def driver():
    driver = get_driver("chrome")  # or parameterize later
    yield driver
    driver.quit()
