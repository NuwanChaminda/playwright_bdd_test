
from pages.base_page import BasePage

class ProductPage(BasePage):

    RELATED_SECTION = "text=Similar"
    PRODUCT_CARD = "[data-testid='product-card']"

    def open_home(self, base_url):
        self.open(base_url)

    def related_section_visible(self):
        return self.is_visible(self.RELATED_SECTION)

    def related_products_count(self):
        return self.page.locator(self.PRODUCT_CARD).count()
