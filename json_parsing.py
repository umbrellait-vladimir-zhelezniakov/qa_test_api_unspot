import requests

def test_json_parking():
    url = "https://uit-dev.unspot.tech/api/auth/login"
    myobj = {'password': 'zehr213HA2', 'username':'vladimir.zhelezniakov@umbrellait.com'}
    x = requests.post(url, json = myobj)
    print(x.text)
    if x.status_code == 200:
     print("Дроу бро!Давно не виделись, вот тебе TOKEN!")
    elif x.status_code == 401:
     print("Неверные креды, ты хацкер!?")
    else:
        print("Ты бэк сломал!")



