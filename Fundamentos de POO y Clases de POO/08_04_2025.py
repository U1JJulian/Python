import asyncio 
import aiohttp
from bs4 import BeautifulSoup

async def obtener_titulo(url):
    async with aiohttp.ClientSession() as session:
        html = await resp.text()
        soup = BeautifulSoup(html, 'html.parser')
        print(f"{url} -> {soup.title.string}")
    
async def main():
    urls = [
            'https://www.python.org',
            'https://www.wikipedia.org',
            'https://www.githubcom',

    ]
    await asyncio.gather(*(obtener_titulo(url) for url in urls))

asyncio.run(main())
        