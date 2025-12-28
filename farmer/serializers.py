# farmer/serializers.py

from rest_framework import serializers
from .models import Province, City, Village, Farmer, Supervisor, Commitment

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = "__all__"



class VillageSerializer(serializers.ModelSerializer):
    """اسکیما برای روستا (Village)"""
    class Meta:
        model = Village
        fields = "__all__"

class FarmerSerializer(serializers.ModelSerializer):
    """اسکیما برای کشاورز (Farmer)"""
    class Meta:
        model = Farmer
        fields = "__all__"


class SupervisorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor
        fields = "__all__"


class CommitmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commitment
        fields = "__all__"
