import allure
from framework.base_page import BasePage
from framework.elements import PageElement
from framework.locators import VacancyPageLocators


class VacancyPageElements(BasePage):
    """This class have Page Elements for 'Vacancy Page'"""
    @property
    def breadcrumb_link(self) -> PageElement:
        return PageElement(self.browser, *VacancyPageLocators.BREADCRUMB_LINK)

    @property
    def select_tab(self) -> PageElement:
        return PageElement(self.browser, *VacancyPageLocators.SELECT_TAB)

    @property
    def search_field(self) -> PageElement:
        return PageElement(self.browser, *VacancyPageLocators.SEARCH_FIELD)

    @property
    def vac_search_button(self) -> PageElement:
        return PageElement(self.browser, *VacancyPageLocators.VAC_SEARCH_BUTTON)

    @property
    def vacancy_item(self) -> PageElement:
        return PageElement(self.browser, *VacancyPageLocators.VACANCY_ITEM)

    @property
    def vac_search_result_item_notice(self) -> PageElement:
        return PageElement(self.browser, *VacancyPageLocators.VAC_SEARCH_RESULT_ITEM_NOTICE)

    @property
    def show_more_button(self) -> PageElement:
        return PageElement(self.browser, *VacancyPageLocators.SHOW_MORE_BUTTON)

    @property
    def description_about_vacancy(self) -> PageElement:
        return PageElement(self.browser, *VacancyPageLocators.DESCRIPTION_ABOUT_VACANCY)

    @property
    def title_about_vacancy_in_description_vacancy_page(self) -> PageElement:
        return PageElement(self.browser, *VacancyPageLocators.TITLE_ABOUT_VACANCY_IN_DESCRIPTION_VACANCY_PAGE)


class VacancyPage(VacancyPageElements):
    """This class have Page Objects for 'Vacancy Page'"""
    def should_be_vacancy_page(self):
        self.should_be_vacancy_url()
        self.should_be_vacancy_breadcrumb_link()

    def should_be_vacancy_url(self):
        assert "vacancy" in self.browser.current_url, 'In URL ABSENT VACANCY word'

    def should_be_vacancy_breadcrumb_link(self):
        assert self.breadcrumb_link.is_element_present, "vacancy form is not presented breadcrumb link"

    def input_search_field_text(self, search_text: str):
        """Method to input text in the search field"""
        with allure.step(f"Input text in the search field {search_text}"):
            self.search_field.send_keys(search_text)

    def verify_vacancy_list(self, search_text: str):
        """Method to verify the vacancy list after searching"""
        with allure.step("Verify the vacancy list after searching"):
            search_button = self.vac_search_button.execute_script_click
            wait_new_list = self.vacancy_item.wait_for_text_in_element(text_=search_text)
            if wait_new_list:
                vacancy_list = self.vacancy_item.get_elements
                assert [vacancy.text.find(search_text) for vacancy in
                        vacancy_list], "guest should see correct search vac list"
            else:
                assert self.vac_search_result_item_notice.is_element_present is True, ("guest should see correct "
                                                                                       "search vacancy list")

    def show_more_button_should_work(self):
        """'Show more button' should be seen, while yet new more vacancies"""
        with allure.step("Show more button' should be seen, while yet new more vacancies"):
            show_more_button_present = self.show_more_button.is_element_present

            while show_more_button_present is True:
                self.show_more_button.click()
                show_more_button_present = self.show_more_button.is_element_present

    def open_vacancy_by_index(self, vacancy_index: int):
        """Open any vacancy by index and return vacancy title text before click vacancy index"""
        with allure.step(f"Open vacancy by index {vacancy_index} and return vacancy title text before click vacancy"):
            vacancy_list = self.vacancy_item.get_elements
            vacancy_title_text = vacancy_list[vacancy_index].text
            vacancy_list[vacancy_index].click()
            return vacancy_title_text

    def is_description_form_present(self):
        """Check if the vacancy description form is present"""
        return self.description_about_vacancy.is_element_present

    def get_vacancy_title_in_description(self):
        """Get the title of the vacancy on the description page"""
        with allure.step(f"Get the title of the vacancy on the description page"):
            return self.title_about_vacancy_in_description_vacancy_page.text