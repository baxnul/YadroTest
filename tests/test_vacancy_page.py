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
    def test_guest_should_see_vacancy_page(self, vacancy_page, browser):
        """This test checks if the object is correctly seen on the Vacancy page"""
        assert "vacancy" in browser.current_url, 'In URL ABSENT VACANCY word'
        assert vacancy_page.breadcrumb_link.is_element_present, "vacancy form is not presented breadcrumb link"
        assert vacancy_page.select_tab.text == "Вакансии", "Vacancy tab is not displayed selected"

    @pytest.mark.functional
    @pytest.mark.regress
    @pytest.mark.parametrize('search_text', search_field_text_list)
    def test_guest_can_input_search_query_vacancy(self, vacancy_page, search_text):
        """guest can input search field, and this search field should be correct visible,
            and after guest should see correct vacancy name in vacancy list"""
        with allure.step(f"Input text in the search field {search_text}"):
            vacancy_page.search_field.send_keys(search_text)

        with allure.step("Verify the vacancy list after searching"):
            search_button = vacancy_page.vac_search_button.execute_script_click
            wait_new_list = vacancy_page.vacancy_item.wait_for_text_in_element(text_=search_text)
            if wait_new_list:
                vacancy_list = vacancy_page.vacancy_item.get_elements
                assert [vacancy.text.find(search_text) for vacancy in
                        vacancy_list], "guest should see correct search vac list"
            else:
                assert vacancy_page.vac_search_result_item_notice.is_element_present is True, (
                    "guest should see correct "
                    "search vacancy list")

        assert vacancy_page.search_field.get_attribute("value") == search_text, ("Text in Search field "
                                                                                 "is not correct visible")

    @pytest.mark.functional
    @pytest.mark.regress
    @pytest.mark.timeout(60)
    def test_pagination_button(self, vacancy_page):
        """guest can click pagination button, and should see added scope new vacancy,
            if vacancy ended, user shouldn't see pagination button"""
        show_more_button_present = vacancy_page.show_more_button.is_element_present

        with allure.step("Show more button' should be seen, while yet new more vacancies"):
            while show_more_button_present is True:
                vacancy_page.show_more_button.click()
                show_more_button_present = vacancy_page.show_more_button.is_element_present

        assert vacancy_page.show_more_button.is_element_present is False, ("Show more button should disappear when "
                                                                           "scrolling the page to the end")

    @pytest.mark.parametrize('vacancy_index', all_vacancy_index)
    @pytest.mark.integration
    @pytest.mark.regress
    @pytest.mark.timeout(60)
    def test_open_vacancy_page(self, vacancy_page, vacancy_index):
        """guest can open any vacancy index, and should see new page current vacancy,
            have description selected vacancy"""
        with allure.step(f"Open vacancy by index {vacancy_index} and return vacancy title text before click vacancy"):
            vacancy_list = vacancy_page.vacancy_item.get_elements
            before_click_vacancy_title_text = vacancy_list[vacancy_index].text

        vacancy_list[vacancy_index].click()

        with allure.step(f"Get the title of the vacancy on the description page"):
            after_click_vacancy_title_text = vacancy_page.title_about_vacancy_in_description_vacancy_page.text

        assert vacancy_page.description_about_vacancy.is_element_present, "Vacancy description form is not present"
        assert before_click_vacancy_title_text == after_click_vacancy_title_text, (
            "Vacancy title before click this index"
            " and title after open this vacancy are different")
