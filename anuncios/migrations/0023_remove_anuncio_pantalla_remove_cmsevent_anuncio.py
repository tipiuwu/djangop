# Generated by Django 5.0 on 2024-01-26 20:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0022_cmsevent_anuncio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anuncio',
            name='Pantalla',
        ),
        migrations.RemoveField(
            model_name='cmsevent',
            name='Anuncio',
        ),
    ]
