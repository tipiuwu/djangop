# views/resumen.py
from django.shortcuts import render
from anuncios.models import Pantalla
from ..models import Anuncio
from ..forms import PantallaForm  # Asegúrate de importar el formulario correcto
from django.contrib.auth.models import User

def resumen(request):
    anuncios_activos_count = Anuncio.objects.filter(listo=True).count()
    pantallas_activas = Pantalla.objects.filter(estado=True)
    pante_true = Pantalla.objects.filter(estado=True)
    pante_false = Pantalla.objects.filter(estado=False)
    pante_all = Pantalla.objects.all()
    pantalla = pante_true.first()
    salidas_minimas = pantalla.salidas_minimas_por_hora
    tiempo_cada_espacio = pantalla.tiempo_cada_espacio_seg
    
    # Obtén la lista de usuarios y anuncios
    usuarios = User.objects.all()
    anuncios = Anuncio.objects.all()

    context = {
        'anuncios_activos_count': anuncios_activos_count,
        'pantallas_activas': pantallas_activas,
        'pante_true': pante_true,
        'pante_false': pante_false,
        'pante_all': pante_all,
        'some_variable_from_view': 'Esta es una variable desde la vista de resumen.',
        'grafica_data': {
            'salidas_minimas': salidas_minimas,
            'tiempo_cada_espacio': tiempo_cada_espacio,
        'usuarios': usuarios,

        },
        'usuarios': usuarios,
        'anuncios': anuncios,
    }
    return render(request, 'resumen/resumen.html', context)
