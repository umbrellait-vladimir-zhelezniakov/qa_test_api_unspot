import requests


def test_inventory(page):
    response = page.request.get('https://uit-dev.unspot.tech')
    print(response.status)
    print(response.text)
    print(response.json)
