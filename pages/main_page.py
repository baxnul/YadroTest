from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_careers_page(self):
        careers_link = self.browser.find_element(*MainPageLocators.CAREERS_LINK)
        careers_link.click()

    def should_be_careers_link(self):
        assert self.is_element_present(*MainPageLocators.CAREERS_LINK), "Careers link is not presented"

