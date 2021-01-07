from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint

def index(request):
    url = config('BASE_URL')
    city = "Berlin"
    r = requests.get(url.format(city))
    data = r.json()
    context = {
        "city" : city,
        'temp' : data["main"]["temp"],
        'description' : data["weather"][0]["description"],
        'icon' : data["weather"][0]["icon"],
    }
    return render(request, "weather/index.html", context)