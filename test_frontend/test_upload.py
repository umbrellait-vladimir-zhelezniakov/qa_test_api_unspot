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


def test_select_multiple(page):
    page.goto('https://zimaev.github.io/upload/')
    time.sleep(2)
    page.set_input_files("#formFile", "hello.txt")
    time.sleep(2)
    page.locator("#file-submit").click()
    time.sleep(2)