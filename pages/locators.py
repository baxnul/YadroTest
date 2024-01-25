from selenium.webdriver.common.by import By

""" ALL LOCATOR have selector and locator
    Example: (Tuple have: By selector, locator)
    and some LOCATOR have timeout wait
    Example: (Tuple have: By selector, locator, timeout wait) """


class BasePageLocators:
    pass


class MainPageLocators:
    CAREERS_LINK = (By.CSS_SELECTOR, "[href='https://careers.yadro.com']")


class CareersPageLocators:
    WELCOME_SECTION = (By.CSS_SELECTOR, "[class='welcome__section d-flex']")
    CAREERS_NAV_MENU = (By.CSS_SELECTOR, "[class='navmenu__section _top']")
    MAIN_PAGE_LINK = (By.CSS_SELECTOR, "[imgfield='tn_img_1540301280185']")
    CAREERS_NAV_ITEM_VACANCY = (By.ID, "menu-item-16")


class VacancyPageLocators:
    SELECT_TAB = (By.CSS_SELECTOR, "[aria-current='page']")
    BREADCRUMB_LINK = (By.CSS_SELECTOR, "[class='breadcrumbs']")
    SEARCH_FIELD = (By.XPATH, "//div[@class='vac__search']//input")
    VACANCY_ITEM = (By.CLASS_NAME, "vac__result-item-title")
    VAC_SEARCH_BUTTON = (By.CLASS_NAME, "vac__search-btn")
    VAC_SEARCH_RESULT_ITEM_NOTICE = (By.CSS_SELECTOR, "[class='vac__result-item _notice']")
    SHOW_MORE_BUTTON = (By.XPATH, "//div[@class='vac__result-more']/button")