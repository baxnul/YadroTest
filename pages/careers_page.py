from framework.locators import CareersPageLocators

from framework.base_page import BasePage
from framework.elements import PageElement


class CareersPage(BasePage):
    """This class have page elements for 'Careers Page'"""

    @property
    def welcome_section(self) -> PageElement:
        return PageElement(self.browser, *CareersPageLocators.WELCOME_SECTION)

    @property
    def careers_nav_menu(self) -> PageElement:
        return PageElement(self.browser, *CareersPageLocators.CAREERS_NAV_MENU)

    @property
    def main_page_link(self) -> PageElement:
        return PageElement(self.browser, *CareersPageLocators.MAIN_PAGE_LINK)

    @property
    def careers_nav_item_vacancy(self) -> PageElement:
        return PageElement(self.browser, *CareersPageLocators.CAREERS_NAV_ITEM_VACANCY)
