import pytest

from pages.careers_page import CareersPage
from pages.main_page import MainPage
from pages.links import YadroUrl


class TestYadroTopMenuMainPage:
    """Test the yardo-top-menu"""
    @pytest.mark.smoke
    def test_guest_should_see_vacancy_link(self, browser):
        page = MainPage(browser, YadroUrl.YADRO_MAIN_PAGE_LINK)
        page.open()
        page.should_be_careers_link()

    @pytest.mark.integration
    def test_guest_can_go_to_vacancy_page(self, browser):
        page = MainPage(browser, YadroUrl.YADRO_MAIN_PAGE_LINK)
        page.open()
        page.go_to_careers_page()
        careers_page = CareersPage(browser, browser.current_url)
        careers_page.should_be_careers_page()

