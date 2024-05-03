from django.db import connections
from django.http import HttpResponse

from .models import *

def migracion_Cursor(request):
    with connections['ocs'].cursor() as cursor:
        cursor.execute("SELECT SSN, Equipo, SO, type, MACADDR, IPADDRESS, Semaforo, smodel FROM Vista_Equipos")
        ocs = cursor.fetchall()
        for oc in ocs:
            SSN, Equipo, SO, type, MACADDR, IPADDRESS, Semaforo, smodel = oc
            with connections['default'].cursor() as sima_cursor:
                sima_cursor.execute(
                    "SELECT * FROM sima_equipo WHERE SSN = %s AND Nombre = %s AND SO = %s AND tipo = %s AND MACADDR = %s AND IPADDRESS = %s AND Semaforo = %s AND smodel = %s",
                    [SSN, Equipo, SO, type, MACADDR, IPADDRESS, Semaforo, smodel]
                )
                equipo = sima_cursor.fetchall()
                if not equipo:
                    with connections['default'].cursor() as sima_save_cursor:
                        sima_save_cursor.execute(
                            "INSERT INTO sima_equipo (SSN, Nombre, SO, tipo, MACADDR, IPADDRESS, Semaforo, inventario, ubicacion, smodel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            [SSN, Equipo, SO, type, MACADDR, IPADDRESS, Semaforo, '', '', smodel]
                        )
    return HttpResponse("ok")


def Actualizar_Ubicacion(request):
    return HttpResponse("ok")
