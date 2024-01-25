from .base_page import BasePage
from .locators import VacancyPageLocators


class VacancyPage(BasePage):
    def should_be_vacancy_page(self):
        self.should_be_vacancy_url()
        self.should_be_vacancy_breadcrumb_link()

    def should_be_vacancy_url(self):
        assert "vacancy" in self.browser.current_url, 'In URL ABSENT VACANCY word'

    def should_be_vacancy_breadcrumb_link(self):
        assert self.is_element_present(
            *VacancyPageLocators.BREADCRUMB_LINK), "vacancy form is not presented breadcrumb link"

    def should_be_active_tab_vacancy(self):
        assert self.get_element(
            *VacancyPageLocators.SELECT_TAB).text == "Вакансии", "Vacancy tab is not displayed selected"

    def should_not_be_active_tab_internship(self):
        assert self.get_element(
            *VacancyPageLocators.SELECT_TAB).text != "Стажировка", "Vacancy tab is not displayed selected"

    def guest_can_input_search_field_text(self, search_text: str):
        """guest can input search field text, and after guest should see correct vacancy name in vacancy list"""
        search_field = self.get_element(*VacancyPageLocators.SEARCH_FIELD)
        search_field.send_keys(search_text)
        search_button = self.get_element(*VacancyPageLocators.VAC_SEARCH_BUTTON)
        search_button.click()
        assert search_field.get_attribute("value") == search_text, "Text in Search field is not correct visible"
        vacancy_list = self.get_elements(*VacancyPageLocators.VACANCY_ITEM)
        assert [vacancy.text.find(search_text) or self.is_element_present(
            *VacancyPageLocators.VAC_SEARCH_RESULT_ITEM_NOTICE) is True for vacancy in
                vacancy_list], "guest should see correct search vac list"

    def show_more_button_should_work(self):
        """Show more button should be seen, while yet new more vacancies"""
        show_more_button_present = self.is_element_present(*VacancyPageLocators.SHOW_MORE_BUTTON)

        while show_more_button_present is True:
            show_more_button = self.get_element(*VacancyPageLocators.SHOW_MORE_BUTTON)
            show_more_button.click()
            show_more_button_present = self.is_element_present(*VacancyPageLocators.SHOW_MORE_BUTTON)
