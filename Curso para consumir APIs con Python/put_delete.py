import requests


URL = 'https://httpbin.org/delete'


response = requests.delete(URL, 
                        params={'name':'eduardo'}, 
                        headers = {'version':'2.0'},
                        data={'idEval':'1'})

if response.status_code == 200:

    payload = response.json()
    print(payload)