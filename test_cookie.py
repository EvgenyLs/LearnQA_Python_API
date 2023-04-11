import requests

url = "https://playground.learnqa.ru/api/homework_cookie"


class TestCookie:
    def test_cookie(self):
        response = requests.get(url)
        response_cookies = dict(response.cookies)
        print("response_cookies: ", response_cookies)

        assert "HomeWork" in response_cookies, "The HomeWork field is missing"

        cookie_value = response.cookies.get("HomeWork")
        assert cookie_value == "hw_value", "Wrong cookies in the response"
