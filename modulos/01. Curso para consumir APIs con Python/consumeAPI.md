
#       👩‍💻 Curso para consumir APIs con Python


        MODULO I
        ¿Qué son los servicios web?
        - Protocolo HTTP
        - Verbos de HTTP
        - Objetos JSON

        MODULO II
        Libreria REQUEST

        MODULO III
        PROYECTO

---

## ⚙ ENTORNO DE TRABAJO

**CREAR el entorno de trabajo**

[🔗 Manual para crear enviroments Python](https://gist.github.com/MayumyCH/8641ce303572488239692db3a07f2334)

- Entorno de trabajo desde gitbash

        python3 -m venv env
        ls
        source env/Scripts/activate

- Instalar librerias 

        pip install requests


**DIRIGIRME y ACTIVAR el entorno de trabajo**

Por estar dentro de un workspace tengo que dirigirme a la carpeta del proyecto para activar el enviroment

        cd modulos/'01. Curso para consumir APIs con Python'
        source env/Scripts/activate
        python main.py

---
## MODULO I


🔶 PROTOCOLO 🔶

        HTTP || Hypertext transfer Protocol
        --> Los datos son enviados en texto plano

        HTTPS <>  Protocolo SEGURO de transferencia de HyperTexto
        --> Crea una conexion segura encriptada entre el CLIENTE y el SERVIDOR

        *STATELEES*: 
        Cuando la comunicacion entte el cliente y el servidor haya culminado toda la informacion se pierde.
        Un SERVIDOR trata CADA PETICION COMO una NUEVA peticion de un cliente nuevo

        📌 Toda informacion de la conexión debe ser almacenada de manera externa (Cookies/Sesiones)
 
        _HTTP Y HTTPS son protocolos de comunicacion (enviar y recibir) para transferir informacion 
        a traves de internet)_
        Ambos protocolos no almacenan ningun tipo de estado una vez la comunicación haya finalizado.


🔶 METODOS (VERBOS) DE PROTOCOLO 🔶

Que accion es lo que debe realizar nuestro servidor y que es lo que necesita nuestro cliente 

        GET: 
        Permite OBTENER un recurso por parte del Servidor.
        Por Ejemplo: Una pagina web, un video, una imagen, un objeto en formato Json, etc.

        POSTS:
        Permite CREAR recursos en el servidor.
        Por Ejemplo: Secciones, imagenes, nuevos archivos, nuevos registros en la BD, etc.

        PUT:
        ACTUALIZAR algun recurso en nuestro servidor.
        Por Ejemplo: Actualizar un registro en la BD, modificar archivos ya existentes.

        DELETE:
        ELIMINAR un recurso por parte del servidor
        Por Ejemplo: Eliminar un registro en la BD, Eliminar archivos alojados en el servidor.


🔶 OBJETOS JSON 🔶

        JSON <> JavaScrip Object Notation
        Formato que permite representar dato de una forma sencilla


## MODULO II

🔗 [Link de Servidor prueba Verbos HTTP](https://httpbin.org/#/HTTP_Methods)

🔗 [Link de Servidor prueba Random User](https://randomuser.me/)

🔗 [Link del codigo de GET/POSTS/PUT/DELETE 🛠](https://github.com/MayumyCH/bootcamp_ciencia_de_datos_avanzado/tree/main/modulos/01.%20Curso%20para%20consumir%20APIs%20con%20Python/codigos)

![img](https://raw.githubusercontent.com/MayumyCH/bootcamp_ciencia_de_datos_avanzado/main/modulos/01.%20Curso%20para%20consumir%20APIs%20con%20Python/resources/Verbos%20HTTP.png)



# MODULO III

## Crear aplicacion con github

- PASO 1: 

  Ingresar al sgte [🔗 Link Github Setting](https://github.com/settings/profile) , luego dirigirse a  `<> Developer setting`

- PASO 2:

  Nos dirigira a esta seccion: 

  ![img](https://raw.githubusercontent.com/MayumyCH/bootcamp_ciencia_de_datos_avanzado/main/modulos/01.%20Curso%20para%20consumir%20APIs%20con%20Python/resources/createAplicaction.png)

  Click en `OAuth Apps` y en esta seccion presionar  `New OAuth App`.
  Luego llenar :

  ![img](https://raw.githubusercontent.com/MayumyCH/bootcamp_ciencia_de_datos_avanzado/main/modulos/01.%20Curso%20para%20consumir%20APIs%20con%20Python/resources/detailsAplicaction2.png)

  Hacer check en `Enable Device Flow` y por ultimo click en `Register application` y te debe dar dos *Client's de interes*; estos nos ayudaran para implementar la autenticacion OAuth.

  ![img](https://raw.githubusercontent.com/MayumyCH/bootcamp_ciencia_de_datos_avanzado/main/modulos/01.%20Curso%20para%20consumir%20APIs%20con%20Python/resources/clientsAplication3.png)

- PASO 3:

Generar el codigo para realizar los sgtes pasos:
- Obtener codigo
- Obtener AccesToken
- Obtener al usuario Autenticado

🔗 [Link del CODIGO para la APLICACIÓN](https://github.com/MayumyCH/bootcamp_ciencia_de_datos_avanzado/blob/main/modulos/01.%20Curso%20para%20consumir%20APIs%20con%20Python/Proyecto/main.py)

🔗 [Link de la DOCUMENTACION OFICIAL de GITHUB](https://docs.github.com/en/apps/oauth-apps/building-oauth-apps/authorizing-oauth-apps)


