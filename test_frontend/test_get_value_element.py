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

def test_get_value_element(page):
 page.goto('https://zimaev.github.io/table/')
 row = page.locator("tr")
 print(row.all_text_contents())