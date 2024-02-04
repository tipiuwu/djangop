from django.urls import path
from .views import Resumen
from .views.Pantalla import PantallaListView, PantallaCreateView, PantallaUpdateView, PantallaShowView, PantallaDeleteView, PantallaDelete,PantallaDetailView
from .views.Anuncio import AnuncioListView, AnuncioCreateView, AnuncioUpdateView, AnuncioShowView, AnuncioDeleteView, AnuncioDelete,PantallaDetailView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... Otras rutas existentes ...
    path('resumen/', Resumen.resumen, name='resumen'),  # Esta línea es suficiente
    path('pantallas/', PantallaListView.as_view(), name='lista_pantallas'),
    path('pantallas/agregar/', PantallaCreateView.as_view(), name='agregar_pantalla'),
    path('pantallas/editar/<pk>', PantallaUpdateView.as_view(), name='editar_pantalla'),
    path('pantallas/mostrar/<pk>', PantallaShowView.as_view(), name='mostrar_pantalla'),
    path('pantallas/eliminar/<id>', PantallaDelete, name='eliminar_pantalla'),
    path('anuncios/', AnuncioListView.as_view(), name='lista_anuncios'),
    path('anuncios/agregar/', AnuncioCreateView.as_view(), name='agregar_anuncio'),
    path('anuncios/editar/<pk>', AnuncioUpdateView.as_view(), name='editar_anuncio'),
    path('anuncios/mostrar/<pk>', AnuncioShowView.as_view(), name='mostrar_anuncio'),
    path('anuncios/eliminar/<id>', AnuncioDelete, name='eliminar_anuncio'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)