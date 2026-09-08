import urllib.parse
import os
from dotenv import load_dotenv
import asyncio
import httpx

load_dotenv()


async def fetch_my_ip():
    main_route = "https://ipapi.co/json/?"
    key = os.getenv('IPAPI_KEY2')
    api = main_route + urllib.parse.urlencode({'key' : key})

    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        return response.json()



async def fetch_target_ip(ip_address):
    main_route = f"https://ipapi.co/{ip_address}/json/?"
    key = os.getenv('IPAPI_KEY2')
    api = main_route + urllib.parse.urlencode({'key' : key})

    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        return response.json()
