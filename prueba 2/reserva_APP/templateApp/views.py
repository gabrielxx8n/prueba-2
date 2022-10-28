from cgitb import reset
from django.shortcuts import render, redirect

import templateApp
from templateApp.models import reservas
from templateApp.forms import FormsReserva

# Create your views here.
def index(request):
    return render(request,'index.html')

def listaReserva(request):
    reservate = reservas.objects.all()
    data = {'reservate' : reservate}
    return render(request, 'reserva.html', data) 

def agregarReserva(request):
    form = FormsReserva()
    if request.method == 'POST':
        form = FormsReserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarReserva.html', data)

def actualizarReserva(request, id):
        rese = reservas.objects.get(id = id)
        form = FormsReserva(instance=rese)
        if request.method == 'POST':
            form = FormsReserva(request.POST, instance=rese)
            if form.is_valid():
                form.save()
            return index(request)
        data = {'form': form}
        return render(request, 'agregarReserva.html', data)

def eliminarReserva(request, id):
        rese = reservas.objects.get(id = id)
        rese.delete()
        return redirect('/reserva')