from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404
from .models import Medicamento 
from django.conf.urls.static import static
from . import views
from django.urls import path


urlpatterns = [
    path('medicamento/lista_medicamento/', views.lista_medicamento, name='lista_medicamento'),
    path('medicamento/alta_medicamento/', views.alta_medicamento, name='alta_medicamento'),
    path('eliminacion_medicamento/<int:id_medicamento>/', views.eliminacion_medicamento, name='eliminacion_medicamento'),
    path('modificaciones_medicamento/<int:id_medicamento>/', views.modificaciones_medicamento, name='modificaciones_medicamento'),
     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

def lista_medicamento(request):
    # Aquí puedes buscar los medicamentos de la base de datos más adelante
    return render(request, 'medicamento/lista_medicamento.html')

def alta_medicamento(request):
    return render(request, 'medicamento/alta_medicamento.html')

def eliminacion_medicamento(request, id_medicamento):
    # Lógica para eliminar aquí
    return redirect('lista_medicamento')

def modificaciones_medicamento(request, id_medicamento):
    return render(request, 'medicamento/modificaciones_medicamento.html')