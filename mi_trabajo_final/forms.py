import datetime
from django import forms
from .models import Canciones

ANIO_ACTUAL = datetime.date.today().year

class ArtistaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    nacionalidad = forms.CharField(max_length=100)
    fecha_de_inicio = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, ANIO_ACTUAL +1)))
    genero_musical = forms.CharField(max_length=100, required=False)

class DiscosForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    artista=forms.CharField(max_length=100)
    fecha_de_lanzamiento = forms.DateField(widget=forms.SelectDateWidget(years=range(1900, ANIO_ACTUAL +1)))

class InstrumentosForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    tipo = forms.CharField(max_length=100)
    descripcion = forms.CharField(widget=forms.Textarea, max_length=500)
     
    
class CancionesForm(forms.ModelForm):
    class Meta:
        model = Canciones
        fields = ("titulo", "artista", "disco")
