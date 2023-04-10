import requests

url = "https://playground.learnqa.ru/api/compare_query_type"
methods = ['GET', 'POST', 'PUT', 'DELETE']
request_type = [requests.post, requests.put, requests.delete]


without_method_response = requests.get(url)
print('without method: ', without_method_response.status_code, without_method_response.text)


wrong_method_response = requests.head(url)
print('wrong_response: ', wrong_method_response.status_code, wrong_method_response.text)


right_method_post_response = requests.post(url, data={'method': 'POST'})
print('right_response_post', right_method_post_response.status_code, right_method_post_response.text)


for m in methods:
    for t in request_type:
        response = t(url, data={'method': m})
        print(m, t, response.status_code, response.text)


for m in methods:
    response = requests.get(url, params={'method': m})
    print(m, 'function get', response.status_code, response.text)
