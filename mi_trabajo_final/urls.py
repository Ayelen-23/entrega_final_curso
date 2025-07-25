
from django.urls import path
from .views import (inicio, agregar_artista, artistas, buscar_artistas, agregar_discos, agregar_instrumentos, about,
                    CancionesCreateView, CancionesListView, CancionesDeleteView,CancionesDetailView, CancionesUpdateView
                    , ArtistasDetailView, ArtistasUpdateView, ArtistaDeleteView, ArtistasListView) 

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar_artista/', agregar_artista, name='agregar_artista'),
    path('artistas/', artistas, name='artistas'),
    path('buscar_artistas/', buscar_artistas, name='buscar_artistas'),
    path('agregar_artista/', agregar_artista, name='agregar_artista'),
    path('discos/', agregar_discos, name='discos'),
    path('instrumentos/', agregar_instrumentos, name='instrumentos'),
    path('about/' , about, name='about'),
    path('detalle_artista/<int:pk>/', ArtistasDetailView.as_view(), name='detalle_artista'),
    path('editar_artista/<int:pk>/', ArtistasUpdateView.as_view(), name='editar_artista'),
    path('eliminar_artista/<int:pk>/', ArtistaDeleteView.as_view(), name='eliminar_artista'),
    path('lista_artista/', ArtistasListView.as_view(), name='lista_artistas'),
    path('lista_canciones/', CancionesListView.as_view(), name='lista_canciones'),
    path('agregar_canciones/', CancionesCreateView.as_view(), name='agregar_canciones'),
    path('detalle_canciones/<int:pk>/', CancionesDetailView.as_view(), name='detalle_canciones'),
    path('editar_canciones/<int:pk>/', CancionesUpdateView.as_view(), name='editar_canciones'),
    path('eliminar_canciones/<int:pk>/', CancionesDeleteView.as_view(), name='eliminar_canciones'),
]

