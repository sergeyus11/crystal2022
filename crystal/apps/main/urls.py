from django.contrib import admin
from django.urls import path
from .views import index, about_main, wholesaler, retail, quality, contacts, catalog, vkusvil


urlpatterns = [
    path('', index, name='home'), # находится по адресу http://127.0.0.1:8000/main/
    path('about/', about_main, name='about_main'),
    path('catalog/', catalog, name='catalog_url'),
    path('wholesaler/', wholesaler, name='wholesaler'),
    path('retail/', retail, name='retail'),
    path('quality/', quality, name='quality'),
    path('contacts/', contacts, name='contacts'),
    path('vkusvil/', vkusvil, name='vkusvil'),

]