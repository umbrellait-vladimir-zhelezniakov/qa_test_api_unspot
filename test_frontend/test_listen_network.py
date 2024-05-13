from playwright.sync_api import Playwright, sync_playwright, expect
import pytest
import re
import time

def test_listen_network(page):
    page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
    page.on("request", lambda request: print(">>", request.method, request.url))
    page.on("response", lambda response: print("<<", response.status, response.url))
    page.goto('https://uit-dev.unspot.tech')