from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import time

@pytest.fixture
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1000,
            "height": 1080,
        }
    }

def test_dialogs(page):
    page.goto("https://zimaev.github.io/dialog/")
    time.sleep(3)
    page.on("dialog", lambda dialog: dialog.accept('15'))
    page.get_by_text("Диалог Prompt").click()
    time.sleep(3)