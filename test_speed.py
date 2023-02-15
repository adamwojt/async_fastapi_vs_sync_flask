import aiohttp
import asyncio
import time

FLASK_URL = "http://127.0.1:8001/"
FAST_API_URL = "http://127.0.1:8000/"
NUM_REQUESTS = 20



async def get_response(session, url):
    async with session.get(url) as resp:
        response = await resp.json()
        return resp.status


async def main(url:str):

    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, NUM_REQUESTS):
            tasks.append(asyncio.ensure_future(get_response(session, url)))

        results = await asyncio.gather(*tasks)
        assert all([200 == r for r in results])

start_time = time.time()
asyncio.run(main(FAST_API_URL))
print("FAST API ASYNC TOOK --- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
asyncio.run(main(FLASK_URL))
print("FLASK TOOK --- %s seconds ---" % (time.time() - start_time))
