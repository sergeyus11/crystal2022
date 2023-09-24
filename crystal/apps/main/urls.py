from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from .views import IndexView, AccountView, LoginOptionsView, EmailConflictView, about_main, wholesaler, retail, quality, contacts, catalog, vkusvil


urlpatterns = [
    path('', IndexView.as_view(), name='home'), # находится по адресу http://127.0.0.1:8000/
    path('accounts/login_options/', LoginOptionsView.as_view(), name='login_options'),
    path('accounts/email_conflict/', EmailConflictView.as_view(), name='account_email_conflict'),
    path('accounts/profile/', AccountView.as_view(), name='account'),
    path('about/', about_main, name='about_main'),
    path('catalog/', catalog, name='catalog_url'),
    path('wholesaler/', wholesaler, name='wholesaler'),
    path('retail/', retail, name='retail'),
    path('quality/', quality, name='quality'),
    path('contacts/', contacts, name='contacts'),
    path('vkusvil/', vkusvil, name='vkusvil'),
]
