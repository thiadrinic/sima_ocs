from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import views


router = routers.DefaultRouter()

router.register(r'hardware', views.HardwareViewSet, 'hardware')
router.register(r'vista_equipos', views.Vista_EquiposViewSet, 'vista_equipos')
#router.register(r'sima_equipos', views.Sima_EquiposViewSet, 'sima_equipos')

urlpatterns = [
    path('api/sima_ocs', views.obtener_datos_sima, name='migracionDB'),
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Simaocs API')),
]
