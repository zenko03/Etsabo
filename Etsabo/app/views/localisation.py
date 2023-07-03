from django.shortcuts import render, redirect, HttpResponse
from .. import models

def pharmacie(request : HttpResponse):
    return render(request, 'localisation_pharmacie_test.html')