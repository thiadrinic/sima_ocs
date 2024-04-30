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