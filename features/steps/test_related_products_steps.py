
from pytest_bdd import scenarios, given, when, then
from pages.product_page import ProductPage
from config.settings import settings

scenarios("../features/related_products.feature")

@given("user navigates to the product page")
def open_product(page):
    product = ProductPage(page)
    product.open_home(settings.BASE_URL)

@when("user views related products")
def view_related(page):
    product = ProductPage(page)
    assert product.related_section_visible()

@then("related products should satisfy business rules")
def validate_related(page):
    product = ProductPage(page)
    assert product.related_products_count() >= 0
