import aiohttp
import asyncio


async def send_request():
    async with aiohttp.ClientSession() as session:
        async with session.post("http://127.0.0.1:8080/ads/",
                                json={
                                    "heading": "Something",
                                    "description": "Some text about something",
                                    "creator": "Myself"
                                }) as resp:
            print(resp.status)
            creation_result = await resp.json()
            print(creation_result)
            ad_id = creation_result['id']
        async with session.get(f"http://127.0.0.1:8080/ads/{ad_id}") as resp:
            print(resp.status)
            creation_result = await resp.json()
            print(creation_result)
        async with session.delete(f"http://127.0.0.1:8080/ads/{ad_id}") as resp:
            print(resp.status)
            creation_result = await resp.json()
            print(creation_result)

asyncio.run(send_request())
