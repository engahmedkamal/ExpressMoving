from rest_framework import serializers
from .models import Vehicle, VehicleType


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'type')


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('size', 'cost', 'vehicle_img')
