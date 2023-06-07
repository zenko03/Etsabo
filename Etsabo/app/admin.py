from django.contrib import admin
from .models import Medecin, Patient, Message, Specialite
# Register your models here.
admin.site.register(Medecin)
admin.site.register(Patient)
admin.site.register(Message)
admin.site.register(Specialite)

