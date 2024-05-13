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


def test_drag_and_drop(page):
    page.goto('https://zimaev.github.io/draganddrop/')
    time.sleep(1)
    page.drag_and_drop("#drag", "#drop")
    time.sleep(1)