from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from .models import sima_equipo
from .serializers import *
from .migracionDB import *


# Create your views here.
class Sima_EquiposViewSet(viewsets.ModelViewSet):
    serializer_class = Sima_EquipoSerializer
    queryset = sima_equipo.objects.all()

class Sima_PerifericosViewSet(viewsets.ModelViewSet):
    serializer_class = Sima_PerifericosSerializer
    queryset = sima_equipo_perifericos.objects.all()

def Pruebas(request):
    data=Actualizar_Perifericos_Mouse(request)
    data2=Actualizar_Perifericos_Monitor(request)
    data3=Actualizar_Perifericos_Teclado(request)
    return HttpResponse(data, data2, data3)
