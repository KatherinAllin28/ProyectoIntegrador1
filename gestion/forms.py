from django import forms
from . import models

class CreateCliente(forms.ModelForm):
    class Meta:
        model = models.Cliente
        fields = ['nombreCliente', 'emailCliente', 'telefonoCliente','idCliente']