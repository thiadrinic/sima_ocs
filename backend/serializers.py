from rest_framework import serializers

from .models import sima_equipo


class Sima_EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = sima_equipo
        fields = '__all__'