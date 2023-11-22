from django.shortcuts import render
from .models import Medicos,Paciente
from .formularios import add_medic as fm
from .formularios import add_paciente as fp
from django.http import HttpResponseRedirect

# Create your views here.
#view para la pagina principal
def index(request):
    return render(request,"index.html")

#view para la lista de medicos
def lis_med(request):
    medicos = Medicos.objects.all()
    return render(request,"lismed.html",{"lismed":medicos})

#view para agregar nuevos medicos
def add_medic(request):
    if request.method == "POST":
        formulario = fm.MedicForm(request.POST)
        if formulario.is_valid():
            nuevo_reg = Medicos()
            nuevo_reg.Nombre = formulario.data["nombre"]
            nuevo_reg.Apellidos = formulario.data["apellidos"]
            nuevo_reg.Especialidad = formulario.data["especialidad"]
            nuevo_reg.save()
            return HttpResponseRedirect("/")
    else:
        formulario = fm.MedicForm()
        return render(request,"add_med.html",{"form":formulario})
    
#view para listar todos los pacientes
def lis_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request,"lispad.html",{'lispad':pacientes})

#view para agregar nuevos pacientes al sistema
def ag_pacientes(request):
    medicos = Medicos.objects.all()
    if request.method == 'POST':
        formulario = fp.add_paciente(request.POST)
        if formulario.is_valid():
            nuevo_reg = Paciente()
            nuevo_reg.Nombre = formulario.data['Nombre']
            nuevo_reg.Apellidos = formulario.data['Apellidos']
            nuevo_reg.fecha_nacimiento = request.POST['date_of_birth']
            nuevo_reg.sexo = formulario.data['Sexo']
            nuevo_reg.altura = formulario.data['altura']
            medico = Medicos.objects.get(id=(request.POST['medicos']))
            print(type(medico))
            nuevo_reg.medico_id = medico
            nuevo_reg.save()
            return HttpResponseRedirect('/')
    else:
        formulario = fp.add_paciente()
        return render(request,'add_paciente.html',{'form':formulario,'medics':medicos})
