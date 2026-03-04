
class BasePage:

    def __init__(self, page):
        self.page = page

    def open(self, url):
        self.page.goto(url)

    def click(self, locator):
        self.page.locator(locator).click()

    def is_visible(self, locator):
        return self.page.locator(locator).first.is_visible()

    def get_text(self, locator):
        return self.page.locator(locator).inner_text()
