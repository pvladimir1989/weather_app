from django.urls import path, include
from rest_framework import routers

from . import views
from .views import CityViewSet

router = routers.DefaultRouter()
router.register(r'city', CityViewSet)

urlpatterns = [
    path('', views.index),
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
