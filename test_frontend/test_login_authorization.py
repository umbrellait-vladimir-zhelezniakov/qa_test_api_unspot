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

def test_login_authorization(page):
    page.goto("https://uit-sg.unspot.tech/login")
    time.sleep(2) #page.wait_for_selector()
    page.locator("[data-test=\"input_login\"]").click()
    time.sleep(2)
    page.locator("[data-test=\"input_login\"]").fill("firnasromura@gmail.com")
    time.sleep(2)
    page.locator("[data-test=\"input_password\"]").click()
    time.sleep(2)
    page.locator("[data-test=\"input_password\"]").fill("z7tMVk3BFD") #page.locator(data-test=\"input_password\").fill("z7tMVk3BFD")
    time.sleep(2)
    page.locator("[data-test=\"button_login\"]").click()
    time.sleep(2)
    page.get_by_role("button", name="Пропустить").click()
    time.sleep(2)
    page.close()


