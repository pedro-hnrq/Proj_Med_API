from django.contrib import admin
from django.urls import path, include
from agendamento.urls import router
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    # DRF Admin
    path('api-auth/', include('rest_framework.urls')),
    #DRF Endepoints
    path('api/v1/', include('agendamento.urls')),
    path('api/v2/', include(router.urls)),

    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    
]
