import requests

response = requests.get(url="https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response)

response = requests.head(url="https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response)

response = requests.request(url="https://playground.learnqa.ru/ajax/api/compare_query_type",
                            method='get')
print(response)

our_methods = ['get', 'post', 'put', 'delete', 'head']
for i in our_methods:
    for j in our_methods:
        response = requests.request(f"{i}", url="https://playground.learnqa.ru/ajax/api/compare_query_type",
                                    method=f"{j}")
        print(response)