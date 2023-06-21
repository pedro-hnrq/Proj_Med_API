from django.db import models
from .choices import GeneroChoi

class Medico(models.Model):
    nome = models.CharField(max_length=100)
    nome_social = models.CharField(max_length=100)
    crm = models.CharField(max_length=25, unique=True)
    especialidade = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f'Nome do médico: {self.nome} - CRM: {self.crm}'


class Consulta(models.Model):
    data_hora = models.DateTimeField()
    profissional = models.ForeignKey(Medico, related_name='consultas', on_delete=models.CASCADE)
    paciente = models.CharField(max_length=100)
    genero = models.CharField(max_length=2, choices=GeneroChoi.choices)

    def __str__(self):
        return f"Consulta ficou marcado {self.data_hora} com o Médico {self.profissional.nome_social}"
