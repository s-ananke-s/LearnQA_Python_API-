import requests

class TestHeader:
    def test_header(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response = requests.get(url)
        header_value = response.headers["x-secret-homework-header"]

        expected_cookies = 'Some secret value'
        actual_cookies = header_value
        assert actual_cookies == expected_cookies, "Actual header value in the response is not correct"