from .base_page import BasePage
from .locators import CareersPageLocators


class CareersPage(BasePage):
    def should_be_careers_page(self):
        self.should_be_careers_url()
        self.should_be_careers_welcome_section()
        self.should_be_careers_nav_menu()
        self.should_be_main_page_link()
        self.should_be_vacancy_link()

    def should_be_careers_url(self):
        assert "careers" in self.browser.current_url, 'In URL ABSENT CAREERS word'

    def should_be_careers_welcome_section(self):
        """should be 'welcome message section'"""
        self.is_element_present(*CareersPageLocators.WELCOME_SECTION), 'Welcome message section not displayed'

    def should_be_careers_nav_menu(self):
        """should be 'nav' menu on presented"""
        assert self.is_element_present(*CareersPageLocators.CAREERS_NAV_MENU), "careers page nav_menu is not presented"

    def should_be_main_page_link(self):
        assert self.is_element_present(*CareersPageLocators.MAIN_PAGE_LINK)

    def should_be_vacancy_link(self):
        """should be 'vacancy' button in Nav Menu"""
        assert self.is_element_present(
            *CareersPageLocators.CAREERS_NAV_ITEM_VACANCY), "Vacancy button in Nav Menu is not presented"

    def go_to_vacancy_page(self):
        """click on vacancy button on Nav Menu"""
        careers_link = self.browser.find_element(*CareersPageLocators.CAREERS_NAV_ITEM_VACANCY)
        careers_link.click()
