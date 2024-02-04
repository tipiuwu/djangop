# models.py
from django.db import models
from django.contrib.auth.models import User

class Anuncio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    OPCIONES_ENUM = (
        ('Archivo', 'Archivo'),
        ('Widgets', 'Widgets'),
        ('Lista Inteligente', 'Lista Inteligente'),
    )
    tipo = models.CharField(max_length=17, choices=OPCIONES_ENUM)
    file = models.FileField(upload_to="videos_imagenes", null=True)
    audio_en_video = models.BooleanField()
    listo = models.BooleanField()
    alta = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class Pantalla(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    imagen = models.ImageField(upload_to='ruta_de_guardado/', max_length=100)
    estado = models.BooleanField()
    ancho_en_pixeles = models.IntegerField()
    alto_en_pixeles = models.IntegerField()
    tiempo_cada_espacio_seg = models.IntegerField()
    nro_espacios_publicitarios = models.IntegerField()
    salidas_minimas_por_hora = models.IntegerField()
    lunes = models.BooleanField()
    martes = models.BooleanField()
    miercoles = models.BooleanField()
    jueves = models.BooleanField()
    viernes = models.BooleanField()
    sabado = models.BooleanField()
    domingo = models.BooleanField()
    anuncios = models.ManyToManyField(Anuncio, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    latitud = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    longitud = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pantallas')

    def __str__(self):
        return str(self.nombre)
