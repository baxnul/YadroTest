import time

import pytest

from pages.links import YadroUrl
from pages.vacancy_page import VacancyPage

search_field_text_list = ["Python Developer", "JavaScript", "Python"]


class TestVacancyPage:
    @pytest.mark.smoke
    def test_guest_should_see_vacancy_page(self, browser):
        page = VacancyPage(browser, YadroUrl.YADRO_VACANCY_PAGE_LINK)
        page.open()
        page.should_be_vacancy_page()
        page.should_be_active_tab_vacancy()
        page.should_not_be_active_tab_internship()

    @pytest.mark.functional
    @pytest.mark.parametrize('text', search_field_text_list)
    def test_guest_can_input_search_query_vacancy(self, browser, text):
        """guest can input search field, and this search field should be correct visible,
            and after guest should see correct vacancy name in vacancy list"""
        page = VacancyPage(browser, YadroUrl.YADRO_VACANCY_PAGE_LINK)
        page.open()
        page.guest_can_input_search_field_text(search_text=text)
