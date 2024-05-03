from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from . import views


router = routers.DefaultRouter()
router.register(r'equipos', views.Sima_EquiposViewSet, 'equipos')

urlpatterns = [
    path('api/', include(router.urls)),
    path('docs/', include_docs_urls(title='Simaocs API')),
]