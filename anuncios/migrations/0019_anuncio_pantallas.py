# Generated by Django 5.0 on 2024-01-26 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0018_remove_cmsevent_fecha_final1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='pantallas',
            field=models.ManyToManyField(related_name='anuncios', to='anuncios.pantalla'),
        ),
    ]
