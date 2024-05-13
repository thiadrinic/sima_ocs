from django.db import models

# Create your models here.
class sima_equipo(models.Model):
    id=models.IntegerField(default=0,primary_key=True)
    SSN = models.CharField(max_length=255, null=True, blank=True)
    Nombre = models.CharField(max_length=255, null=True, blank=True)
    SO = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=255, null=True, blank=True)
    MACADDR = models.CharField(max_length=255, null=True, blank=True)
    IPADDRESS = models.CharField(max_length=255, null=True, blank=True)
    Semaforo = models.CharField(max_length=255, null=True, blank=True)
    inventario = models.CharField(max_length=255, null=True, blank=True)
    ubicacion = models.CharField(max_length=255, null=True, blank=True)
    smodel = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'sima_equipo'

class sima_vista_equipo(models.Model):
    id=models.IntegerField(default=0,primary_key=True)
    SSN = models.CharField(max_length=255, null=True, blank=True)
    Nombre = models.CharField(max_length=255, null=True, blank=True)
    SO = models.CharField(max_length=255, null=True, blank=True)
    tipo = models.CharField(max_length=255, null=True, blank=True)
    MACADDR = models.CharField(max_length=255, null=True, blank=True)
    IPADDRESS = models.CharField(max_length=255, null=True, blank=True)
    Semaforo = models.CharField(max_length=255, null=True, blank=True)
    inventario = models.CharField(max_length=255, null=True, blank=True)
    unidad = models.CharField(max_length=255, null=True, blank=True)
    smodel = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'Vista_Equipo_Ubicacion'


class sima_equipo_perifericos(models.Model):
    id=models.IntegerField(default=0,primary_key=True)
    equipo_id=models.IntegerField(default=0)
    tipo_perif=models.CharField(max_length=255)
    serie_perif=models.CharField(max_length=255)
    marca_perif=models.CharField(max_length=255)
    modelo_perif = models.CharField(max_length=255)
    inventario_perif = models.CharField(max_length=255)
    estado_perif = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'sima_equipo_perif'

class sima_equipo_software(models.Model):
    id=models.IntegerField(default=0,primary_key=True)
    id_equipo=models.IntegerField(default=0)
    software=models.CharField(max_length=255)
    distribuidor = models.CharField(max_length=255)
    version=models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'sima_equipo_software'

class sima_mantenimiento(models.Model):
    ID = models.AutoField(primary_key=True)
    ID_EQUIPO = models.CharField(max_length=200, null=True, blank=True)
    PERIODO = models.CharField(max_length=10, null=True, blank=True)
    FECHA = models.DateField(null=True, blank=True)
    ID_UBICACION = models.CharField(max_length=200, null=True, blank=True)
    CODSITIO = models.CharField(max_length=200, null=True, blank=True)
    CODPISO = models.CharField(max_length=200, null=True, blank=True)
    CODEPENDENCIA = models.CharField(max_length=200, null=True, blank=True)
    USUARIO1 = models.CharField(max_length=200, null=True, blank=True)
    USUARIO2 = models.CharField(max_length=200, null=True, blank=True)
    CARGO = models.CharField(max_length=200, null=True, blank=True)
    CHK1 = models.CharField(max_length=100, null=True, blank=True)
    CHK2 = models.CharField(max_length=100, null=True, blank=True)
    CHK3 = models.CharField(max_length=100, null=True, blank=True)
    CHK4 = models.CharField(max_length=100, null=True, blank=True)
    CHK5 = models.CharField(max_length=100, null=True, blank=True)
    CHK6 = models.CharField(max_length=100, null=True, blank=True)
    CHK7 = models.CharField(max_length=100, null=True, blank=True)
    CHK8 = models.CharField(max_length=100, null=True, blank=True)
    CHK9 = models.CharField(max_length=100, null=True, blank=True)
    CHK10 = models.CharField(max_length=100, null=True, blank=True)
    CHK11 = models.CharField(max_length=100, null=True, blank=True)
    OBSERVACIONES = models.CharField(max_length=300, null=True, blank=True)
    USUARIO3 = models.CharField(max_length=200, null=True, blank=True)
    TMANTENIMIENTO = models.CharField(max_length=30, null=True, blank=True)
    UNIRESPONSABLE = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'sima_mantenimiento'


class sima_servicio(models.Model):
    id = models.AutoField(primary_key=True)
    id_equipo = models.IntegerField(null=True, blank=True)
    ticket = models.CharField(max_length=45, null=True, blank=True)
    id_agente = models.IntegerField(null=True, blank=True)
    fecha = models.DateField(null=True, blank=True)
    solicitud = models.CharField(max_length=150, null=True, blank=True)
    detalle = models.CharField(max_length=500, null=True, blank=True)
    recomendacion = models.CharField(max_length=500, null=True, blank=True)
    id_cliente = models.IntegerField(null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'sima_servicio'

class sima_unidad(models.Model):
    id = models.AutoField(primary_key=True)
    nomenclatura = models.CharField(max_length=45, null=True, blank=True)
    unidad = models.CharField(max_length=100, null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'sima_unidad'

class sima_equipo_hardware(models.Model):
    id = models.AutoField(primary_key=True)
    id_equipo = models.IntegerField(default=None, null=True)
    motherboard = models.CharField(max_length=45, default=None, null=True)
    processor = models.CharField(max_length=100, default=None, null=True)
    slots_memory = models.CharField(max_length=45, default=None, null=True)
    memory = models.CharField(max_length=45, default=None, null=True)
    hdd1 = models.CharField(max_length=45, default=None, null=True)
    hdd2 = models.CharField(max_length=45, default=None, null=True)
    typessd = models.CharField(max_length=45, default=None, null=True)
    sdd = models.CharField(max_length=45, default=None, null=True)
    gpu = models.CharField(max_length=45, default=None, null=True)
    ethernet_card = models.CharField(max_length=45, default=None, null=True)

    class Meta:
        managed = False
        db_table = 'sima_hardware'