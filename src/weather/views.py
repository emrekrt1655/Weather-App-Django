from django.shortcuts import render
from decouple import config
import requests
from pprint import pprint
from .models import City
from .forms import CityForm

def index(request):
    form = CityForm()
    cities = City.objects.all()
    url = config('BASE_URL')
    city_data = []
    for city in cities:
        print(city)
        r = requests.get(url.format(city))
        data = r.json()
        weather_data = {
            "city" : city.name,
            'temp' : data["main"]["temp"],
            'description' : data["weather"][0]["description"],
            'icon' : data["weather"][0]["icon"],
        }
        city_data.append(weather_data)
    
    context = {
        "city_data" : city_data,
        "form" : form
    }
    
    return render(request, "weather/index.html", context)