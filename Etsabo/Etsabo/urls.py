"""Etsabo URL Configuration

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
from app.views import views as v
from app.views import chat as chat
from app.views import localisation as localisation

urlpatterns = [
    path('', v.home,name='home'),
    path('boutique/',v.boutique,name='boutique'),
    path('listeDiscu/',v.listeDiscu,name='listeDiscu'),
    path('chat/', chat.chat, name='chat'),
    path('chat/conversation/', chat.get_current_conversation, name='conversation'),
    path('chat/send/', chat.envoyer_message, name='send'),
    path('localisation/pharmacie/', localisation.pharmacie, name='localisation_pharmacie')
]

from django.urls import path
from app.views import views


