import aiohttp
import asyncio
import time
import json

start_time = time.time()

url = "https://jsonplaceholder.typicode.com/posts/{}"

MAX_REQUESTS = 10

semaphore = asyncio.Semaphore(MAX_REQUESTS)

async def fetch_post_data(session, post_id):
    async with semaphore:
        async with session.get(url.format(post_id)) as response:
            if response.status == 200:
                return await response.json()
            else:
                print(f"Error code: {response.status}")
                return None


async def fetch_posts():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_post_data(session, post_id) for post_id in range(1, 78)]
        responses = await asyncio.gather(*tasks)

        with open("posts.json", "w") as f:
            f.write("[\n")
            first_entry = True
            for data in responses:
                if not first_entry:
                    f.write(',\n')
                json.dump(data, f, indent=4)
                first_entry = False
            f.write("\n]")

asyncio.run(fetch_posts())

total_time = time.time() - start_time

print(f"Total time needed: {total_time:.2f}")
