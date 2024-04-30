from rest_framework import viewsets

from .models import Hardware, Vista_Equipos
from .serializers import *


# Create your views here.

class HardwareViewSet(viewsets.ModelViewSet):
    serializer_class = HardwareSerializer
    queryset = Hardware.objects.all()

class Vista_EquiposViewSet(viewsets.ModelViewSet):
    serializer_class = Vista_EquiposSerializer
    queryset = Vista_Equipos.objects.all()

