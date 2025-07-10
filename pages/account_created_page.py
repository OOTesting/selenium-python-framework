from locators import AccountCreatedPageLocators
from pages import BasePage, Header
from models.user import User


class AccountCreatedPage(Header, BasePage):
    path = "/account_created"
    locators = AccountCreatedPageLocators()

    def open_page(self):
        self.open(self.path)

    def is_account_created(self) -> bool:
        return self.is_element_present(self.locators.LABEL_ACCOUNT_CREATED)

    def click_button_continue(self):
        self.find_clickable_element(self.locators.BUTTON_CONTINUE).click()