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
        assert self.get_element(*VacancyPageLocators.SELECT_TAB)
