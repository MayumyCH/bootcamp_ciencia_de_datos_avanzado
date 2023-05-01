import requests

URL = 'https://randomuser.me/api/'
count = int(input("Ingrese la cantidad de usuarios: "))

response = requests.get(URL, params={'results':count})

if response.status_code == 200:

    payload = response.json()
    result = payload.get('results')
    #print(len(result))

    for user in result:
        name = user.get('name')
        #print(f"{name['title']} {name['first']} {name['last']}")

        print("{title} {first} {last}".format(**name)) # Pasando el diccionario name
