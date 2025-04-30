# Alumno: Jose Julian Gonzalez Medrano
# No. Control: 21100215

import string
from toolz import compose

# Lista de palabras comunes (stopwords) que queremos eliminar
stopwords = ["el", "la", "de", "sobre", "y", "a", "en", "por"]

# Puntuación adicional que no está incluida en string.punctuation
# Esto incluye signos en español como ¡ y ¿
# Por el idioma de la libreria que es ingles y que se utiliza al final ya sea ! o para la pregunta ?
puntuacion_extra = "¡¿" #Incluimos estos puntuaciones extra para el idioma en español :D
todos_los_signos = string.punctuation + puntuacion_extra

# Función pura que elimina signos de puntuación (incluye español)
def eliminar_puntuacion(texto):
    """
    Función pura que elimina signos de puntuación.
    No modifica el texto original. No tiene efectos secundarios.
    """
    return texto.translate(str.maketrans("", "", todos_los_signos))

# Función pura que convierte el texto a minúsculas
def a_minusculas(texto):
    """
    Función pura que convierte el texto a minúsculas.
    Siempre devuelve el mismo resultado con la misma entrada.
    """
    return texto.lower()

# Función pura que elimina las stopwords del texto
def eliminar_stopwords(texto, stopwords):
    """
    Función pura que elimina las palabras definidas como stopwords.
    Usa comprensión de listas para generar un nuevo texto limpio.
    """
    return " ".join([palabra for palabra in texto.split() if palabra not in stopwords])

# Función extra: contar número de palabras (análisis)
def contar_palabras(texto):
    """
    Función pura que cuenta cuántas palabras hay en el texto.
    """
    return len(texto.split())

# Pipeline funcional (composición de funciones)
# El orden es: eliminar puntuación → convertir a minúsculas → eliminar stopwords
procesar_texto = compose(
    lambda t: eliminar_stopwords(t, stopwords),
    a_minusculas,
    eliminar_puntuacion
)

# Bloque de pruebas
if __name__ == "__main__":
    texto_original = "El rápido zorro marrón, salta sobre el perro perezoso. ¡Y corre a través del bosque!"

    texto_procesado = procesar_texto(texto_original)
    cantidad_palabras = contar_palabras(texto_procesado)

    print("Texto original:", texto_original)
    print("Texto procesado:", texto_procesado)
    print("Cantidad de palabras (sin stopwords):", cantidad_palabras)
