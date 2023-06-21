from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (MedicosAPIView, MedicoAPIView, ConsultasAPIView, ConsultaAPIView,
                   MedicoViewSet, ConsultaViewSet ) 


router = SimpleRouter()
router.register('medicos', MedicoViewSet)
router.register('consultas', ConsultaViewSet)


urlpatterns = [
    path('medicos/', MedicosAPIView.as_view(), name='medicos'),
    path('medicos/<int:pk>/', MedicoAPIView.as_view(), name='medico'),
    path('medicos/<int:medico_pk>/consultas/',ConsultasAPIView.as_view(), name='medico_consulta'),

    path('consultas/', ConsultasAPIView.as_view(), name='consultas'),
    path('consultas/<int:consulta_pk>', ConsultaAPIView.as_view(), name='consulta')
]