# Alumno: Jose Julian Gonzalez Medrano
# No. Control: 21100215

from collections import namedtuple

# --------------------------------------
# Definición de estructuras inmutables
# --------------------------------------

# Un archivo tiene un nombre y un tamaño (en bytes)
Archivo = namedtuple('Archivo', ['nombre', 'tamano'])

# Un directorio tiene un nombre y una lista de contenidos (archivos o subdirectorios)
Directorio = namedtuple('Directorio', ['nombre', 'contenido'])

# -----------------------------
# Funciones puras y recursivas
# -----------------------------

# Función recursiva para calcular el tamaño total de un directorio
# Esta función es pura: no modifica el sistema de archivos ni tiene efectos secundarios
def calcular_tamano(directorio):
    total = 0
    for elemento in directorio.contenido:
        if isinstance(elemento, Archivo):
            total += elemento.tamano
        elif isinstance(elemento, Directorio):
            total += calcular_tamano(elemento)
    return total

# Función recursiva para navegar el sistema por una ruta (lista de nombres)
# También es pura: no altera nada y siempre da el mismo resultado para la misma entrada
def navegar(directorio, ruta):
    if not ruta:
        return directorio
    siguiente = ruta[0]
    for elemento in directorio.contenido:
        if isinstance(elemento, Directorio) and elemento.nombre == siguiente:
            return navegar(elemento, ruta[1:])
    return None  # Ruta no encontrada

# Función adicional: listar todos los archivos dentro de un directorio, recursivamente
# Pura y recursiva: no modifica el sistema ni produce efectos secundarios
def listar_archivos(directorio):
    archivos = []
    for elemento in directorio.contenido:
        if isinstance(elemento, Archivo):
            archivos.append(elemento)
        elif isinstance(elemento, Directorio):
            archivos.extend(listar_archivos(elemento))
    return archivos

# -----------------------------------------------------
# Sistema de archivos de prueba (estructura ficticia)
# -----------------------------------------------------

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

# -------------------------------------
# Bloque de pruebas / Ejemplo de uso
# -------------------------------------

# Tamaño total del sistema
print("Tamaño total del sistema:", calcular_tamano(sistema_archivos), "bytes")

# Navegación a una ruta específica
ruta = ['imagenes', 'vacaciones']
subdir = navegar(sistema_archivos, ruta)

if subdir:
    print(f"\nContenido de /{'/'.join(ruta)}:")
    for item in subdir.contenido:
        print("-", item)
    print("Tamaño del subdirectorio:", calcular_tamano(subdir), "bytes")
else:
    print("Ruta no encontrada")

# Listar todos los archivos del sistema
print("\nLista completa de archivos:")
for archivo in listar_archivos(sistema_archivos):
    print(f"- {archivo.nombre} ({archivo.tamano} bytes)")

