from fastapi import FastAPI  # Importamos la clase FastAPI correctamente

app = FastAPI()  # Creamos una instancia de la aplicación

@app.get("/")  # Definimos una ruta GET para la raíz "/"
async def root():  # Usamos una función asincrónica (async) que se ejecuta cuando visitamos la raíz
    return {"message": "Hello World!"}  # Retornamos un diccionario como respuesta en formato JSON
