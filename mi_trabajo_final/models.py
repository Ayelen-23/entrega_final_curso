from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Artista(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_de_inicio = models.DateField()
    genero_musical = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mis_artistas')

    def __str__(self):
        return self.nombre
    
class Discos(models.Model):
    nombre = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    fecha_de_lanzamiento = models.DateField()
    
    def __str__(self):
        return self.nombre

class Instrumentos(models.Model):
    nombre = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
   
    
    def __str__(self):
        return self.nombre
    

class Canciones(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE, related_name='canciones')
    disco = models.CharField(max_length=100, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mis_canciones')
    

    def __str__(self):
        return self.titulo









