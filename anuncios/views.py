# from django.http import HttpResponse


# def index(request):
#     return HttpResponse("Este es index en Anuncios ...")


# views.py
from django.shortcuts import render
# views.py
from django.shortcuts import render
from .models import Pantalla
# views.py
# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Pantalla
from .forms import AnuncioPantallaForm

class PantallaDetailView(DetailView):
    model = Pantalla
    template_name = 'pantallas/detail.html'
    context_object_name = 'pantalla'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anuncio_form'] = AnuncioPantallaForm()
        return context

def lista_pantallas(request):
    cantidad_pantallas = Pantalla.objects.count()

    context = {
        'cantidad_pantallas': cantidad_pantallas,
    }

    return render(request, 'anuncios\templates\resumen\resumen.html', context)

def index(request):
    context = {
        'some_variable_from_view': 'Esta es una variable desde la vista de anuncios.',
    }
    return render(request, 'anuncios/anuncios_index.html', context)
