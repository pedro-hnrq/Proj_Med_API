from rest_framework import generics, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Medico, Consulta
from .serializers import MedicoSerializer, ConsultaSerializer

""""
API V1
"""


class MedicosAPIView(generics.ListCreateAPIView):
    """
    API Medico - Listar e Criar
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    


class MedicoAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API Medico - Atualizar e Deletar
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class ConsultasAPIView(generics.ListCreateAPIView):
    """
    API Consulta - Listar e Criar
    """
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        if self.kwargs.get('medico_pk'):
            return self.queryset.filter(profissional=self.kwargs.get('medico_pk'))
        return self.queryset.all()


class ConsultaAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    API Consulta - Atualizar e Deletar
    """
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    


# TODO: poderá realizar novas implementações no API entrando as novas versões para se consumidas. 

""""
API V2
"""

class MedicoViewSet(viewsets.ModelViewSet):
    """
    API Medico - Listar e Criar
    """
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer

    @action(detail=True, methods=['get'])
    def consultas(self, request, pk=None):
        profissional = self.get_object()
        serializer = ConsultaSerializer(profissional.consultas.all(), many=True)
        return Response(serializer.data)


class ConsultaViewSet(viewsets.ModelViewSet):
    """
    API Consulta - Listar e Criar
    """
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

    def get_queryset(self):
        if self.kwargs.get('medico_pk'):
            return self.queryset.filter(profissional=self.kwargs.get('medico_pk'))
        return self.queryset.all()

