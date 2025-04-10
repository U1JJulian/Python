import string
from toolz import compose

stopwords = ["el", "la", "de", "sobre"]

def eliminar_puntuacion(texto):
    return texto.translate(str.maketrans("", "", string.punctuation))

def a_minusculas(texto):
    return texto.lower()

def eliminar_stopwords(texto, stopwords):
    return " ".join([palabra for palabra in texto.split() if palabra not in stopwords])

# Pipeline funcional usando composición
procesar_texto = compose(
    lambda t: eliminar_stopwords(t, stopwords),
    a_minusculas,
    eliminar_puntuacion
)

texto = "El rápido zorro marrón, salta sobre el perro perezoso."
print(procesar_texto(texto))
