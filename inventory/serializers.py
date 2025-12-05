from rest_framework import serializers
from .models import (
    Seed, Pesticide, FactorySeed, FactoryPesticide,
    FarmersSeed, FarmersPesticide, FactorySugar, FactoryWaste,
    FarmersSugarDelivery, FarmersWasteDelivery
)


class SeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seed
        fields = "__all__"


class PesticideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pesticide
        fields = "__all__"


class FactorySeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorySeed
        fields = "__all__"


class FactoryPesticideSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryPesticide
        fields = "__all__"


class FarmersSeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersSeed
        fields = "__all__"


class FarmersPesticideSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersPesticide
        fields = "__all__"


class FactorySugarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactorySugar
        fields = "__all__"


class FactoryWasteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryWaste
        fields = "__all__"


class FarmersSugarDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersSugarDelivery
        fields = "__all__"


class FarmersWasteDeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmersWasteDelivery
        fields = "__all__"