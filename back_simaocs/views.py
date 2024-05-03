from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.response import Response

from .models import sima_equipo
from .migracionDB import *
from .serializers import *

import json


# Create your views here.

class Sima_EquiposViewSet(viewsets.ModelViewSet):
    serializer_class = Sima_EquipoSerializer
    queryset = sima_equipo.objects.all()


def obtener_datos_sima(request):
    with connections['simaocs'].cursor() as cursor:
        cursor.execute("SELECT SSN, Nombre, SO, tipo, MACADDR, IPADDRESS, Semaforo, inventario, ubicacion, smodel FROM sima_equipo")
        rows = cursor.fetchall()

    # Convertir las tuplas en diccionarios
    datos = [{'SSN': row[0], 'Nombre': row[1], 'SO': row[2], 'tipo': row[3], 'MACADDR': row[4], 'IPADDRESS': row[5], 'Semaforo': row[6], 'inventario': row[7], 'ubicacion': row[8], 'smodel': row[9]} for row in rows]

    #serializer = sima_equiposSerializer(data=datos, many=True)
    #serializer.is_valid(raise_exception=True)

    json_data = json.dumps(datos)
    return HttpResponse(json_data, content_type='application/json')
    #return Response(serializer.data)
def ejecutar_copia(request):
    # Llama a la función copiar_datos para realizar la copia
    migracion_Cursor(request)
    # Redirecciona o muestra un mensaje de éxito
    return HttpResponse("La copia de datos se ha ejecutado correctamente.")

