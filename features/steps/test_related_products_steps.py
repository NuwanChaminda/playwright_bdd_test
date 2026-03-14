
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import sync_playwright
from pages.related_products_page import RelatedProductsPage
from pages.products_page import ProductsPage
import allure
import time
import pytest

scenarios("../related_products.feature")

@given("user opens wallet search page")
def open_page(page):
    ProductsPage(page).open_wallet_page()

@when("related products are visible", target_fixture="new_page")
def wait_products(page):
    page.wait_for_selector("a[href*='/itm/']")
    p = ProductsPage(page)
    with page.context.expect_page() as new_page_event:
        p.click_first()
    new_page = new_page_event.value
    new_page.wait_for_load_state("domcontentloaded")
    return new_page



@then(parsers.parse("validate testcase {tc:d}"))
def validate_tc(new_page,get_start_time,tc):
    rp = RelatedProductsPage(new_page)
    with allure.step(f"Validate TC-{tc:03d}"):

        if tc == 1:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            assert rp.related_section_visible()

        elif tc == 2:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            title = new_page.locator("//h2[@class='busU']")
            assert "Similar items" in title.inner_text()

        elif tc == 3:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            assert rp.product_count() <= 6

        elif tc == 4:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            assert rp.product_count() == 6

        elif tc == 5:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            assert new_page.locator(":has-text('Out of stock')").count() == 0

        elif tc == 6:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            labels = new_page.locator("//a[@class='wwfl']").all()
            aria_labels = [el.get_attribute("aria-label") for el in labels]
            assert all(label and "wallet" in label.lower() for label in aria_labels)

        # elif tc == 7:
        #     assert rp.product_count() > 0

        elif tc == 8:
            links = rp.links().all()
            hrefs = [l.get_attribute("href") for l in links]
            assert len(hrefs) == len(set(hrefs))

        elif tc == 9:
            links = rp.links().all()
            hrefs = [l.get_attribute("href") for l in links]
            assert len(hrefs) == len(set(hrefs))

        elif tc == 10:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            # get main product price
            main_price_text = new_page.locator("//div[@data-testid='x-price-primary']//span").first.inner_text()

            main_price = float(main_price_text.replace("US $", "").replace("$", "").strip())

            # calculate ±20% range
            min_price = main_price * 0.8
            max_price = main_price * 1.2

            # get similar product prices
            similar_prices = new_page.locator("//div[@class='aQ4i']//span")

            values = []

            for i in range(similar_prices.count()):
                price_text = similar_prices.nth(i).inner_text()

                price_value = float(price_text.replace("$", "").strip())

                values.append(price_value)

            # validate prices within range
            assert all(min_price <= v <= max_price for v in values)

        # elif tc == 11:
        #     new_page.wait_for_load_state("domcontentloaded")
        #     new_page.wait_for_selector("//h2[text()='Similar items']")
        #     # get main product price
        #     main_price_text = new_page.locator("//div[@data-testid='x-price-primary']//span").first.inner_text()
        #
        #     main_price = float(main_price_text.replace("US $", "").replace("$", "").strip())
        #
        #     # calculate ±20% range
        #     min_price = main_price * 0.8
        #
        #     # get similar product prices
        #     similar_prices = new_page.locator("//div[@class='aQ4i']//span")
        #
        #     values = []
        #
        #     for i in range(similar_prices.count()):
        #         price_text = similar_prices.nth(i).inner_text()
        #
        #         price_value = float(price_text.replace("$", "").strip())
        #
        #         values.append(price_value)
        #
        #     # validate prices within range
        #     assert all(v > min_price for v in values)

        # elif tc == 12:
        #     new_page.wait_for_load_state("domcontentloaded")
        #     new_page.wait_for_selector("//h2[text()='Similar items']")
        #     # get main product price
        #     main_price_text = new_page.locator("//div[@data-testid='x-price-primary']//span").first.inner_text()
        #
        #     main_price = float(main_price_text.replace("US $", "").replace("$", "").strip())
        #
        #     # calculate ±20% range
        #     max_price = main_price * 1.2
        #
        #     # get similar product prices
        #     similar_prices = new_page.locator("//div[@class='aQ4i']//span")
        #
        #     values = []
        #
        #     for i in range(similar_prices.count()):
        #         price_text = similar_prices.nth(i).inner_text()
        #
        #         price_value = float(price_text.replace("$", "").strip())
        #
        #         values.append(price_value)
        #
        #     # validate prices within range
        #     assert all(v <= max_price for v in values)

        # elif tc == 13:

        # elif tc == 14:
        #     rp = RelatedProductsPage(new_page)
        #     rp.open_wallet_page()
        #     rp.wait_for_products()
        #     images = rp.images().all()
        #     for img in images:
        #         assert img.get_attribute("src") is not None

        elif tc == 15:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            assert rp.images().count() > 0
            assert rp.titles().count() > 0
            assert rp.prices().count() > 0

        elif tc == 16:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            imgs = rp.images().all()
            for img in imgs:
                assert img.get_attribute("src") is not None

        # elif tc == 17:
        #     rp = RelatedProductsPage(new_page)
        #     rp.open_wallet_page()
        #     rp.wait_for_products()
        #     count = rp.product_cards().count()
        #     assert count > 0

        elif tc == 18:
            start = new_page.url
            with new_page.context.expect_page() as new_page_event2:
                rp.click_first()
            new_page2 = new_page_event2.value
            new_page2.wait_for_load_state("domcontentloaded")
            assert new_page2.url != start

        elif tc == 19:
            # rp.open_wallet_page()
            rp.wait_for_products()
            assert rp.prices().count() > 0

        elif tc == 20:
            rp.wait_for_products()
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            titles = rp.titles()
            count_title = titles.count()
            for i in range(count_title):
                text = titles.nth(i).text_content()
                assert text is not None and text.strip() != "", f"h3 at index {i} has no text"

        # elif tc == 21:
        #     assert page.locator("text='Best Seller'").count() >= 0

        # elif tc == 22:
        #     cards = rp.links()
        #     boxes = [c.bounding_box() for c in cards.all()]
        #     assert all(b["y"] == boxes[0]["y"] for b in boxes)

        # elif tc == 23:
        #     page.set_viewport_size({"width": 375, "height": 800})
        #     assert rp.product_count() > 0

        # elif tc == 24:
        #     rp = RelatedProductsPage(page)
        #     rp.open_wallet_page()
        #     rp.wait_for_products()
        #     assert rp.product_cards().first.is_visible()

        elif tc == 25:
            new_page.wait_for_load_state("domcontentloaded")
            new_page.wait_for_selector("//h2[text()='Similar items']")
            assert time.time() - get_start_time < 10.0

        # elif tc == 26:
        #     rp = RelatedProductsPage(page)
        #     rp.open_wallet_page()
        #     rp.wait_for_products()
        #     assert rp.images().count() > 0

        # elif tc == 27:
        #     rp = RelatedProductsPage(page)
        #     rp.open_wallet_page()
        #     rp.wait_for_products()
        #     prices = rp.prices().all_inner_texts()
        #     assert len(prices) > 0

        # elif tc == 28:
        #     rp = RelatedProductsPage(page)
        #     rp.open_wallet_page()
        #     rp.wait_for_products()
        #     assert rp.product_cards().count() >= 1

        # elif tc == 29:
        #     rp = RelatedProductsPage(page)
        #     rp.open_wallet_page()
        #     rp.wait_for_products()
        #     assert rp.titles().count() > 0

        # elif tc == 30:
        #     rp = RelatedProductsPage(page)
        #     rp.open_wallet_page()
        #     rp.wait_for_products()
        #     first_img = rp.images().first
        #     assert first_img.is_visible()
        #
        # elif tc == 31:
        #     card = rp.links().first
        #     card.hover()
        #     assert card.evaluate("e => getComputedStyle(e).transform") is not None
        #
        # elif tc == 32:
        #     carousel = page.locator(".carousel")
        #     page.mouse.wheel(500, 0)
        #     assert carousel.is_visible()
        #
        # elif tc == 33:
        #     assert page.locator("[aria-label]").count() > 0
        #
        # elif tc == 34:
        #     page.keyboard.press("Tab")
        #     assert page.evaluate("document.activeElement") is not None
        #
        # elif tc == 35:
        #     assert page.locator("meta[name='description']").count() > 0

        elif tc == 36:
            # with sync_playwright() as p:
            #
            #     # browser = p.chromium.launch()
            #     # page = browser.new_page()

            responses = []

            new_page.on("response", lambda response: responses.append(response))

                # page.goto(rp.send_url())
            rp.wait_for_products()
                # page.wait_for_selector("a[href*='/itm/']")

            cache_found = False

            for r in responses:
                headers = r.headers
                if "cache-control" in headers:
                    cache_found = True
                    break

            assert cache_found, "Cache-Control header not found"

        # elif tc == 37:
        #     with sync_playwright() as p:
        #
        #         browser = p.chromium.launch()
        #         page = browser.new_page()
        #
        #         page.goto("https://www.ebay.com/sch/i.html?_nkw=wallet")
        #         page.wait_for_selector("a[href*='/itm/']")
        #
        #         wallet_products = page.locator("h3").all_inner_texts()
        #
        #         page.goto("https://www.ebay.com/sch/i.html?_nkw=backpack")
        #         page.wait_for_selector("a[href*='/itm/']")
        #
        #         backpack_products = page.locator("h3").all_inner_texts()
        #
        #         assert wallet_products != backpack_products
        #
        #         browser.close()

        # elif tc == 38:
        #     with page.expect_request("**analytics**"):
        #         rp.click_first()
        #
        # elif tc == 39:
        #     with sync_playwright() as p:
        #
        #         browser = p.chromium.launch()
        #         page = browser.new_page()
        #
        #         page.goto(rp.send_url())
        #         page.wait_for_selector("a[href*='/itm/']")
        #
        #         first_list = page.locator("h3").all_inner_texts()
        #
        #         page.reload()
        #         page.wait_for_selector("a[href*='/itm/']")
        #
        #         second_list = page.locator("h3").all_inner_texts()
        #
        #         assert len(second_list) > 0
        #
        #         browser.close()
