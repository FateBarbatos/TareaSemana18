# Generated by Django 4.2.7 on 2023-11-21 02:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.TextField()),
                ('Apellidos', models.TextField()),
                ('Especialidad', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.TextField()),
                ('Apellidos', models.TextField()),
                ('fecha_nacimiento', models.DateField()),
                ('sexo', models.TextField()),
                ('altura', models.FloatField()),
                ('medico_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Practica18.medicos')),
            ],
        ),
    ]
