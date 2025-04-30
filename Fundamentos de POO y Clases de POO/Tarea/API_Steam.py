import requests

# -------------------------------
# 🔑 Configuración inicial
# -------------------------------
API_KEY = "F61CEA3498ADBD8EA82D1B9C1DDE585F"  # Coloca tu clave API de Steam
STEAM_ID = "76561199544813783"  # Reemplaza con tu SteamID64
APP_ID = "756530"  # Tokyo Ghoul 

# -------------------------------
# 1️⃣ Obtener lista de juegos del usuario
# -------------------------------
print("\n🎮 Lista de juegos del usuario:")
url_juegos = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={API_KEY}&steamid={STEAM_ID}&format=json"
resp_juegos = requests.get(url_juegos)
juegos = resp_juegos.json()

if 'games' in juegos['response']:
    print("Total juegos:", juegos['response']['game_count'])
    for juego in juegos['response']['games'][:10]:  # Solo primeros 5
        print(f"- AppID: {juego['appid']}, Tiempo jugado: {juego['playtime_forever']} min")
else:
    print("No se encontraron juegos o el perfil es privado.")

# -------------------------------
# 2️⃣ Obtener amigos del usuario
# -------------------------------
print("\n👥 Lista de amigos del usuario:")
url_amigos = f"http://api.steampowered.com/ISteamUser/GetFriendList/v1/?key={API_KEY}&steamid={STEAM_ID}"
resp_amigos = requests.get(url_amigos)
amigos = resp_amigos.json()

if 'friendslist' in amigos:
    for amigo in amigos['friendslist']['friends'][:5]:  # Solo primeros 5
        print("- Friend SteamID:", amigo['steamid'])
else:
    print("No se encontraron amigos o el perfil es privado.")

# -------------------------------
# 3️⃣ Obtener logros del usuario en un juego
# -------------------------------
print(f"\n🏆 Logros en el juego con AppID {APP_ID}:")
url_logros = f"http://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v0001/?appid={APP_ID}&key={API_KEY}&steamid={STEAM_ID}"
resp_logros = requests.get(url_logros)
logros = resp_logros.json()

if 'playerstats' in logros and 'achievements' in logros['playerstats']:
    for logro in logros['playerstats']['achievements'][:30]:  # Solo primeros 5
        print(f"- {logro['apiname']} | Estado: {'✅' if logro['achieved'] else '❌'}")
else:
    print("No se pudieron obtener logros o el juego no tiene habilitados los logros.")

# -------------------------------
# 4️⃣ Obtener detalles de un juego
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
else:
    print("No se pudieron obtener los detalles del juego.")

# -------------------------------
# 5️⃣ Obtener noticias recientes de un juego
# -------------------------------
print(f"\n📰 Noticias recientes de {APP_ID}:")
url_noticias = f"http://api.steampowered.com/ISteamNews/GetNewsForApp/v0002/?appid={APP_ID}&count=3&format=json"
resp_noticias = requests.get(url_noticias)
noticias = resp_noticias.json()

for noticia in noticias['appnews']['newsitems']:
    print(f"- {noticia['title']}")
    print(f"  {noticia['url']}\n")

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