
class ProductsPage:

    RELATED_SECTION = "section:has-text('Similar items')"
    PRODUCT_SEARCH = "//a[@class='s-card__link image-treatment']/img[@loading='eager']"
    PRODUCT_CARDS = "//a[@class='wwfl']"
    PRODUCT_TITLE = "h3, [role=heading]"
    PRODUCT_PRICE = "[class*=price]"
    PRODUCT_IMAGE = "img"
    BEST_SELLER_BADGE = ":has-text('Best Seller')"
    URL = "https://www.ebay.com/sch/i.html?_nkw=wallet+slim"

    def __init__(self, page):
        self.page = page

    def open_wallet_page(self):
        self.page.goto(self.URL)

    def related_section_visible(self):
        return self.page.locator(self.RELATED_SECTION).is_visible()

    def product_count(self):
        return self.page.locator(self.PRODUCT_CARDS).count()

    def titles(self):
        return self.page.locator(self.PRODUCT_TITLE)

    def prices(self):
        return self.page.locator(self.PRODUCT_PRICE)

    def images(self):
        return self.page.locator(self.PRODUCT_IMAGE)

    def links(self):
        return self.page.locator(self.PRODUCT_SEARCH)

    def click_first(self):
        self.links().first.click()

    def wait_for_products(self):
        self.page.wait_for_selector(self.PRODUCT_CARDS)

    def product_cards(self):
        return self.page.locator(self.PRODUCT_CARDS)

    def send_url(self):
        return self.URL
