from rest_framework import serializers

from .models import *


class Sima_UbicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = sima_unidad
        fields = '__all__'

#class Sima_EquipoSerializer(serializers.ModelSerializer):
#    modelo2_data = Sima_UbicacionSerializer(read_only=True)
#    class Meta:
#        model = sima_equipo
        #fields = '__all__'
#        fields =['SSN', 'Nombre', 'SO', 'tipo', 'MACADDR', 'IPADDRESS', 'Semaforo', 'inventario', 'smodel', 'modelo2_data']

class Sima_EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = sima_vista_equipo
        fields = '__all__'

class Sima_PerifericosSerializer(serializers.ModelSerializer):
    class Meta:
        model = sima_equipo_perifericos
        fields = '__all__'

class Sima_SoftwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = sima_equipo_software
        fields = '__all__'

class Sima_ServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = sima_servicio
        fields = '__all__'

class Sima_HardwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = sima_equipo_hardware
        fields = '__all__'

class Sima_MantenimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = sima_mantenimiento
        fields = '__all__'


