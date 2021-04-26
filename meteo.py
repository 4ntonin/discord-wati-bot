import requests
import os


def get_temp(city):
    key = os.getenv('OPENWEATHERMAP_API_KEY')
    print(key)
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={key}&lang=fr")
    r = response.json()
    k = r['main']['temp']
    f = r['main']['feels_like']
    s = r['weather'][0]['description']
    name = r['name']
    f -= 273.15
    c = k - 273.15
    return name, round(c, 1), round(f, 1), s
