# Generated by Django 5.0 on 2024-02-02 01:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0036_remove_pantalla_anuncios_pantalla_anuncios'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoAnuncioPantalla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(null=True, upload_to='archivos_anuncios')),
                ('anuncio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anuncios.anuncio')),
                ('pantalla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='anuncios.pantalla')),
            ],
        ),
        migrations.AddField(
            model_name='pantalla',
            name='archivos_anuncios',
            field=models.ManyToManyField(related_name='pantallas_archivos', through='anuncios.ArchivoAnuncioPantalla', to='anuncios.anuncio'),
        ),
    ]
