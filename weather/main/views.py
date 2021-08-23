import os
from datetime import datetime

import requests
from django.shortcuts import render

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import City
from .serializers import CitySerializer

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


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['city']
    search_fields = ['city', 'temperature']
    ordering_fields = ['temperature']
