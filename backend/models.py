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


class sima_equipo_perifericos(models.Model):
    id=models.IntegerField(default=0,primary_key=True)
    equipo_id=models.IntegerField(default=0)
    tipo_perif=models.CharField(max_length=255)
    marca_perif=models.CharField(max_length=255)
    modelo_perif = models.CharField(max_length=255)
    inventario_perif = models.CharField(max_length=255)
    estado_perif = models.CharField(max_length=255)
    class Meta:
        managed = False
        db_table = 'sima_equipo_perif'
