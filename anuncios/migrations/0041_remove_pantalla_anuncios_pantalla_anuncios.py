# Generated by Django 5.0 on 2024-02-02 13:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0040_remove_pantalla_anuncios_pantalla_anuncios'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pantalla',
            name='anuncios',
        ),
        migrations.AddField(
            model_name='pantalla',
            name='anuncios',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='anuncios.anuncio'),
        ),
    ]
