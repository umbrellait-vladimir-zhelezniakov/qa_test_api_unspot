import requests

def test_headers():
    headers = {"some_headers": "193887474"}
    response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers = headers)
    print(response.text)
    print(response.headers)