import pytest

from pages.careers_page import CareersPage
from pages.main_page import MainPage
from framework.links import YadroUrl


class TestYadroTopMenuMainPage:
    """Test the yardo-top-menu"""

    @pytest.fixture(scope="function")
    def main_page(self, browser) -> MainPage:
        """This fixture creates a MainPage object"""
        page = MainPage(browser, YadroUrl.YADRO_MAIN_PAGE_LINK)
        page.open()
        return page

    @pytest.mark.smoke
    @pytest.mark.regress
    def test_guest_should_see_vacancy_link(self, main_page):
        assert main_page.careers_link.is_element_present, "Careers link is not presented"

    @pytest.mark.integration
    @pytest.mark.regress
    def test_guest_can_go_to_vacancy_page(self, main_page, browser):
        main_page.careers_link.click()
        careers_page = CareersPage(browser, browser.current_url)
        assert "careers" in careers_page.url, "URL should have text 'careers'"
        assert careers_page.careers_nav_menu.is_element_present, "careers page nav_menu is not presented"
