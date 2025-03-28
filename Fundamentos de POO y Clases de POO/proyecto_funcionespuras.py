import string
from toolz import compose

def eliminar_puntuacion(texto):
    return texto.translate(str.maketrans("", "", string.punctuation))

def a_minusculas(texto):
    return texto.lower()

def eliminar_stopwords(texto, stopwords):
    return " ".join([palabra for palabra in texto.split() if palabra not in stopwords])

# Versión con parámetros normales
def procesar_texto(texto, stopwords=["el", "la", "de"]):
    texto = eliminar_puntuacion(texto)
    texto = a_minusculas(texto)
    texto = eliminar_stopwords(texto, stopwords)
    return texto

# Versión con compose (alternativa)
procesar_texto_compose = compose(
    lambda t: eliminar_stopwords(t, ["el", "la", "de"]),
    a_minusculas,
    eliminar_puntuacion
)

texto = "El rapido zorro marron, salta sobre el perro perezoso."
print(procesar_texto(texto))