# Generated by Django 5.0 on 2024-02-02 01:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0033_remove_pantalla_anuncios_pantalla_anuncios'),
    ]

    operations = [
        migrations.AddField(
            model_name='cmsevent',
            name='anuncio_vinculado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pantallas_vinculadas', to='anuncios.anuncio'),
        ),
    ]