import os
from datetime import datetime

import requests
from django.shortcuts import render
from .models import City

WEATHER_KEY = os.getenv('WEATHER_KEY')


def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=' + str(WEATHER_KEY)

    city = 'Tokyo'
    r = requests.get(url.format(city)).json()

    # if request.method == 'POST':
    #     form = CityForm(request.POST)
    #     form.save()

    # form = CityForm()

    # cities = City.objects.all()
    # weather_data = []

    # for city in cities:
    #     r = requests.get(url.format(city)).json()

    city_weather = {
        'city': city,
        'temperature': r['main']['temp'],
        'longitude': r['coord']['lon'],
        'latitude': r['coord']['lat'],
        'time': r['dt'],
    }

    City.objects.create(city=city_weather['city'],
                        temperature=city_weather['temperature'],
                        longitude=city_weather['longitude'],
                        latitude=city_weather['latitude'],
                        time=datetime.fromtimestamp(city_weather['time']))

    context = {'weather_data': city_weather}
    return render(request, 'weather.html', context)
