from django.contrib import admin
from django.urls import path
from FinalApp.views import usuario, crear_user_form, inicio, buscar, user_login

urlpatterns = [
    path('', inicio, name="inicio"),
    path('user/', usuario, name=""),
    path('login/', user_login, name="inicio de sesión"),
    path('create/', crear_user_form, name="crear usuario"),
    path('buscar/', buscar, name="buscar usuario"),

]
