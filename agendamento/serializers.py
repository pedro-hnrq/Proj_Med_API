from rest_framework import serializers
from .models import Medico, Consulta

class ConsultaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Consulta
        fields = (
            'id',
            'data_hora',
            'profissional',
            'paciente',
            'genero',
        )


class MedicoSerializer(serializers.ModelSerializer):
    consultas = serializers.HyperlinkedRelatedField (
        many=True, read_only=True, view_name='consulta-detail')
    class Meta:
        model = Medico
        fields = (
            'id',
            'nome',
            'nome_social',
            'crm',
            'especialidade',
            'consultas'
        )