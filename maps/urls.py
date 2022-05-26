import imp
from django.urls import path
from .views import maps, coordinates_form

urlpatterns = [
    path('', coordinates_form, name='coordinates-form'),
    path('map', maps, name='maps'),
]