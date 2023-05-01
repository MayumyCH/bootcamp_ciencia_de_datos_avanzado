import requests
import webbrowser #Libreria propia de python
from settings import CLIENT_ID
from settings import SECRET_ID


# CREAR UNA APLICACION

# (MANUAL)
# Generar Aplicacion en GITHUB: CodigoFacilitoPython
# ---------------------------------------------------
# Aplicacion en el item de: Settings/ Developer settings


# (AUTOMATICO)
# Obtener codigo
# Obtener AccesToken
# Obtener al usuario Autenticado


# Obtener codigo
# ---------------------------------------------------
# Esta funcion nos va a traer el codigo del usuario al loguearse con github a la aplicación
def get_url_code():
    print("> get_url_code")

    url = 'https://github.com/login/oauth/authorize'
    params = {
        'client_id':CLIENT_ID,
        'scope':'user'
    }

    response = requests.get(url, params=params)
    return response.url

# Obtener AccesToken
# ---------------------------------------------------
# Esta funcion nos dara un token para que el usuario pueda navegar
def get_access_token(code):
    print("> get_access_token")

    url = 'https://github.com/login/oauth/access_token'
    params = {
        'client_id':CLIENT_ID,
        'client_secret':SECRET_ID,
        'code':code
    }
    headers = {
    'Accept':'application/json',
    }

    response = requests.post(url, params=params, headers=headers)

    if response.status_code == 200:
        payload = response.json()
        
        return payload.get('access_token')


# Obtener al usuario Autenticado
# ---------------------------------------------------
# 

def get_user(access_token):
    print("> get_access_token")

    url = 'https://api.github.com/user'

    headers = {
    'Accept':'application/vnd.github+json',
    'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        payload = response.json()
        
        return payload


if __name__ == '__main__':
    
    url = get_url_code()
    webbrowser.open(url)

    code = input('Ingresa el codigo: ')
    code = code.strip().replace('\n','')

    access_token = get_access_token(code)

    user = get_user(access_token)

    print(user)
