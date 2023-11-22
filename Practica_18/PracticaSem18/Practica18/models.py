from django.db import models

# Create your models here.

class Medicos(models.Model):
    Nombre = models.TextField()
    Apellidos = models.TextField()
    Especialidad = models.TextField()

    #metodo string del modelo

class Paciente(models.Model):
    Nombre = models.TextField()
    Apellidos = models.TextField()
    fecha_nacimiento = models.TextField
    sexo = models.TextField()
    altura = models.FloatField()
    medico_id = models.ForeignKey(Medicos,on_delete=models.CASCADE)
    
    #metodo string para los modelos