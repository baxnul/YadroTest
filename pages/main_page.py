from framework.base_page import BasePage
from framework.elements import PageElement
from framework.locators import MainPageLocators


class MainPageElements(BasePage):
    @property
    def careers_link(self) -> PageElement:
        return PageElement(self.browser, *MainPageLocators.CAREERS_LINK, timeout=10)


class MainPage(MainPageElements):
    def go_to_careers_page(self):
        self.careers_link.click()