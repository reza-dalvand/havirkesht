from rest_framework import serializers
from .models import (
    Car, Driver, Carriage, CarriageStatus, BulkSmsJob,
    FarmersLoad, FactoryCommitmentTonnage
)


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class DriverSerializer(serializers.ModelSerializer):
    """اسکیما برای راننده (Driver)"""
    class Meta:
        model = Driver
        fields = "__all__"


class CarriageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriage
        fields = "__all__"


class CarriageStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarriageStatus
        fields = "__all__"


class BulkSmsJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = BulkSmsJob
        fields = "__all__"


class FarmersLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersLoad
        fields = "__all__"


class FactoryCommitmentTonnageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryCommitmentTonnage
        fields = "__all__"