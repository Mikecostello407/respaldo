from django.shortcuts import render
from .models import Vehiculo, Categoria
from .forms import VehiculoForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def vista_vehiculos(request):
    vVehiculos = Vehiculo.objects.all()
    contexto = {'nombre':'Mike Costello', 'vehiculos':vVehiculos}
    return render(request, 'vehiculos.html', contexto)
    
def form_vehiculo(request):
    datos = {
        'form': VehiculoForm()
    }
    if request.method== 'POST':
        formulario = VehiculoForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardado correctamente"
    return render(request, 'form_vehiculo.html', datos)

def form_mod_vehiculo(request, id):
    vehiculo = Vehiculo.objects.get(patente=id)
    wir = {
        'form': VehiculoForm(instance=vehiculo)
    }
    return render(request, 'form_mod_vehiculo.html', wir)