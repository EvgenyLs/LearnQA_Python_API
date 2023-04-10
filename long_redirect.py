import requests

url = "https://playground.learnqa.ru/api/long_redirect"

response = requests.get(url, allow_redirects=True)
print(response.history)
print("The number of redirects: ", len(response.history))

first_response = response.history[0]
second_response = response.history[1]
print(first_response.url, second_response.url, response.url, sep="\n")
