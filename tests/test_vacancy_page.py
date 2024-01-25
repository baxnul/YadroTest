import time

import pytest

from pages.links import YadroUrl
from pages.vacancy_page import VacancyPage

search_field_text_list = ["Python Developer", "JavaScript", "Python"]
all_vacancy_index = [0, 9]


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

    @pytest.mark.functional
    def test_pagination_button(self, browser):
        """guest can click pagination button, and should see added scope new vacancy"""
        page = VacancyPage(browser, YadroUrl.YADRO_VACANCY_PAGE_LINK)
        page.open()
        page.show_more_button_should_work()

    @pytest.mark.parametrize('vacancy_index', all_vacancy_index)
    @pytest.mark.integration
    def test_open_vacancy_page(self, browser, vacancy_index):
        """guest can click any vacancy, and should see new page current vacancy, have description selected vacancy"""
        page = VacancyPage(browser, YadroUrl.YADRO_VACANCY_PAGE_LINK)
        page.open()
        page.open_any_vacancy_page(vacancy_index=vacancy_index)
