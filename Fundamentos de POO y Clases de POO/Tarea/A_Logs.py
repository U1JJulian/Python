# Alumno: Jose Julian Gonzalez Medrano
# No. Control: 21100215

from itertools import groupby
from functools import reduce
from operator import itemgetter
from datetime import datetime

# ------------------------------------------------------------
# Datos de entrada: Logs simulados
# Cada log es una tupla inmutable: (timestamp, tipo, mensaje)
# ------------------------------------------------------------
logs = (
    ("2025-04-10 08:23:11", "ERROR", "Base de datos no disponible"),
    ("2025-04-10 09:15:45", "INFO", "Inicio de sesión exitoso"),
    ("2025-04-10 11:03:27", "ERROR", "Timeout de red"),
    ("2025-04-11 10:55:11", "WARNING", "CPU al 90%"),
    ("2025-04-11 11:01:00", "ERROR", "Archivo no encontrado"),
    ("2025-04-11 12:00:01", "INFO", "Archivo cargado"),
    ("2025-04-11 12:05:44", "ERROR", "Base de datos no disponible"),
    ("2025-04-12 08:33:12", "ERROR", "Timeout de red"),
)

# ----------------------
# Funciones puras
# ----------------------

# Convierte el timestamp (string) a objeto date
# Función pura: no modifica nada, retorna un nuevo valor
def extraer_fecha(log):
    fecha_completa = datetime.strptime(log[0], "%Y-%m-%d %H:%M:%S")
    return fecha_completa.date()

# Transforma los logs incluyendo la fecha extraída
logs_con_fecha = tuple((extraer_fecha(log), log[1], log[2]) for log in logs)

# Agrupa logs por fecha usando itertools.groupby
# Función pura: retorna nuevo diccionario agrupado, sin alterar los logs
def agrupar_por_fecha(logs):
    ordenados = sorted(logs, key=itemgetter(0))  # importante ordenar antes de agrupar
    return {fecha: list(grupo) for fecha, grupo in groupby(ordenados, key=itemgetter(0))}

# Cuenta cuántos logs hay de un cierto tipo (ej. ERROR) en un grupo
# Usa functools.reduce para sumar condicionalmente
def contar_tipo_en_grupo(grupo, tipo):
    return reduce(lambda acc, log: acc + (1 if log[1] == tipo else 0), grupo, 0)

# Genera un reporte por fecha, incluyendo conteos por tipo
# Función pura: retorna nuevo diccionario
def generar_reporte_por_fecha(logs):
    agrupados = agrupar_por_fecha(logs)
    return {
        fecha: {
            "total": len(grupo),
            "ERROR": contar_tipo_en_grupo(grupo, "ERROR"),
            "WARNING": contar_tipo_en_grupo(grupo, "WARNING"),
            "INFO": contar_tipo_en_grupo(grupo, "INFO")
        }
        for fecha, grupo in agrupados.items()
    }

# Genera reporte total por tipo de log (global)
# Función pura: retorna diccionario
def generar_reporte_por_tipo(logs):
    tipos = sorted(logs, key=itemgetter(1))  # ordenar por tipo antes de agrupar
    agrupados = groupby(tipos, key=itemgetter(1))
    return {tipo: len(list(grupo)) for tipo, grupo in agrupados}

# ----------------------
# Bloque de pruebas
# ----------------------

if __name__ == "__main__":
    reporte_fecha = generar_reporte_por_fecha(logs_con_fecha)
    reporte_tipo = generar_reporte_por_tipo(logs_con_fecha)

    print("Resumen por Fecha:\n")
    for fecha, datos in reporte_fecha.items():
        print(f"{fecha}:")
        print(f" -- Total: {datos['total']}")
        print(f"     - ERROR: {datos['ERROR']}")
        print(f"     - WARNING: {datos['WARNING']}")
        print(f"     - INFO: {datos['INFO']}\n")

    print("Resumen Global por Tipo:\n")
    for tipo, cantidad in reporte_tipo.items():
        print(f"   - {tipo}: {cantidad} logs")
