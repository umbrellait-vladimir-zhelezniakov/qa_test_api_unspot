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

def test_checkbox(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    time.sleep(2)
    page.locator("text=Default checkbox").check()
    time.sleep(2)
    page.locator("text=Checked checkbox").check()
    time.sleep(2)
    page.locator("text=Default radio").check()
    time.sleep(2)
    page.locator("text=Default checked radio").check()
    time.sleep(2)
    page.locator("text=Checked switch checkbox input").check()
    time.sleep(2)