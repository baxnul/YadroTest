from framework.base_page import BasePage
from framework.elements import PageElement
from framework.locators import MainPageLocators


class MainPage(BasePage):
    @property
    def careers_link(self) -> PageElement:
        return PageElement(self.browser, *MainPageLocators.CAREERS_LINK, timeout=10)

    def go_to_careers_page(self):
        self.careers_link.click()

