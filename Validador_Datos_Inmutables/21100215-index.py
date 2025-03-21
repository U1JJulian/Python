# Control de Calidad de Productos en una Fábrica
# Programación Funcional en Python

from typing import Tuple

# Definimos una tupla para representar un producto (peso, largo, ancho, alto, lote)
Producto = Tuple[float, float, float, float, str]

# Función pura para validar el peso de un producto
def validar_peso(producto: Producto) -> bool:
    peso_min, peso_max = 100.0, 500.0  # Rango permitido en gramos
    return peso_min <= producto[0] <= peso_max

# Función pura para validar las dimensiones (largo, ancho, alto)
def validar_dimensiones(producto: Producto) -> bool:
    largo_min, largo_max = 10.0, 50.0  # cm
    ancho_min, ancho_max = 5.0, 30.0  # cm
    alto_min, alto_max = 2.0, 20.0  # cm
    return (largo_min <= producto[1] <= largo_max and
            ancho_min <= producto[2] <= ancho_max and
            alto_min <= producto[3] <= alto_max)

# Función pura para validar el identificador de lote
def validar_lote(producto: Producto) -> bool:
    return producto[4].startswith("LOTE-") and producto[4][5:].isdigit()

# Lista de productos de prueba
productos = [
    (150.0, 25.0, 10.0, 5.0, "LOTE-12345"),  # Válido
    (90.0, 20.0, 15.0, 5.0, "LOTE-67890"),  # Peso inválido
    (200.0, 55.0, 12.0, 5.0, "LOTE-ABCDE"), # Dimensiones inválidas y lote incorrecto
    (300.0, 20.0, 10.0, 10.0, "LOTE-98765") # Válido
]

# Aplicar validaciones usando filter()
productos_validos = list(filter(lambda p: validar_peso(p) and validar_dimensiones(p) and validar_lote(p), productos))

# Imprimir resultados
print("Productos válidos:")
for producto in productos_validos:
    print(producto)
