class BasePageElements:
    pass


class BasePage(BasePageElements):
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        """Открыть ссылку"""
        self.browser.get(self.url)
