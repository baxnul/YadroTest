import pytest
from loguru import logger

from pages.careers_page import CareersPage
from pages.links import YadroUrl
from pages.vacancy_page import VacancyPage


class TestCareersPage:
    @pytest.mark.smoke
    def test_guest_should_see_careers_page(self, browser):
        page = CareersPage(browser, YadroUrl.YADRO_CAREERS_LINK)
        page.open()
        page.should_be_careers_page()

    @pytest.mark.integration
    def test_guest_can_go_to_vacancy_page(self, browser):
        page = CareersPage(browser, YadroUrl.YADRO_CAREERS_LINK)
        page.open()
        page.go_to_vacancy_page()
        vacancy_page = VacancyPage(browser, browser.current_url)
        vacancy_page.should_be_vacancy_page()
