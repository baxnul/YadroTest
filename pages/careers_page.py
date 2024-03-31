from framework.locators import CareersPageLocators

from framework.base_page import BasePage
from framework.elements import PageElement


class CareersPageElements(BasePage):
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


class CareersPage(CareersPageElements):
    def should_be_careers_page(self):
        """Should be on the main page"""
        self.should_be_careers_url()
        self.should_be_careers_welcome_section()
        self.should_be_careers_nav_menu()
        self.should_be_main_page_link()
        self.should_be_vacancy_link()

    def should_be_careers_url(self):
        """URL should have text 'careers'"""
        assert "careers" in self.browser.current_url, 'In URL ABSENT CAREERS word'

    def should_be_careers_welcome_section(self):
        """should be 'welcome message section'"""
        assert self.welcome_section.is_element_present, 'Welcome message section not displayed'

    def should_be_careers_nav_menu(self):
        """should be 'nav' menu on presented"""
        assert self.careers_nav_menu.is_element_present, "careers page nav_menu is not presented"

    def should_be_main_page_link(self):
        """should be main page link"""
        assert self.main_page_link.is_element_present is True, "main page link note found"

    def should_be_vacancy_link(self):
        """should be 'vacancy' button in Nav Menu"""
        assert self.careers_nav_item_vacancy.is_element_present, "Vacancy button in Nav Menu is not presented"

    def go_to_vacancy_page(self):
        """click on vacancy button on Nav Menu"""
        self.careers_nav_item_vacancy.click()