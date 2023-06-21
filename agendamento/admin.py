from django.contrib import admin
from .models import Medico, Consulta

@admin.register(Medico)
class MedicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nome_social', 'crm', 'especialidade')


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('data_hora', 'profissional', 'paciente', 'genero')