import requests
from random import randint


def get_xkcd_image():
    random = randint(0, 300)
    response = requests.get(f'http://xkcd.com/{random}/info.0.json')
    return response.json()['img']


def get_multiple_images(number):
    return [get_xkcd_image() for _ in range(number)]
