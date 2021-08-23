from django.db import models


class City(models.Model):
    city = models.CharField(max_length=25)
    time = models.DateTimeField(verbose_name='Время', auto_now_add=False)
    longitude = models.FloatField(verbose_name="Долгота", default=0)
    latitude = models.FloatField(verbose_name="Широта", default=0)
    temperature = models.FloatField(verbose_name='Температура', default=0)

    def __str__(self):
        return self.city

    class Meta:
        verbose_name_plural = 'cities'
