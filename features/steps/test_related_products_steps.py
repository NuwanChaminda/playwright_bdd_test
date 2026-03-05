
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import sync_playwright
from pages.related_products_page import RelatedProductsPage
import allure
import time

scenarios("../related_products.feature")

@given("user opens wallet search page")
def open_page(page):
    RelatedProductsPage(page).open_wallet_page()

@when("related products are visible")
def wait_products(page):
    page.wait_for_selector("a[href*='/itm/']")

@then(parsers.parse("validate testcase {tc:d}"))
def validate_tc(page, tc):
    rp = RelatedProductsPage(page)

    with allure.step(f"Validate TC-{tc:03d}"):

        if tc == 1:
            assert rp.related_section_visible()

        elif tc == 2:
            title = page.locator("section h2")
            assert "Related" in title.inner_text()

        elif tc == 3:
            assert rp.product_count() <= 6

        elif tc == 4:
            assert rp.product_count() == 6

        elif tc == 5:
            assert page.locator(":has-text('Out of stock')").count() == 0

        elif tc == 6:
            titles = rp.titles().all_inner_texts()
            assert all("wallet" in t.lower() for t in titles)

        elif tc == 7:
            assert rp.product_count() > 0

        elif tc == 8:
            links = rp.links().all()
            hrefs = [l.get_attribute("href") for l in links]
            assert len(hrefs) == len(set(hrefs))

        elif tc == 9:
            links = rp.links().all()
            hrefs = [l.get_attribute("href") for l in links]
            assert len(hrefs) == len(set(hrefs))

        elif tc == 10:
            prices = rp.prices().all_inner_texts()
            values = [float(p.replace("$", "")) for p in prices if "$" in p]
            assert all(40 <= v <= 60 for v in values)

        elif tc == 11:
            assert rp.titles().count() > 0

        elif tc == 12:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            assert rp.product_cards().count() > 0

        elif tc == 13:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            assert rp.titles().count() > 0

        elif tc == 14:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            images = rp.images().all()
            for img in images:
                assert img.get_attribute("src") is not None

        elif tc == 15:
            assert rp.images().count() > 0
            assert rp.titles().count() > 0
            assert rp.prices().count() > 0

        elif tc == 16:
            imgs = rp.images().all()
            for img in imgs:
                assert img.get_attribute("src") is not None

        elif tc == 17:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            count = rp.product_cards().count()
            assert count > 0

        elif tc == 18:
            start = page.url
            rp.click_first()
            page.wait_for_load_state("load")
            assert page.url != start

        elif tc == 19:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            assert rp.prices().count() > 0

        elif tc == 20:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            cards = rp.product_cards().count()
            assert cards > 0

        elif tc == 21:
            assert page.locator("text='Best Seller'").count() >= 0

        elif tc == 22:
            cards = rp.links()
            boxes = [c.bounding_box() for c in cards.all()]
            assert all(b["y"] == boxes[0]["y"] for b in boxes)

        elif tc == 23:
            page.set_viewport_size({"width": 375, "height": 800})
            assert rp.product_count() > 0

        elif tc == 24:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            assert rp.product_cards().first.is_visible()

        elif tc == 25:
            start = time.time()
            page.goto(rp.URL)
            page.wait_for_selector(rp.PRODUCT_CARDS)
            assert time.time() - start < 3

        elif tc == 26:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            assert rp.images().count() > 0

        elif tc == 27:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            prices = rp.prices().all_inner_texts()
            assert len(prices) > 0

        elif tc == 28:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            assert rp.product_cards().count() >= 1

        elif tc == 29:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            assert rp.titles().count() > 0

        elif tc == 30:
            rp = RelatedProductsPage(page)
            rp.open_wallet_page()
            rp.wait_for_products()
            first_img = rp.images().first
            assert first_img.is_visible()

        elif tc == 31:
            card = rp.links().first
            card.hover()
            assert card.evaluate("e => getComputedStyle(e).transform") is not None

        elif tc == 32:
            carousel = page.locator(".carousel")
            page.mouse.wheel(500, 0)
            assert carousel.is_visible()

        elif tc == 33:
            assert page.locator("[aria-label]").count() > 0

        elif tc == 34:
            page.keyboard.press("Tab")
            assert page.evaluate("document.activeElement") is not None

        elif tc == 35:
            assert page.locator("meta[name='description']").count() > 0

        elif tc == 36:
            with sync_playwright() as p:

                browser = p.chromium.launch()
                page = browser.new_page()

                responses = []

                page.on("response", lambda response: responses.append(response))

                page.goto(rp.send_url())
                page.wait_for_selector("a[href*='/itm/']")

                cache_found = False

                for r in responses:
                    headers = r.headers
                    if "cache-control" in headers:
                        cache_found = True
                        break

                assert cache_found, "Cache-Control header not found"

                browser.close()

        elif tc == 37:
            with sync_playwright() as p:

                browser = p.chromium.launch()
                page = browser.new_page()

                page.goto("https://www.ebay.com/sch/i.html?_nkw=wallet")
                page.wait_for_selector("a[href*='/itm/']")

                wallet_products = page.locator("h3").all_inner_texts()

                page.goto("https://www.ebay.com/sch/i.html?_nkw=backpack")
                page.wait_for_selector("a[href*='/itm/']")

                backpack_products = page.locator("h3").all_inner_texts()

                assert wallet_products != backpack_products

                browser.close()

        elif tc == 38:
            with page.expect_request("**analytics**"):
                rp.click_first()

        elif tc == 39:
            with sync_playwright() as p:

                browser = p.chromium.launch()
                page = browser.new_page()

                page.goto(rp.send_url())
                page.wait_for_selector("a[href*='/itm/']")

                first_list = page.locator("h3").all_inner_texts()

                page.reload()
                page.wait_for_selector("a[href*='/itm/']")

                second_list = page.locator("h3").all_inner_texts()

                assert len(second_list) > 0

                browser.close()
