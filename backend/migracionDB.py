from django.db import connections
from django.http import HttpResponse, JsonResponse

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
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM sima_unidad")
        unidades = cursor.fetchall()
        for unidad in unidades:
            ub = unidad[1]
            with connections['default'].cursor() as sima_cursor:
                sima_cursor.execute("SELECT id FROM `SimaURP-OCS`.sima_equipo WHERE SUBSTRING(Nombre, 1, 2) = %s", [ub])
                equipos = sima_cursor.fetchall()
                for equipo in equipos:
                    with connections['default'].cursor() as sima_save_cursor:
                        sima_save_cursor.execute(
                            "UPDATE sima_equipo SET ubicacion = %s WHERE id = %s",
                            [unidad[0], equipo[0]]
                        )
    return HttpResponse("Campo Actualizado")

def Actualizar_Inventario(request):
    with connections['sima'].cursor() as cursor:
        cursor.execute("SELECT * FROM sis_mant_equipo")
        inventario = cursor.fetchall()
        for invent in inventario:
            with connections['default'].cursor() as sima_cursor:
                sima_cursor.execute("SELECT id FROM `SimaURP-OCS`.sima_equipo WHERE Nombre = %s", [invent[30]])
                equipos = sima_cursor.fetchall()
                for equipo in equipos:
                    with connections['default'].cursor() as sima_save_cursor:
                        sima_save_cursor.execute(
                            "UPDATE sima_equipo SET inventario = %s WHERE id = %s",
                            [invent[3], equipo[0]]
                        )
    return HttpResponse("ok")

def Actualizar_Perifericos_Monitor(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM sima_equipo")
        equipo = cursor.fetchall()
        for e in equipo:
            with connections['sima'].cursor() as sima_cursor:
                sima_cursor.execute("SELECT  ESERIE, CODFIC, MMARCA, MMODELO, MSERIE, MINVENTARIO, PERIODO FROM iTopDB.sis_hard_fic_pre "
                                    "WHERE ESERIE= %s "
                                    "GROUP BY ESERIE "
                                    "ORDER BY CODFIC DESC", [e[1]])
                perifericos = sima_cursor.fetchall()
                for periferico in perifericos:
                    with connections['default'].cursor() as sima_save_cursor:
                        sima_save_cursor.execute(
                            "insert into sima_equipo_perif (equipo_id, tipo_perif, serie_perif, marca_perif, modelo_perif, inventario_perif, estado_perif ) values (%s, %s, %s, %s, %s, %s, %s)",
                            [e[0], 'MN', periferico[4], periferico[2],periferico[3], periferico[5], '1']
                        )
    return HttpResponse("ok")

def Actualizar_Perifericos_Teclado(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM sima_equipo")
        equipo = cursor.fetchall()
        for e in equipo:
            with connections['sima'].cursor() as sima_cursor:
                sima_cursor.execute("SELECT  ESERIE, CODFIC, TMARCA, TMODELO, TSERIE, TINVENTARIO, PERIODO FROM iTopDB.sis_hard_fic_pre "
                                    "WHERE ESERIE= %s "
                                    "GROUP BY ESERIE "
                                    "ORDER BY CODFIC DESC", [e[1]])
                perifericos = sima_cursor.fetchall()
                for periferico in perifericos:
                    with connections['default'].cursor() as sima_save_cursor:
                        sima_save_cursor.execute(
                            "insert into sima_equipo_perif (equipo_id, tipo_perif, serie_perif, marca_perif, modelo_perif, inventario_perif, estado_perif ) values (%s, %s, %s, %s, %s, %s, %s)",
                            [e[0], 'TC', periferico[4], periferico[2],periferico[3], periferico[5], '1']
                        )
    return HttpResponse("ok")

def Actualizar_Perifericos_Mouse(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM sima_equipo")
        equipo = cursor.fetchall()
        for e in equipo:
            with connections['sima'].cursor() as sima_cursor:
                sima_cursor.execute("SELECT  ESERIE, CODFIC, OMARCA, OMODELO, OSERIE, OINVENTARIO, PERIODO FROM iTopDB.sis_hard_fic_pre "
                                    "WHERE ESERIE= %s "
                                    "GROUP BY ESERIE "
                                    "ORDER BY CODFIC DESC", [e[1]])
                perifericos = sima_cursor.fetchall()
                for periferico in perifericos:
                    with connections['default'].cursor() as sima_save_cursor:
                        sima_save_cursor.execute(
                            "insert into sima_equipo_perif (equipo_id, tipo_perif, serie_perif, marca_perif, modelo_perif, inventario_perif, estado_perif ) values (%s, %s, %s, %s, %s, %s, %s)",
                            [e[0], 'MS', periferico[4], periferico[2],periferico[3], periferico[5], '1']
                        )
    return HttpResponse("ok")

def Actualizar_Software(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM sima_equipo")
        equipo = cursor.fetchall()
        for e in equipo:
            with connections['ocs'].cursor() as sima_cursor:
                sima_cursor.execute("SELECT  ssn, name, PUBLISHER, VERSION FROM Vista_Software "
                                    "WHERE ssn= %s ", [e[1]])
                softwares = sima_cursor.fetchall()
                for software in softwares:
                    with connections['default'].cursor() as sima_save_cursor:
                        sima_save_cursor.execute("Insert into sima_equipo_software (id_equipo, software, version, distribuidor) values (%s, %s, %s, %s)"
                                                 , [e[0], software[1], software[2], software[3]])
    return HttpResponse("ok")


def Actualizar_Mantenimiento(request):
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM sima_equipo")
        equipo = cursor.fetchall()
        for e in equipo:
            with connections['ocs'].cursor() as sima_cursor:
                sima_cursor.execute("SELECT  ssn, name, PUBLISHER, VERSION FROM sis_hard_fic_pre "
                                    "WHERE ssn= %s ", [e[1]])
                softwares = sima_cursor.fetchall()
                for software in softwares:
                    with connections['default'].cursor() as sima_save_cursor:
                        sima_save_cursor.execute("Insert into sima_equipo_software (id_equipo, software, version, distribuidor) values (%s, %s, %s, %s)"
                                                 , [e[0], software[1], software[2], software[3]])
    return HttpResponse("ok")



