"""Module providing a fixture."""
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
    def test_guest_should_see_careers_page(self, careers_page):
        """Guest should see careers page"""
        careers_page.should_be_careers_page()

    @pytest.mark.integration
    @pytest.mark.regress
    def test_guest_can_go_to_vacancy_page(self, careers_page, browser):
        """Guest can go to vacancy page"""
        careers_page.go_to_vacancy_page()
        vacancy_page = VacancyPage(browser, browser.current_url)
        assert vacancy_page.url == browser.current_url
        assert vacancy_page.breadcrumb_link.is_element_present, "vacancy form is not presented breadcrumb link"
