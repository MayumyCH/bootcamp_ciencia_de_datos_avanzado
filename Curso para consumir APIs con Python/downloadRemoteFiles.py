import requests

URL = 'https://codigofacilito.com/images/cody' # Retorna una imagen png

response = requests.get(URL,
                        stream=True) # stream: NO CIERRA la PETICION hasta que TERMINE la DESCARGA

# stream: 
# Via que informa al request que realice la peticion manteniendose activo
# De tal forma que el servidor pueda mandar enviar en fragmentos (chunck) el archivo a descargar.
# Esta conexion se va a cerrar unicamente cuando el archivo este descargado en su totalidad.

if response.status_code == 200:
    with open('images/cody.png','wb') as file: #wb <> Escritura Binaria | with <> Contexto
        for chunk in response.iter_content(1024): # Leer los fragmentos del archivo remoto
            file.write(chunk)
