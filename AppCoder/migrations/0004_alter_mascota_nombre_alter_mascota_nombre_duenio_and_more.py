# Generated by Django 4.1.7 on 2023-04-09 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_mascota_raza'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='nombre',
            field=models.CharField(default='No tiene', max_length=20),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='nombre_duenio',
            field=models.CharField(default='No tiene', max_length=20),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='raza',
            field=models.CharField(default='Desconocida', max_length=20),
        ),
    ]