# Generated by Django 5.0 on 2024-01-26 20:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0025_remove_anuncio_pantalla_remove_cmsevent_pantalla_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pantalla',
            name='anuncios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='anuncios_pantalla', to='anuncios.anuncio'),
        ),
    ]
