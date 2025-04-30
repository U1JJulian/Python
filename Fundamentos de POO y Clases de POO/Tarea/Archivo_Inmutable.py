#Alumno: Jose Julian Gonzalez Medrano
#No. Control: 21100215
from collections import namedtuple

# Definición de estructuras inmutables
Archivo = namedtuple('Archivo', ['nombre', 'tamano'])
Directorio = namedtuple('Directorio', ['nombre', 'contenido'])  # contenido: lista de Archivos o Directorios

# Función recursiva para calcular el tamaño total de un directorio
def calcular_tamano(directorio):
    total = 0
    for elemento in directorio.contenido:
        if isinstance(elemento, Archivo):
            total += elemento.tamano
        elif isinstance(elemento, Directorio):
            total += calcular_tamano(elemento)
    return total

# Función recursiva para navegar una ruta dentro del sistema
def navegar(directorio, ruta):
    if not ruta:
        return directorio
    siguiente = ruta[0]
    for elemento in directorio.contenido:
        if isinstance(elemento, Directorio) and elemento.nombre == siguiente:
            return navegar(elemento, ruta[1:])
    return None  # Ruta no encontrada

# ----------------------
# Ejemplo de estructura
# ----------------------

sistema_archivos = Directorio('home', [
    Archivo('notas.txt', 100),
    Directorio('documentos', [
        Archivo('cv.pdf', 200),
        Archivo('tesis.docx', 500)
    ]),
    Directorio('imagenes', [
        Archivo('foto1.jpg', 1500),
        Archivo('foto2.png', 2300),
        Directorio('vacaciones', [
            Archivo('playa.jpg', 1800)
        ])
    ])
])

# ----------------------
# Ejemplo de uso
# ----------------------

print("Tamaño total del sistema:", calcular_tamano(sistema_archivos), "bytes")

ruta = ['imagenes', 'vacaciones']
subdir = navegar(sistema_archivos, ruta)

if subdir:
    print(f"Contenido de /{'/'.join(ruta)}:")
    for item in subdir.contenido:
        print("-", item)
    print("Tamaño del subdirectorio:", calcular_tamano(subdir), "bytes")
else:
    print("Ruta no encontrada")
