import requests
import json
import pprint



def test_user_auth_unspot():
    myobj = {'password': 'ASD456zaratystra', 'username': 'vladimir.zhelezniakov@umbrellait.com'}
    response_auth = requests.post("https://uit-dev.unspot.tech/api/auth/login", json = myobj)
    fulltoken = response_auth.text
    tokens = json.loads(fulltoken)
    tokens["Bearer"] = tokens["token"]
    del tokens ["token"]
    del tokens ["refresh_token"]
    new_token = tokens.pop("Bearer")
    #print(new_token)

    headers = {
    'Authorization': 'Bearer '+new_token
    }

    response_me = requests.get("https://uit-dev.unspot.tech/api/me", headers=headers )
    # print(response_me.status_code)
    # print(response_me.text)

    return headers  # возвращает



