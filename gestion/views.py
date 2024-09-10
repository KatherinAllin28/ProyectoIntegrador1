from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Cliente
from django.contrib.auth.decorators import login_required
from . import forms
#from venta.models import Venta
from datetime import datetime 

import matplotlib.pyplot as plt
import matplotlib
import io
import base64

import google.generativeai as genai



@login_required(login_url="login")
def gestion(request):
    clientes = Cliente.objects.filter(author_id=request.user.id)
    return render(request, 'gestion.html',{'clientes':clientes})

@login_required(login_url="login")
def crearCliente(request):
    if request.method == 'POST':
        form = forms.CreateCliente(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author_id = request.user.id
            instance.save()
            return redirect('../gestion')
    else:
        form = forms.CreateCliente()
    return render(request, 'crearCliente.html', { 'form': form })

def delete(request,id):
    cliente = Cliente.objects.get(id = id)
    cliente.delete()
    return redirect("gestion")

@login_required(login_url="login")
def detalleCliente(request,id):
    cliente = Cliente.objects.get(id = id)

    return render(request, 'detalleCliente.html', {'detalle_cliente':cliente})