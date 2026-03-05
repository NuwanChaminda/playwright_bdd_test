
import pytest
import os
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()

@pytest.fixture
def page(browser, request):
    context = browser.new_context(record_video_dir="reports/videos")
    page = context.new_page()
    yield page
    if request.node.rep_call.failed:
        os.makedirs("reports/screenshots", exist_ok=True)
        page.screenshot(path=f"reports/screenshots/{request.node.name}.png")
    context.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
