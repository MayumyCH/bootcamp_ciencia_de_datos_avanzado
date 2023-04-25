import requests

URL = 'https://httpbin.org/cookies'

cookies = {
    'session': 'abc123',
    'name': 'cody',
}

response = requests.get(URL,cookies=cookies) 

if response.status_code == 200:
    payload = response.json()
    print(payload)
