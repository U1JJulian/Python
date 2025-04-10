from itertools import groupby
from functools import reduce
from operator import itemgetter
from datetime import datetime

# Logs simulados: (timestamp, tipo, mensaje)
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

# Convertir a estructura con fecha como objeto date
def extraer_fecha(log):
    fecha_completa = datetime.strptime(log[0], "%Y-%m-%d %H:%M:%S")
    return fecha_completa.date()

logs_con_fecha = tuple((extraer_fecha(log), log[1], log[2]) for log in logs)

# Agrupar por fecha
def agrupar_por_fecha(logs):
    ordenados = sorted(logs, key=itemgetter(0))
    return {fecha: list(grupo) for fecha, grupo in groupby(ordenados, key=itemgetter(0))}

# Contar errores en grupo
def contar_tipo_en_grupo(grupo, tipo):
    return reduce(lambda acc, log: acc + (1 if log[1] == tipo else 0), grupo, 0)

# Reporte por fecha
def generar_reporte_por_fecha(logs):
    agrupados = agrupar_por_fecha(logs)
    reporte = {}
    for fecha, grupo in agrupados.items():
        resumen = {
            "total": len(grupo),
            "ERROR": contar_tipo_en_grupo(grupo, "ERROR"),
            "WARNING": contar_tipo_en_grupo(grupo, "WARNING"),
            "INFO": contar_tipo_en_grupo(grupo, "INFO")
        }
        reporte[fecha] = resumen
    return reporte

# Reporte por tipo (global)
def generar_reporte_por_tipo(logs):
    tipos = sorted(logs, key=itemgetter(1))
    agrupados = groupby(tipos, key=itemgetter(1))
    return {tipo: len(list(grupo)) for tipo, grupo in agrupados}

# Mostrar reportes
def mostrar_reporte_completo():
    print("Resumen por Fecha:\n")
    por_fecha = generar_reporte_por_fecha(logs_con_fecha)
    for fecha, datos in por_fecha.items():
        print(f"{fecha}:")
        print(f" -- Total: {datos['total']}")
        print(f"     - ERROR: {datos['ERROR']}")
        print(f"     - WARNING: {datos['WARNING']}")
        print(f"     - INFO: {datos['INFO']}\n")

    print("Resumen Global por Tipo:\n")
    por_tipo = generar_reporte_por_tipo(logs_con_fecha)
    for tipo, cantidad in por_tipo.items():
        print(f"   - {tipo}: {cantidad} logs")

# Main
if __name__ == "__main__":
    mostrar_reporte_completo()
