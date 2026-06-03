from django.contrib import admin

from .models import Hueco, Deposito, Supervisor, Medicamento

admin.site.register(Hueco)
admin.site.register(Deposito)
admin.site.register(Supervisor)
admin.site.register(Medicamento)
# Register your models here.
