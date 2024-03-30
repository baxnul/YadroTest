import pytest

from pages.careers_page import CareersPage
from framework.links import YadroUrl
from pages.vacancy_page import VacancyPage


class TestCareersPage:
    """This class for test in Careers Page"""

    @pytest.fixture(scope="function")
    def careers_page(self, browser) -> CareersPage:
        """This fixture creates a CareersPage object"""
        page = CareersPage(browser, YadroUrl.YADRO_CAREERS_LINK)
        page.open()
        return page

    @pytest.mark.smoke
    @pytest.mark.regress
    def test_guest_should_see_careers_page(self, browser, careers_page):
        """Guest should see careers page"""
        assert "careers" in browser.current_url, 'In URL ABSENT CAREERS word'
        assert careers_page.welcome_section.is_element_present, 'Welcome message section not displayed'
        assert careers_page.careers_nav_menu.is_element_present, "careers page nav_menu is not presented"
        assert careers_page.main_page_link.is_element_present is True, "main page link note found"
        assert careers_page.careers_nav_item_vacancy.is_element_present, "Vacancy button in Nav Menu is not presented"

    @pytest.mark.integration
    @pytest.mark.regress
    def test_guest_can_go_to_vacancy_page(self, careers_page, browser):
        """Guest can go to vacancy page"""
        careers_page.careers_nav_item_vacancy.click()
        vacancy_page = VacancyPage(browser, browser.current_url)
        assert vacancy_page.url == browser.current_url
        assert vacancy_page.breadcrumb_link.is_element_present, "vacancy form is not presented breadcrumb link"
