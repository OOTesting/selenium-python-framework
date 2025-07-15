import pytest
import allure
from pages.home_page import HomePage
from utils.custom_logger import customLogger 

logger = customLogger()

@allure.feature("Home Page")
@allure.story("Validate home page title")
@allure.severity(allure.severity_level.NORMAL)
def test_home_page_title(browser, config):

    logger = customLogger()

    base_url = config["base_url"]
    path = "/" 
    logger.info("Starting test: test_home_page_title")

    with allure.step("Open Home Page"):
        home_page = HomePage(driver=browser, base_url=config["base_url"])
        home_page.open()
        logger.info(f"Navigated to {config['base_url']}")

    with allure.step("Validate page title contains 'Automation Exercise'"):
        actual_title = browser.title
        logger.debug(f"Actual title received: {actual_title}")
        assert "Automation Exercise" in actual_title, f"Expected title to contain 'Automation Exercise' but got '{actual_title}'"

    with allure.step("Validate scrolling in home page"):
        assert home_page.scroll_carousel_twice_and_confirm()
        logger.info(f"Scrolling through home page")

    with allure.step("Attach final screenshot"):
        try:
            allure.attach(
                browser.get_screenshot_as_png(),
                name="Final Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            logger.info("Screenshot attached to Allure report.")
        except Exception as e:
            logger.warning(f"Failed to attach screenshot: {str(e)}")

    logger.info("Completed test: test_home_page_title")
