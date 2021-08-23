from django.contrib import admin

from main.models import City


class CityAdmin(admin.ModelAdmin):
    list_display = ('city', 'time', 'longitude', 'latitude', 'temperature')


admin.site.register(City, CityAdmin)
