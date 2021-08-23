from rest_framework import serializers

from .models import City


class CitySerializer(serializers.ModelSerializer):
    """ Список объявлений"""

    class Meta:
        model = City
        fields = '__all__'
