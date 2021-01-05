from django.http import HttpResponse
import datetime
from django.template.loader import get_template 
from django.shortcuts import render

def curso(request):
    fecha = datetime.datetime.now() 
    return render(request,"curso.html",{"now":fecha})

def saludo_plantilla(request): 
    temas = ["A","B","C","D"]
    return render(request,"plantilla.html",{"temas_curso":temas})

def saludo(request): 
    return HttpResponse("Hola a todos!") 

def saludo_html(request): 
    documento="<html><body><h1>Hola a todos Django!</h1></body></html>"
    return HttpResponse(documento) 

def despedida(request): 
    return HttpResponse("Hasta luego!")

def get_fecha(request): 
    fecha_actual=datetime.datetime.now() 
    documento="<html><body><h1>Fecha: %s</h1></body></html>"%fecha_actual 
    return HttpResponse(documento)

def calcular_edad(request,edad,agno): 
    periodo=agno-2020 
    edad_futura=edad+periodo 
    documento="<html><body><h2>En el año %s tendrás %s años"%(agno,edad_futura) 
    return HttpResponse(documento)