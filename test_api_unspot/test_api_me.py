from test_user_autth_unspot import test_user_auth_unspot
import requests
import json
import pprint



def test_api_me():
    headers = test_user_auth_unspot()
    response_me = requests.get("https://uit-dev.unspot.tech/api/me", headers=headers )
    print(response_me.status_code)
    print(response_me.text)