# Generated by Django 5.0 on 2024-02-02 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0034_cmsevent_anuncio_vinculado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cmsevent',
            name='anuncio_vinculado',
        ),
    ]
