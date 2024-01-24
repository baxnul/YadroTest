from selenium.common.exceptions import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Открыть ссылку"""
        self.browser.get(self.url)

    def get_element(self, by, locator, timeout=10):
        """Найти и получить элемент для дальнейшего взаимодействия с ним"""
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((by, locator))
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {locator} not found: {e}")
            return None

    def get_elements(self, by, locator, timeout=10) -> list:
        """Найти и получить список элементов для дальнейшего взаимодействия с ними"""
        try:
            elements = WebDriverWait(self.browser, timeout).until(
                EC.presence_of_all_elements_located((by, locator))
            )
            return elements
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Elements with locator locator not found: {e}")
            return []

    def is_element_present(self, by, locator, timeout=4) -> bool:
        """Проверка на присутсвие элемента на странице"""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return False
        return True

    def is_not_element_present(self, by, locator, timeout=4) -> bool:
        """Элемент не появляется на странице в течение заданного времени.
        Упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый"""
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return True
        return False

    def element_to_be_clickable(self, by, locator, timeout=10):
        """Ждать пока элемент не станет кликабельным, получаем элемент для дальнейшего взаимодействия с ним"""
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {locator} not found: {e}")
            return None

    def visibility_of_element_located(self, by, locator, timeout=10):
        """Ждать пока элемент не станет видимый,
           получить элемент для дальнейшего взаимодействия с ним"""
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.visibility_of_element_located((by, locator))
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {locator} not found: {e}")
            return None

    def wait_for_text_in_element(self, by, locator, text_, timeout=10) -> bool:
        """Ждать появления текста в элементе,
            на вход принимает локатор и текст"""
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.text_to_be_present_in_element((by, locator), text_)
            )
            return True
        except TimeoutException:
            return False

    def execute_script_click(self, by, locator, timeout=10) -> bool:
        """Ждать пока элемент не станет кликабельным и выполнить клик на нем при помощи JAVA SCRIPT"""
        try:
            element = WebDriverWait(self.browser, timeout).until(
                EC.element_to_be_clickable((by, locator))
            )
            self.browser.execute_script("arguments[0].click();", element)
            return True
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {locator} not found: {e}")
            return False

    def is_disappeared(self, by, locator, timeout=4) -> bool:
        """Проверить, что какой-то элемент исчезает.
         Будет ждать до тех пор, пока элемент не исчезнет."""
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(
                EC.presence_of_element_located((by, locator)))
        except TimeoutException:
            return False
        return True

    def switch_to_last_window(self):
        """Переключиться на последнюю вкладку"""
        return self.browser.switch_to.window(self.browser.window_handles[-1])
