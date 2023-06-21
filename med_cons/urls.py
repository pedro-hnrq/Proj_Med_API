from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # DRF Admin
    path('api-auth/', include('rest_framework.urls')),
    #DRF Endepoints
    path('api/v1/', include('agendamento.urls')),
]
