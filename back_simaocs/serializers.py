from rest_framework import serializers

from .models import *


class HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hardware
        fields = '__all__'


class Vista_EquiposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vista_Equipos
        fields = '__all__'

class Sima_EquipoSerializer(serializers.ModelSerializer):
     class Meta:
         model = sima_equipos
         fields = '__all__'


class sima_equiposSerializer(serializers.Serializer):
    SSN = serializers.CharField()
    Nombre = serializers.CharField()
    SO = serializers.CharField()
    tipo = serializers.CharField()
    MACADDR = serializers.CharField()
    IPADDRESS = serializers.CharField()
    Semaforo = serializers.CharField()
    inventario = serializers.CharField()
    ubicacion = serializers.CharField()
    smodel = serializers.CharField()
