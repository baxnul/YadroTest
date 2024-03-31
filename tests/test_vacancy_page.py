import allure
import pytest

from framework.links import YadroUrl
from pages.vacancy_page import VacancyPage

search_field_text_list = ["Python Developer", "JavaScript", "Python"]
all_vacancy_index = [0, 9]


class TestVacancyPage:
    """Test class for testing vacancy page functionality"""

    @pytest.fixture(scope="function")
    def vacancy_page(self, browser) -> VacancyPage:
        """This fixture creates a VacancyPage object"""
        page = VacancyPage(browser, YadroUrl.YADRO_VACANCY_PAGE_LINK)
        page.open()
        return page

    @pytest.mark.smoke
    @pytest.mark.regress
    def test_guest_should_see_vacancy_page(self, vacancy_page):
        """This test checks if the object is correctly seen on the Vacancy page"""
        vacancy_page.should_be_vacancy_page()
        assert vacancy_page.select_tab.text == "Вакансии", "Vacancy tab is not displayed selected"

    @pytest.mark.functional
    @pytest.mark.regress
    @pytest.mark.parametrize('search_text', search_field_text_list)
    def test_guest_can_input_search_query_vacancy(self, vacancy_page, search_text):
        """guest can input search field, and this search field should be correct visible,
            and after guest should see correct vacancy name in vacancy list"""
        vacancy_page.input_search_field_text(search_text=search_text)
        vacancy_page.verify_vacancy_list(search_text=search_text)
        assert vacancy_page.search_field.get_attribute("value") == search_text, ("Text in Search field "
                                                                                 "is not correct visible")

    @pytest.mark.functional
    @pytest.mark.regress
    @pytest.mark.timeout(60)
    def test_pagination_button(self, vacancy_page):
        """guest can click pagination button, and should see added scope new vacancy,
            if vacancy ended, user shouldn't see pagination button"""
        vacancy_page.show_more_button_should_work()
        assert vacancy_page.show_more_button.is_element_present is False, ("Show more button should disappear when "
                                                                           "scrolling the page to the end")

    @pytest.mark.parametrize('vacancy_index', all_vacancy_index)
    @pytest.mark.integration
    @pytest.mark.regress
    @pytest.mark.timeout(60)
    def test_open_vacancy_page(self, vacancy_page, vacancy_index):
        """guest can open any vacancy index, and should see new page current vacancy,
            have description selected vacancy"""
        before_click_vacancy_title_text = vacancy_page.open_vacancy_by_index(vacancy_index=vacancy_index)
        after_click_vacancy_title_text = vacancy_page.get_vacancy_title_in_description()
        assert vacancy_page.is_description_form_present(), "Vacancy description form is not present"
        assert before_click_vacancy_title_text == after_click_vacancy_title_text, (
            "Vacancy title before click this index"
            " and title after open this vacancy are different")
