# forms.py
from django import forms
from .models import Pantalla, Anuncio

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BaseForm, self).__init__(*args, **kwargs)
        
        for field_name in self.fields:
            field = self.fields[field_name]
            widget = field.widget
            attrs = widget.attrs
            
            if 'class' in attrs:
                attrs['class'] += ' form-control'
            else:
                attrs['class'] = 'form-control'
class PantallaForm(BaseForm):
    class Meta:
        model = Pantalla
        fields = [
            'id',
            'imagen',
            'nombre',
            'estado',
            'ancho_en_pixeles',
            'alto_en_pixeles',
            'tiempo_cada_espacio_seg',
            'nro_espacios_publicitarios',
            'salidas_minimas_por_hora',
            'lunes',
            'martes',
            'miercoles',
            'jueves',
            'viernes',
            'sabado',
            'domingo',
            'latitud',
            'longitud',
            'usuario',
        ]




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['imagen'].widget.attrs.update({'accept': 'image/*'})
class AnuncioForm(BaseForm):
    class Meta:
        model = Anuncio
        fields = '__all__'

from django_select2.forms import Select2MultipleWidget

class AnuncioPantallaForm(forms.ModelForm):
    class Meta:
        model = Pantalla
        fields = ['anuncios']
        widgets = {
            'anuncios': Select2MultipleWidget(attrs={'data-dropdown-auto-width': 'true'})
        }
