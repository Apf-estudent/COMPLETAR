from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento

def lista_medicamento(request):
    medicamento = Medicamento.objects.all()
    return render(request, "lista_medicamento.html", {"medicamento": medicamento})

# 2. Vista para el formulario de alta
def alta_medicamento(request):

    return render(request, "alta_medicamento.html")

def eliminacion_medicamento(request, id_medicamento):
    medicamento = get_object_or_404(Medicamento, pk=id_medicamento)
    medicamento.delete()
    return redirect('lista_medicamento')

def modificaciones_medicamento(request, id_medicamento):
    medicamento = get_object_or_404(Medicamento, pk=id_medicamento)
    return render(request, "modificaciones_medicamento.html", {"medicamento": medicamento})