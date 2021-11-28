import requests

class TestCookies:
    def test_cookies(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response = requests.post(url)
        cookie_value = response.cookies
        dict_cookie = cookie_value.get_dict()

        expected_cookies = {"HomeWork":"hw_value"}
        actual_cookies = dict_cookie
        assert actual_cookies == expected_cookies, "Actual cookies in the response is not correct"

