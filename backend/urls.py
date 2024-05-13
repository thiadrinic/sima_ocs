from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import views


router = routers.DefaultRouter()
router.register(r'equipo', views.Sima_EquipoViewSet, 'equipo')
router.register(r'equipos', views.Sima_EquiposViewSet, 'equipos')
router.register(r'perifericos', views.Sima_PerifericosViewSet, 'perifericos')
router.register(r'software', views.Sima_SoftwareViewSet, 'software')
router.register(r'hardware', views.Sima_HardwareViewSet, 'hardware')
router.register(r'mantenimiento', views.Sima_MantenimientoViewSet, 'mantenimiento')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Simaocs API')),
    path('test/', views.Pruebas),
]