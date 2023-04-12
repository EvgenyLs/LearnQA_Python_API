import requests

url = "https://playground.learnqa.ru/api/homework_header"


class TestHeader:
    def test_header(self):
        response = requests.get(url)
        print('x-secret-homework-header: ', response.headers['x-secret-homework-header'])

        assert 'x-secret-homework-header' in response.headers, \
            "The x-secret-homework-header field is missing in the response"

        x_secret_homework_header_value = 'Some secret value'
        assert x_secret_homework_header_value == response.headers['x-secret-homework-header'], \
            "Wrong x-secret-homework-header in the response"
