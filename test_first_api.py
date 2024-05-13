import pytest
import requests

class TestFirstAPI:
    names = [
    ("Vitalii"),
    ("Arseniy"),
    ("")
]



    @pytest.mark.parametrize('name', names)
    def test_first_api(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {'name':name}

        response = requests.get(url, params=data)

        assert response.status_code == 200, "Неверный код ответа "

        response_dict = response.json()
        assert "answer" in response_dict, "В ответе нет поля «ответ»"

        expected_response_test = f"Hello, {name}"
        actual_response_text = response_dict["answer"]
        assert actual_response_text == expected_response_test, "Фактический текст в ответе неверен."

        if response.status_code == 200:
            print("200 прилетел БРАТ!")