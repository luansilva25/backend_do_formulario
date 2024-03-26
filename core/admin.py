from django.contrib import admin
from .models import Formulario, Hobbies, Linguagens, Estados

class Formulario:
    admin.site.register(Formulario)
    admin.site.register(Hobbies)
    admin.site.register(Linguagens),
    admin.site.register(Estados)

