import requests
from getpass import getpass # Pedir una contrasenia y que esta no se exponga en la terminal

# BASIC AUTHENTICATION
URL = 'https://httpbin.org/basic-auth/cody/1234'

# SESSION
password = getpass("Ingresa la contraseña: ")
session = requests.Session()
session.auth = ('cody', password) # Tupla (user, password)

response = session.get(URL)

if response.status_code == 200:
    payload = response.json()
    print(payload)

if response.status_code == 401:
    print("Unsuccessful authentication.")
