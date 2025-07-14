# utils/webmanager.py

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

class WebManager:
    def __init__(self, browser: str = "chrome"):
        self.browser = browser.lower()
        self.driver = None

    def start_browser(self):
        if self.browser == "chrome":
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()),
                options=options
            )

        elif self.browser == "firefox":
            options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(
                service=FirefoxService(GeckoDriverManager().install()),
                options=options
            )
        else:
            raise ValueError(f"Unsupported browser: {self.browser}")
        
        return self.driver

    def stop_browser(self):
        if self.driver:
            self.driver.quit()
