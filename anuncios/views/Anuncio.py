from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from ..models import Anuncio
from ..forms import AnuncioForm
from django.contrib import messages
from django.shortcuts import render, redirect
from ..forms import AnuncioForm
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


class AnuncioListView(ListView):
    model = Anuncio
    template_name = 'anuncios/index.html'
    context_object_name = 'anuncios'

class AnuncioCreateView(CreateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncios/create.html'
    # fields = '__all__'
    success_url = reverse_lazy('lista_anuncios')

class AnuncioUpdateView(UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncios/edit.html'
    success_url = reverse_lazy('lista_anuncios')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_update'] = True  # Esto puede ser útil en tu plantilla para saber si estás editando
        return context

class AnuncioShowView(UpdateView):
    model = Anuncio
    form_class = AnuncioForm
    template_name = 'anuncios/show.html'
    # fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for field in context['form'].fields.values():
            field.widget.attrs['disabled'] = True
        return context

    success_url = reverse_lazy('lista_anuncios')

class AnuncioDeleteView(DeleteView):
    model = Anuncio
    template_name = 'anuncios/delete.html'
    success_url = reverse_lazy('lista_anuncios')

def AnuncioDelete(request,id):
    anuncio = get_object_or_404(Anuncio, id=id)
    anuncio.delete()
    messages.success(request,"Anuncio eliminado correctamente")
    return redirect('lista_anuncios')