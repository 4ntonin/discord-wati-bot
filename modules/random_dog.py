import requests


def get_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    dog = response.json()
    return dog['message']
