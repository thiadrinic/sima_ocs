from django.shortcuts import render
from rest_framework import viewsets

from .models import sima_equipo
from .serializers import Sima_EquipoSerializer


# Create your views here.
class Sima_EquiposViewSet(viewsets.ModelViewSet):
    serializer_class = Sima_EquipoSerializer
    queryset = sima_equipo.objects.all()

