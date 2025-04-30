import requests
URL = "http://127.0.0.1:8000"

respuesta = requests.get(URL)
datos = respuesta.json()
print(datos)