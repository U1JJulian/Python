import requests

# -------------------------------
# 🔑 Configuración inicial
# -------------------------------
API_KEY = "F61CEA3498ADBD8EA82D1B9C1DDE585F"  # Coloca tu clave API de Steam
STEAM_ID = "76561199544813783"  # Reemplaza con tu SteamID64
APP_ID = "744900"  # Tokyo ghoul

# -------------------------------
# 1️⃣ Obtener logros globales de un juego
# -------------------------------
print(f"\n🏆 Logros globales en el juego con AppID {APP_ID}:")
url_logros_globales = f"http://api.steampowered.com/ISteamUserStats/GetGlobalAchievementPercentagesForApp/v0002/?appid={APP_ID}&key={API_KEY}"
resp_logros_globales = requests.get(url_logros_globales)

# Imprimir la respuesta cruda para depuración
print("Respuesta cruda:", resp_logros_globales.text)

try:
    logros_globales = resp_logros_globales.json()
    if 'achievementpercentages' in logros_globales:
        for logro in logros_globales['achievementpercentages']['achievements'][:5]:  # Solo primeros 5
            print(f"- {logro['name']} | {logro['percent']}% de jugadores los han conseguido")
    else:
        print("No se pudieron obtener los logros globales del juego.")
except Exception as e:
    print(f"Error al procesar JSON: {e}")

# -------------------------------
# 2️⃣ Obtener reseñas de un juego
# -------------------------------
print(f"\n💬 Reseñas recientes de {APP_ID}:")
url_resenas = f"https://store.steampowered.com/api/appreviews/{APP_ID}?json=1&key={API_KEY}&filter=recent"
resp_resenas = requests.get(url_resenas)
resenas = resp_resenas.json()

if 'reviews' in resenas:
    for resena in resenas['reviews'][:5]:  # Solo las 5 primeras
        print(f"- {resena['author']['steamid']}: {resena['review'][:100]}...")  # Solo el principio de la reseña
else:
    print("No se pudieron obtener reseñas del juego.")

# -------------------------------
# 3️⃣ Comprobar si el usuario está jugando
# -------------------------------
print(f"\n👾 Comprobando si el usuario está en línea o jugando:")
url_estado = f"http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key={API_KEY}&steamids={STEAM_ID}"
resp_estado = requests.get(url_estado)
estado = resp_estado.json()

if 'response' in estado and 'players' in estado['response']:
    jugador = estado['response']['players'][0]
    if jugador['personastate'] == 1:
        print(f"El usuario {jugador['personaname']} está en línea (sin juego actual).")
    elif jugador['personastate'] == 3:
        print(f"El usuario {jugador['personaname']} está jugando {jugador['gameextrainfo']}.")
    else:
        print(f"El usuario {jugador['personaname']} está {jugador['personastate']}.")
else:
    print("No se pudo obtener el estado del usuario.")

# -------------------------------
# 4️⃣ Obtener detalles del juego (precio, género, etc.)
# -------------------------------
print(f"\n🧾 Detalles del juego con AppID {APP_ID}:")
url_detalles = f"https://store.steampowered.com/api/appdetails?appids={APP_ID}"
resp_detalles = requests.get(url_detalles)
detalles = resp_detalles.json()

if detalles[APP_ID]['success']:
    info = detalles[APP_ID]['data']
    print("Nombre:", info['name'])
    print("Géneros:", [g['description'] for g in info['genres']])
    print("Desarrollador:", info['developers'])
    print("Precio:", info['price_overview']['final_formatted'])
else:
    print("No se pudieron obtener los detalles del juego.")
