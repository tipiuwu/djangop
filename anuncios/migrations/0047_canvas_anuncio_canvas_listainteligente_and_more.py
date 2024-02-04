# Generated by Django 5.0 on 2024-02-03 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0046_remove_anuncio_multiplefile_remove_anuncio_tipo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Canvas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('tipo1', 'Tipo 1'), ('tipo2', 'Tipo 2')], max_length=20)),
                ('nombre', models.CharField(max_length=200)),
                ('carpetas', models.CharField(max_length=200)),
                ('widget', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='anuncio',
            name='canvas',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='anuncios.canvas'),
        ),
        migrations.CreateModel(
            name='ListaInteligente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('tipoA', 'Tipo A'), ('tipoB', 'Tipo B')], max_length=20)),
                ('nombre', models.CharField(max_length=200)),
                ('carpetas', models.CharField(max_length=200)),
                ('modo_reproduccion', models.CharField(max_length=50)),
                ('files', models.ManyToManyField(related_name='lista_inteligente_files', to='anuncios.anuncio')),
            ],
        ),
        migrations.AddField(
            model_name='anuncio',
            name='lista_inteligente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='anuncios.listainteligente'),
        ),
    ]
