import requests


def get_fox():
    response = requests.get("http://randomfox.ca/floof")
    fox = response.json()
    return fox['image']
