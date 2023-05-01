import requests

# ----------------------  POST

URL = 'https://httpbin.org/post'

data = {
    'username': 'mayu',
    'password': 'password123',
}

# Enviar informacion por el CUERPO de la PETICION

response = requests.post(URL, data=data) # <> Item Form

if response.status_code == 200:

    payload = response.json()
    print(payload)
    print("\n",response.url,"\n")