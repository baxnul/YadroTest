import pytest
from loguru import logger

from pages.links import YadroUrl
from pages.vacancy_page import VacancyPage


class TestVacancyPage:
    @pytest.mark.smoke
    @logger.catch()
    def test_guest_should_see_vacancy_page(self, browser):
        page = VacancyPage(browser, YadroUrl.YADRO_CAREERS_LINK)
        page.open()
        page.should_be_vacancy_page()


