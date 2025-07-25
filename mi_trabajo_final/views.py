from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import ArtistaForm, CancionesForm, DiscosForm, InstrumentosForm
from .models import Artista, Canciones, Discos, Instrumentos
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.
def inicio(request):
    return render(request, 'mi_trabajo_final/inicio.html')

def about(request):
    return render(request, 'mi_trabajo_final/about.html')


#Artistas

@login_required
def agregar_artista(request):
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            nuevo_artista = Artista(
            nombre = form.cleaned_data['nombre'],
            nacionalidad = form.cleaned_data['nacionalidad'],
            fecha_de_inicio = form.cleaned_data['fecha_de_inicio'],
            genero_musical = form.cleaned_data['genero_musical']
            )
            nuevo_artista.usuario = request.user

            nuevo_artista.save()
            return redirect('inicio')

    else:
        form = ArtistaForm()
    return render(request, 'mi_trabajo_final/agregar_artista.html', {'form': form})


def artistas(request):
    Artistas = Artista.objects.all()
    return render(request, 'mi_trabajo_final/artistas.html', {'artistas': Artistas})

def buscar_artistas(request):
    if request.method == 'GET':
        nombre = request.GET.get('nombre', '').strip()
        Artistas = []
        if nombre:
            Artistas = Artista.objects.filter(nombre__icontains=nombre)
        return render(request, 'mi_trabajo_final/artistas.html', {'artistas': Artistas, 'nombre': nombre})
    
class ArtistasUpdateView(UpdateView):
    model = Artista
    form_class = ArtistaForm
    template_name = 'mi_trabajo_final/agregar_artistas.html'
    success_url = reverse_lazy('lista_artistas')

class ArtistasListView(LoginRequiredMixin,ListView):
    model = Artista
    template_name = 'mi_trabajo_final/lista_artistas.html'
    context_object_name = 'artistas'
    def get_queryset(self):
        return Artista.objects.filter(usuario=self.request.user)

class ArtistasDetailView(DetailView):
    model = Artista
    template_name = 'mi_trabajo_final/detalle_artista.html'
    context_object_name = 'artista'

class ArtistaDeleteView(LoginRequiredMixin,DeleteView):
    model = Artista
    template_name = 'mi_trabajo_final/eliminar_artista.html'
    success_url = reverse_lazy('lista_artistas')

#Discos
def agregar_instrumentos(request):
    if request.method == 'POST':
        form = InstrumentosForm(request.POST)
        if form.is_valid():
            nuevo_instrumento = Instrumentos(
            nombre= form.cleaned_data['nombre'],
            tipo = form.cleaned_data['tipo'],
            descripcion = form.cleaned_data['descripcion']
            )
            nuevo_instrumento.save()
            return redirect('inicio')
    else:
        form = InstrumentosForm()
    return render(request, 'mi_trabajo_final/agregar_instrumentos.html', {'form': form})

def agregar_discos(request):
    if request.method == 'POST':
        form = DiscosForm(request.POST)
        if form.is_valid():
            nuevo_disco = Discos(
            nombre = form.cleaned_data['nombre'],
            artista = form.cleaned_data['artista'],
            fecha_de_lanzamiento = form.cleaned_data['fecha_de_lanzamiento']
            )
            nuevo_disco.save()
            return redirect('inicio')
    else:
        form = DiscosForm()
    return render(request, 'mi_trabajo_final/agregar_discos.html', {'form': form})


#Canciones



class CancionesListView(LoginRequiredMixin,ListView):
    model = Canciones
    template_name = 'mi_trabajo_final/lista_canciones.html'
    context_object_name = 'canciones'
    def get_queryset(self):
        return Canciones.objects.filter(usuario=self.request.user)
    


class CancionesCreateView(LoginRequiredMixin,CreateView):
    model = Canciones
    form_class = CancionesForm
    template_name = 'mi_trabajo_final/agregar_canciones.html'
    success_url = reverse_lazy('lista_canciones')
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)

class CancionesDetailView(LoginRequiredMixin,DetailView):
    model = Canciones
    template_name = 'mi_trabajo_final/detalle_canciones.html'
    context_object_name = 'cancion'

class CancionesUpdateView(LoginRequiredMixin,UpdateView):
    model = Canciones
    form_class = CancionesForm
    template_name = 'mi_trabajo_final/agregar_canciones.html'
    success_url = reverse_lazy('lista_canciones')

class CancionesDeleteView(LoginRequiredMixin,DeleteView):
    model = Canciones
    template_name = 'mi_trabajo_final/eliminar_canciones.html'
    success_url = reverse_lazy('lista_canciones')
    
#BLogs


