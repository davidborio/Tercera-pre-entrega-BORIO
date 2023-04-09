"""tercera_entrega URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.views.generic import ListView
from AppCoder.views import mostrar_mis_tareas, mostrar_mascotas,mostrar_personas, crear_persona, BuscarPersonas,crear_mascota, BuscarMascotas


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mis-tareas/<criterio>', mostrar_mis_tareas, name="mis-tareas"),
    path('personas', mostrar_personas, name="personas"),
    path('personas/crear', crear_persona, name="personas-crear"),
    path("personas/list", BuscarPersonas.as_view(), name="personas-list"), #as_view es un metodo de clase que convierte una class based vire en una function based view ya que path necesita una funcion yse leesta dando una clase.
    path("mascotas/crear", crear_mascota, name="mascotas-crear"),
    path('mascotas', mostrar_mascotas,name="mascotas"),
    path("mascotas/list", BuscarMascotas.as_view(), name="mascotas-list")
]
