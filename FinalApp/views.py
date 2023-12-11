from django.shortcuts import render
from django.http import HttpResponse

def saludo(request):
    contexto = {}
    return HttpResponse(request, 'templates', contexto)

