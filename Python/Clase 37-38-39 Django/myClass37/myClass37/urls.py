"""myClass37 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myClass37.views import ren, saludo, saludo_html, despedida, get_fecha, calcular_edad,saludo_plantilla,myPlantalla

urlpatterns=[
    path("Admin/",admin.site.urls),
    path("Saludo/",saludo),
    path("Saludohtml/",saludo_html),
    path("Despedida/",despedida),
    path("FECHA/",get_fecha),
    path("edades/<int:edad>/<int:agno>",calcular_edad), # http://127.0.0.1:8000/edades/25/2025
    path("saludosPlantilla/",saludo_plantilla),
    path("render/",ren),
    path("myPlantilla/",myPlantalla)



]
