from django.db import models


# Create your models here.
class Hardware(models.Model):
    ID = models.AutoField(primary_key=True)
    DEVICEID = models.CharField(max_length=255)
    NAME = models.CharField(max_length=255, null=True, blank=True)
    WORKGROUP = models.CharField(max_length=255, null=True, blank=True)
    USERDOMAIN = models.CharField(max_length=255, null=True, blank=True)
    OSNAME = models.CharField(max_length=255, null=True, blank=True)
    OSVERSION = models.CharField(max_length=255, null=True, blank=True)
    OSCOMMENTS = models.CharField(max_length=255, null=True, blank=True)
    PROCESSORT = models.CharField(max_length=255, null=True, blank=True)
    PROCESSORS = models.IntegerField(default=0)
    PROCESSORN = models.SmallIntegerField(null=True, blank=True)
    MEMORY = models.IntegerField(null=True, blank=True)
    SWAP = models.IntegerField(null=True, blank=True)
    IPADDR = models.CharField(max_length=255, null=True, blank=True)
    DNS = models.CharField(max_length=255, null=True, blank=True)
    DEFAULTGATEWAY = models.CharField(max_length=255, null=True, blank=True)
    ETIME = models.DateTimeField(null=True, blank=True)
    LASTDATE = models.DateTimeField(null=True, blank=True)
    LASTCOME = models.DateTimeField(null=True, blank=True)
    QUALITY = models.DecimalField(max_digits=7, decimal_places=4, null=True, blank=True)
    FIDELITY = models.BigIntegerField(default=1)
    USERID = models.CharField(max_length=255, null=True, blank=True)
    TYPE = models.IntegerField(null=True, blank=True)
    DESCRIPTION = models.CharField(max_length=255, null=True, blank=True)
    WINCOMPANY = models.CharField(max_length=255, null=True, blank=True)
    WINOWNER = models.CharField(max_length=255, null=True, blank=True)
    WINPRODID = models.CharField(max_length=255, null=True, blank=True)
    WINPRODKEY = models.CharField(max_length=255, null=True, blank=True)
    USERAGENT = models.CharField(max_length=50, null=True, blank=True)
    CHECKSUM = models.BigIntegerField(default=262143)
    SSTATE = models.IntegerField(default=0)
    IPSRC = models.CharField(max_length=255, null=True, blank=True)
    UUID = models.CharField(max_length=255, null=True, blank=True)
    ARCH = models.CharField(max_length=10, null=True, blank=True)
    CATEGORY_ID = models.IntegerField(null=True, blank=True)
    ARCHIVE = models.IntegerField(null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'hardware'

class Vista_Equipos(models.Model):
    SSN = models.CharField(max_length=255, null=True, blank=True)
    smanufacturer = models.CharField(max_length=255, null=True, blank=True)
    smodel = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    bversion = models.CharField(max_length=255, null=True, blank=True)
    bdate = models.CharField(max_length=255, null=True, blank=True)
    id =models.CharField(primary_key=True,max_length=255)
    Equipo = models.CharField(max_length=255, null=True, blank=True)
    SO = models.CharField(max_length=255, null=True, blank=True)
    Osversion = models.CharField(max_length=255, null=True, blank=True)
    PROCESSORT = models.CharField(max_length=255, null=True, blank=True)
    RAM = models.CharField(max_length=255, null=True, blank=True)
    ARCH = models.CharField(max_length=255, null=True, blank=True)
    MON_MANUFACTURER= models.CharField(max_length=255, null=True, blank=True)
    MON_CAPTION = models.CharField(max_length=255, null=True, blank=True)
    MON_SERIAL = models.CharField(max_length=255, null=True, blank=True)
    VID_NAME = models.CharField(max_length=255, null=True, blank=True)
    VID_MEMORY = models.CharField(max_length=255, null=True, blank=True)
    MACADDR = models.CharField(max_length=255, null=True, blank=True)
    IPADDRESS = models.CharField(max_length=255, null=True, blank=True)
    Tipo = models.CharField(max_length=255, null=True, blank=True)
    Semaforo = models.CharField(max_length=255, null=True, blank=True)
    fecha = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        managed = False
        db_table = 'Vista_Equipos'

class sima_equipos(models.Model):
    id=models.IntegerField(default=0,primary_key=True)
    SSN = models.CharField(max_length=255, null=True, blank=True)
    Nombre = models.CharField(max_length=255, null=True, blank=True)
    SO = models.CharField(max_length=255, null=True, blank=True)
    type = models.CharField(max_length=255, null=True, blank=True)
    MACADDR = models.CharField(max_length=255, null=True, blank=True)
    IPADDRESS = models.CharField(max_length=255, null=True, blank=True)
    Semaforo = models.CharField(max_length=255, null=True, blank=True)
    inventario = models.CharField(max_length=255, null=True, blank=True)
    ubicacion = models.CharField(max_length=255, null=True, blank=True)
    smodel = models.CharField(max_length=255, null=True, blank=True)
    class Meta:
        managed = False
        db_table = 'sima_equipo'