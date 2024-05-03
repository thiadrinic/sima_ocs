from django.db import connections
from django.http import HttpResponse

from .models import *

def migracionDB(request):
    ocs=Vista_Equipos.objects.all()
    for i in ocs:
        equipo = sima_equipos.objects.using('simaocs').filter(SSN=i.SSN,Nombre=i.Equipo,SO=i.SO,tipo=i.type,MACADDR=i.MACADDR,IPADDRESS=i.IPADDRESS,Semaforo=i.Semaforo,smodel=i.smodel)
        if not equipo:
            equipo = sima_equipos(SSN=i.SSN,Nombre=i.Equipo,SO=i.SO,tipo=i.type,MACADDR=i.MACADDR,IPADDRESS=i.IPADDRESS,Semaforo=i.Semaforo,inventario='',ubicacion='',smodel=i.smodel)
            equipo.save(using='simaocs')
    return HttpResponse("ok")


def migracion_Cursor(request):
    with connections['ocs'].cursor() as cursor:
        cursor.execute("SELECT SSN, Equipo, SO, type, MACADDR, IPADDRESS, Semaforo, smodel FROM Vista_Equipos")
        ocs = cursor.fetchall()
        for oc in ocs:
            SSN, Equipo, SO, type, MACADDR, IPADDRESS, Semaforo, smodel = oc
            with connections['simaocs'].cursor() as sima_cursor:
                sima_cursor.execute(
                    "SELECT * FROM sima_equipo WHERE SSN = %s AND Nombre = %s AND SO = %s AND tipo = %s AND MACADDR = %s AND IPADDRESS = %s AND Semaforo = %s AND smodel = %s",
                    [SSN, Equipo, SO, type, MACADDR, IPADDRESS, Semaforo, smodel]
                )
                equipo = sima_cursor.fetchall()
                if not equipo:
                    with connections['simaocs'].cursor() as sima_save_cursor:
                        sima_save_cursor.execute(
                            "INSERT INTO sima_equipo (SSN, Nombre, SO, tipo, MACADDR, IPADDRESS, Semaforo, inventario, ubicacion, smodel) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            [SSN, Equipo, SO, type, MACADDR, IPADDRESS, Semaforo, '', '', smodel]
                        )
    return HttpResponse("ok")
