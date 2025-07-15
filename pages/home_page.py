from locators import HomePageLocators
from pages import Header, BasePage
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


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
    
    def verify_category_titles_exist(self) -> bool:
        """
        Verifies that Women, Men, and Kids category links are present.
        """
        return all([
            self.is_element_present(self.locators.WOMEN_CATEGORY),
            self.is_element_present(self.locators.MEN_CATEGORY),
            self.is_element_present(self.locators.KIDS_CATEGORY)
        ])

    def randomly_expand_any_category(self) -> bool:
        """
        Randomly selects a category and verifies its subcategories show up.
        """
        category = random.choice(["Women", "Men", "Kids"])
        return self.expand_category_and_verify_menu(category)

    def click_carousel_control(self, direction: str):
        """Clicks the carousel control: 'right' or 'left'."""
        if direction == "right":
            control = self.locators.SLIDER_CAROUSEL_RIGHT
        elif direction == "left":
            control = self.locators.SLIDER_CAROUSEL_LEFT
        else:
            raise ValueError("Direction must be 'right' or 'left'")

        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(control)).click()
        self.wait(1.5)

    def scroll_carousel_twice_and_confirm(self) -> bool:
        """
        Clicks the right carousel arrow twice and confirms successful scroll.
        """

        # Wait until the carousel control is clickable
        control = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.locators.SLIDER_CAROUSEL)
        )

        # Scroll / click twice
        for _ in range(2):
            control.click()
            self.wait(1)     