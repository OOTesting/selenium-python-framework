import pytest
import allure
from pages.home_page import HomePage
from pages.login import LoginPage
from utils.custom_logger import customLogger 

logger = customLogger()

@allure.feature("Login Page")
@allure.story("Validate the login page")
@allure.severity(allure.severity_level.NORMAL)

def test_login_page(browser, config):                               
    logger = customLogger()

    base_url = config["base_url"]
    path = "/login" 
    logger.info("Starting test: Access the login page")


    with allure.step("Open Login Page"):
        home_page = HomePage(driver=browser, base_url=config["base_url"])
        LoginPage.open(path=path)  # Navigate to the login page
        logger.info("Navigated to login page")

    with allure.step("Verify login page is opened"):
        assert LoginPage.is_opened(), "Login page opened successfully"

    with allure.step("Perform login with known credentials"):
        LoginPage.login("oorupabo+101@gmail.com", "Zcap21ab1973")
        logger.info("Logged into site")

    with allure.step("Assert logout button is visible"):
        assert LoginPage.find_clickable_element(
            LoginPage.locators.HEADER_BUTTON_LOGOUT
        ).is_displayed(), "Logout button not visible after login"
        logger.info("Verfiy Loggout button is shown")
