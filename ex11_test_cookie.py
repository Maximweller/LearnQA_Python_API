import requests


class TestCookie:
    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.get(url)
        cookie_value = response.cookies.get_dict()
        print(cookie_value)

        assert 'HomeWork' in cookie_value, "There is not cookie"
