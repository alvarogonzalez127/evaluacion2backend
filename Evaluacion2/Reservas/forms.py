from django import forms
from django.forms import CharField, SelectDateWidget
from Reservas.models import reserva



class ReservasForm(forms.ModelForm):
    class Meta:
        model = reserva
        fields = '__all__'
    nombre = forms.CharField(label="Nombre",max_length=255, min_length=5, required=True)
    telefono = forms.IntegerField(label="Teléfono", required=True)
    fechareserva = forms.DateField(label="Fecha Reserva", required=True, widget=forms.SelectDateWidget)
    horareserva = forms.TimeField(label="Hora Reserva", required=True)
    cantidadpersonas = forms.IntegerField(label="Cantidad de personas", required=True)
    estado = forms.CharField(label="Estado", required=True)
    observacion = forms.CharField(label="Observaciones", required=True)
