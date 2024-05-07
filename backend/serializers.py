from rest_framework import serializers

from .models import *


class Sima_EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = sima_equipo
        fields = '__all__'

class Sima_PerifericosSerializer(serializers.ModelSerializer):
    class Meta:
        model = sima_equipo_perifericos
        fields = '__all__'