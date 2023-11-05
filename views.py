from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludar(request):
    saludo= "hola chicos"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http

def saludar_con_fecha(request):
    hoy = datetime.now()
    saludo= f"hola chicos, hoy es día {hoy.day}, mes {hoy.month}, hora {hoy. hour}, minutos {hoy.minute}"
    respuesta_http = HttpResponse(saludo)
    return respuesta_http