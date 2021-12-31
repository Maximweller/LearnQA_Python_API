import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

responses = response.history
last_response = response

last_response_url = last_response.url
num_of_redirect = len(responses) - 1

print(f"Итоговый url: {last_response_url}")
print(f"Всего переходов: {num_of_redirect}")