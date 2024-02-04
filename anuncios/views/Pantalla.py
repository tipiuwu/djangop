from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Pantalla
from ..forms import PantallaForm
from django.contrib import messages
import json
from ..models import Anuncio
# views.py
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic.edit import UpdateView
from ..models import Pantalla
from ..forms import PantallaForm
# views.py
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from ..models import Pantalla
from ..forms import AnuncioPantallaForm

class PantallaDetailView(DetailView):
    model = Pantalla
    template_name = 'pantallas/detail.html'
    context_object_name = 'pantalla'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anuncio_form'] = AnuncioPantallaForm()
        return context


class PantallaShowView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/show.html'
    success_url = reverse_lazy('lista_pantallas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pantalla = self.object

        # Obtén los anuncios asociados a la pantalla
        anuncios_asociados = pantalla.anuncios.all()

        # Agrega el formulario de Anuncio
        anuncio_form = AnuncioForm()
        context['anuncio_form'] = anuncio_form

        context['anuncios_asociados'] = anuncios_asociados
        return context

    def post(self, request, *args, **kwargs):
        pantalla = self.get_object()
        anuncio_form = AnuncioForm(request.POST, request.FILES)

        if anuncio_form.is_valid():
            nuevo_anuncio = anuncio_form.save()
            pantalla.anuncios.add(nuevo_anuncio)

        return super().get(request, *args, **kwargs)
        
class PantallaListView(ListView):
    model = Pantalla
    template_name = 'pantallas/index.html'
    context_object_name = 'pantallas'

class PantallaCreateView(CreateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/create.html'
    # fields = '__all__'
    success_url = reverse_lazy('resumen')


# views.py
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from ..models import Pantalla
from ..forms import PantallaForm  # Asegúrate de importar tu formulario
from anuncios.models import Anuncio  # Ajusta según la ubicación de tu modelo Anuncio
from django.urls import reverse
class PantallaUpdateView(UpdateView):
    model = Pantalla
    form_class = AnuncioPantallaForm
    template_name = 'pantallas/edit.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anuncios'] = Anuncio.objects.all()
        context['form'] = self.get_form()  # Asegura que el formulario esté en el contexto
        return context


    def form_valid(self, form):
        # Llamamos al método form_valid de la superclase para realizar
        # el procesamiento predeterminado y obtener la respuesta.
        response = super().form_valid(form)

        # Obtener los IDs de los anuncios seleccionados
        anuncios_seleccionados_ids = self.request.POST.getlist('anuncios', [])

        # Limpiar los anuncios asociados previamente a la pantalla
        self.object.anuncios.clear()

        # Asignar los anuncios seleccionados a la pantalla
        for anuncio_id in anuncios_seleccionados_ids:
            anuncio_seleccionado = Anuncio.objects.get(id=anuncio_id)
            self.object.anuncios.add(anuncio_seleccionado)

        # Retornar la respuesta
        return response

    def get_success_url(self):
        # Obtener la URL de la pantalla actual usando su ruta 'mostrar_pantalla'
        return reverse('editar_pantalla', args=[str(self.object.pk)])
    
class PantallaShowView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/show.html'
    # fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for field in context['form'].fields.values():
            field.widget.attrs['disabled'] = True
        return context

    success_url = reverse_lazy('lista_pantallas')

class PantallaDeleteView(DeleteView):
    model = Pantalla
    template_name = 'pantallas/delete.html'
    success_url = reverse_lazy('lista_pantallas')

def PantallaDelete(request,id):
    pantalla = get_object_or_404(Pantalla, id=id)
    pantalla.delete()
    messages.success(request,"Pantalla eliminado correctamente")
    return redirect('lista_pantallas')
class PantallaShowView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/show.html'
    success_url = reverse_lazy('lista_pantallas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for field in context['form'].fields.values():
            field.widget.attrs['disabled'] = True
        
        # Obtén los datos necesarios
        salidas_minimas = self.object.salidas_minimas_por_hora
        tiempo_cada_espacio = self.object.tiempo_cada_espacio_seg

        # Añade los datos al contexto en formato JSON
        context['data'] = json.dumps({
            'salidas_minimas': salidas_minimas,
            'tiempo_cada_espacio': tiempo_cada_espacio,
        })
        
        return context

class PantallaListView(ListView):
    model = Pantalla
    template_name = 'pantallas/index.html'
    context_object_name = 'pantallas'

class PantallaCreateView(CreateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/create.html'
    # fields = '__all__'
    success_url = reverse_lazy('resumen')


class PantallaShowView(UpdateView):
    model = Pantalla
    form_class = PantallaForm
    template_name = 'pantallas/show.html'
    success_url = reverse_lazy('lista_pantallas')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Deshabilitar los campos de PantallaForm
        for field in context['form'].fields.values():
            field.widget.attrs['disabled'] = True

        return context
class PantallaDeleteView(DeleteView):
    model = Pantalla
    template_name = 'pantallas/delete.html'
    success_url = reverse_lazy('lista_pantallas')

def PantallaDelete(request,id):
    pantalla = get_object_or_404(Pantalla, id=id)
    pantalla.delete()
    messages.success(request,"Pantalla eliminado correctamente")
    return redirect('lista_pantallas')