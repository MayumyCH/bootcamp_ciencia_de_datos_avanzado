import requests

# ----------------------  ENCABEZADOS

URL = 'https://httpbin.org/post'

# Query (Por la URL) -> GET | params
# Cuerpo de la peticion -> POST | data

# Encabezado (headers) -> TODOS LOS VERBOS | headers
# <> Para enviar metadata al servidor 

headers = { # Envio de datos por ENCABEZADO
    'course': 'Curso de Python',
    'version':'2.0',
    'autor':'Eduardo Ismael'
}

params = { # Envio de datos por QUERY
    'platform': 'Codigo Facilito',
    'navegador':'Edge'
}

data = {  # Envio de datos por CUERPO - Informacion mas reservada
    'username':'mayu',
    'pass':'123'
}

response = requests.post(URL, headers=headers, params=params, data=data) # headers | args | form

if response.status_code == 200:

    payload = response.json()
    print(payload)
    print(response.url)