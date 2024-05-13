import requests

def test_get_hello():
 payload = {"name": "User"}
 response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
 print(response.text)