# Generated by Django 5.2.3 on 2025-07-23 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_trabajo_final', '0003_canciones'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='canciones',
            name='duracion',
        ),
        migrations.RemoveField(
            model_name='canciones',
            name='fecha_lanzamiento',
        ),
        migrations.AddField(
            model_name='canciones',
            name='disco',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
