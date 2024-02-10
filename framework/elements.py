from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageElement:
    def __init__(self, browser: WebDriver, by, locator, timeout=2):
        self.browser = browser
        self.by = by
        self.locator = locator
        self.timeout = timeout

    @property
    def get_element(self):
        """Найти и получить элемент для дальнейшего взаимодействия с ним"""
        try:
            element = WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_element_located((self.by, self.locator))
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {self.locator} not found: {e}")
            return None

    def click(self):
        self.get_element.click()

    def send_keys(self, keys):
        self.get_element.send_keys(keys)

    @property
    def text(self):
        return self.get_element.text

    def get_attribute(self, value):
        return self.get_element.get_attribute(value)

    @property
    def get_elements(self) -> list:
        """Найти и получить список элементов для дальнейшего взаимодействия с ними"""
        try:
            elements = WebDriverWait(self.browser, self.timeout).until(
                EC.presence_of_all_elements_located((self.by, self.locator))
            )
            return elements
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Elements with locator locator not found: {e}")
            return []

    @property
    def is_element_present(self) -> bool:
        """Проверка на присутсвие элемента на странице"""
        try:
            WebDriverWait(self.browser, self.timeout, 1, TimeoutException).until(
                EC.presence_of_element_located((self.by, self.locator)))
        except TimeoutException:
            return False
        return True

    @property
    def is_not_element_present(self) -> bool:
        """Элемент не появляется на странице в течение заданного времени.
        Упадет, как только увидит искомый элемент. Не появился: успех, тест зеленый"""
        try:
            WebDriverWait(self.browser, self.timeout).until(EC.presence_of_element_located((self.by, self.locator)))
        except TimeoutException:
            return True
        return False

    @property
    def element_to_be_clickable(self):
        """Ждать пока элемент не станет кликабельным, получаем элемент для дальнейшего взаимодействия с ним"""
        try:
            element = WebDriverWait(self.browser, self.timeout).until(
                EC.element_to_be_clickable((self.by, self.locator))
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {self.locator} not found: {e}")
            return None

    @property
    def visibility_of_element_located(self):
        """Ждать пока элемент не станет видимый,
           получить элемент для дальнейшего взаимодействия с ним"""
        try:
            element = WebDriverWait(self.browser, self.timeout).until(
                EC.visibility_of_element_located((self.by, self.locator))
            )
            return element
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {self.locator} not found: {e}")
            return None

    def wait_for_text_in_element(self, text_: str | None = None) -> bool:
        """Ждать появления текста в элементе,
            на вход принимает локатор и текст"""
        try:
            WebDriverWait(self.browser, self.timeout).until(
                EC.text_to_be_present_in_element((self.by, self.locator), text_)
            )
            return True
        except TimeoutException:
            return False

    @property
    def execute_script_click(self) -> bool:
        """Ждать пока элемент не станет кликабельным и выполнить клик на нем при помощи JAVA SCRIPT"""
        try:
            element = WebDriverWait(self.browser, self.timeout).until(
                EC.element_to_be_clickable((self.by, self.locator))
            )
            self.browser.execute_script("arguments[0].click();", element)
            return True
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Element with locator {self.locator} not found: {e}")
            return False

    @property
    def is_disappeared(self) -> bool:
        """Проверить, что какой-то элемент исчезает.
         Будет ждать до тех пор, пока элемент не исчезнет."""
        try:
            WebDriverWait(self.browser, self.timeout, 1).until_not(
                EC.presence_of_element_located((self.by, self.locator)))
        except TimeoutException:
            return False
        return True

    @property
    def switch_to_last_window(self):
        """Переключиться на последнюю вкладку"""
        return self.browser.switch_to.window(self.browser.window_handles[-1])
