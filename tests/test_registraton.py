import allure
import pytest
from tests.base_case import BaseCase
from utils.user_importer import import_user
from locators.locators import BasePageLocators


@allure.suite("Smoke")
@allure.epic("Registration")
@allure.feature("Registration with email and password")

class TestRegistration(BaseCase):
    @allure.title("Create a registered user")
    @pytest.mark.parametrize(
        "user", import_user(file_name="tests/test_data/AE-1.xlsx")
    )
    def test_ae_1_valid_user_can_be_created(self, user_manager, user):
        # Arrange
        ...
        # Act
        self.home_page.open()
        self.home_page.click_header_button_login()
        self.login_page.signup(user)
        self.signup_page.create_account(user)
        self.account_created_page.click_button_continue()
        self.home_page.click_header_button_delete_account()
        # Assert
        assert self.account_deleted_page.is_account_deleted()

    @allure.title("Register User with existing email")
    @pytest.mark.parametrize(
        "user", import_user(file_name="tests/tests_data/AE-5.xlsx")
    )
    def test_ae_5_register_user_with_existing_email(self, user_manager, user):
        # Arrange
        user_manager.create_user(user)
        # Act
        self.home_page.open()
        self.home_page.click_header_button_login()
        self.login_page.signup(user)
        # Assert
        assert self.login_page.is_opened()