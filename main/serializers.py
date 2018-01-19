from rest_framework import serializers
from .models import Vehicle, VehicleType, Configuration,Order


class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = ('id', 'type')


class VehicleTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('size', 'cost', 'vehicle_img')


class ConfigurationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ('value',)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('description','url')