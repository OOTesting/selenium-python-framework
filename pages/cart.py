from locators import ProductPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    path = "/view_cart"
    locators = ProductPageLocators()
    
    def open_page(self):
        self.open(self.path)

    def is_opened(self) -> bool:
        return self.is_element_present(self.locators.CART_LABEL)
