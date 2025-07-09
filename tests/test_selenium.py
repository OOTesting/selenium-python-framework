from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pytest

@pytest.mark.selenium
def test_selenium():
    driver = webdriver.Chrome()
    driver.get("https://google.co.uk")
    driver.quit()