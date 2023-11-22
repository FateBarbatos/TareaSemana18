from django import forms
from Practica18.models import Medicos

class add_paciente(forms.Form):
    Nombre = forms.CharField(max_length=100)
    Apellidos = forms.CharField(max_length=100)
    sexo = (
        ('Masculino',u'Masculino'),
        ('Femenino',u'Femenino'),
        ('Otro',u'Otro'),
        )
    Sexo = forms.ChoiceField(choices=sexo)
    altura = forms.FloatField()