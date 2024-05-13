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

def test_selector(page):
    page.goto('https://zimaev.github.io/select/')
    time.sleep(1)
    page.select_option('#floatingSelect', value="3")
    time.sleep(1)
    page.select_option('#floatingSelect', index=1)
    time.sleep(1)
    page.select_option('#floatingSelect', label="Нашел и завел bug")
    time.sleep(1)
    page.select_option('#skills', value=["playwright", "python"])
    time.sleep(1)