import requests
import pytest


data = [('1', 'Mozilla/5.0 (Linux; U; Android 4.0.2; en-us; Galaxy Nexus Build/ICL53F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30', 'Mobile', 'No', 'Android'),
        ('2', 'Mozilla/5.0 (iPad; CPU OS 13_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/91.0.4472.77 Mobile/15E148 Safari/604.1', 'Mobile', 'Chrome', 'iOS'),
        ('3', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', 'Googlebot', 'Unknown', 'Unknown'),
        ('4', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.100.0', 'Web', 'Chrome', 'No'),
        ('5', 'Mozilla/5.0 (iPad; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1', 'Mobile', 'No', 'iPhone')]


@pytest.mark.parametrize('data_set, user_agent, expected_platform, expected_browser, expected_device', data)
class TestUserAgent:
    def test_user_agent(self, data_set, user_agent, expected_platform, expected_browser, expected_device):
        url = "https://playground.learnqa.ru/ajax/api/user_agent_check"
        header = {"User-Agent": user_agent}
        response = requests.get(url, headers=header)
        response_dict = response.json()

        assert 'platform' in response_dict, "There is not 'platform' field in the response"
        assert 'browser' in response_dict, "There is not 'browser' field in the response"
        assert 'device' in response_dict, "There is not 'device' field in the response"

        actual_platform = response_dict['platform']
        assert expected_platform == actual_platform, f"Wrong platform, data_set: {data_set}"

        actual_browser = response_dict['browser']
        assert expected_browser == actual_browser, f"Wrong browser, data_set: {data_set}"

        actual_device = response_dict['device']
        assert expected_device == actual_device, f"Wrong device, data_set: {data_set}"
