from rest_framework import viewsets

from .models import Hardware
from .serializers import HardwareSerializer


# Create your views here.

class HardwareViewSet(viewsets.ModelViewSet):
    serializer_class = HardwareSerializer
    queryset = Hardware.objects.all()
