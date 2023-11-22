"""
URL configuration for PracticaSem18 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from Practica18 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #url para la pagina de inicio
    path('',views.index),
    #url para la lista de medicos
    path('meds/',views.lis_med,name="meds"),
    #url para agregar nuevos medicos
    path('add_med/',views.add_medic,name="add_med"),

    #urls para la lista de pacientes
    path('pacs/',views.lis_pacientes,name='pacs'),
    #url para agregar nuevos pacientes al sistema
    path('add_pacs/',views.ag_pacientes,name='ag_pacientes'),
]
