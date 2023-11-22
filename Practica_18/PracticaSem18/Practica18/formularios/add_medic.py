from django import forms

class MedicForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellidos = forms.CharField(max_length=100)
    especialidad = forms.CharField(max_length=100)
