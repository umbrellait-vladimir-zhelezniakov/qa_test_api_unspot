import pytest

@pytest.fixture
def browser_context_args(browser_context_args):
    return {

        "viewport": {
            "width": 1000,
            "height": 1080,
        }
    }

def test_screenshot(page):
    page.goto('https://zimaev.github.io/select/')
    page.screenshot(path="screenshot.png", full_page=True)