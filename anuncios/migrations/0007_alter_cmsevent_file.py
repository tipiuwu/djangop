# Generated by Django 5.0 on 2024-01-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anuncios', '0006_cmsevent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cmsevent',
            name='file',
            field=models.FileField(null=True, upload_to='anunpantalla'),
        ),
    ]
