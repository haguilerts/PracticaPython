from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from ProyectoWebApp import views

urlpatterns=[
        path('',views.home, name="Home"),
        path('servicios',views.servicios,name="Servicios"),
        path('tienda',views.tienda,name="Tienda"),
        path('contacto',views.contacto,name="Contacto"),
        path('blog',views.blog,name="Blog"),
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


