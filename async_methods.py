from asyncio import gather, create_task
from aiohttp import ClientSession
from random import randint


async def get_xkcd_image(session):
    random = randint(0, 300)
    response = await session.get(f'http://xkcd.com/{random}/info.0.json')
    text = await response.json()
    return text['img']


async def get_multiple_images(number):
    async with ClientSession() as session:
        tasks = [create_task(get_xkcd_image(session)) for _ in range(number)]
        result = await gather(*tasks)
    return result
