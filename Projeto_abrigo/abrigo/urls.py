"""
URL configuration for abrigo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from app_adotantes.views import adotantes
from django.conf import settings
from django.conf.urls.static import static
from app_paginas_gerais.views import inicial, sobre
from app_animais.views import animais
from app_voluntarios.views import voluntarios

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adotantes/', adotantes),
    path('', inicial, name='inicial'),
    path('sobre/', sobre, name='sobre'),
    path('animais/', animais, name='animais'  ),
    path('voluntarios/', voluntarios, name='voluntarios' ),
     path('adocao/', include('app_usuarios.urls', namespace='usuarios')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
