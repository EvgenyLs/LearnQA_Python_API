import requests
import pytest
from test_framework.lib.base_case import BaseCase
from test_framework.lib.assertions import Assertions


class TestUserAuth(BaseCase):
    exclude_params = ["no_cookie", "no_token", "no_token_and_cookie"]

    def setup_method(self):
        url1 = "https://playground.learnqa.ru/api/user/login"
        data = {'email': 'vinkotov@example.com', 'password': '1234'}
        response1 = requests.post(url1, data=data)

        self.auth_sid = self.get_cookie(response1, 'auth_sid')
        self.token = self.get_header(response1, 'x-csrf-token')
        self.user_id_from_auth_method = self.get_json_value(response1, 'user_id')

    def test_user_auth(self):
        url2 = "https://playground.learnqa.ru/api/user/auth"
        response2 = requests.get(url2, headers={'x-csrf-token': self.token}, cookies={'auth_sid': self.auth_sid})

        Assertions.assert_json_value_by_name(
            response2,
            "user_id",
            self.user_id_from_auth_method,
            "user_id from auth isn't equal user_id from check"
        )

    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth_check(self, condition):
        url2 = "https://playground.learnqa.ru/api/user/auth"
        if condition == "no_cookie":
            print("check with no_cookie")
            response2 = requests.get(url2, headers={'x-csrf-token': self.token})
        elif condition == "no_token":
            print("check with no token")
            response2 = requests.get(url2, cookies={'auth_sid': self.auth_sid})
        else:
            print("check with no token and cookie")
            response2 = requests.get(url2)

        Assertions.assert_json_value_by_name(
            response2,
            'user_id',
            0,
            f"User is authorized with condition {condition}"
        )
