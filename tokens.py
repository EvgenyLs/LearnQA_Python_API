import json
import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url)
print(response.status_code, response.text)
obj = json.loads(response.text)
token = obj["token"]
pause = obj["seconds"]

response = requests.get(url, params={"token": token})
print(response.status_code, response.text)

obj = json.loads(response.text)
status = obj["status"]
if status == "Job is NOT ready":
    time.sleep(pause + 1)
    response = requests.get(url, params={"token": token})
    print(response.status_code, response.text)
else:
    print("wrong status")


