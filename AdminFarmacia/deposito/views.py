from collections import defaultdict
from tempfile import template
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from matplotlib.style import context
from .models import *

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse
# Importamos todos tus modelos explícitamente para evitar errores
from .models import Deposito, Supervisor, Medicamento, Hueco  

# Create your views here.
def inicio(request):
    return render(request, "pagina_base/inicio.html")


# ==========================================
# FUNCIONES PARA DEPÓSITO
# ==========================================
def lista_deposito(request):
    depositos = Deposito.objects.all()
    return render(request, "lista_deposito.html", {"depositos": depositos})


def alta_deposito(request):
    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        if descripcion:
            deposito = Deposito(descripcion=descripcion)
            deposito.save()
        return redirect("lista_deposito")

    depositos = Deposito.objects.all()
    return render(request, "alta_deposito.html", {"depositos": depositos})


def eliminacion_deposito(request, id_deposito):
    deposito = get_object_or_404(Deposito, id_deposito=id_deposito)
    if request.method == "POST":
        deposito.delete()
        return redirect("lista_deposito")
    return render(request, "elimina_deposito.html", {"deposito": deposito})


def modificaciones_deposito(request, id_deposito):
    deposito = get_object_or_404(Deposito, id_deposito=id_deposito)
    if request.method == "POST":
        descripcion = request.POST.get("descripcion")
        if descripcion:
            deposito.descripcion = descripcion
            deposito.save()
        return redirect("lista_deposito")
    return render(request, "modificacion_deposito.html", {"deposito": deposito})


# ==========================================
# FUNCIONES PARA HUECO
# ==========================================
def lista_hueco(request):
    huecos = Hueco.objects.all()
    return render(request, "lista_hueco.html", {"huecos": huecos})


def alta_hueco(request):
    # Aquí irá tu lógica para crear un hueco más adelante
    return render(request, "alta_hueco.html")


def eliminacion_hueco(request, id_hueco):
    hueco = get_object_or_404(Hueco, id_hueco=id_hueco)
    hueco.delete()
    return redirect('lista_hueco')


def modificaciones_hueco(request, id_hueco):
    hueco = get_object_or_404(Hueco, id_hueco=id_hueco)
    return render(request, "modificaciones_hueco.html", {"hueco": hueco})


# ==========================================
# FUNCIONES PARA SUPERVISOR
# ==========================================
def lista_supervisor(request):
    supervisores = Supervisor.objects.all()
    return render(request, "lista_supervisor.html", {"supervisores": supervisores})


def alta_supervisor(request):
    return render(request, "alta_supervisor.html")


def eliminacion_supervisor(request, id_supervisor):
    pass


def modificacion_supervisor(request, id_supervisor):
    pass


# ==========================================
# FUNCIONES PARA MEDICAMENTO
# ==========================================
def lista_medicamento(request):
    medicamento = Medicamento.objects.all()
    return render(request, "lista_medicamento.html", {"medicamento": medicamento})


def alta_medicamento(request):
    return render(request, "alta_medicamento.html")


def eliminacion_medicamento(request, id_medicamento):
    pass


def modificaciones_medicamento(request, id_medicamento):
    pass