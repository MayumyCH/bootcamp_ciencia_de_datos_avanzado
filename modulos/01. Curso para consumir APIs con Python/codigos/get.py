import requests



# ----------------------  GET

URL = 'https://httpbin.org/get' # URL del SERVIDOR
response = requests.get(URL) # Realiza una peticion GET

print(response) # Objeto tipo response
print(response.status_code) # Codigo de status rpta
print(response.text) # Cuerpo de la rpta - Objeto de tipo String
print(type(response.text)) # Objeto de tipo String
print(response.json()) #Serializar el cuerpo de la rpta

payload = response.json() # Diccionario
print(payload.get('origin'))
print(payload.get('url'))

print(response.url)

# ----------------------  QUERYS

print("\n \nquerys")
# query <> Podemos mandar informacion al servidor
# Todo lo que esta despues del (?) 

URL = 'https://httpbin.org/get?name=edu&password=987&email=edu@codeFacilito.com'
response = requests.get(URL)

if response.status_code == 200:

    payload = response.json()
    params = payload['args']

    print(params['name'])
    print(params['password'])
    print(params['email'])


URL_2 = 'https://httpbin.org/get'

params = {
    'name': 'mayu',
    'password': '123',
    'email': 'mayu@codefacilito.com',
}

response = requests.get(URL_2, params=params) # Params <> args

if response.status_code == 200:

    payload = response.json()
    params = payload['args']

    print(params['name'])
    print(params['password'])
    print(params['email'])

    print(response.url)
