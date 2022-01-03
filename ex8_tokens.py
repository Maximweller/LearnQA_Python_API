import requests
import time
import json

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

response = requests.get(url=url)
print(response.text)
obj = json.loads(response.text)
payload = {'token': obj["token"]}

response = requests.get(url=url, params=payload)
print(response.text)
time.sleep(obj["seconds"]+1)
response = requests.get(url=url, params=payload)
print(response.text)
