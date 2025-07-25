from django.contrib import admin
from .models import Artista, Discos, Instrumentos, Canciones

# Register your models here
register_models = [Artista, Discos, Instrumentos, Canciones]

admin.site.register(register_models)