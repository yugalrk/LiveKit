import asyncio
import aiohttp
import os
from dotenv import load_dotenv

load_dotenv()

async def main():
    async with aiohttp.ClientSession() as s:
        r = await s.get(
            'https://api.anam.ai/v1/personas',
            headers={'Authorization': f'Bearer {os.environ["ANAM_API_KEY"]}'}
        )
        data = await r.json()
        print(data)

asyncio.run(main())