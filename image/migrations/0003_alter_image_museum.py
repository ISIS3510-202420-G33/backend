# Generated by Django 5.1.1 on 2024-09-17 19:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_image_museum'),
        ('museum', '0003_remove_museum_artworks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='museum',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='museum.museum'),
        ),
    ]
