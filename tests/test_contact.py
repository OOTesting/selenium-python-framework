import pytest
import allure
from pages.contact_us import ContactUsPage
from pages.home_page import HomePage
from utils.custom_logger import customLogger 

logger = customLogger()

@allure.feature("Contact Us Page")
@allure.story("Validate home page title")
@allure.severity(allure.severity_level.NORMAL)
def test_contact_page_title(browser, config):                               
    logger = customLogger()

    base_url = config["base_url"]
    path = "/contact_us" 
    logger.info("Starting test: Validate contact us page")


    with allure.step("Open Contact Us Page"):
        contact_us_page = ContactUsPage(driver=browser, base_url=config["base_url"], open_on_init=False)
        contact_us_page.open(path=path)  # Navigate to the contact page
        logger.info("Navigated to Contact Us page")

    with allure.step("Verify Contact Us Page is opened"):
        assert contact_us_page.is_opened(), "Contact Us page did not open successfully"

    with allure.step("Fill Contact Form"):
        contact_us_page.fill_contact_form(
            name="John Doe",
            email="john.doe@example.com",
            message="This is a test message.",
            file_path=None  # or provide a valid file path if needed
        )
        logger.info("Contact form filled")

    with allure.step("Submit the form"):
        contact_us_page.click_submit_button()
        contact_us_page.accept_alert()
        logger.info("Form submitted and alert handled")

    with allure.step("Verify success message is displayed"):
        assert contact_us_page.is_message_sent(), "Success message was not displayed"
        logger.info("Success message confirmed")

