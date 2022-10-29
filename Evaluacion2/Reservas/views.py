from django.shortcuts import redirect, render
from Reservas.forms import ReservasForm
from Reservas.models import reserva

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listadoReservas(request):
    Reservas = reserva.objects.all()
    data = {'Reserva': Reservas}
    return render(request,'reservas.html',data)

def agregarReserva(request):
    form = ReservasForm()
    if request.method == 'POST':
        form = ReservasForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)

def eliminarReserva(request,id):
    reservas = reserva.objects.get(id = id)
    reservas.delete()
    return redirect('/reservas')

def actualizarReserva(request,id):
    reservas = reserva.objects.get(id = id)
    form = ReservasForm(instance=reservas)
    if request.method == 'POST':
        form = ReservasForm(request.POST, instance=reservas)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarreserva.html', data)