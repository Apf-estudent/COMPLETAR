from django.contrib import admin
from .models import Estado, Nivel_Riesgo, Medicamento

admin.site.register(Estado)
admin.site.register(Nivel_Riesgo)
admin.site.register(Medicamento)

# Register your models here.
