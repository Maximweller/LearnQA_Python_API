import requests


class TestHeader:
    def test_header(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        header_value = response.headers
        print(header_value)

        assert header_value is not None, "There are no header"