from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets, generics

from .models import sima_equipo, sima_unidad
from .serializers import *
from .migracionDB import *


# Create your views here.
class Sima_EquipoViewSet(viewsets.ModelViewSet):
    serializer_class = Sima_EquipoSerializer
    queryset = sima_equipo.objects.all()

class Sima_EquiposViewSet(viewsets.ModelViewSet):
    serializer_class = Sima_EquipoSerializer
    queryset = sima_equipo.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        # Crear una lista para almacenar los objetos modificados
        modified_queryset = []
        for obj in queryset:
            ubicacion_id = obj.ubicacion  # Acceder al id de ubicacion
            if ubicacion_id:  # Verificar si ubicacion_id no es None o vacío
                modelo2_obj = sima_unidad.objects.filter(id=ubicacion_id).first()
                obj.modelo2_data = modelo2_obj
            else:
                obj.modelo2_data = None  # Manejar el caso en que ubicacion_id sea None o vacío
            # Agregar el objeto modificado a la lista
            modified_queryset.append(obj)
        return modified_queryset


class Sima_PerifericosViewSet(viewsets.ModelViewSet):
    serializer_class = Sima_PerifericosSerializer
    queryset = sima_equipo_perifericos.objects.all()

#class Sima_SoftwareViewSet(viewsets.ModelViewSet):
#    serializer_class = Sima_SoftwareSerializer
#    queryset = sima_equipo_software.objects.all()

class Sima_SoftwareViewSet(viewsets.ModelViewSet):
    serializer_class = Sima_SoftwareSerializer

    def get_queryset(self):
        id_equipo = self.request.query_params.get('id_equipo', None)  # Obtener el parámetro id_equipo de la consulta
        if id_equipo is not None and id_equipo != '':
            queryset = sima_equipo_software.objects.filter(id_equipo=id_equipo)
        else:
            queryset = sima_equipo_software.objects.all()  # Obtener todos los valores de la tabla
        return queryset


class Sima_HardwareViewSet(viewsets.ModelViewSet):
    serializer_class = Sima_HardwareSerializer
    queryset = sima_hardware.objects.all()
def Pruebas(request):
    data=Actualizar_Software(request)
    return HttpResponse(data)
