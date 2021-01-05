from django.http import HttpResponse
from django.template import Template,Context

def saludo(request):
    return HttpResponse("Hola a todos!")

def saludo_html(request):
    documento="""<html><body><h1>Hola a todoosss!</h1></body></html>"""
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse("chauuu, Hasta luego!")

import datetime
def get_fecha(request):
    fecha_actual=datetime.datetime.now()
    documento="""<html><body><h1>Fecha Actual: %s</h1></body></html>"""%fecha_actual
    return HttpResponse(documento)

def calcular_edad(request,edad,agno):
    periodo=agno-2020 
    edad_futura=edad+periodo
    documento="<html><body><h2> En el año %s tendrás %s años"%( agno,edad_futura) 
    return HttpResponse(documento)
#-----------------------------------------------------


#-----------------------------------------------------
def saludo_plantilla(request):
    nombre="Giovanny"
    apellido="Aguilar"
    fecha=datetime.datetime.now()
    temas=["Plantillas","Modelos","Formularios","Vistas"] 
#    arch=open("C:\\xampp\\htdocs\\Python_Codo_A_Codo\\Python\\Clase 37-38-39 Django\\Clase37\\templates\\home.html")
    arch=open("C:/xampp/htdocs/Python_Codo_A_Codo/Python/Clase 37-38-39 Django/Clase37/templates/home.html")
    plt=Template(arch.read())        
    arch.close()       
    ctx=Context({"nombre_persona":nombre,"apellido_persona":apellido,"now":fecha,"temas_curso":temas})
    documento=plt.render(ctx)        
    return HttpResponse(documento)

# ------------------- otra forma mucho mejor -------------- 

#from django.template import loader # importo todo 

from django.template.loader import get_template
from django.shortcuts import render
def ren(request):
    nombre="Giovanny"
    return render(request,"prueba.html",{"nombre":nombre})

def myPlantalla(request):
    nombre="Giovanny"
    temas=["html","javaScript","python","Django"] 
    fecha=datetime.datetime.now()

    pagina="hijo.html" #"plantilla.html"
    return render(request,pagina,{"nombre":nombre,"temas_curso":temas,"now":fecha})
#

  