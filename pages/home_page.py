from locators import HomePageLocators
from pages import Header, BasePage


class HomePage(Header, BasePage):
    path = "/"
    locators = HomePageLocators()
    """
    Checks for section HTML tag in home page and returns true or false
    """

    def open_page(self):
        self.open(self.path)

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.SLIDER_CAROUSEL)
