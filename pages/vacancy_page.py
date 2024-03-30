from framework.base_page import BasePage
from framework.elements import PageElement
from framework.locators import VacancyPageLocators


class VacancyPage(BasePage):
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

