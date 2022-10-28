from django import forms
from templateApp.models import reservas

class FormsReserva(forms.ModelForm):
    class Meta:
        model = reservas
        fields = '__all__'