# Generated by Django 5.2.3 on 2025-07-25 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mi_trabajo_final', '0010_discos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrumentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('descripcion', models.TextField(max_length=500)),
            ],
        ),
    ]
