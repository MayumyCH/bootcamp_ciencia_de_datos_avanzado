import requests

URL ='https://api.github.com/user'
access_token = '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'

headers = {
    'Accept':'application/vnd.github+json',
    'Authorization': f'Bearer {access_token}'
}


# CREAR UNA APLIACION EN GITHUB

# Obtenemos el codigo del usuario
# -> https://github.com/login/oauth/authorize?client_id=[CLIENTE:UID]&scope=user

# Realizamos una peticion para obtener el AccesToken
# -> https://github.com/login/oauth/access_token


response = requests.get(URL, headers=headers)


if response.status_code == 200:
    username = response.json().get('login')
    print(username)

#print(response.status_code)
#print(response.text)