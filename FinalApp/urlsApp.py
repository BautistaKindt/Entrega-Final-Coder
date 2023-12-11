from django.contrib import admin
from django.urls import path
from FinalApp.views import saludo

urlpatterns = [
    path('hi/', saludo),
]
